---
type: table
database: Olives_BO
name: GapTransHeaders
schema: dbo
tags: [#backoffice]
foreign_keys:
referenced_by:
  - [[OT_ImportGapTrans]]
  - [[Rpt_GetGapTrans]]
support_relevance: high
last_verified: 2026-07-05
---
# GapTransHeaders


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores gaptransheaders records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| GapTransYear | smallint | NO | ✓ |  |  |
| GapTransNo | bigint | NO | ✓ |  |  |
| SalesmanNo | int | YES |  |  |  |
| Notes | varchar | YES |  |  |  |
| ActionDate | smalldatetime | YES |  |  |  |
| AssginedSalesmanNo | int | YES |  |  |  |
| IsDone | bit | YES |  |  |  |
| DeviceSysID | varchar | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
## Primary Key
CompanyID
GapTransYear
GapTransNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[OT_ImportGapTrans]]
- [[Rpt_GetGapTrans]]

**Writes (2):**
- [[OT_ImportGapTrans]]
- [[Rpt_GetGapTrans]]

## Estimated Size / Volatility
Typical business table
## Common Issues
> [!warning] AUTO-GENERATED — verify before trusting

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]

## Cross-Database

See also: [[OSFA_DB/Tables/GapTransHeaders|FO GapTransHeaders]]
