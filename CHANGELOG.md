# Changelog

All notable changes to this skill are documented in this file (Maintenance rule, section 18 of `SKILL.md`).

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Each entry says what changed, why, and the estimated savings when there are any.
There are no releases yet; everything lives under `[Unreleased]`, grouped by date.

## [Unreleased]

### Changed (2026-10-02, after QA review)
- Captcha / anti-bot block now always means "stop and hand off to a human, or use the official API" (SKILL.md cost ladder, pre-browser checklist, tool table, decision flowchart, all READMEs, `checklists/before-browser.md`). Why: the old wording could be read as "use computer use to get past a captcha", which contradicted the no-bypass rule. Computer use stays for sign-ins (a human completes 2FA), exceptions, and UIs with no API or scriptable DOM.
- Internal script, file and item names replaced with generic ones (`queue.py next --country`, `record_step.py`, `board.py`, `google_api.py`, `video-cli`, `qa.sh`, `FINAL-COMMAND.md`, quota-lock file, script cards, `<ITEM_ID>`). Why: public repo; no names from the real operation.
- `READMEs/README.en.md` removed (the source pattern does not link it from the selector); README wording now says 14 translations plus the English original.
- Banner recompressed to a 256-color optimized PNG (512 KB to 93 KB, same 1280x605). Why: faster README load.
- `CHANGELOG.md` switched to Keep a Changelog format.

### Fixed (2026-10-02, after QA review)
- `scripts/token_log.py`: one-line errors (exit 2) instead of tracebacks for negative values, a missing directory and malformed CSVs; `nan`/`inf` costs rejected; appending to a file without a trailing newline no longer glues two rows together; values starting with `=`, `+`, `-`, `@` (or tab/CR) are prefixed with `'` so spreadsheets do not run them as formulas.

### Added (2026-10-02)
- `token_log.py --lock`: optional exclusive file lock for agents sharing one log. Tests for every edge case above (10 tests).
- Initial skill: cost ladder, pre-browser checklist, "turn it into a script" rule, batches, cheap reading, quota guardrails, bot-to-bot messages, metric (`scripts/token_log.py` + `templates/token-log.csv`), anti-patterns, decision flowchart and the permanent Maintenance rule. Estimated savings: most repeated tasks drop from screenshot-driven sessions to a single script call.
- Browser automation tools section (browse CLI, Browser Use, Playwright, Selenium) and a ban on anti-bot evasion tools for Instagram/WhatsApp.
- Anti-block posture for IG/WhatsApp: official API first; otherwise conservative automation with human approval of every send.
- Quick cheap-vs-expensive examples (`SKILL.md` §4, `examples/flows.md`) and checklists (before the browser, new script, IG/WhatsApp send).
- README in 15 languages (English original + 14 translations) following the owner's pattern (`README.md` + `READMEs/README.<locale>.md`), banner at `assets/banner.png`.

### Changed (2026-10-02)
- Repo switched to English by default (owner's rule): `SKILL.md`, `CHANGELOG.md`, checklists and examples translated; only the README keeps translations.
