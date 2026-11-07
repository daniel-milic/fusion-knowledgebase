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
| Test scenario | Fusion MongoDB | High-level end-to-end scenario |
| Test automation task | Fusion | Executable unit; contains its test data |
| Python script | fusion-scripts repo | Interacts with a page or API |
| Custom Python framework | fusion-scripts repo | Shared patterns and helpers |

## Files in this folder
- [scenarios/](scenarios/) — scenario index and one file per scenario
- [tasks.md](tasks.md) — tasks and the data they hold
- [database.md](database.md) — collections, fields, relationships
- [user-interactions.md](user-interactions.md) — creating scenarios, test runs, tasks
- [scripts-repo.md](scripts-repo.md) — fusion-scripts structure and patterns
