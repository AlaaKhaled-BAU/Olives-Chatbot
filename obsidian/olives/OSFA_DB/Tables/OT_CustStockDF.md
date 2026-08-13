---
type: table
database: OSFA_DB
name: OT_CustStockDF
schema: dbo
tags: [#inventory, #mobile]
foreign_keys:
  - [[OT_CustStockHF]]
referenced_by:
  - [[OT_AddCustStockImages]]
  - [[OT_CustStockDF_CheckExist]]
  - [[OT_CustStockDF_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_CustStockDF



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ | ✓ | [[OT_CustStockHF]] |
| VouYear | smallint | NO | ✓ | ✓ | [[OT_CustStockHF]] |
| VouNo | int | NO | ✓ | ✓ | [[OT_CustStockHF]] |
| ItemNo | varchar | YES | ✓ |  |  |
| UnitCode | varchar | YES | ✓ |  |  |
| Qty | money | NO |  |  |  |
| ItemImage | image | YES |  |  |  |
| IsPostedImage | bit | YES |  |  |  |
| ExpDate | smalldatetime | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
## Primary Key
CompNo
VouYear
VouNo
ItemNo
UnitCode
## Foreign Keys
CompNo, VouYear, VouNo -> [[OT_CustStockHF]](CompNo, VouYear, VouNo)
## Impact / Procedures Using This Table

**Reads (3):**
- [[OT_AddCustStockImages]]
- [[OT_CustStockDF_CheckExist]]
- [[OT_CustStockDF_Insert]]

**Writes (2):**
- [[OT_AddCustStockImages]]
- [[OT_CustStockDF_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Sync conflict**: Same record modified on tablet and BO simultaneously — last-write-wins may lose data
- **Orphan tablet records**: Row with no linked BO counterpart — check sync log
- **Duplicate TabletSysID**: Same tablet transaction inserted twice — run dedup check
- **Missing IsPosted flag**: Data not synced to BO — check tablet connectivity

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
