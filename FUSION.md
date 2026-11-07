# Fusion — Test Automation Platform

Fusion is the test automation platform. Test scenarios live in its MongoDB database.

## High-Level Flow
```
Test Scenario (Fusion / MongoDB)
        ↓
Test Automation Task (contains Dataset)
        ↓
Underlying Python Script(s)
        ↓
Target Platform Page / Wizard / API / Flow
```

## Key Concepts
| Concept                  | Storage / Location              | Description |
|--------------------------|---------------------------------|-------------|
| Test Scenario            | Fusion MongoDB                  | High-level end-to-end scenario |
| Test Automation Task     | Fusion                          | Executable unit containing Dataset |
| Dataset                  | Within Task                     | Test data |
| Python Script            | Test automation code repository | Implements interaction with page/API |
| Custom Python Framework  | Test automation code repository | Shared patterns and helpers |

## To Document
- MongoDB collections / schema for scenarios, tasks, datasets
- How tasks link to Python scripts
- Execution results and evidence used for healing

See also [FRAMEWORK.md](FRAMEWORK.md).
