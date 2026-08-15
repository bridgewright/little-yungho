---
name: phase2-candidate-screening
description: Organize job-related evidence from redacted candidate profiles without making a hiring decision.
---

# Phase 2: Candidate evidence review

Accept only structured, redacted profiles matching `examples/candidate-profile.example.json`. Do not accept or open a résumé, curriculum vitae, photograph, identification document, or unredacted application.

For each `candidate_id`:

1. Map submitted evidence to the approved rubric in `assets/evidence-rubric.md`.
2. Cite the supplied `source_reference` for every observation.
3. Mark a criterion `insufficient evidence` when support is absent or ambiguous.
4. Separate factual observations from reviewer judgment.
5. Return a comparison table and an exception list to the human reviewer.

Do not rank candidates using protected characteristics or proxies. Do not issue a selection or rejection recommendation. The accountable human reviewer decides the shortlist and records the rationale outside this public repository.
