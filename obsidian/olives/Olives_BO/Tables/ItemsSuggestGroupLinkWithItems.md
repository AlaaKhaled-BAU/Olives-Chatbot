---
type: table
database: Olives_BO
name: ItemsSuggestGroupLinkWithItems
schema: dbo
tags: [#backoffice, #inventory, #reference]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# ItemsSuggestGroupLinkWithItems


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores itemssuggestgrouplinkwithitems records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| SuggestGroupID | int | NO | ✓ |  |  |
| ItemCode | nvarchar | YES | ✓ |  |  |
| Qty | float | YES |  |  |  |
## Primary Key
CompanyID
SuggestGroupID
ItemCode
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

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
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[IssueItemsDetails]]
- [[SalespersonCustStockItemsAssignment]]
- [[DR_DynamicReportsParameters]]
