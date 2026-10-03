---
type: table
database: Olives_BO
name: PendingInvoices
schema: dbo
tags: [#backoffice, #billing]
foreign_keys:
referenced_by:
  - [[OT_ImportActionLog]]
support_relevance: high
last_verified: 2026-07-05
---
# PendingInvoices


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores pendinginvoices records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| SalesmanNo | int | NO | ✓ |  |  |
| CustomerNo | nvarchar | YES | ✓ |  |  |
| AliasName | nvarchar | YES | ✓ |  |  |
| ItemNo | nvarchar | YES | ✓ |  |  |
| Qty | float | YES |  |  |  |
| Unit | nvarchar | YES |  |  |  |
| Bonus | float | YES |  |  |  |
| SellPrice | float | YES |  |  |  |
| Ref1 | datetime | YES |  |  |  |
| Ref2 | nvarchar | YES |  |  |  |
| ItemDiscountPerc | float | YES |  |  |  |
| VouDiscountPerc | float | YES |  |  |  |
| CustomerDiscountPerc | float | YES |  |  |  |
| TaxPerc | float | YES |  |  |  |
## Primary Key
CompanyID
SalesmanNo
CustomerNo
AliasName
ItemNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (0):**
_None_

**Writes (1):**
- [[OT_ImportActionLog]]

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
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[ReceiptRequestsInvoicesLink]]
