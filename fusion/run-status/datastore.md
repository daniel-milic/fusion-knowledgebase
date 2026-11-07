# Datastore

A datastore is a dict on a scenario's `run_status` document. It holds values created while the run executes, so later tasks in the scenario can use them.

- Each entry is `reference = value`.
- A reference always starts with `#`.
- A task saves a value under a reference; later tasks, and checkpoints, read it back by that reference.

## Example
1. Task 1 creates a member and saves the client id in the datastore.
2. Task 2 creates an account, retrieving the client id from the datastore.
3. The create-account API response returns the account number, and the task saves it as `#acc1`.
4. In the member portal landing-page script, the checkpoint `Verify Account Number` has the value `#acc1`. The script reads the account number from the page and compares it with `#acc1`.
5. If they match, `run_status` sets `checkpoints / <tid> / Verify Account Number / status` to `PASS`.

See [checkpoints-and-baselines.md](checkpoints-and-baselines.md) for checkpoint values.
