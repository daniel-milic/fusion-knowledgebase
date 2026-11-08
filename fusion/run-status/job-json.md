# job.json

How a task becomes a script run. When a scenario executes, the script for the task's `process` is launched and its `run_job.py` reads a `job.json`. The `job.json` is built from the scenario's task entry and the task definition (rules in [../scenarios/tasks.md](../scenarios/tasks.md)).

Example: `"process": "sonata.sbs.api-service"` runs `regression/sonata/sbs/api-service/run_job.py` (see [../scripts-repo.md](../scripts-repo.md)).

## Keys
| Key | Meaning |
|---|---|
| `app` | Application, e.g. `Sonata SBS` |
| `rx` | Run execution of this task: `<run>X<execution>S<scenario_idx>`. `28X190S24142` is run 28, execution 190, scenario S24142. The job needs this full form (see below) |
| `sid`, `tid`, `tdid` | Scenario id, task id, task definition id (hex text) |
| `job_id`, `task_idx` | Job number and the task's position in the scenario (`001` is first) |
| `process`, `menu`, `description` | From the task |
| `reference`, `scenario_idx` | From the scenario |
| `status` | Task status, e.g. `completed` ([README.md](README.md)) |
| `env` | Test environment, e.g. `TEST02` |
| `branch` | e.g. `main` |
| `Request` | The `Request` group fields: `{name: value}` |
| `Checkpoint` | The `Checkpoint` group: `{checkpoint name: flag}` |
| `Datastore` | The `Datastore` group: `{response field: #reference}` |
| Ungrouped fields | At the top level, e.g. `"sbs-format": "json"` |
| `agent`, `allocated-ts`, `allocated-time`, `completed`, `msg` | Who ran the task and when; `msg` was empty in the example |

## The rx
From Fusion's side the run execution is `28X190` ([test-runs.md](test-runs.md)). In a job the scenario id `S24142` is added, because the framework uses it to create unique given names and surnames for each run, so the data can be matched with expected values. The framework sometimes extracts the `28X190` part when it needs it.

## Example (Create a Client, shortened)
```json
{
  "app": "Sonata SBS",
  "rx": "28X190S24142",
  "sid": "678f33f57ff145673c1334a0",
  "tid": "678f33f57ff145673c1334a1",
  "tdid": "5f37a28e93f681198563bb1c",
  "task_idx": "001",
  "process": "sonata.sbs.api-service",
  "status": "completed",
  "env": "TEST02",
  "menu": "clientService/createClient",
  "sbs-format": "json",
  "Checkpoint": {"Verify Request Sent": "Fail", "Verify Response Received": "Fail"},
  "Datastore": {"client.id$int": "#client1"},
  "Request": {
    "client.clientDetails.forename": "#randomstr1",
    "client.clientDetails.dateOfBirth": "1982-10-26",
    "client.address.0.line1": "4 Bar Street"
  }
}
```

## To document
- Where `job.json` is stored in a run (it holds a task's dataset in `run_status`)
- How `#` tokens in `Request` are resolved at run time
- Whether other applications use the same shape (this sample is a Sonata API task)
