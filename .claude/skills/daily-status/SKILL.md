---
name: daily-status
description: Summarize workflow state, exceptions, deadlines, and required human actions.
---

# Daily status

Read private runtime state without copying it into the repository. Produce a summary matching `examples/status-summary.example.json`.

Report:

- counts by workflow state;
- deadlines within the configured review window;
- missing approvals or evidence;
- scheduling conflicts and overdue responses; and
- one clearly stated next human action.

Use candidate identifiers, not names. Do not include message bodies, contact information, evaluation details, or sensitive attributes. This skill creates a draft status artifact only; it does not post to chat, send email, or update a calendar autonomously.
