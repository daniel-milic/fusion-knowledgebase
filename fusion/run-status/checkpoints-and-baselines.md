# Checkpoints and Baselines

Values are written exactly as they are cased in Fusion. Task and scenario statuses are in [README.md](README.md).

## Checkpoints
A checkpoint verifies a result inside a task. It has a name and a value, and is one of two types:
- **data:** a value on a web page, a Sonata page, or in an API response
- **image:** a captured image

Checkpoints are held in the `checkpoints` dict of the `run_status` document, by `tid` and checkpoint name. Their values and statuses are the run's actual results.

## Statuses
| Level | Values |
|---|---|
| Checkpoint | `FAIL`, `PASS`, `ALERT`, `BASELINE`, `TBT` |
| Baseline | `TBT`, `FAIL`, `PASS` |

- `BASELINE` (checkpoint): no expected value exists yet; the actual value is shown in Fusion web for a tester decision.
- `ALERT` (checkpoint): the value or image does not match the baseline's expected data or image; needs review.

## Flags
`Fail` and `Blocked` are flags, not statuses. Every checkpoint has one. A checkpoint that does not match is set to status `FAIL`; the flag decides what that does to the task and scenario:

| Flag | Effect of a mismatch |
|---|---|
| `Fail` | Scenario status is `FAIL`. The scenario continues until all tasks are complete |
| `Blocked` | Scenario status is `BLOCKED`. The task is set to `stopped` and the scenario does not continue |

In a task definition a checkpoint is a field in group `Checkpoint`. The field `name` is what is checked and its `value` is the flag, chosen from the field's list (`Blocked`, `Fail`). In `job.json` it appears as `"Checkpoint": {"<name>": "<flag>"}`; for example, Create a Client has `Verify Request Sent` and `Verify Response Received`, both `Fail` ([job-json.md](job-json.md)).

An `Info` flag still appears in some older task definitions. It is deprecated, because it does not affect the scenario status. Do not use it.

## Checkpoint values
The value set on a checkpoint in a task decides how it is checked:

| Value | Check |
|---|---|
| `Fail` or `Blocked` | A flag, not a status. Also a signal to look up the `baseline` for the expected value (see below) |
| Any other text | The actual result is compared with that text |
| A regular expression | The actual result is matched against it |
| A datastore reference, e.g. `#acc1` | The actual result is compared with the value saved under that reference ([datastore.md](datastore.md)) |

When the actual result matches, the checkpoint status is `PASS`. When it does not match, it is `FAIL`.

## How a baselined checkpoint is resolved
1. A task in a scenario sets a checkpoint's value to `Fail` or `Blocked`.
2. When a test run is created, the `run_status` document gets a `checkpoints` dict containing that checkpoint with that value.
3. Fusion looks in the `baseline` collection for the checkpoint's expected value.
4. **Expected value is set:** the actual result is compared with it.
   - Match: the checkpoint takes the status held in the baseline (`PASS` or `FAIL`).
   - No match (data value or image): the checkpoint status is `ALERT`.
5. **Expected value is not set:** the checkpoint goes into `BASELINE` status. Fusion web shows the actual value.

## Baseline collection
One document per scenario, found by scenario id (`sid`). It records the expected data results and the baseline status of each checkpoint. It is a separate collection today; it is planned to move into the scenario document.
- `checkpoints / <tid> / <checkpoint name> / expected` — the expected result
- status — `TBT`, `FAIL` or `PASS`

`sid` and `tid` are the MongoDB `_id` as hex text.

### Baselining (tester decision)
The tester decides whether the actual value is a pass or a fail. Fusion then sets the checkpoint's `expected` in the baseline document to the actual result, and its status to the decision (`PASS` or `FAIL`).

### Alerts
Fusion web lists every checkpoint in `ALERT` status. A tester reviews each one to decide whether it is a pass or a fail.

### Image baselines
Baseline images are stored in an Azure file share.

## To document
- Exact field names in the `baseline` and `run_status` documents (sample documents to come)
- What a tester's pass/fail decision on an Alert changes (the baseline, or only that run)
- How a checkpoint whose value is text, a regex or a datastore reference gets its flag (the sample task definition only shows flag lists)
- What `TBT` means, and when a checkpoint or baseline has it
