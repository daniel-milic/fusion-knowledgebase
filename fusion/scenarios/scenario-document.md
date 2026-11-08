# Scenario Document (`scenarios` collection)

One document per scenario. Example used below: reference `AA-INS--MP-S07`, "Member Portal [Insurance Claim IP]".

## Root fields
| Field | Example |
|---|---|
| `_id` | MongoDB id; `sid` is its hex text |
| `reference` | `AA-INS--MP-S07` |
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
| `run` | `checked` or `unchecked`. `unchecked` appears to mean the task is skipped (to confirm) |

Other keys seen, meaning to confirm: `lang` (`py`), `wsdl`, `date`, `tranche`, `Handover`, `Cluster`, `next-row-id`, `scenario-idx`.

## Example shape
`AA-INS--MP-S07` has 29 tasks. The first tasks use Sonata APIs to create the conditions (create client, create account, cash receipt, contribution). Later tasks add insurance and a claim in Sonata, the Member Portal and Sonata Orchestrator, and the last task is an Account Enquiry that verifies the result.

## To document
- Meaning of `date`, `tranche`, `Handover`, `Cluster`, `next-row-id`, `scenario-idx` and `wsdl`
- What `run: unchecked` does
