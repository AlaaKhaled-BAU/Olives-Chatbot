---
type: table
database: OSFA_DB
name: OT_StateAccBalance
schema: dbo
tags: [#inventory, #mobile]
foreign_keys:
referenced_by:
  - [[OT_Online_StateAccBalance]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_StateAccBalance



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| SalesmanNo | smallint | NO | ✓ |  |  |
| CustomerNo | bigint | NO | ✓ |  |  |
| TrType | varchar | YES | ✓ |  |  |
| TrNo | varchar | YES | ✓ |  |  |
| TrSer | smallint | NO | ✓ |  |  |
| TrDate | smalldatetime | NO | ✓ |  |  |
| TrName | varchar | YES |  |  |  |
| Debit | money | YES |  |  |  |
| Credit | money | YES |  |  |  |
| Notes | varchar | YES |  |  |  |
| Balance | money | YES |  |  |  |
## Primary Key
CompNo
SalesmanNo
CustomerNo
TrType
TrNo
TrSer
TrDate
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OT_Online_StateAccBalance]]

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
- [[OSFA_DB/Tables/OT_BonusItemRanges]]
- [[OSFA_DB/Tables/OT_BonusItemPriority]]
- [[OSFA_DB/Tables/CompetitiveItemsImage]]
- [[OSFA_DB/Tables/Invt_ItemsImage]]
