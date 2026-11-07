# fusion-knowledgebase

**Repository:** [daniel-milic/fusion-knowledgebase](https://github.com/daniel-milic/fusion-knowledgebase)  
**Purpose:** Self-documenting AI harness and knowledge base for the enterprise Superannuation tech stack (platforms, functionality, datasets, timings, integrations) and the Fusion test automation platform that validates it.

Enables AI (especially GitHub Copilot) to understand complex superannuation processes, map end-to-end regression coverage, develop and heal scripts, and maintain a unified view of both enterprise platforms and their corresponding test automation in the `fusion-scripts` repository.

> **About this knowledge base:**  
> This repository provides deep insight into the enterprise platforms alongside the Fusion test automation platform.  
> It is the foundation of a self-documenting AI harness that builds structured knowledge and develops the scripts needed to sew end-to-end test automation across complex superannuation processes.

## Navigation

- [PLATFORMS.md](PLATFORMS.md) — High-level platforms overview and integration paths
- [FUSION.md](FUSION.md) — Test automation platform (scenarios, tasks, datasets, MongoDB)
- [FRAMEWORK.md](FRAMEWORK.md) — Custom Python framework patterns
- [platforms/](platforms/) — Detailed platform documentation (pages, wizards, APIs, flows)
- [scripts/](scripts/) — Python scripts to retrieve and assemble knowledge from Fusion and other sources
- [skills/](skills/) — AI skills for documenting superannuation knowledge and maintaining automation

## Enterprise Context

Australian enterprise Superannuation fund with ~20 highly integrated platforms (member-facing and internal). Test automation supports SIT (IT squads) and UAT with end-to-end scenarios.

### Domains
- **Data and AI** — No test automation coverage currently
- **Digital** — All member-facing platforms
- **Advice and Admin** — Mostly internal (+ some member-facing calculators)
- **Enterprise Services** — Boomi centralised APIs

See [PLATFORMS.md](PLATFORMS.md) for details.
