---
type: table
database: OSFA_DB
name: GapTransHeaders
schema: dbo
tags: [#mobile]
foreign_keys:
referenced_by:
  - [[InsertGapTransHeaders]]
  - [[OT_GapTransHeaders_CheckExist]]
support_relevance: high
last_verified: 2026-07-05
---
# GapTransHeaders



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Field Automation (Android tablet) — stores gaptransheaders records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| DeviceSysID | varchar | YES | ✓ |  |  |
| SalesmanNo | int | NO |  |  |  |
| Notes | varchar | YES |  |  |  |
| ActionDate | smalldatetime | YES |  |  |  |
| AssginedSalesmanNo | int | YES |  |  |  |
| IsPosted | bit | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
## Primary Key
CompanyID
DeviceSysID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[InsertGapTransHeaders]]
- [[OT_GapTransHeaders_CheckExist]]

**Writes (1):**
- [[InsertGapTransHeaders]]

## Estimated Size / Volatility
Typical business table
## Common Issues
> [!warning] AUTO-GENERATED — verify before trusting

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies


## See also
- [[Olives_BO/Tables/GapTransHeaders]] (Back Office counterpart table)

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]

## Cross-Database


See also: [[Olives_BO/Tables/GapTransHeaders|BO GapTransHeaders]]
