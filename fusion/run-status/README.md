# Run Status

Everything about executing tests: test runs, the per-scenario execution record, and baselines. Definitions of scenarios and tasks live in [../scenarios/](../scenarios/).

## Collections
| Collection | Holds | Detail |
|---|---|---|
| `test_runs` | All test runs | [test-runs.md](test-runs.md) |
| `run_status` | One document per scenario in a run: its tasks, datastore and checkpoints, with actual results | below |
| `baseline` | Expected results and baseline status per scenario | [checkpoints-and-baselines.md](checkpoints-and-baselines.md) |

## run_status document
Created for each scenario selected when a test run is created. It contains:
- **scenario:** the scenario fields and the scenario status
- **datastore:** runtime values shared between tasks, saved as `#reference = value` ([datastore.md](datastore.md))
- **checkpoints:** a dict by `tid` and checkpoint name, with value and status ([checkpoints-and-baselines.md](checkpoints-and-baselines.md))
- **tasks:** the ordered task list with each task's datasets, and the task status. Tasks with `run: unchecked` in the scenario are not added

The checkpoint values and statuses here are the run's actual results.

## Statuses
Written exactly as cased in Fusion. Checkpoint and baseline statuses are in [checkpoints-and-baselines.md](checkpoints-and-baselines.md).

| Level | Values |
|---|---|
| Task | `queued`, `allocated`, `executing`, `stopped`, `completed` |
| Scenario | `FAIL`, `PASS`, `BLOCKED`, `ALERT`, `BASELINE` |

### Scenario status
The scenario status for that `sid` is determined by the sum of all checkpoints across all tasks in the scenario. Where checkpoints disagree, the scenario takes the first of these that applies:

`ALERT` → `BASELINE` → `BLOCKED` → `FAIL` → `TBT` → `PASS`

- A scenario with status `FAIL` continues until all tasks are complete.
- A `Blocked`-flag checkpoint that does not match sets its task to `stopped` and the scenario to `BLOCKED`; the scenario does not continue (see [checkpoints-and-baselines.md](checkpoints-and-baselines.md)).

## To document
- Exact keys and field names of `run_status` (sample documents to come)
- How a `run_status` document is tied to a run execution (`RX`) and a `sid`
- Confirm the scenario status order reads highest priority first
