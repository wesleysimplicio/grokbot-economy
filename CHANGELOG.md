# Changelog

Every change to the skill goes here (Maintenance rule, section 18 of `SKILL.md`).
Format: `YYYY-MM-DD · what changed · why · estimated savings`.

## 2026-10-02
- Initial version of the `grokbot-economy` skill: cost ladder, pre-browser checklist, "turn it into a script" rule, batches, cheap reading, quota guardrails, bot-to-bot messages, metric (`scripts/token_log.py`), anti-patterns and decision flowchart.
- Browser automation tools section (browse CLI, Browser Use, Playwright, Selenium) and a ban on anti-bot evasion tools for Instagram/WhatsApp.
- Anti-block posture for IG/WhatsApp: official API first; otherwise conservative automation with human approval of every send.
- Permanent Maintenance rule: new cheaper path → PR to this repo + a line in this file.
- Quick cheap-vs-expensive examples in `SKILL.md` §4 and `simplicio-video broll --check` before rendering.
- README in 15 languages following the owner's pattern in his other repos (`README.md` + `READMEs/README.<locale>.md`), banner at `assets/banner.png`.
- Repo switched to English by default (owner's rule): `SKILL.md`, `CHANGELOG.md`, checklists and examples translated; only the README keeps translations.
