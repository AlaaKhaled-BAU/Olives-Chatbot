---
type: table
database: Olives_BO
name: ReprintedTransactions
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[Companies]]
  - [[ReprintReasons]]
referenced_by:
  - [[OT_ImportReprintedTransactions]]
  - [[Rpt_ReasonReprint]]
  - [[Rpt_ReprintCount]]
support_relevance: high
last_verified: 2026-07-05
---
# ReprintedTransactions


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores reprintedtransactions records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[ReprintReasons]] |
| TrTypeID | smallint | NO | ✓ |  |  |
| TrYear | smallint | NO | ✓ |  |  |
| TrNo | int | NO | ✓ |  |  |
| SerID | numeric | YES | ✓ |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| ReprintReasonID | int | YES |  | ✓ | [[ReprintReasons]] |
| CopyCount | int | YES |  |  |  |
| IsRePrint | bit | YES |  |  |  |
| TabletSysID | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
TrTypeID
TrYear
TrNo
SerID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ReprintReasonID -> [[ReprintReasons]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (3):**
- [[OT_ImportReprintedTransactions]]
- [[Rpt_ReasonReprint]]
- [[Rpt_ReprintCount]]

**Writes (1):**
- [[OT_ImportReprintedTransactions]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Orphan lines**: Detail rows without matching header — causes sync failures
- **Posting failure**: IsPosted flag stuck false — check ERP integration log
- **Duplicate vouchers**: Same VouNo generated for different transactions — run dedup check
- **Currency mismatch**: ExRate different from CurrenciesRate table — financial reconciliation off
- **Void inconsistency**: IsVoid flag but original transaction still active — check WF approval

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
