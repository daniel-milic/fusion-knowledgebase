# Checkpoints and Baselines

Status and flag values are written here exactly as they are cased in Fusion.

## Checkpoints
A checkpoint verifies a result inside a task. It has a name and a value, and is one of two types:
- **data:** a value on a web page, a Sonata page, or in an API response
- **image:** a captured image

Actual results belong to a test run and are held on the run's `run_status` document (see [database.md](database.md)).

## Flags
Every checkpoint has a flag, `Fail` or `Blocked`. It decides what a mismatch does:

| Flag | On mismatch |
|---|---|
| `Fail` | Checkpoint status is `FAIL`. Scenario status is `FAIL`. The scenario continues until all tasks are complete |
| `Blocked` | Scenario status is `BLOCKED`. The task is set to `stopped` and the scenario does not continue |

For checkpoints checked against a baseline, the flag is the checkpoint's value (`Fail` or `Blocked`).

## Scenario status
The scenario status in the `run_status` document for that `sid` is determined by the sum of all checkpoints across all tasks in the scenario.

## Checkpoint values
The value set on a checkpoint in a task decides how it is checked:

| Value | Check |
|---|---|
| `Fail` or `Blocked` | The flag, and a signal to look up the `baseline` for the expected value (see below) |
| Any other text | The actual result is compared with that text |
| A regular expression | The actual result is matched against it |
| A datastore reference, e.g. `#acc1` | The actual result is compared with the value saved under that reference (see [datastore.md](datastore.md)) |

When the actual result matches, `run_status` sets `checkpoints / <tid> / <checkpoint name> / status` to `pass`.

## Other checkpoint statuses
| Status | Meaning |
|---|---|
| baseline | No expected value exists yet; the actual value is shown in Fusion web for a tester decision |
| Alert | The value or image does not match the baseline's expected data or image; needs review |

## How a baselined checkpoint is resolved
1. A task in a scenario sets a checkpoint's value to `Fail` or `Blocked`.
2. When a test run is created, the `run_status` document gets a `checkpoints` dict containing that checkpoint with that value.
3. Fusion looks in the `baseline` collection for the checkpoint's expected value.
4. **Expected value is set:** the actual result is compared with it.
   - Match: the checkpoint takes the status held in the baseline (pass or fail).
   - No match (data value or image): the checkpoint status is `Alert`.
5. **Expected value is not set:** the checkpoint goes into `baseline` status. Fusion web shows the actual value.

## Baselining (tester decision)
The tester decides whether the actual value is a pass or a fail. Fusion then updates the scenario's baseline document:
- `checkpoints / <tid> / <checkpoint name> / expected` = the actual result
- status = the tester's decision, pass or fail

The baseline document is found by scenario id (`sid`); `sid` and `tid` are the MongoDB `_id` as hex text. It records the expected values and the baseline status. It is a separate collection today; it is planned to move into the scenario document.

## Alerts
Fusion web lists every checkpoint in `Alert` status. A tester reviews each one to decide whether it is a pass or a fail.

## Image baselines
Baseline images are stored in an Azure file share.

## To document
- Exact field names in the `baseline` and `run_status` documents (sample documents to come)
- What a tester's pass/fail decision on an Alert changes (the baseline, or only that run)
- Where the flag is set for checkpoints whose value is text, a regex or a datastore reference
- The checkpoint status for a `Blocked` flag on mismatch
- Scenario status when all checkpoints pass, and when both `FAIL` and `BLOCKED` occur
- Task statuses other than `stopped`
