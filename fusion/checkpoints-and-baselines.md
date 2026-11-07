# Checkpoints and Baselines

## Checkpoints
A checkpoint verifies a result inside a task. It has a name and a value, and is one of two types:
- **data:** a value on a web page, a Sonata page, or in an API response
- **image:** a captured image

Actual results belong to a test run: they are stored on the run's `run_status` document (see [database.md](database.md)).

## Statuses
| Status | Meaning |
|---|---|
| Fail / Blocked | Reported when there is nothing to compare against; the value is the actual result |
| Baseline | Awaiting a user decision on whether the value is a pass or a fail |
| Alert | The value or image does not match the baseline; needs review |
| Pass / Fail | Final status |

## Baselining
A baseline records what a checkpoint should be, so later runs can be compared.

1. A run reports a checkpoint value of `Fail` or `Blocked`. The value is the **actual** result.
2. A Fusion web process sets the checkpoint to **baseline** status.
3. The user decides whether the value is a pass or a fail.
4. Fusion writes the result to the **baseline** collection, keyed by:
   - `sid` — scenario id
   - `tid` — task id
   - checkpoint name

   `sid` and `tid` are the MongoDB `_id` as hex text.
   - **Pass:** baseline status is pass, with `expected` equal to the value.
   - **Fail:** baseline status is fail, with the `expected` value set.
5. On the next run, if the value matches the baseline, the checkpoint takes the status the baseline holds (pass or fail).

## Mismatch and Alert
If a data value or an image does not match the baseline's expected data or image, the checkpoint status is set to **Alert**. Fusion web lists every checkpoint in Alert status, and a user reviews each one to decide whether it is a pass or a fail.

## Image baselines
Baseline images are stored in an Azure file share. Baseline records for image checkpoints point to them.

## To document
- Where the `expected` value for a fail baseline comes from
- Baseline collection fields
- What a user's pass/fail decision on an Alert changes (the baseline, or only that run)
