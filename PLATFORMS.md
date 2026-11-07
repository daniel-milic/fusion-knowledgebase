# Platforms Overview

High-level view of enterprise platforms and integration paths. Detailed page/wizard/API documentation lives under `platforms/`.

## Domains

### Data and AI
| Platform / Area | Type | Test Automation Coverage |
|-----------------|------|---------------------------|
| Data platforms  | Internal | None |
| AI / ML services| Internal | None |

### Digital (Member-Facing)
All have test automation coverage.

| Platform              | Type          | Primary Users     |
|-----------------------|---------------|-------------------|
| Member Portal         | Web           | Members           |
| Advisor Portal        | Web           | Advisors          |
| Employer Portal       | Web           | Employers         |
| TAL Insurance         | Web / Integration | Members / Advisors |
| Public Web            | Web           | Public / Prospects|
| Mobile App            | Mobile        | Members           |
| Microsites Web        | Web           | Various           |
| Experience Layer APIs | API           | Digital channels  |

### Advice & Admin
| Platform                  | Type          | Primary Use                  |
|---------------------------|---------------|------------------------------|
| Sonata Registry           | Core Registry | Member accounts, products    |
| Sonata ODS DB             | Database      | Operational data store       |
| Sonata APIs               | API           | Registry operations          |
| eCRM                      | CRM           | Customer relationship        |
| Zendesk                   | Service Desk  | Member / advisor support     |
| AdviceOS                  | Advice system | Financial advice             |
| Quadient Letter generation| Document      | Letters, statements          |

### Enterprise Services
| Platform / Component     | Type | Notes |
|--------------------------|------|-------|
| Boomi (centralised APIs) | Integration / APIs | Used by all platforms |

## Integration Paths
- Digital channels → Experience Layer APIs → Boomi → Sonata Registry / other back-office systems
- Advice calculators may surface in member-facing channels
- Letter generation (Quadient) triggered from multiple platforms

Detailed documentation: see [platforms/](platforms/).
