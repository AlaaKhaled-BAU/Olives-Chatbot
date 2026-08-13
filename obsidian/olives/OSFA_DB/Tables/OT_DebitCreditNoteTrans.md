---
type: table
database: OSFA_DB
name: OT_DebitCreditNoteTrans
schema: dbo
tags: [#billing, #mobile]
foreign_keys:
referenced_by:
  - [[DebitCreditNoteList_CheckExist]]
  - [[OT_DebitCreditNoteTrans_Insert]]
  - [[OT_DebitCreditNoteTrans_SELECT]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_DebitCreditNoteTrans



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| VouYear | smallint | NO | ✓ |  |  |
| VouNo | int | NO | ✓ |  |  |
| VouType | smallint | NO | ✓ |  |  |
| VouDate | smalldatetime | YES |  |  |  |
| CustomerNo | varchar | YES |  |  |  |
| SalesmanNo | smallint | YES |  |  |  |
| InvNo | varchar | YES |  |  |  |
| InvAmount | float | YES |  |  |  |
| TotDisccount | float | YES |  |  |  |
| Tax | float | YES |  |  |  |
| NetDisccount | float | YES |  |  |  |
| ServerDate | smalldatetime | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| Notes | varchar | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| Posted | bit | YES |  |  |  |
## Primary Key
CompNo
VouYear
VouNo
VouType
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (3):**
- [[DebitCreditNoteList_CheckExist]]
- [[OT_DebitCreditNoteTrans_Insert]]
- [[OT_DebitCreditNoteTrans_SELECT]]

**Writes (1):**
- [[OT_DebitCreditNoteTrans_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Sync conflict**: Same record modified on tablet and BO simultaneously — last-write-wins may lose data
- **Orphan tablet records**: Row with no linked BO counterpart — check sync log
- **Duplicate TabletSysID**: Same tablet transaction inserted twice — run dedup check
- **Missing IsPosted flag**: Data not synced to BO — check tablet connectivity

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
