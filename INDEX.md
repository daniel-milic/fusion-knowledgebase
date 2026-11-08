# Index

Entry point for AI navigation. Find the row that matches the request, open that file, then open only what it links to.

| If the request is about... | Open |
|---|---|
| Which platforms exist, by domain | [PLATFORMS.md](PLATFORMS.md) |
| A test scenario: what it covers and which platforms it touches | [fusion/scenarios/README.md](fusion/scenarios/README.md) |
| Create, update or maintain a scenario (runsheet) | [fusion/scenarios/runsheet.md](fusion/scenarios/runsheet.md) |
| Scenario JSON: root fields and the tasks list | [fusion/scenarios/scenario-document.md](fusion/scenarios/scenario-document.md) |
| Task definitions (`task_def`), field values and overrides | [fusion/scenarios/tasks.md](fusion/scenarios/tasks.md) |
| `job.json`: how a task becomes a script run | [fusion/run-status/job-json.md](fusion/run-status/job-json.md) |
| Test run execution: `run_status`, task and scenario statuses | [fusion/run-status/README.md](fusion/run-status/README.md) |
| Test runs and run execution ids (`5X12`) | [fusion/run-status/test-runs.md](fusion/run-status/test-runs.md) |
| Datastore (`#` references, values shared between tasks) | [fusion/run-status/datastore.md](fusion/run-status/datastore.md) |
| Checkpoints, flags, statuses, baselines, Alerts | [fusion/run-status/checkpoints-and-baselines.md](fusion/run-status/checkpoints-and-baselines.md) |
| MongoDB collections, fields, relationships | [fusion/database.md](fusion/database.md) |
| How users create scenarios, test runs, tasks | [fusion/user-interactions.md](fusion/user-interactions.md) |
| Fusion overview and high-level flow | [fusion/README.md](fusion/README.md) |
| The fusion-scripts repo: `process` path to script, patterns | [fusion/scripts-repo.md](fusion/scripts-repo.md) |
| A platform (business rules, timings, integrations) | `platforms/<domain>/<platform>/README.md` |
| A page, wizard or API on a platform | `platforms/<domain>/<platform>/<page>.md` |
| This knowledge base: layout, depth, size rules, skills, collection scripts | [management/README.md](management/README.md) |

## Routing rule
1. Read this file.
2. Open the one matching row.
3. Open a platform README only when the request names a platform, then a page file only when it names a page.
