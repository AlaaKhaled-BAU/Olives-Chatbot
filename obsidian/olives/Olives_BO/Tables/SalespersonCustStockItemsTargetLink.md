---
type: table
database: Olives_BO
name: SalespersonCustStockItemsTargetLink
schema: dbo
tags: [#backoffice, #inventory, #sales]
foreign_keys:
referenced_by:
  - [[Pro_Items]]
  - [[Rpt_SalesTargetByCustCount_Telegraph]]
  - [[Rpt_TowerTargets]]
  - [[Rpt_TowerTargetsBO]]
  - [[Rpt_TowerTargets_Distribution]]
support_relevance: high
last_verified: 2026-07-05
---
# SalespersonCustStockItemsTargetLink


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersoncuststockitemstargetlink records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| PositionsID | int | NO | ✓ |  |  |
| ItemCode | nvarchar | YES | ✓ |  |  |
| TargetMonth | int | NO | ✓ |  |  |
| TargetYear | int | NO | ✓ |  |  |
## Primary Key
CompanyID
PositionsID
ItemCode
TargetMonth
TargetYear
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (5):**
- [[Pro_Items]]
- [[Rpt_SalesTargetByCustCount_Telegraph]]
- [[Rpt_TowerTargets]]
- [[Rpt_TowerTargetsBO]]
- [[Rpt_TowerTargets_Distribution]]

**Writes (1):**
- [[Pro_Items]]

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
