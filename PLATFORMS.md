# Platforms

The single list of platforms. Detail lives in `platforms/<domain>/<platform>/`. Only platforms with a folder are linked; add the link when the folder is created.

## digital — member-facing, all with automation coverage
- Member Portal — [platforms/digital/member-portal/](platforms/digital/member-portal/)
- Advisor Portal
- Employer Portal
- TAL Insurance
- Public Web
- Mobile App
- Microsites Web
- Experience Layer APIs

## advice-admin — mostly internal, some member-facing calculators
- Sonata Registry and APIs — [platforms/advice-admin/sonata/](platforms/advice-admin/sonata/)
- Sonata ODS DB
- eCRM
- Zendesk
- AdviceOS
- Quadient letter generation

## integration — shared layer used by all platforms
- Boomi (centralised APIs)

## data-ai — no automation coverage
- Data platforms
- AI / ML services

## Integration paths
- Digital channels → Experience Layer APIs → Boomi → Sonata Registry and other back-office systems
- Advice calculators may surface in member-facing channels
- Letter generation (Quadient) is triggered from multiple platforms
