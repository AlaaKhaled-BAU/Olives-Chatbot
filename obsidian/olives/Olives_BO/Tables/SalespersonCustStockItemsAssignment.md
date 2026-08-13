---
type: table
database: Olives_BO
name: SalespersonCustStockItemsAssignment
schema: dbo
tags: [#backoffice, #inventory, #sales]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[Positions]]
referenced_by:
  - [[Pro_SalesPersonCustStockItemsAssignment]]
support_relevance: high
last_verified: 2026-07-05
---
# SalespersonCustStockItemsAssignment


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersoncuststockitemsassignment records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Positions]] |
| PositionsID | int | NO | ✓ | ✓ | [[Positions]] |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
## Primary Key
CompanyID
PositionsID
ItemCode
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, PositionsID -> [[Positions]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_SalesPersonCustStockItemsAssignment]]

**Writes (1):**
- [[Pro_SalesPersonCustStockItemsAssignment]]

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
- [[Olives_BO/Tables/CustomersReturnItemQtyLimit]]
- [[Olives_BO/Tables/ItemsSuggestGroupLinkWithItems]]
- [[Olives_BO/Tables/SalesPersonItemsBalanceBatches]]
- [[Olives_BO/Tables/ItemsInventory]]
