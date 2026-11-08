# Agent Instructions

## Purpose
This knowledge base provides the context required for GitHub Copilot (in VS Code) to create new Fusion end-to-end test scenarios and update existing ones for Aware Super. It covers Fusion scenario definitions, the Aware tech stack platforms under test, and their mappings to the separate `fusion-scripts` Python automation repository.

## Scope
- Work is limited to the Fusion MongoDB `scenarios` collection (and related task definitions).
- Do not modify other collections (`task_def`, `test_runs`, `run_status`, `baseline`, etc.) unless explicitly required for a scenario change.
- Platform documentation lives under `platforms/<domain>/<platform>/` and mirrors the structure of `fusion-scripts/regression/<domain>/<platform>/`.
- Scenario documentation lives under `fusion/scenarios/`.

## Scenario structure
Each scenario is represented by:
- A JSON document (the actual Fusion `scenarios` collection document)
- A matching Markdown file (`<scenario-id>.md`) based on `management/templates/scenario.md`

The Markdown file must include: purpose, platforms touched, ordered tasks (with script path references), and any coverage gaps.

## Creating or updating scenarios
1. Propose or edit the scenario JSON and its accompanying `.md` file under `fusion/scenarios/`.
2. Ensure tasks reference the correct script path in `fusion-scripts/regression/<domain>/<platform>/<page>`.
3. Keep the scenario as an end-to-end flow: early tasks set up test conditions and data; later tasks perform actions and verify outcomes.
4. Do not write directly to the Fusion MongoDB database from this knowledge base or from Copilot.

## Applying changes
All database updates must be applied on the Dev VM by running the designated update/apply script (provided separately). After the script runs successfully, regenerate the scenarios index if needed using the scripts under `management/scripts/fusion/`.

## Key references
Start at `INDEX.md` to find the right file before reading anything else. For scenario work, always read:
- `fusion/scenarios/README.md` and `management/templates/scenario.md` — scenario conventions
- `fusion/scripts-repo.md` — script mappings and patterns

## Constraints
- Stay within documented platform behaviour, timings, integrations, and existing automation patterns.
- Prefer generating or updating only what is required for a complete, runnable scenario.
- Do not invent business rules, field names, or script paths that are not present in the knowledge base or the `fusion-scripts` repository.
