# Fusion — Test Automation Platform

Fusion is the test automation platform. Test scenarios are stored in its MongoDB database.

## High-level flow
```
Test Scenario (Fusion / MongoDB)
        ↓
Test Automation Task (holds its own test data)
        ↓
Python script in fusion-scripts
        ↓
Target platform page / wizard / API / flow
```

## Key concepts
| Concept | Storage / location | Description |
|---|---|---|
| Test scenario | Fusion MongoDB (`scenarios`) | Usually an end-to-end test; a sequence of tasks |
| Test automation task | Fusion MongoDB (`task_def`) | Executable unit; holds its test data, actions and checkpoints |
| Datastore | `run_status` document | Runtime values shared between a scenario's tasks, referenced as `#name` |
| Checkpoint | Within task | Verifies a result; type data or image |
| Test run | Fusion MongoDB (`test_runs`, `run_status`) | A selection of scenarios and their tasks; each execution has an id like `5X12` |
| Baseline | Fusion MongoDB (`baseline`); images in Azure file share | One document per scenario holding each checkpoint's expected result |
| Python script | fusion-scripts repo | Interacts with a page or API |
| Custom Python framework | fusion-scripts repo | Shared patterns and helpers |

## Contents
- [scenarios/](scenarios/) — scenario definitions: index, [scenario JSON](scenarios/scenario-document.md), and [tasks and task definitions](scenarios/tasks.md)
- [run-status/](run-status/) — test run execution: `test_runs`, `run_status` (scenario, datastore, checkpoints, tasks), statuses, [job.json](run-status/job-json.md), and baselines
- [database.md](database.md) — map of the collections and their relationships
- [user-interactions.md](user-interactions.md) — creating scenarios, test runs, tasks
- [scripts-repo.md](scripts-repo.md) — fusion-scripts structure and patterns
