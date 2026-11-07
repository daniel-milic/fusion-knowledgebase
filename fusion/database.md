# Fusion Database (MongoDB)

## Collections
| Collection | Holds |
|---|---|
| `scenarios` | Scenario definitions |
| `task_def` | Task definitions |
| `test_runs` | Test runs |
| `run_status` | One document per scenario in a run: its tasks, datasets, checkpoints and their actual results |
| `baseline` | One document per scenario (`sid`) holding the expected result and status of each checkpoint |

## run_status document
Created for each scenario selected when a test run is created.
- Scenario fields
- Tasks list, with each task's datasets, ordered
- Checkpoints dict: for each checkpoint (by `tid` and name), value and status. A value of `Fail` or `Blocked` means look up the baseline

The checkpoint values and statuses in `run_status` are the run's actual results. They are compared with `baseline`.

## baseline document
One per scenario, found by `sid`.
- `checkpoints / <tid> / <checkpoint name> / expected` — the expected result
- status — pass or fail, as decided by a tester

## Relationships
- Scenario → task → script
- Test run → selected scenarios → one `run_status` document each
- `sid` and `tid` are the MongoDB `_id` as hex text
- Baseline images are stored in an Azure file share, not in MongoDB

## To document
- Fields of `scenarios`, `task_def` and `test_runs`
- Exact field names of `baseline` and `run_status` (sample documents to come)
