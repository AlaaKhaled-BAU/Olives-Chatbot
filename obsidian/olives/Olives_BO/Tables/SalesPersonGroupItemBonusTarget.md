---
type: table
database: Olives_BO
name: SalesPersonGroupItemBonusTarget
schema: dbo
tags: [#backoffice, #inventory, #reference, #sales]
foreign_keys:
  - [[Companies]]
  - [[ItemsUnits]]
  - [[SalesPersonsGroups]]
referenced_by:
  - [[Pro_SalesPersonGroupItemBonusTarget]]
  - [[Pro_SalesPersonItemBonusTarget_Online]]
  - [[Pro_SalesPersonItemBonusTarget_OnlineErrorReporting]]
  - [[Rpt_SalesPersonItemBonusTarget]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesPersonGroupItemBonusTarget


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersongroupitembonustarget records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersonsGroups]] |
| SalesPersonGroupID | int | NO | ✓ | ✓ | [[SalesPersonsGroups]] |
| TargetYear | smallint | NO | ✓ |  |  |
| ItemCode | nvarchar | YES | ✓ |  |  |
| UnitID | nvarchar | YES | ✓ | ✓ | [[ItemsUnits]] |
| M1 | float | YES |  |  |  |
| M2 | float | YES |  |  |  |
| M3 | float | YES |  |  |  |
| M4 | float | YES |  |  |  |
| M5 | float | YES |  |  |  |
| M6 | float | YES |  |  |  |
| M7 | float | YES |  |  |  |
| M8 | float | YES |  |  |  |
| M9 | float | YES |  |  |  |
| M10 | float | YES |  |  |  |
| M11 | float | YES |  |  |  |
| M12 | float | YES |  |  |  |
| Source | smallint | YES |  |  |  |
## Primary Key
CompanyID
SalesPersonGroupID
TargetYear
ItemCode
UnitID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, UnitID -> [[ItemsUnits]](CompanyID, ID)
CompanyID, SalesPersonGroupID -> [[SalesPersonsGroups]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (5):**
- [[Pro_SalesPersonGroupItemBonusTarget]]
- [[Pro_SalesPersonItemBonusTarget_Online]]
- [[Pro_SalesPersonItemBonusTarget_OnlineErrorReporting]]
- [[Rpt_SalesPersonItemBonusTarget]]

**Writes (1):**
- [[Pro_SalesPersonGroupItemBonusTarget]]

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
