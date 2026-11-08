# Scenario Document (`scenarios` collection)

One document per scenario. Example used below: reference `AA-INS--MP-S07`, "Member Portal [Insurance Claim IP]".

## Root fields
| Field | Example |
|---|---|
| `_id` | MongoDB id; `sid` is its hex text |
| `reference` | `AA-INS--MP-S07` (see Reference convention) |
| `scenario_idx` | `24142` |
| `description` | `Member Portal [Insurance Claim IP]` |
| `domain` | `Advice and Administration` |
| `stream` | `Insurance` |
| `test_set` | `Claims` |
| `test_plan` | `P1 Regression` |
| `priority` | `Critical` |
| `assignment` | `Released` |
| `jira` | `SS-5823` |
| `tc` | `88488,AAT-862` (comma-separated test case references) |
| `Status`, `Purpose`, `comment` | empty in the example |
| `tasks` | ordered list of tasks (below) |

`domain` is Fusion's own label. It does not have to match the folder names under `platforms/`.

## tasks list
Tasks are in execution order. Each entry:

| Key | Meaning |
|---|---|
| `tid` | Task id, hex text. Unique to this task entry |
| `tdid` | `_id` of the task definition in `task_def` |
| `process` | Dot path to the script, e.g. `sonata.sbs.api-service` `<domain>.<platform>.<page>` (see [../scripts-repo.md](../scripts-repo.md)) |
| `menu` | The page or API operation, e.g. `rest/sbs/clientService/createClient` or `Insurance Menu / Claims / Claim Notification` |
| `description` | Short label for the task (not on every task) |
| `fields` | List of `{id, value}`. `id` is the field id in the task definition. Overrides the definition's default (see [tasks.md](tasks.md)) |
| `run` | `checked` or `unchecked`. `unchecked` tasks stay in the scenario but are skipped in a run ([tasks.md](tasks.md)) |
| `tranche` | Which version of a task definition this is, e.g. `Tranche 2` |
| `Handover` | `checked` keeps the next task on the same agent |

`Cluster` also appears; no framework reference has been found, so it may be particular to one script.

Other keys seen, meaning to confirm: `lang` (`py`), `wsdl`, `date`, `next-row-id`, `scenario-idx`.

## Reference convention
`reference` is unique and set by the user. The scenarios page in Fusion web sorts by it. It is built from abbreviations, usually stream, test set and scenario index, e.g. `AA-INS-MP-S07`:
- `AA` Advice & Admin
- `INS` Insurance
- `MP` Member Portal
- `S07` scenario 7. The `S` keeps the list in alphanumeric order

Stream is usually the platform name. Stream and test set are both abbreviated, e.g. Member Portal `MP`, Term Deposit `TD`. Sometimes a test set index (`001`, `002`) is used as well or on its own.

The sample's `AA-INS--MP-S07` has an extra hyphen and does not follow the convention.

## Example shape
`AA-INS--MP-S07` has 26 tasks. The first tasks use Sonata APIs to create the conditions (create client, create account, cash receipt, contribution). Later tasks add insurance and a claim in Sonata, the Member Portal and Sonata Orchestrator, and the last task is an Account Enquiry that verifies the result.

## To document
- Meaning of `date`, `next-row-id`, `scenario-idx` and `wsdl`
- Whether the scenario markdown file is named by `reference`, `scenario_idx` or `_id`
