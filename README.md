# Rizon — Enterprise Superannuation Test Automation Knowledge Base

**Project:** Rizon  
**Purpose:** Self-documenting AI harness and knowledge base that provides deep insight into the enterprise tech stack (platforms, functionality, datasets, timings, integrations) and the Fusion test automation platform that validates it.

Enables AI to understand complex superannuation processes, map end-to-end regression coverage, develop and heal scripts, and maintain a unified view of both enterprise platforms and their corresponding test automation.

> **About Rizon:**  
> Rizon enables AI to deeply understand the enterprise tech stack alongside the test automation platform.  
> It is the foundation of a self-documenting AI harness that builds structured knowledge and develops the scripts needed to sew end-to-end test automation across complex superannuation processes.

## Navigation

- [PLATFORMS.md](PLATFORMS.md) — High-level platforms overview and integration paths
- [FUSION.md](FUSION.md) — Test automation platform (scenarios, tasks, datasets, MongoDB)
- [FRAMEWORK.md](FRAMEWORK.md) — Custom Python framework patterns
- [platforms/](platforms/) — Detailed platform documentation (pages, wizards, APIs, flows)

## Enterprise Context

Australian enterprise Superannuation fund with ~20 highly integrated platforms (member-facing and internal). Test automation supports SIT (IT squads) and UAT with end-to-end scenarios.

### Domains
- **Data and AI** — No test automation coverage currently
- **Digital** — All member-facing platforms
- **Advice and Admin** — Mostly internal (+ some member-facing calculators)
- **Enterprise Services** — Boomi centralised APIs

See [PLATFORMS.md](PLATFORMS.md) for details.
