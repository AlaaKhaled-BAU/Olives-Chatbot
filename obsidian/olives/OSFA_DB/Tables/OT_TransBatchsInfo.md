---
type: table
database: OSFA_DB
name: OT_TransBatchsInfo
schema: dbo
tags: [#inventory, #mobile]
foreign_keys:
referenced_by:
  - [[OT_TransBatchsInfo_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_TransBatchsInfo



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| VouType | smallint | NO | ✓ |  |  |
| VouYear | smallint | NO | ✓ |  |  |
| VouNo | int | NO | ✓ |  |  |
| ItemNo | varchar | YES | ✓ |  |  |
| Unit | varchar | YES | ✓ |  |  |
| BatchNo | varchar | YES | ✓ |  |  |
| Qty | money | NO | ✓ |  |  |
| ExpireDate | smalldatetime | YES |  |  |  |
| Bonus | money | YES |  |  |  |
## Primary Key
CompNo
VouType
VouYear
VouNo
ItemNo
Unit
BatchNo
Qty
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OT_TransBatchsInfo_Insert]]

**Writes (1):**
- [[OT_TransBatchsInfo_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Sync conflict**: Same record modified on tablet and BO simultaneously — last-write-wins may lose data
- **Orphan tablet records**: Row with no linked BO counterpart — check sync log
- **Duplicate TabletSysID**: Same tablet transaction inserted twice — run dedup check
- **Missing IsPosted flag**: Data not synced to BO — check tablet connectivity

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
- [[Olives_BO/Procedures/OT_ImportReturnOrderMerch]]
