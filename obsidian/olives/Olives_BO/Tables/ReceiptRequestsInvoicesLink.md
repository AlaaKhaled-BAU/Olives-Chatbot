---
type: table
database: Olives_BO
name: ReceiptRequestsInvoicesLink
schema: dbo
tags: [#backoffice, #billing]
foreign_keys:
referenced_by:
  - [[Pro_ReceiptRequests]]
support_relevance: high
last_verified: 2026-07-05
---
# ReceiptRequestsInvoicesLink


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores receiptrequestsinvoiceslink records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| OrderYear | smallint | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| PaidTransYear | smallint | NO | ✓ |  |  |
| PaidTransNo | int | NO | ✓ |  |  |
| PaidTransTypeID | smallint | NO | ✓ |  |  |
## Primary Key
CompanyID
OrderYear
OrderNo
PaidTransYear
PaidTransNo
PaidTransTypeID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_ReceiptRequests]]

**Writes (1):**
- [[Pro_ReceiptRequests]]

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
- [[Olives_BO/Tables/Pos_InvoiceOrderHF]]
- [[Olives_BO/Tables/PriceListQtyRanges]]
