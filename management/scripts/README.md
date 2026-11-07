# Knowledge Retrieval Scripts

Python scripts that pull knowledge from Fusion (MongoDB scenarios and tasks) and other sources to keep this knowledge base current and to support AI-assisted maintenance of the `fusion-scripts` repository.

## Intended Capabilities
- Query Fusion for scenarios and tasks, including their data
- Map tasks to underlying Python scripts in the automation codebase
- Extract platform/page/API coverage
- Generate or update documentation stubs
- Produce summaries of current automation capabilities for AI consumption

## Structure
```
management/scripts/
├── README.md
├── fusion/          # Fusion MongoDB queries and extractors
├── platforms/       # Helpers that relate scenarios to platform pages/APIs
└── utils/           # Shared connection, formatting, and export helpers
```

Scripts in this repo are primarily for knowledge extraction and documentation support. The actual test automation Python scripts live in the separate `fusion-scripts` repository.
