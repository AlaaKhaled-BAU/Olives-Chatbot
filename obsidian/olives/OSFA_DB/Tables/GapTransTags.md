---
type: table
database: OSFA_DB
name: GapTransTags
schema: dbo
tags: [#mobile]
foreign_keys:
referenced_by:
  - [[InsertGapTransTags]]
support_relevance: high
last_verified: 2026-07-05
---
# GapTransTags



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Field Automation (Android tablet) — stores gaptranstags records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| DeviceSysID | varchar | YES | ✓ |  |  |
| GapTagID | int | NO | ✓ |  |  |
| GapTagValue | varchar | YES |  |  |  |
## Primary Key
CompanyID
DeviceSysID
GapTagID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[InsertGapTransTags]]

**Writes (1):**
- [[InsertGapTransTags]]

## Estimated Size / Volatility
Typical business table
## Common Issues
> [!warning] AUTO-GENERATED — verify before trusting

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies


## See also
- [[Olives_BO/Tables/GapTransTags]] (Back Office counterpart table)

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]

## Cross-Database


See also: [[Olives_BO/Tables/GapTransTags|BO GapTransTags]]
