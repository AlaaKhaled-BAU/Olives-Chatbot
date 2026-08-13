---
type: table
database: Olives_BO
name: CompetitveItemsDataDF
schema: dbo
tags: [#backoffice, #inventory]
foreign_keys:
  - [[Companies]]
  - [[CompetitveItemsDataHF]]
referenced_by:
  - [[OT_ImportCompetitveItemsData]]
  - [[Pro_CompetitveItemsDataDF]]
  - [[Rpt_CustomerStockandCompetitveItems]]
  - [[SalesmanInfo]]
support_relevance: high
last_verified: 2026-07-05
---
# CompetitveItemsDataDF


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores competitveitemsdatadf records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[CompetitveItemsDataHF]] |
| TrYear | smallint | NO | ✓ | ✓ | [[CompetitveItemsDataHF]] |
| TrNo | int | NO | ✓ | ✓ | [[CompetitveItemsDataHF]] |
| CompetitiveItem | nvarchar | YES | ✓ |  |  |
| Qty | money | YES |  |  |  |
| Price | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| ItemImage | image | YES |  |  |  |
| ShelfPrice | float | YES |  |  |  |
| RetailPrice | float | YES |  |  |  |
| WholeSalePrice | float | YES |  |  |  |
## Primary Key
CompanyID
TrYear
TrNo
CompetitiveItem
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, TrYear, TrNo -> [[CompetitveItemsDataHF]](CompanyID, TrYear, TrNo)
## Impact / Procedures Using This Table

**Reads (3):**
- [[Pro_CompetitveItemsDataDF]]
- [[Rpt_CustomerStockandCompetitveItems]]
- [[SalesmanInfo]]

**Writes (1):**
- [[OT_ImportCompetitveItemsData]]

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
