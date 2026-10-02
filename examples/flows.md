# Cheap flow examples

Real commands from our flow, with placeholders instead of sensitive data.
Check `--help` before using them: flags may have changed. If they did, update this file (SKILL.md §18).
Script and CLI names are generic (`queue.py`, `record_step.py`, `board.py`, `google_api.py`, `video-cli`, `qa.sh`). Map each one to the real tool in your runbook.

## 1. Control spreadsheet (`queue.py`)

❌ Expensive: open the spreadsheet in the browser, scroll, find the row, edit cell by cell, take screenshots.

✅ Cheap:
```bash
Q=<scripts-dir>/queue.py
python3 $Q next --country <COUNTRY> --all         # next actionable item and why the others are blocked
python3 $Q lock <ITEM_ID> --agent "<bot>"
python3 $Q show <ITEM_ID>                         # only the row you need
python3 $Q mark <ITEM_ID> --status "<new status>" --note "<1 line>" --agent "<bot>"   # backs up on its own
python3 $Q unlock <ITEM_ID>
```
When `record_step.py` exists, use it to write spreadsheet + board in a single call.
`queue.py` is the only way to edit the sales spreadsheet.

## 2. Drive (`google_api.py` / MCP connector)

❌ Expensive: Drive web UI, drag and drop, checking the folder with screenshots.

✅ Cheap:
- Check whether it already exists (idempotency): Drive connector search with `parentId = '<DRIVE_FOLDER_ID>' and title contains '<ITEM_ID>'`.
- Upload a **new** file: `UploadFile` (Drive connection, `destination.folderId = <DRIVE_FOLDER_ID>`) or `google_api.py` (OAuth) when available.
- Download: `DownloadFile` with `<DRIVE_FILE_ID>`.
- New **version** of the same file (e.g. the master spreadsheet): follow the runbook procedure; do not create a duplicate file.

## 3. Coordination board (Paperclip, `board.py`)

❌ Expensive: open the UI, read the whole card, paste logs into a comment.

✅ Cheap: `board.py` to read the **last N** comments and post **one** short comment:
`[<Project>/<COUNTRY>] <ITEM_ID>: <what changed> · next: <step> · proof: <path>`. Logs go to a file; the comment carries the path.

## 4. Videos (`video-cli` + `FINAL-COMMAND.md`)

❌ Expensive: one LLM per video, building the render command from memory, watching the video several times.

✅ Cheap:
```bash
video-cli validate <contract.yaml>
video-cli voice    <contract.yaml>     # hash cache: lines already generated do not call the API
video-cli check    <item-dir>          # concept, plan, licenses and layout in seconds
video-cli render   <contract.yaml>     # local backend, no cost
bash <scripts-dir>/qa.sh <item-dir>    # objective QA + one look at the contact sheet
```
Watermark-free final: run **exactly** the command in `<item-dir>/FINAL-COMMAND.md`.
If that file carries a "DO NOT DELIVER" warning, do not render or send.

## 5. Prospect batch

```text
list.csv ──> script cards batch ──> voice batch ──> visual batch + render ──> failure-only report
```
- One input CSV, one script per stage, every stage idempotent.
- The voice batch respects the quota-lock file and stops at the first 429.
- Report: `37/40 ok · failed: <ITEM_ID> voice 429 (resumes HH:MM), <ITEM_ID_2> render: missing asset`.

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

✅ `[Videos/<COUNTRY>] <ITEM_ID> render ok, QA ok · need: owner OK to send · preview: <path> · priority: yes (send at HH:MM)`
