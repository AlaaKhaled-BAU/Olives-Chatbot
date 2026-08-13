---
type: table
database: Olives_BO
name: Receipts_PaidTransChecks
schema: dbo
tags: [#backoffice, #billing]
foreign_keys:
referenced_by:
  - [[OT_ImportReceipts]]
  - [[Pro_ChecksByStatusDetails]]
  - [[Pro_ReceiptPaid]]
  - [[Pro_Receipts]]
  - [[Rpt_ALLReturnChecks]]
  - [[Rpt_ChecksByStatus]]
  - [[Rpt_ChequeStatusWithSettelment]]
support_relevance: high
last_verified: 2026-07-05
---
# Receipts_PaidTransChecks


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores receipts paidtranschecks records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| TransactionYear | smallint | NO | ✓ |  |  |
| TransactionNo | int | NO | ✓ |  |  |
| TransactionTypeID | smallint | NO | ✓ |  |  |
| PaidTransBankID | int | NO | ✓ |  |  |
| PaidTransBranchID | int | NO | ✓ |  |  |
| PaidTransYear | smallint | NO | ✓ |  |  |
| PaidTransNo | int | NO | ✓ |  |  |
| PaidTransTypeID | smallint | NO | ✓ |  |  |
| PaidTransCustomerID | bigint | NO | ✓ |  |  |
| PaidTransChequeNo | int | NO | ✓ |  |  |
| PaidAmount | float | YES |  |  |  |
## Primary Key
CompanyID
TransactionYear
TransactionNo
TransactionTypeID
PaidTransBankID
PaidTransBranchID
PaidTransYear
PaidTransNo
PaidTransTypeID
PaidTransCustomerID
PaidTransChequeNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (6):**
- [[Pro_ChecksByStatusDetails]]
- [[Pro_ReceiptPaid]]
- [[Pro_Receipts]]
- [[Rpt_ALLReturnChecks]]
- [[Rpt_ChecksByStatus]]
- [[Rpt_ChequeStatusWithSettelment]]

**Writes (2):**
- [[OT_ImportReceipts]]
- [[Pro_ReceiptPaid]]

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
