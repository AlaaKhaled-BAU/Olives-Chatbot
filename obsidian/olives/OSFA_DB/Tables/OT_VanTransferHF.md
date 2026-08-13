---
type: table
database: OSFA_DB
name: OT_VanTransferHF
schema: dbo
tags: [#mobile, #order]
foreign_keys:
referenced_by:
  - [[OT_VanTransferHF_CheckExist]]
  - [[OT_VanTransferHF_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_VanTransferHF



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| OrderYear | smallint | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| FromSalesman | int | NO |  |  |  |
| ToSalesman | int | NO |  |  |  |
| OrderDate | smalldatetime | YES |  |  |  |
| Notes | varchar | YES |  |  |  |
| GPSX | varchar | YES |  |  |  |
| GPSY | varchar | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| PrintOriginalCount | int | YES |  |  |  |
| PrintCopyCount | int | YES |  |  |  |
| IsPosted | bit | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| ServerDate | smalldatetime | YES |  |  |  |
## Primary Key
CompNo
OrderYear
OrderNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[OT_VanTransferHF_CheckExist]]
- [[OT_VanTransferHF_Insert]]

**Writes (1):**
- [[OT_VanTransferHF_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Sync conflict**: Same record modified on tablet and BO simultaneously — last-write-wins may lose data
- **Orphan tablet records**: Row with no linked BO counterpart — check sync log
- **Duplicate TabletSysID**: Same tablet transaction inserted twice — run dedup check
- **Missing IsPosted flag**: Data not synced to BO — check tablet connectivity

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
