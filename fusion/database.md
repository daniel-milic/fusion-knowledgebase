# Fusion Database (MongoDB)

## Collections
| Collection | Holds |
|---|---|
| `scenarios` | Scenario definitions |
| `task_def` | Task definitions |
| `test_runs` | Test runs |
| `run_status` | One document per scenario in a run: its tasks, datasets, checkpoints and their actual results |
| `baseline` | Expected result per checkpoint; key is `sid`, `tid`, checkpoint name |

## run_status document
Created for each scenario selected when a test run is created.
- Scenario fields
- Tasks list, with each task's datasets, ordered
- Checkpoints list: for each, `tid`, checkpoint name, value, status

The checkpoint values and statuses in `run_status` are the run's actual results. They are compared with `baseline`.

## Relationships
- Scenario → task → script
- Test run → selected scenarios → one `run_status` document each
- `sid` and `tid` are the MongoDB `_id` as hex text
- Baseline images are stored in an Azure file share, not in MongoDB

## To document
- Fields of `scenarios`, `task_def` and `test_runs`
- Fields of `baseline`
