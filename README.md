<h1 align="center">grokbot-economy</h1>

<p align="center">
  <strong>A permanent skill that makes every Grok Bot work through ready-made, deterministic paths and stop burning tokens.</strong><br />
  <em>Commands stay in English so they can be copied exactly.</em>
</p>

<p align="center">
<a href="https://github.com/wesleysimplicio/grokbot-economy/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/wesleysimplicio/grokbot-economy?style=flat-square" /></a>
<img alt="Grok Bot skill" src="https://img.shields.io/badge/Grok%20Bot-skill-2fe6a0?style=flat-square" />
<img alt="SKILL.md English" src="https://img.shields.io/badge/SKILL.md-English-0ea5e9?style=flat-square" />
<a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-yellow?style=flat-square" /></a>
</p>

<p align="center">
<a href="README.md">English</a> | <a href="READMEs/README.pt-BR.md">Português</a> | <a href="READMEs/README.es-ES.md">Español</a> | <a href="READMEs/README.ja-JP.md">日本語</a> | <a href="READMEs/README.ko-KR.md">한국어</a> | <a href="READMEs/README.zh-CN.md">简体中文</a> | <a href="READMEs/README.it-IT.md">Italiano</a> | <a href="READMEs/README.fr-FR.md">Français</a> | <a href="READMEs/README.ru-RU.md">Русский</a> | <a href="READMEs/README.pl-PL.md">Polski</a> | <a href="READMEs/README.hi-IN.md">हिन्दी</a> | <a href="READMEs/README.ar-SA.md">العربية</a> | <a href="READMEs/README.he-IL.md">עברית</a> | <a href="READMEs/README.ms-MY.md">Bahasa Melayu</a> | <a href="READMEs/README.id-ID.md">Bahasa Indonesia</a>
</p>

<p align="center">
  <img src="assets/banner.png" alt="Abstract cost ladder: cheap scripted steps on the left, expensive computer use on the right" width="860" />
</p>

---

## The short version

`grokbot-economy` is a skill for Grok Bot, an LLM desktop assistant with a shell, file reads, MCP connectors, plugins, a box browser, the `browse` CLI and screenshot-driven computer-use subagents. It tells the bot to **plan, review and handle exceptions with the LLM, and execute with code**: repeated work becomes a script, batches go through CSV/JSON, the browser is a last resort, paid credits need the owner's OK, and bot-to-bot messages stay short.

The skill itself (`SKILL.md`) and the rest of the repository are in English. Only this README is translated, into 15 languages.

## Install

1. **Easiest:** in a Grok Bot chat, ask the bot to save it as a skill:

   ```text
   Save the skill at this URL as a skill named grokbot-economy, keeping its description: https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md
   ```

2. **Manual:** copy all of `SKILL.md` (frontmatter included) into the bot's skill editor, or paste it in chat and ask the bot to save it as a skill.
3. **Agents that read skill folders** (Cursor/Claude style):

   ```bash
   mkdir -p <skills-dir>/grokbot-economy && curl -fsSL https://raw.githubusercontent.com/wesleysimplicio/grokbot-economy/main/SKILL.md -o <skills-dir>/grokbot-economy/SKILL.md
   ```

Then invoke it with `/grokbot-economy` or mention it in routines. Its description makes bots load it at the start of any task, before opening the browser, before repeating a task and when messaging other bots.

## Principles

| # | Path | Use it for |
|---|---|---|
| 1 | Script/CLI | anything that already has a script |
| 2 | MCP | Drive, Gmail, GitHub, Calendar... |
| 3 | Plugin/skill | ready-made third-party recipes |
| 4 | API | services without a connector |
| 5 | `browse` CLI (text/DOM) | sites without an API, read as text |
| 6 | Computer use (screenshots) | only sign-in (a human completes 2FA), exceptions, UIs with no API or scriptable DOM; captcha/anti-bot block → stop and hand off to a human, or use the official API |

- **The LLM plans; code executes.** A task seen twice becomes a script with `--dry-run`, idempotency and a test.
- **Pre-browser checklist:** script? connector? plugin? API? can `browse` do it by text?
- **Batches via CSV/JSON + script**, never field by field in a UI; report only failures.
- **Cheap reading:** `rg` + offset/limit reads, no full dumps, no re-reading, no sleep/poll loops.
- **Money guardrails:** never spend paid credits (TTS over quota, clipping credits, ads) without the owner's explicit OK; respect quota lock files.
- **Safe file edits:** dry-run, test on copies, backup + atomic swap, file locks, small diffs.
- **Instagram/WhatsApp:** official API first; otherwise conservative, human-paced, human-approved sends; no anti-bot evasion tools; stop at the first warning.
- **Bot-to-bot messages:** short, point to file paths, batch items, no ack-only messages.
- **Right-sized model:** low effort for mechanical work, high effort only for judgment; long jobs in the background.

## Repository contents

| File | What |
|---|---|
| [`SKILL.md`](SKILL.md) | The skill: cost ladder, checklists, browser tool options, anti-patterns, decision flowchart, maintenance rule |
| [`CHANGELOG.md`](CHANGELOG.md) | Every change to the skill, with the reason and estimated savings |
| [`examples/flows.md`](examples/flows.md) | Concrete flows: spreadsheet, Drive, coordination board, videos, batches, sends |
| [`checklists/`](checklists/) | Before the browser, new script, Instagram/WhatsApp send |
| [`scripts/token_log.py`](scripts/token_log.py) | Append-only tokens/cost-per-task logger (stdlib, `--selftest`) |
| [`templates/token-log.csv`](templates/token-log.csv) | Metric template (CSV header + examples) |
| [`tests/`](tests/) | Unit tests for the logger |
| [`assets/banner.png`](assets/banner.png) | README banner |

## Measure it

Log tokens/cost per task and the path used. If `browse` or `computer-use` dominate the summary, a script is missing.

```bash
python3 scripts/token_log.py add --agent "<bot>" --task "<task>" --path script --tokens 1200 --cost 0
python3 scripts/token_log.py summary
python3 scripts/token_log.py --selftest && python3 -m unittest discover -s tests
```

## Contributing

- Found a cheaper path (new script, connector, API, plugin, CLI flag)? Open a PR changing `SKILL.md` **and** add a line to `CHANGELOG.md` (date, what, why, estimated savings). This is a permanent rule for all bots.
- Keep `SKILL.md` short (< ~250 lines), imperative and in English.
- **Public repo:** no tokens, keys, emails, phone numbers, client names, file IDs, hostnames or internal URLs. Use placeholders like `<DRIVE_FILE_ID>`.
- Run the selftest and the unit tests before opening the PR.

## License

MIT. See [LICENSE](LICENSE).
