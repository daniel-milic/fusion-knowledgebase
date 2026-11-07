# Checkpoints and Baselines

## Checkpoints
A checkpoint verifies a result inside a task. It has a name and a value, and is one of two types:
- **data:** a value on a web page, a Sonata page, or in an API response
- **image:** a captured image

## Baselining
A baseline records what a checkpoint should be, per checkpoint, so later runs can be compared.

1. A run reports a checkpoint value of `Fail` or `Blocked`. The value is the **actual** result.
2. A Fusion web process sets the checkpoint to **baseline** status.
3. The user decides whether the value is a pass or a fail.
4. Fusion writes the result to the **baseline collection**, keyed by:
   - `sid` — scenario id
   - `tid` — task id
   - checkpoint name

   `sid` and `tid` are the MongoDB `_id` as hex text.
   - **Pass:** baseline status is pass, with `expected` equal to the value.
   - **Fail:** baseline status is fail, with the `expected` value set.
5. On the next run, if the checkpoint matches its baseline, it takes the status the baseline holds (pass or fail).

## To document
- What happens on a run when the value does not match the baseline
- Where the `expected` value for a fail baseline comes from
- Baseline collection fields
