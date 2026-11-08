# fusion-scripts Repository

Structure and conventions of the automation repo that Fusion tasks drive.

## Layout
## Process path to script
A task's `process` field is a dot path to its script. Replace the dots with slashes, put it under `regression/`, and add `run_job.py`:

| `process` | Script |
|---|---|
| `sonata.sbs.api-service` | `regression/sonata/sbs/api-service/run_job.py` |
| `digital.microsites.register` | `regression/digital/microsites/register/run_job.py` |
| `digital.member-portal.insurance.claims` | `regression/digital/member-portal/insurance/claims/run_job.py` |

The path is 3 or 4 levels deep. The first levels seen are `sonata` and `digital`. `run_job.py` reads the task's `job.json` ([run-status/job-json.md](run-status/job-json.md)).

Platform docs in this knowledge base follow these paths as closely as possible. Registry processes start with `sonata`, while the knowledge base groups Sonata under `platforms/advice-admin/sonata/`; how the two map is still to be confirmed.

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
