---
name: research-staffing
description: Orchestrate a human-controlled staffing workflow for a short-term research team.
---

# Research staffing workflow

Run the five workflow stages in sequence. At the beginning, read `CLAUDE.md`, `config/workflow.example.json`, and `docs/responsible-use.md`.

## Non-negotiable controls

- Work only with fictional or properly redacted records.
- Use non-identifying `candidate_id` values in analytical outputs.
- Do not request or process résumés, birth dates, home addresses, photographs, government identifiers, or protected characteristics.
- Never infer missing evidence.
- Stop for explicit human approval before publication, invitations, selection, rejection, or onboarding communication.
- Do not send an external message unless a separately configured private integration requires and records approval.

## Sequence

1. Run `/phase0-project-setup` and obtain approval for the staffing brief.
2. Run `/phase1-job-posting` and obtain approval for each publication draft.
3. Run `/phase2-candidate-screening` on redacted evidence profiles, then ask a human to decide the shortlist.
4. Run `/phase3-interview-coordination` and obtain approval for proposed invitations.
5. Run `/phase4-selection-handoff` after the named decision owner records the outcome.

At every transition, report completed artifacts, unresolved exceptions, the required decision, and the next stage. If an input contract is incomplete, stop and describe the missing field rather than continuing with an assumption.
