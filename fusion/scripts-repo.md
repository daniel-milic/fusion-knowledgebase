# fusion-scripts Repository

Structure and conventions of the automation repo that Fusion tasks drive.

## Layout
Scripts sit under `regression/<domain>/<platform>/<page>`, matching the domain and platform folders in this knowledge base.

## Framework patterns
- Page object / component patterns
- API client patterns (Sonata, Experience Layer, Boomi)
- Dataset consumption
- Test data builders
- Assertions and verification helpers
- Logging, reporting, and evidence capture
- Environment configuration (SIT / UAT)
- Common utilities (dates, superannuation calculations, identifiers)
- Naming conventions and task linkage

> Goal: an AI reading this repo can generate a new script that matches existing patterns and links correctly to a task and dataset.
