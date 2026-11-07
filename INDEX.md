# Index

Entry point for AI navigation. Find the row that matches the request, open that file, then open only what it links to.

| If the request is about... | Open |
|---|---|
| Which platforms exist, by domain | [PLATFORMS.md](PLATFORMS.md) |
| A test scenario: what it covers and which platforms it touches | [fusion/scenarios/README.md](fusion/scenarios/README.md) |
| Tasks and their test data | [fusion/tasks.md](fusion/tasks.md) |
| Checkpoints, baselines, pass/fail logic | [fusion/checkpoints-and-baselines.md](fusion/checkpoints-and-baselines.md) |
| MongoDB collections, fields, relationships | [fusion/database.md](fusion/database.md) |
| How users create scenarios, test runs, tasks | [fusion/user-interactions.md](fusion/user-interactions.md) |
| Fusion overview and high-level flow | [fusion/README.md](fusion/README.md) |
| The fusion-scripts repo: layout, patterns, where a script goes | [fusion/scripts-repo.md](fusion/scripts-repo.md) |
| A platform (business rules, timings, integrations) | `platforms/<domain>/<platform>/README.md` |
| A page, wizard or API on a platform | `platforms/<domain>/<platform>/<page>.md` |
| This knowledge base: layout, depth, size rules, skills, collection scripts | [management/README.md](management/README.md) |

## Routing rule
1. Read this file.
2. Open the one matching row.
3. Open a platform README only when the request names a platform, then a page file only when it names a page.
