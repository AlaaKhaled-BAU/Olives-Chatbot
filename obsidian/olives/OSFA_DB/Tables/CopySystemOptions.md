---
type: table
database: OSFA_DB
name: CopySystemOptions
schema: dbo
tags: [#mobile]
referenced_by:
  - [[OT_CopySystemOption]]
  - [[Technical_CopySystemoptionsForSeveralSalespersons]]
  - [[Technical_OT_CopySystemOption]]
support_relevance: high
last_verified: 2026-07-05
---
# CopySystemOptions



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Field Automation (Android tablet) — stores copysystemoptions records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | YES |  |  |  |
| SalesmanID | int | YES |  |  |  |
| Op_ID | int | YES |  |  |  |
## Primary Key
(none)
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (3):**
- [[OT_CopySystemOption]]
- [[Technical_CopySystemoptionsForSeveralSalespersons]]
- [[Technical_OT_CopySystemOption]]

**Writes (1):**
- [[Technical_CopySystemoptionsForSeveralSalespersons]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Missing reference values**: Required dropdown items not present — selection fails on tablet
- **Duplicate codes**: Same code used for different descriptions — mapping ambiguity
- **Orphan references**: Referenced by deleted records — FK violation on delete attempt

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
- [[Olives_BO/Procedures/Technical_Activate_DeactivateLoginbybarcode_Atieh]]
