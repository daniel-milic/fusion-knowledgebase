# fusion-knowledgebase

Knowledge base for an Australian superannuation fund's enterprise platforms and the Fusion test automation platform that tests them. Its purpose is to give AI tools enough context to generate and heal tests in the separate `fusion-scripts` repo.

Start at [INDEX.md](INDEX.md). AI tools: see [AGENTS.md](AGENTS.md) for instructions.

## Layout
- `AGENTS.md` — instructions for AI tools (Copilot, Codex and others)
- `INDEX.md` — entry point and routing table
- `PLATFORMS.md` — the single list of platforms by domain
- `platforms/<domain>/<platform>/` — platform docs, mirroring `fusion-scripts/regression/<domain>/<platform>/`
- `fusion/` — Fusion scenarios, tasks, database, user interactions, and the fusion-scripts repo structure
- `management/` — skills, layout rules, knowledge depth, and collection scripts
