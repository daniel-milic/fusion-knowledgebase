# Scenario Runsheet

How to create, update and maintain scenarios. Nothing is written to the Fusion MongoDB database from this knowledge base or from Copilot. Copilot prepares the content; a script on the Dev VM applies it.

## Which route
New scenarios and new tasks get a `sid` and `tid` from the backend, so they go through the backend API. Only value changes to tasks that already exist can update the scenario document directly.

| Change | Route | Script |
|---|---|---|
| Create a new scenario | Backend API (assigns the `sid` and every `tid`) | *(to document)* |
| Add a task to an existing scenario | Backend API (assigns the `tid`) | *(to document)* |
| Change values in an existing task (field values, `run`, and so on) | Update the scenario document directly | *(to document)* |

Each operation has its own script. All are run on the Dev VM.

## Before any change
1. Read the files listed under Key references in `AGENTS.md`.
2. For each task, choose the task definition (`tdid`) and check its `process` is a real `<domain>.<platform>.<page>` with a script at `fusion-scripts/regression/<domain>/<platform>/<page>/run_job.py` ([../scripts-repo.md](../scripts-repo.md)).
3. Check each field `id` exists in the task definition, and set values using the rules in [tasks.md](tasks.md). Leave out fields you want to be absent; use `''` to override a default so the script ignores the field.
4. Keep the scenario end to end: early tasks create the data, later tasks act and verify ([README.md](README.md)).
5. Check `reference` is unique and follows the convention in [scenario-document.md](scenario-document.md).

## Create a new scenario
1. Prepare the scenario content: root fields and the ordered tasks (`tdid`, `process`, `menu`, `description`, `fields`). Do not set `_id` or `tid`, because the backend assigns them (confirm what the script expects).
2. Run the create script on the Dev VM.
3. Record the `sid` and `tid`s it returns.
4. Write `<scenario-id>.md` from `management/templates/scenario.md`, with the ordered tasks and script paths.
5. Regenerate the scenarios index with `management/scripts/fusion/`.
6. Check the scenario and its tasks in Fusion web.

## Add a task to an existing scenario
1. Prepare the new task entry and its position in the order.
2. Run the add-task script on the Dev VM. The backend assigns the `tid`.
3. Record the new `tid`, and update the task list in `<scenario-id>.md`.
4. Check the scenario in Fusion web.

## Change values in an existing task
1. Edit the task's field values in the scenario JSON, using the same `tid`.
2. Run the update script on the Dev VM.
3. Update `<scenario-id>.md` if the purpose, platforms or gaps changed.
4. Check the scenario in Fusion web.

To stop a task running without removing it, set `run` to `unchecked` (a value change).

## Maintaining scenarios
- Keep `<scenario-id>.md` in step with the scenario in Fusion. Regenerate the index after any change.
- Record coverage gaps in the scenario file.
- When a task definition has several versions, pick the right `tranche` ([tasks.md](tasks.md)).
- Do not change other collections (`task_def`, `test_runs`, `run_status`, `baseline`) unless a scenario change requires it.

## To document
- The name, location and arguments of each script, and the input format each expects
- Whether removing or reordering tasks, deleting a scenario, and changing root fields (for example `description` or `reference`) go through the API or a direct update
- How to confirm a change worked beyond checking Fusion web
