# Little Yungho

Little Yungho is a reference implementation of an agent-assisted staffing workflow for short-term research teams. It translates a fragmented operating process—project intake, role publication, candidate assessment, interview coordination, and selection handoff—into a sequence of explicit, reviewable stages.

The project is designed as a portfolio demonstration of enterprise AI product judgment. It emphasizes human approval, deterministic state transitions, data minimization, and operational traceability rather than unattended hiring decisions.

> This repository contains fictional examples only. It is not affiliated with any employer, does not include applicant résumés or personal data, and must not be used as the sole basis for an employment decision.

## Product thesis

Recruiting automation is not primarily a text-generation problem. The difficult work is maintaining a reliable operating contract across several people, channels, and decision points. Little Yungho therefore separates:

- agent-assisted drafting and synthesis;
- deterministic workflow state and validation;
- explicit human approval before consequential actions; and
- private operational data from shareable process definitions.

## Workflow

| Stage | Responsibility | Required human control |
| --- | --- | --- |
| 0. Project setup | Define scope, dates, role requirements, and decision owners | Approve the staffing brief |
| 1. Role publication | Produce channel-appropriate copy from one approved brief | Approve every external post |
| 2. Candidate screening | Apply a job-related rubric to redacted candidate profiles | Review evidence and decide the shortlist |
| 3. Interview coordination | Propose interview windows and track responses | Confirm invitations before sending |
| 4. Selection handoff | Prepare a decision record and onboarding handoff | A named decision owner approves the outcome |
| Daily status | Summarize open actions, exceptions, and deadlines | No autonomous external messages |

The `/research-staffing` skill orchestrates the complete workflow. Each stage can also be invoked independently from `.claude/skills/`.

## Repository structure

```text
.claude/skills/             English agent instructions for the workflow
config/workflow.example.json
                            Safe, fictional configuration
examples/                   Redacted input and output contracts
tests/                      Deterministic privacy and schema checks
docs/                       Architecture and responsible-use notes
```

Runtime records, credentials, browser sessions, messages, and candidate documents are deliberately excluded from version control.

## Quick start

```bash
git clone https://github.com/bridgewright/little-yungho.git
cd little-yungho
python3 -m unittest discover -s tests -v
```

Open the repository in Claude Code and run:

```text
/research-staffing
```

Copy `config/workflow.example.json` to a private runtime location before adapting the workflow. Do not commit real candidate or company information.

## Design boundaries

- Candidate profiles must be redacted and limited to job-relevant evidence.
- Protected characteristics, photographs, birth dates, home addresses, and government identifiers are prohibited.
- The agent may summarize evidence and flag missing information; it may not make or communicate a final hiring decision.
- External publication, interview invitations, rejection notices, and selection messages require human approval.
- Integrations are represented as interfaces. No credentials or active production automation are included.

See [Architecture](docs/architecture.md), [Responsible use](docs/responsible-use.md), and [Security](SECURITY.md) before adapting the project.

## License

Source code and original documentation are available under the [MIT License](LICENSE). Third-party services and trademarks remain subject to their respective terms.
