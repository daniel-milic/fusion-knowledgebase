# Tasks

A task is the executable unit of a scenario. A scenario's task entry (see [scenario-document.md](scenario-document.md)) points at a task definition in `task_def` through `tdid`, and the `process` field says which script runs it.

## What a task does
Any combination of:
- **Test data:** create the conditions the scenario needs
- **Actions:** perform the steps
- **Verify outcome:** check results

Verification is often in the same task that performs the action.

## Task definition (`task_def`)
One document per kind of task, e.g. Create a Client (`menu`: `clientService/createClient`).

| Key | Meaning |
|---|---|
| `_id` | The `tdid` used by scenarios |
| `process` | Dot path to the script, e.g. `sonata.sbs.api-service` |
| `application` | e.g. `Sonata SBS` |
| `description`, `menu` | Name and page or operation |
| `lang` | e.g. `py` |
| `fields` | The task's fields (below) |

### Field keys
| Key | Meaning |
|---|---|
| `id` | Number, unique within the definition. Scenario fields refer to it |
| `name` | The key given to the script. For APIs it is a dotted path with array indexes, e.g. `client.address.0.line1`. A suffix such as `$int` appears on some names (e.g. `id$int`); it seems to mark the type (to confirm) |
| `label`, `description` | Shown to the person editing the scenario |
| `group` | `Request`, `Checkpoint` or `Datastore`; no group means a task setting such as `sbs-format` (`json` or `xml`) |
| `list_box` | Allowed values, one per line. May be `code:label` pairs, or `Checkbox` |
| `hide` | Hides the field in the editor |
| `page` | The editor tab the field appears on |
| `value` | Default value |

### Field groups
| Group | `name` | `value` |
|---|---|---|
| `Request` | Input to the web page, Sonata page or API | The input value |
| `Checkpoint` | What is checked | The flag: `Blocked` or `Fail`; some checkpoints also allow `Info` (see [../run-status/checkpoints-and-baselines.md](../run-status/checkpoints-and-baselines.md)) |
| `Datastore` | A response field to keep, e.g. `client.id$int` | The `#reference` to save it under, e.g. `#client1` (see [../run-status/datastore.md](../run-status/datastore.md)) |

## Which value is used
For each field in the task definition:
1. If the scenario's task entry has a field with the same `id` and a `value`, that value is used, even if it is `''`.
2. Otherwise the definition's default `value` is used.
3. If neither has a value, the field is not provided when the test run is created.

The result, grouped by `group`, is the task's `job.json` ([../run-status/job-json.md](../run-status/job-json.md)).

Example (Create a Client): the scenario sets field 11 (forename) to `#randomstr1`, which replaces the default `GN1`. Field 12 (second forename) has no value anywhere, so it is not provided.

## Value forms seen in scenario fields
| Form | Examples | Notes |
|---|---|---|
| `#name` | `#randomstr1`, `#MOBILE`, `#client1`, `#acc1`, `#dob` | Datastore references or generated values. They stay as `#` tokens in `job.json` |
| Age | `44yo` | Becomes a date of birth in `job.json` (`1982-10-26`) |
| Relative date | `d-127`, `d-24:Friday`, `today` | Meaning to confirm |
| `@name` | `@Emp1-number` | Meaning to confirm |
| Checkbox | `checked`, `unchecked` | |

## To document
- Meaning of the `d-<n>`, `d-<n>:<weekday>` and `@name` forms
- Why some scenario fields with a `Checkbox` list (ids 29, 34, 35, 38 in Create a Client) do not appear in that task's `job.json` `Request`, and why a field set to `''` is also absent
- The effect of the `Info` flag
- Environment differences (TEST, DEV, PPD)
