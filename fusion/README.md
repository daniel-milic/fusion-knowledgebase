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
| Test scenario | Fusion MongoDB | Usually an end-to-end test; a sequence of tasks |
| Test automation task | Fusion | Executable unit; holds its test data, actions and checkpoints |
| Checkpoint | Within task | Verifies a result; type data or image |
| Baseline | Fusion MongoDB (baseline collection) | Expected result per scenario, task and checkpoint |
| Python script | fusion-scripts repo | Interacts with a page or API |
| Custom Python framework | fusion-scripts repo | Shared patterns and helpers |

## Files in this folder
- [scenarios/](scenarios/) — scenario index and one file per scenario
- [tasks.md](tasks.md) — tasks and the data they hold
- [checkpoints-and-baselines.md](checkpoints-and-baselines.md) — verifying results and baselining
- [database.md](database.md) — collections, fields, relationships
- [user-interactions.md](user-interactions.md) — creating scenarios, test runs, tasks
- [scripts-repo.md](scripts-repo.md) — fusion-scripts structure and patterns
