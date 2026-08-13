---
type: table
database: Olives_BO
name: CompetitiveItems
schema: dbo
tags: [#backoffice, #inventory]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[ItemsCategories]]
referenced_by:
  - [[OT_SendCompData]]
  - [[Pro_CompetitiveItems]]
  - [[Rpt_CustomerStockandCompetitveItems]]
support_relevance: high
last_verified: 2026-07-05
---
# CompetitiveItems


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores competitiveitems records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[ItemsCategories]] |
| CompetitiveItemCode | nvarchar | YES | ✓ |  |  |
| ItemCode | nvarchar | YES |  | ✓ | [[Items]] |
| Name | nvarchar | YES |  |  |  |
| CategCode | nvarchar | YES |  | ✓ | [[ItemsCategories]] |
| CompetitiveCompany | nvarchar | YES |  |  |  |
| ItemImage | image | YES |  |  |  |
## Primary Key
CompanyID
CompetitiveItemCode
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, CategCode -> [[ItemsCategories]](CompanyID, CategCode)
## Impact / Procedures Using This Table

**Reads (3):**
- [[OT_SendCompData]]
- [[Pro_CompetitiveItems]]
- [[Rpt_CustomerStockandCompetitveItems]]

**Writes (1):**
- [[Pro_CompetitiveItems]]

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
