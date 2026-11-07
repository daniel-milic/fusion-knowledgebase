# Index

Entry point for AI navigation. Find the row that matches the request, open that file, then open only what it links to.

| If the request is about... | Open |
|---|---|
| Which platforms exist and which domain they sit in | [PLATFORMS.md](PLATFORMS.md) |
| A test scenario: what it covers, its steps, its platforms | [fusion/scenarios.md](fusion/scenarios.md) |
| Tasks, datasets, test data | [fusion/tasks-and-datasets.md](fusion/tasks-and-datasets.md) |
| MongoDB collections, fields, relationships | [fusion/database.md](fusion/database.md) |
| How users create scenarios, test runs, tasks | [fusion/user-interactions.md](fusion/user-interactions.md) |
| Fusion overview and high-level flow | [fusion/README.md](fusion/README.md) |
| The fusion-scripts repo: layout, patterns, where a script goes | [fusion/scripts-repo.md](fusion/scripts-repo.md) |
| A platform (business rules, timings, integrations) | `platforms/<domain>/<platform>/README.md` |
| A page, wizard or API on a platform | `platforms/<domain>/<platform>/<page>.md` |
| This knowledge base: skills, layout, depth, collection scripts | [management/README.md](management/README.md) |

## Domains
- [platforms/digital/](platforms/digital/) — member-facing platforms
- [platforms/advice-admin/](platforms/advice-admin/) — registry, CRM, advice, letters
- [platforms/enterprise-services/](platforms/enterprise-services/) — Boomi and shared services
- [platforms/data-ai/](platforms/data-ai/) — data and AI platforms (no automation coverage yet)

## Routing rule
1. Read this file.
2. Open the one matching row.
3. Open a platform README only when the request names a platform, then a page file only when it names a page.
