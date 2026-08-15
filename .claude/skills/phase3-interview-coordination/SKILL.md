---
name: phase3-interview-coordination
description: Prepare human-approved interview options and maintain scheduling state.
---

# Phase 3: Interview coordination

Use the human-approved shortlist and role-based interviewer availability. Produce candidate-specific time options in the configured time zone.

Maintain these states: `options_required`, `approval_pending`, `invitation_ready`, `response_pending`, `confirmed`, `reschedule_required`, and `closed`.

Before an invitation is sent, show the human owner:

- candidate identifier;
- proposed time and time zone;
- interviewer roles;
- meeting format; and
- the exact message text.

Never expose one candidate's information to another candidate. Do not send or modify calendar events without explicit approval. When there is a conflict, propose alternatives and keep the prior appointment unchanged until a human confirms the replacement.
