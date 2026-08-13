---
type: table
database: OSFA_DB
name: OT_VanTransferDF
schema: dbo
tags: [#mobile, #order]
foreign_keys:
referenced_by:
  - [[OT_VanTransferDF_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_VanTransferDF



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| OrderYear | smallint | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| SalesmanNo | int | NO | ✓ |  |  |
| ItemNo | varchar | YES | ✓ |  |  |
| UnitCode | varchar | YES | ✓ |  |  |
| Qty | money | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
## Primary Key
CompNo
OrderYear
OrderNo
SalesmanNo
ItemNo
UnitCode
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OT_VanTransferDF_Insert]]

**Writes (1):**
- [[OT_VanTransferDF_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Sync conflict**: Same record modified on tablet and BO simultaneously — last-write-wins may lose data
- **Orphan tablet records**: Row with no linked BO counterpart — check sync log
- **Duplicate TabletSysID**: Same tablet transaction inserted twice — run dedup check
- **Missing IsPosted flag**: Data not synced to BO — check tablet connectivity

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
