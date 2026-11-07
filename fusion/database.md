# Fusion Database (MongoDB)

Map of the collections. Detail is in the folder for each.

| Collection | Holds | Detail |
|---|---|---|
| `scenarios` | Scenario definitions | [scenarios/](scenarios/) |
| `task_def` | Task definitions | [scenarios/tasks.md](scenarios/tasks.md) |
| `test_runs` | All test runs | [run-status/test-runs.md](run-status/test-runs.md) |
| `run_status` | Per-scenario execution record: scenario, datastore, checkpoints, tasks | [run-status/](run-status/) |
| `baseline` | Expected results and baseline status per scenario | [run-status/checkpoints-and-baselines.md](run-status/checkpoints-and-baselines.md) |

## Relationships
- Scenario → task → script
- Test run → selected scenarios → one `run_status` document each
- `run_status` checkpoints are compared with `baseline` by `sid`, `tid` and checkpoint name
- `sid` and `tid` are the MongoDB `_id` as hex text
- Baseline images are stored in an Azure file share, not in MongoDB

## To document
- Fields of `scenarios`, `task_def`, `test_runs`, `run_status` and `baseline` (sample documents to come)
