# Scenarios

"Scenario" always means a test scenario in Fusion. Most are end-to-end tests.

## Shape
A scenario is a sequence of tasks:
1. **First tasks** create the test conditions (test data).
2. **Last tasks** perform the actions and check the results (verify outcome).

See [tasks.md](tasks.md); each task can create data, act, and verify.

This folder holds definitions (`scenarios` and `task_def` collections). What happens when they are run, including statuses, is in [../run-status/](../run-status/).

## Index
One line per scenario. Each scenario has its own file, `<scenario-id>.md`, in this folder, based on `management/templates/scenario.md`.

Generate this table from Fusion with the scripts in `management/scripts/fusion/`; do not maintain it by hand.

| Scenario | Summary | Platforms |
|---|---|---|
| | | |
