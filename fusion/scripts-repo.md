# fusion-scripts Repository

Structure and conventions of the automation repo that Fusion tasks drive.

## Domains
The first level under `regression/` is the domain:

| Domain | Covers |
|---|---|
| `digital` | Digital (member-facing) platforms |
| `sonata` | Admin (the Sonata registry) |
| `advice` | Advice platforms |
| `investments` | Investments |

## Process path to script
A task's `process` field is a dot path: `<domain>.<platform>.<page>`. Replace the dots with slashes, put it under `regression/`, and add `run_job.py`:

| `process` | Script |
|---|---|
| `sonata.sbs.api-service` | `regression/sonata/sbs/api-service/run_job.py` |
| `digital.microsites.register` | `regression/digital/microsites/register/run_job.py` |
| `digital.member-portal.insurance.claims` | `regression/digital/member-portal/insurance/claims/run_job.py` |

The page part can be nested (`insurance/claims`). `run_job.py` reads the task's `job.json` ([run-status/job-json.md](run-status/job-json.md)).

Platform docs in this knowledge base use the same names: `platforms/<domain>/<platform>/`, with a page doc per page.

## Framework patterns
- Page object / component patterns
- API client patterns (Sonata, Experience Layer, Boomi)
- Reading task data
- Test data builders
- Assertions and verification helpers
- Logging, reporting, and evidence capture
- Environment configuration (SIT / UAT)
- Common utilities (dates, superannuation calculations, identifiers)
- Naming conventions and task linkage

> Goal: an AI reading this repo can generate a new script that matches existing patterns and links correctly to a task.
