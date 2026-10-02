# Checklist: before opening the browser

Answer in order. The first "yes" ends the checklist: use that path.

- [ ] **Ready script/CLI?** `ls <scripts-dir>` · `rg -l '<task>' <runbook-dir>` · `<cli> --help`
- [ ] **MCP connector?** List the server's tools (Drive, Gmail, GitHub, Calendar...) and use the one that fits.
- [ ] **Plugin/skill?** `browse skills find <domain>` or the installed skills.
- [ ] **Direct API?** `gh api`, the service's REST API, `UploadFile` / `DownloadFile`.
- [ ] **browse CLI by text?** `browse open <url> --session <task>` → `browse snapshot` / `browse get text body`.
- [ ] **Captcha or anti-bot block?** Stop and hand off to a human, or use the official API. Never use computer use to get past it.
- [ ] **Only computer use left?** (sign-in with a human completing 2FA, exceptions, UIs with no API or scriptable DOM) Write a closed goal ("sign in and stop"), a screenshot budget and the point where control returns to the script.

Afterwards: log the path you used with `scripts/token_log.py add ...`.
Did this by hand for the 2nd time? → "turn it into a script" rule (SKILL.md §3).
