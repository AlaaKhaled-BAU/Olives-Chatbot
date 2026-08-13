---
type: table
database: OSFA_DB
name: OT_BatchsInfo
schema: dbo
tags: [#inventory, #mobile]
foreign_keys:
referenced_by:
  - [[OT_AppService]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_BatchsInfo



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| SalesmanNo | int | NO | ✓ |  |  |
| ItemNo | varchar | YES | ✓ |  |  |
| BatchNo | varchar | YES | ✓ |  |  |
| ExpireDate | smalldatetime | YES |  |  |  |
| Qty | money | YES |  |  |  |
| Ref1 | varchar | YES |  |  |  |
| Ref2 | varchar | YES |  |  |  |
| BatchBarcode | varchar | YES |  |  |  |
## Primary Key
CompNo
SalesmanNo
ItemNo
BatchNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OT_AppService]]

**Writes (0):**
_None_

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Sync conflict**: Same record modified on tablet and BO simultaneously — last-write-wins may lose data
- **Orphan tablet records**: Row with no linked BO counterpart — check sync log
- **Duplicate TabletSysID**: Same tablet transaction inserted twice — run dedup check
- **Missing IsPosted flag**: Data not synced to BO — check tablet connectivity

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
