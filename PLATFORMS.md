# Platforms

One list of platforms by domain. Platform detail lives in `platforms/<domain>/<platform>/`. Only platforms with a folder are linked.

## digital (member-facing)
All have test automation coverage.
- Member Portal — [platforms/digital/member-portal/](platforms/digital/member-portal/)
- Advisor Portal
- Employer Portal
- TAL Insurance
- Public Web
- Mobile App
- Microsites Web
- Experience Layer APIs

## advice-admin
- Sonata Registry and APIs — [platforms/advice-admin/sonata/](platforms/advice-admin/sonata/)
- Sonata ODS DB
- eCRM
- Zendesk
- AdviceOS
- Quadient letter generation

## enterprise-services
- Boomi (centralised APIs) — [platforms/enterprise-services/](platforms/enterprise-services/)

## data-ai
No automation coverage.
- Data platforms
- AI / ML services

## Integration paths
- Digital channels → Experience Layer APIs → Boomi → Sonata Registry and other back-office systems
- Advice calculators may surface in member-facing channels
- Letter generation (Quadient) is triggered from multiple platforms
