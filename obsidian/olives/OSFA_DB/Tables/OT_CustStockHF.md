---
type: table
database: OSFA_DB
name: OT_CustStockHF
schema: dbo
tags: [#inventory, #mobile]
foreign_keys:
referenced_by:
  - [[OT_CustStockHF_CheckExist]]
  - [[OT_CustStockHF_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_CustStockHF



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| VouYear | smallint | NO | ✓ |  |  |
| VouNo | int | NO | ✓ |  |  |
| VouDate | smalldatetime | YES |  |  |  |
| CustomerNo | varchar | YES |  |  |  |
| SalesmanNo | smallint | YES |  |  |  |
| Posted | bit | NO |  |  |  |
| Notes | varchar | YES |  |  |  |
| GPSX | varchar | YES |  |  |  |
| GPSY | varchar | YES |  |  |  |
| RouteID | int | YES |  |  |  |
| DocType | smallint | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| PrintOriginalCount | int | YES |  |  |  |
| PrintCopyCount | int | YES |  |  |  |
| ServerDate | smalldatetime | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
## Primary Key
CompNo
VouYear
VouNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[OT_CustStockHF_CheckExist]]
- [[OT_CustStockHF_Insert]]

**Writes (1):**
- [[OT_CustStockHF_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Sync conflict**: Same record modified on tablet and BO simultaneously — last-write-wins may lose data
- **Orphan tablet records**: Row with no linked BO counterpart — check sync log
- **Duplicate TabletSysID**: Same tablet transaction inserted twice — run dedup check
- **Missing IsPosted flag**: Data not synced to BO — check tablet connectivity

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
