# Architecture

Little Yungho uses a stage-gated workflow rather than a single autonomous agent.

```text
Approved staffing brief
        ↓
Publication draft → human approval
        ↓
Redacted candidate profiles → evidence-based assessment → human shortlist
        ↓
Interview options → human-approved invitations
        ↓
Decision record → named approver → onboarding handoff
```

Each stage consumes a defined input, produces a structured output, and stops at a review gate. A stable `project_id` and non-identifying `candidate_id` connect records without exposing candidate names in analytical artifacts.

The repository contains the orchestration contract and safe examples. Production integrations and runtime data remain outside the public boundary.
