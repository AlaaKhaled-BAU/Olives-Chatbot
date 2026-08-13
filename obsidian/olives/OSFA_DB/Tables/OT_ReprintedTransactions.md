---
type: table
database: OSFA_DB
name: OT_ReprintedTransactions
schema: dbo
tags: [#mobile]
foreign_keys:
referenced_by:
  - [[OT_ReprintedTransactions_CheckExist]]
  - [[OT_ReprintedTransactions_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_ReprintedTransactions



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| TrTypeID | smallint | NO | ✓ |  |  |
| TrYear | smallint | NO | ✓ |  |  |
| TrNo | int | NO | ✓ |  |  |
| SerID | numeric | YES | ✓ |  |  |
| TrID | int | NO | ✓ |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| ReprintReasonID | int | YES |  |  |  |
| CopyCount | int | YES |  |  |  |
| IsRePrint | bit | YES |  |  |  |
| TabletSysID | nvarchar | YES |  |  |  |
| Posted | bit | YES |  |  |  |
## Primary Key
CompNo
TrTypeID
TrYear
TrNo
SerID
TrID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[OT_ReprintedTransactions_CheckExist]]
- [[OT_ReprintedTransactions_Insert]]

**Writes (1):**
- [[OT_ReprintedTransactions_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Orphan lines**: Detail rows without matching header — causes sync failures
- **Posting failure**: IsPosted flag stuck false — check ERP integration log
- **Duplicate vouchers**: Same VouNo generated for different transactions — run dedup check
- **Currency mismatch**: ExRate different from CurrenciesRate table — financial reconciliation off
- **Void inconsistency**: IsVoid flag but original transaction still active — check WF approval

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
