# Cheap flow examples

Real commands from our flow, with placeholders instead of sensitive data.
Check `--help` before using them: flags may have changed. If they did, update this file (SKILL.md §18).
CLI names and flags (`fila.py`, `--pais`, `marcar`...) are kept exactly as the tools define them.

## 1. Control spreadsheet (`fila.py`)

❌ Expensive: open the spreadsheet in the browser, scroll, find the row, edit cell by cell, take screenshots.

✅ Cheap:
```bash
F=<scripts-dir>/fila.py
python3 $F proximo --pais <COUNTRY> --todos      # next actionable item and why the others are blocked
python3 $F lock P0XX --agente "<bot>"
python3 $F ver P0XX                              # only the row you need
python3 $F marcar P0XX --status "<new status>" --obs "<1 line>" --agente "<bot>"   # backs up on its own
python3 $F unlock P0XX
```
When `registrar.py` exists, use it to write spreadsheet + board in a single call.
`fila.py` is the only way to edit the sales spreadsheet.

## 2. Drive (`gapi.py` / MCP connector)

❌ Expensive: Drive web UI, drag and drop, checking the folder with screenshots.

✅ Cheap:
- Check whether it already exists (idempotency): Drive connector search with `parentId = '<DRIVE_FOLDER_ID>' and title contains 'P0XX'`.
- Upload a **new** file: `UploadFile` (Drive connection, `destination.folderId = <DRIVE_FOLDER_ID>`) or `gapi.py` (OAuth) when available.
- Download: `DownloadFile` with `<DRIVE_FILE_ID>`.
- New **version** of the same file (e.g. the master spreadsheet): follow the runbook procedure; do not create a duplicate file.

## 3. Coordination board (Paperclip, `pc.py`)

❌ Expensive: open the UI, read the whole card, paste logs into a comment.

✅ Cheap: `pc.py` to read the **last N** comments and post **one** short comment:
`[<Project>/<COUNTRY>] P0XX: <what changed> · next: <step> · proof: <path>`. Logs go to a file; the comment carries the path.

## 4. Videos (`simplicio-video` + `FINAL-COMANDO.md`)

❌ Expensive: one LLM per video, building the render command from memory, watching the video several times.

✅ Cheap:
```bash
simplicio-video validate <contract.yaml>
simplicio-video voice    <contract.yaml>     # hash cache: lines already generated do not call the API
simplicio-video broll    <prospect-dir> --check   # concept, plan, licenses and layout in seconds
simplicio-video render   <contract.yaml>     # local backend, no cost
bash <scripts-dir>/qa_v2.sh <prospect-dir>    # objective QA + one look at the contact sheet
```
Watermark-free final: run **exactly** the command in `<prospect-dir>/FINAL-COMANDO.md`.
If that file carries a "DO NOT DELIVER" warning, do not render or send.

## 5. Prospect batch

```text
list.csv ──> fichas batch ──> voice batch ──> visual batch + render ──> failure-only report
```
- One input CSV, one script per stage, every stage idempotent.
- The voice batch respects the quota lock file and stops at the first 429.
- Report: `37/40 ok · failed: P0XX voice 429 (resumes HH:MM), P0YY render: missing asset`.

## 6. Sends (Gmail, Instagram DM, WhatsApp Web)

Always required first: **the owner's OK for that specific video** + an approved template text.

| Channel | Path | Notes |
|---|---|---|
| Gmail | MCP connector/API: draft → approval → send | never through the browser |
| WhatsApp | Official API (WhatsApp Business Platform / Cloud API) if the account has it; otherwise `browse` on the already signed-in session | human pace, daily cap, stop at the first warning |
| Instagram DM | Official API (Instagram Messaging API) if the account is eligible; otherwise `browse` on the already signed-in session | same; computer use only for sign-in/challenge, then hand off to a human |

First message (template example): `Your video is ready, here's the preview.` + the mp4 (not a link).
A single reminder after 3 days. Never a price in a proactive message.

**Honest risk:** IG/WA automation can get the owner's account blocked. Hence: one send at a time, human approval of each, no anti-bot evasion, no mass sending, and stop at the first warning.

## 7. Bot-to-bot message

❌ "Hi! How are you? So, as we discussed before, the context is... (40 lines)"

✅ `[Videos/<COUNTRY>] P0XX render ok, QA ok · need: owner OK to send · preview: <path> · priority: yes (send at HH:MM)`
