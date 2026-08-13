---
type: table
database: Olives_BO
name: TransactionsSuggestedItems
schema: dbo
tags: [#backoffice, #inventory]
foreign_keys:
referenced_by:
  - [[OT_ImportSalesInvoices]]
  - [[OT_ImportSalesOrders]]
support_relevance: high
last_verified: 2026-07-05
---
# TransactionsSuggestedItems


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores transactionssuggesteditems records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | YES |  |  |  |
| VouType | smallint | YES |  |  |  |
| VouYear | smallint | YES |  |  |  |
| VouNo | int | YES |  |  |  |
| ItemNo | varchar | YES |  |  |  |
| Unit | varchar | YES |  |  |  |
| Qty | float | YES |  |  |  |
| UnitPrice | float | YES |  |  |  |
| Ref1 | varchar | YES |  |  |  |
| Ref2 | varchar | YES |  |  |  |
## Primary Key
(none)
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (0):**
_None_

**Writes (2):**
- [[OT_ImportSalesInvoices]]
- [[OT_ImportSalesOrders]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Duplicate barcodes**: Multiple items sharing same barcode — POS picks wrong item
- **Price mismatch**: Sell price in Items differs from PriceListDetails — customer charged wrong amount
- **Stock discrepancy**: QtyInAllStores differs from sum of StoreBalances — run CALCITEMBALANCE
- **Missing units**: Item has no valid ItemUnits — cannot be sold
- **Tax config wrong**: IsTaxExempt flag incorrect — ZATCA/legal reporting mismatch

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Glossary]]
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[MMS_ItemsCategories]]
- [[IssueItemsDetails]]
- [[SalespersonCustStockItemsAssignment]]
