# Layout, Depth and Size Rules

## Layout
- Top level holds INDEX, README, PLATFORMS, `platforms/`, `fusion/` and `management/` only.
- Domain folders live under `platforms/` and mirror `fusion-scripts/regression/<domain>/`.
- Platform folders (`platforms/<domain>/<platform>/`) mirror `fusion-scripts/regression/<domain>/<platform>/`.
- Page and API docs sit in the platform folder, named after the script path, so the doc path can be worked out from the script path.
- One concern per file. Create a file only when it holds real content.
- Every platform README uses the same headings (see `templates/`).
- The platform list lives only in `PLATFORMS.md`. Do not repeat it in other indexes.
- Every file is linked from INDEX, PLATFORMS.md, or its folder's README.

## Depth
Document what a test or a developer needs, and no more.
- **Scenario:** purpose, platforms, tasks, gaps.
- **Platform:** purpose, business rules, timings, integrations, test data.
- **Page / API:** fields, validations, downstream calls. Only for pages with automation.
- **Stop when** a new test could be generated from the doc without guessing.

## Size
- Split any file that passes about 150 lines.
- Keep `INDEX.md` under about 40 lines.
- A folder with more than 5 files gets an index with one line per file.
- Generate long lists (scenarios, tasks) from Fusion with `management/scripts/`, not by hand.
