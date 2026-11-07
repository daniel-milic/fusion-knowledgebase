# Tasks

A task is the executable unit of a scenario. It holds its own test data and links to a script in fusion-scripts.

## What a task does
Any combination of:
- **Test data:** create the conditions the scenario needs
- **Actions:** perform the steps
- **Verify outcome:** check results

Verification is often in the same task that performs the action.

## What a task contains
- **Fields and values** to input into a web page, a Sonata page, or an API. A value can read from the scenario's datastore (see [datastore.md](datastore.md))
- **Datastore saves:** a task can save runtime values (e.g. a client id or account number) under a `#reference` for later tasks
- **Checkpoints** to verify data on web pages, Sonata pages, or API responses (see [checkpoints-and-baselines.md](checkpoints-and-baselines.md))

## To document
- Task fields in `task_def` and how a task links to its script
- Environment differences (SIT / UAT)
