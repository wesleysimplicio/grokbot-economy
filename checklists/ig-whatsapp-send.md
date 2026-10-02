# Checklist: Instagram DM / WhatsApp send

Before every send (one at a time):

- [ ] Is there a usable official API (WhatsApp Business Platform / Cloud API, Instagram Messaging API)? If yes, use it.
- [ ] The owner approved **this** video file for **this** recipient.
- [ ] The text is exactly an approved template. No price in proactive messages.
- [ ] The channel is allowed for this country/contact (local rules, do-not-contact requests).
- [ ] Recipient's business hours; under the daily cap; human-paced gap since the last send.
- [ ] Already signed in to the right account (do not sign out, do not switch accounts).
- [ ] Idempotency: is the video already in the conversation? Then **do not resend**; just record it.
- [ ] No anti-bot evasion tool (e.g. `undetected-chromedriver`) and no mass sending.
- [ ] Any warning, action block, challenge, captcha or "unusual activity"? **Stop** and hand off to a human.
- [ ] Afterwards: record it (spreadsheet/board via the script) and keep one proof (one screenshot).
