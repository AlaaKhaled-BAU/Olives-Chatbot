---
type: table
database: Olives_BO
name: ItemsSuggestGroupLink
schema: dbo
tags: [#backoffice, #inventory, #reference]
foreign_keys:
referenced_by:
  - [[Pro_AssignItemsSuggestGroupForCustomers]]
support_relevance: high
last_verified: 2026-07-05
---
# ItemsSuggestGroupLink


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores itemssuggestgrouplink records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| CustomerID | bigint | NO | ✓ |  |  |
| SuggestGroupID | int | NO | ✓ |  |  |
| TargetMonth | smallint | NO | ✓ |  |  |
| TargetYear | smallint | NO | ✓ |  |  |
| TargetCount | float | YES |  |  |  |
| InvoiceMinQtyUnit | nvarchar | YES |  |  |  |
| InvoiceMinQty | float | YES |  |  |  |
| InvoiceMinQty_Main | float | YES |  |  |  |
## Primary Key
CompanyID
CustomerID
SuggestGroupID
TargetMonth
TargetYear
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_AssignItemsSuggestGroupForCustomers]]

**Writes (1):**
- [[Pro_AssignItemsSuggestGroupForCustomers]]

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
