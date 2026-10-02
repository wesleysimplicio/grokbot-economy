#!/usr/bin/env python3
"""token_log.py: append-only log of tokens/cost per task (CSV). Stdlib only, no network.

Usage:
  python3 scripts/token_log.py add --agent BOT --task "render P0XX" --path script \
      --tokens 1200 [--cost 0.0] [--notes "..."] [--file token-log.csv] [--dry-run]
  python3 scripts/token_log.py summary [--file token-log.csv]
  python3 scripts/token_log.py --selftest

path must be one of: script, mcp, plugin, api, browse, computer-use.
Default file: $TOKEN_LOG_FILE or ./token-log.csv. The header is written once; rows are only appended.
"""
import argparse
import csv
import datetime as dt
import os
import sys
import tempfile

FIELDS = ["date", "agent", "task", "path", "est_tokens", "cost_usd", "notes"]
PATHS = ["script", "mcp", "plugin", "api", "browse", "computer-use"]


def default_file():
    return os.environ.get("TOKEN_LOG_FILE", "token-log.csv")


def add(file, agent, task, path, tokens, cost=0.0, notes="", date=None, dry_run=False):
    if path not in PATHS:
        raise ValueError(f"path must be one of {PATHS}")
    if tokens < 0 or cost < 0:
        raise ValueError("tokens and cost must be >= 0")
    row = {
        "date": date or dt.datetime.now().astimezone().isoformat(timespec="minutes"),
        "agent": agent, "task": task, "path": path,
        "est_tokens": int(tokens), "cost_usd": f"{float(cost):.4f}",
        "notes": notes.replace("\n", " "),
    }
    if dry_run:
        return row
    new = not os.path.exists(file) or os.path.getsize(file) == 0
    with open(file, "a", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        if new:
            w.writeheader()
        w.writerow(row)
    return row


def summary(file):
    tot = {}
    if not os.path.exists(file):
        return tot
    with open(file, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            t = tot.setdefault(r["path"], {"tasks": 0, "tokens": 0, "cost": 0.0})
            t["tasks"] += 1
            t["tokens"] += int(r["est_tokens"] or 0)
            t["cost"] += float(r["cost_usd"] or 0)
    return tot


def print_summary(tot):
    if not tot:
        print("(empty log)")
        return
    print(f"{'path':<13}{'tasks':>6}{'tokens':>10}{'cost_usd':>10}")
    for p in sorted(tot, key=lambda k: -tot[k]["tokens"]):
        t = tot[p]
        print(f"{p:<13}{t['tasks']:>6}{t['tokens']:>10}{t['cost']:>10.4f}")


def selftest():
    with tempfile.TemporaryDirectory() as d:
        f = os.path.join(d, "log.csv")
        add(f, "bot-a", "task 1", "script", 100, 0.0, "ok")
        add(f, "bot-a", "task 2", "computer-use", 5000, 0.05, "login\nwith 2fa")
        add(f, "bot-b", "task 3", "script", 50)
        assert add(f, "x", "dry", "api", 1, dry_run=True)["path"] == "api"
        with open(f, encoding="utf-8") as fh:
            lines = fh.read().splitlines()
        assert lines[0] == ",".join(FIELDS), lines[0]
        assert len(lines) == 4, lines  # header + 3 rows, dry-run not written, newline flattened
        tot = summary(f)
        assert tot["script"] == {"tasks": 2, "tokens": 150, "cost": 0.0}, tot
        assert tot["computer-use"]["tokens"] == 5000
        for bad in (lambda: add(f, "a", "t", "telepathy", 1), lambda: add(f, "a", "t", "api", -1)):
            try:
                bad()
                raise AssertionError("expected ValueError")
            except ValueError:
                pass
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
    a.add_argument("--dry-run", action="store_true")
    s = sub.add_parser("summary")
    s.add_argument("--file", default=None)
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest()
    if args.cmd == "add":
        row = add(args.file or default_file(), args.agent, args.task, args.path,
                  args.tokens, args.cost, args.notes, dry_run=args.dry_run)
        print(("dry-run: " if args.dry_run else "logged: ") + ",".join(str(row[k]) for k in FIELDS))
        return 0
    if args.cmd == "summary":
        print_summary(summary(args.file or default_file()))
        return 0
    ap.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
