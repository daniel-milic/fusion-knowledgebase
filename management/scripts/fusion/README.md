# Fusion Knowledge Scripts

Scripts that connect to the Fusion MongoDB database to retrieve:

- Test scenarios
- Automation tasks
- Data and parameters held by those tasks
- Links between tasks and the Python scripts they drive

## Scripts
| Script | Does |
|---|---|
| `get_scenario.py <sid>` | Read-only. Retrieves the scenario and the `task_def` documents its tasks use, and writes `<sid>.json` and `tdids.json` |

Run scripts with `DATABASE_CONNECTION_STRING` set (and `DATABASE_NAME` if the database is not `qaas`).

These outputs feed documentation in this knowledge base and help Copilot understand current coverage when working in the `fusion-scripts` repo.
