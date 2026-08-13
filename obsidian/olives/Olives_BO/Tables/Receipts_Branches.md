---
type: table
database: Olives_BO
name: Receipts_Branches
schema: dbo
tags: [#backoffice, #billing]
foreign_keys:
referenced_by:
  - [[OT_ImportReceipts]]
support_relevance: high
last_verified: 2026-07-05
---
# Receipts_Branches


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores receipts branches records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| TransactionTypeID | smallint | NO | ✓ |  |  |
| TransactionYear | smallint | NO | ✓ |  |  |
| TransactionNo | int | NO | ✓ |  |  |
| BranchID | int | NO | ✓ |  |  |
| Amount | float | YES |  |  |  |
| Ref1 | varchar | YES |  |  |  |
| Ref2 | varchar | YES |  |  |  |
## Primary Key
CompanyID
TransactionTypeID
TransactionYear
TransactionNo
BranchID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (0):**
_None_

**Writes (1):**
- [[OT_ImportReceipts]]

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
- [[Glossary]]
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[ReceiptRequestsInvoicesLink]]
- [[MMS_PaymentsChecksDetails]]
- [[MMS_TaxType]]
