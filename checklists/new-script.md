# Checklist: turn a repeated task into a script

- [ ] The task has shown up 2+ times (or will repeat in a batch).
- [ ] Is there a similar script to **extend**? (`rg -l` before creating another one)
- [ ] Input via CSV/JSON or arguments; no typing into a UI.
- [ ] `--help` with a 1–3 line usage example.
- [ ] `--dry-run` on everything that writes.
- [ ] Idempotent: running it twice does not duplicate anything (check before acting).
- [ ] Backup + write to a temp file + atomic swap for live files.
- [ ] Respects quota lock files and file locks; never spends paid credits without the owner's OK.
- [ ] Short output: summary + failures only.
- [ ] `--selftest` or a test in `tests/`, run and passing.
- [ ] No secrets in the code (read from env vars; never print them).
- [ ] Documented in the runbook (command + when to use it) and, if it made things cheaper, a PR to this skill + `CHANGELOG.md`.
