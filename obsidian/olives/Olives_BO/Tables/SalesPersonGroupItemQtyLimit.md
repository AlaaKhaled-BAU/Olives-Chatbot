---
type: table
database: Olives_BO
name: SalesPersonGroupItemQtyLimit
schema: dbo
tags: [#backoffice, #inventory, #reference, #sales]
foreign_keys:
referenced_by:
  - [[Pro_ItemsTargetGroup]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesPersonGroupItemQtyLimit


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersongroupitemqtylimit records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| SalesPersonGroupID | int | NO | ✓ |  |  |
| ItemsTargetGroup | nvarchar | YES | ✓ |  |  |
| UnitID | nvarchar | YES |  |  |  |
| SoldQtyLimit | float | YES |  |  |  |
## Primary Key
CompanyID
SalesPersonGroupID
ItemsTargetGroup
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_ItemsTargetGroup]]

**Writes (1):**
- [[Pro_ItemsTargetGroup]]

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
