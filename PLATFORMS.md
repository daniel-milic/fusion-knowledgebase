# Platforms

The single list of platforms. Detail lives in `platforms/<domain>/<platform>/`. Only platforms with a folder are linked; add the link when the folder is created.

## Core facts
- **Sonata is the central registry.** It holds super members, employers, their accounts, and insurance. Every platform connects to Sonata.
- **Boomi integrates to all platforms.**
- **Experience API sits above Boomi** and serves the microsites, employer portal, mobile app and public portal.
- **eCRM holds all clients**, mostly for advisors. A client does not have to be a super member to get advice, though they can be both. Employers and advisors can also be clients.

## Test environments
TEST01, TEST02, TEST03, TEST04, DEV01, DEV04, PPD01, PPD02

## Domains
The domain names match `fusion-scripts/regression/<domain>/`: `digital`, `sonata` (admin), `advice` and `investments`.

### digital — member-facing, all with automation coverage
| Platform | Built as | Connects via |
|---|---|---|
| Member Portal — [platforms/digital/member-portal/](platforms/digital/member-portal/) | Sonata web app | Sonata |
| Employer Portal | In-house | Experience API |
| Mobile App | In-house | Experience API |
| Microsites | In-house | Experience API |
| Public Portal (AEM, Adobe) | In-house | Experience API |
| Advisor Portal | *(to document)* | *(to document)* |
| TAL Insurance | *(to document)* | *(to document)* |

### sonata — admin
| Platform | Notes |
|---|---|
| Sonata Registry and APIs — [platforms/sonata/](platforms/sonata/) | Bravura product. Central registry. Platforms seen in scripts: `sbs`, `insurance`, `orchestrator`, `employer-services`, `system` |

### advice
| Platform | Notes |
|---|---|
| eCRM — [platforms/advice/ecrm/](platforms/advice/ecrm/) | Clients, mostly advisor-facing |
| AdviceOS — [platforms/advice/adviceos/](platforms/advice/adviceos/) | Bravura product. Financial advice |

### investments
No platforms documented yet.

## Not yet assigned to a domain
Sonata ODS DB (operational data store), Zendesk (service desk), Quadient (letter generation).

## Outside the regression domains
| Platform | Notes |
|---|---|
| Boomi | Centralised APIs. Integrates to all platforms |
| Experience API | Above Boomi, for the in-house digital channels |
| Babel (SuperStream gateway) | Bravura product. No test coverage at present |
| ATO gateway | No test coverage at present |
| Data platforms, AI / ML services | No automation coverage |

## Integration paths
- In-house digital channels → Experience API → Boomi → Sonata and other platforms
- Member Portal → Sonata directly (it is a Sonata web app)
- Everything → Sonata for member, employer, account and insurance data
- eCRM client data is shared with advisor-facing platforms
- Advice calculators may surface in member-facing channels
- Quadient letters are triggered from multiple platforms
