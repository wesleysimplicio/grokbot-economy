#!/usr/bin/env python3
"""token_log.py: append-only log of tokens/cost per task (CSV). Stdlib only, no network.

Usage:
  python3 scripts/token_log.py add --agent BOT --task "render <ITEM_ID>" --path script \
      --tokens 1200 [--cost 0.0] [--notes "..."] [--file token-log.csv] [--lock] [--dry-run]
  python3 scripts/token_log.py summary [--file token-log.csv]
  python3 scripts/token_log.py --selftest

path must be one of: script, mcp, plugin, api, browse, computer-use.
Default file: $TOKEN_LOG_FILE or ./token-log.csv (relative to the current directory; set
TOKEN_LOG_FILE to a fixed path to avoid logs landing in unexpected folders).
The header is written once; rows are only appended. --lock takes an exclusive file lock
(POSIX flock) while writing, so parallel agents never interleave rows or duplicate the header.
Text values starting with = + - @ (or a tab/CR) are prefixed with ' so spreadsheets do not run
them as formulas. Errors print one line to stderr and exit with code 2 (no traceback).
"""
import argparse
import csv
import datetime as dt
import io
import math
import os
import sys
import tempfile

try:
    import fcntl  # POSIX only
except ImportError:  # pragma: no cover
    fcntl = None

FIELDS = ["date", "agent", "task", "path", "est_tokens", "cost_usd", "notes"]
PATHS = ["script", "mcp", "plugin", "api", "browse", "computer-use"]
FORMULA_PREFIXES = ("=", "+", "-", "@", "\t", "\r")


class LogError(Exception):
    """User-facing error: printed as one line, no traceback."""


def default_file():
    return os.environ.get("TOKEN_LOG_FILE", "token-log.csv")


def clean_text(value):
    """Flatten newlines and neutralize spreadsheet formulas."""
    value = str(value).replace("\r\n", " ").replace("\n", " ").replace("\r", " ")
    if value.startswith(FORMULA_PREFIXES):
        value = "'" + value
    return value


def make_row(agent, task, path, tokens, cost=0.0, notes="", date=None):
    if path not in PATHS:
        raise LogError(f"path must be one of {', '.join(PATHS)} (got {path!r})")
    try:
        tokens = int(tokens)
        cost = float(cost)
    except (TypeError, ValueError):
        raise LogError("tokens must be an integer and cost a number")
    if not math.isfinite(cost):
        raise LogError("cost must be a finite number (no nan/inf)")
    if tokens < 0 or cost < 0:
        raise LogError("tokens and cost must be >= 0")
    return {
        "date": date or dt.datetime.now().astimezone().isoformat(timespec="minutes"),
        "agent": clean_text(agent), "task": clean_text(task), "path": path,
        "est_tokens": tokens, "cost_usd": f"{cost:.4f}", "notes": clean_text(notes),
    }


def add(file, agent, task, path, tokens, cost=0.0, notes="", date=None, dry_run=False, lock=False):
    row = make_row(agent, task, path, tokens, cost, notes, date)
    if dry_run:
        return row
    parent = os.path.dirname(os.path.abspath(file))
    if not os.path.isdir(parent):
        raise LogError(f"directory does not exist: {parent}")
    if lock and fcntl is None:
        raise LogError("--lock needs a POSIX system (fcntl not available)")
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=FIELDS, lineterminator="\n")
    try:
        with open(file, "a+b") as fh:
            if lock:
                fcntl.flock(fh.fileno(), fcntl.LOCK_EX)
            try:
                fh.seek(0, os.SEEK_END)
                size = fh.tell()
                if size == 0:
                    w.writeheader()
                else:
                    fh.seek(size - 1)
                    if fh.read(1) not in (b"\n", b"\r"):
                        buf.write("\n")  # file edited by hand without a trailing newline
                w.writerow(row)
                fh.seek(0, os.SEEK_END)
                fh.write(buf.getvalue().encode("utf-8"))
                fh.flush()
            finally:
                if lock:
                    fcntl.flock(fh.fileno(), fcntl.LOCK_UN)
    except OSError as e:
        raise LogError(f"cannot write {file}: {e.strerror or e}")
    return row


def summary(file):
    tot = {}
    if not os.path.exists(file):
        return tot
    try:
        with open(file, newline="", encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            missing = [f for f in ("path", "est_tokens", "cost_usd") if f not in (reader.fieldnames or [])]
            if missing:
                raise LogError(f"{file}: header is missing {', '.join(missing)} (expected {','.join(FIELDS)})")
            for r in reader:
                try:
                    tokens = int(r["est_tokens"] or 0)
                    cost = float(r["cost_usd"] or 0)
                except (TypeError, ValueError):
                    raise LogError(f"{file}:{reader.line_num}: bad number in est_tokens/cost_usd")
                if not math.isfinite(cost):
                    raise LogError(f"{file}:{reader.line_num}: cost_usd is not finite")
                t = tot.setdefault(r["path"], {"tasks": 0, "tokens": 0, "cost": 0.0})
                t["tasks"] += 1
                t["tokens"] += tokens
                t["cost"] += cost
    except OSError as e:
        raise LogError(f"cannot read {file}: {e.strerror or e}")
    return tot


def print_summary(tot):
    if not tot:
        print("(empty log)")
        return
    print(f"{'path':<13}{'tasks':>6}{'tokens':>10}{'cost_usd':>10}")
    for p in sorted(tot, key=lambda k: -tot[k]["tokens"]):
        t = tot[p]
        print(f"{p:<13}{t['tasks']:>6}{t['tokens']:>10}{t['cost']:>10.4f}")


def _expect_error(fn):
    try:
        fn()
    except LogError:
        return
    raise AssertionError("expected LogError")


def selftest():
    with tempfile.TemporaryDirectory() as d:
        f = os.path.join(d, "log.csv")
        add(f, "bot-a", "task 1", "script", 100, 0.0, "ok")
        add(f, "bot-a", "task 2", "computer-use", 5000, 0.05, "login\nwith 2fa", lock=fcntl is not None)
        add(f, "bot-b", "task 3", "script", 50)
        assert add(f, "x", "dry", "api", 1, dry_run=True)["path"] == "api"
        with open(f, encoding="utf-8") as fh:
            lines = fh.read().splitlines()
        assert lines[0] == ",".join(FIELDS), lines[0]
        assert len(lines) == 4, lines  # header + 3 rows, dry-run not written, newline flattened
        tot = summary(f)
        assert tot["script"] == {"tasks": 2, "tokens": 150, "cost": 0.0}, tot
        assert tot["computer-use"]["tokens"] == 5000
        for bad in (lambda: add(f, "a", "t", "telepathy", 1), lambda: add(f, "a", "t", "api", -1),
                    lambda: add(f, "a", "t", "api", 1, float("nan")), lambda: add(f, "a", "t", "api", 1, float("inf")),
                    lambda: add(os.path.join(d, "nope", "x.csv"), "a", "t", "api", 1)):
            _expect_error(bad)
        assert add(f, "=cmd()", "+x", "api", 1, notes="@y", dry_run=True)["agent"] == "'=cmd()"
        with open(f, "a", encoding="utf-8") as fh:  # simulate a hand edit without trailing newline
            fh.write("2026-01-01T00:00+00:00,h,t,mcp,7,0.0000,no newline")
        add(f, "bot-c", "task 4", "mcp", 3)
        assert summary(f)["mcp"] == {"tasks": 2, "tokens": 10, "cost": 0.0}, summary(f)
    print("selftest ok")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--selftest", action="store_true")
    sub = ap.add_subparsers(dest="cmd")
    a = sub.add_parser("add")
    a.add_argument("--agent", required=True)
    a.add_argument("--task", required=True)
    a.add_argument("--path", required=True, choices=PATHS)
    a.add_argument("--tokens", type=int, required=True)
    a.add_argument("--cost", type=float, default=0.0)
    a.add_argument("--notes", default="")
    a.add_argument("--file", default=None)
    a.add_argument("--lock", action="store_true", help="exclusive file lock while writing (POSIX)")
    a.add_argument("--dry-run", action="store_true")
    s = sub.add_parser("summary")
    s.add_argument("--file", default=None)
    args = ap.parse_args(argv)
    try:
        if args.selftest:
            return selftest()
        if args.cmd == "add":
            row = add(args.file or default_file(), args.agent, args.task, args.path,
                      args.tokens, args.cost, args.notes, dry_run=args.dry_run, lock=args.lock)
            print(("dry-run: " if args.dry_run else "logged: ") + ",".join(str(row[k]) for k in FIELDS))
            return 0
        if args.cmd == "summary":
            print_summary(summary(args.file or default_file()))
            return 0
    except LogError as e:
        print(f"token_log: error: {e}", file=sys.stderr)
        return 2
    ap.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
