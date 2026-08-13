---
type: table
database: Olives_BO
name: NewCompetitiveItems
schema: dbo
tags: [#backoffice, #inventory]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[ItemsCategories]]
referenced_by:
  - [[OT_ImportNewCompetitiveItems]]
  - [[Pro_NewCompetitiveItems]]
  - [[SalesmanInfo]]
support_relevance: high
last_verified: 2026-07-05
---
# NewCompetitiveItems


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores newcompetitiveitems records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[ItemsCategories]] |
| NewCompetitiveItemCode | nvarchar | YES | ✓ |  |  |
| SalesPerson | int | YES |  |  |  |
| ItemCode | nvarchar | YES |  | ✓ | [[Items]] |
| Name | nvarchar | YES |  |  |  |
| CategCode | nvarchar | YES |  | ✓ | [[ItemsCategories]] |
| CompetitiveCompany | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
NewCompetitiveItemCode
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, CategCode -> [[ItemsCategories]](CompanyID, CategCode)
## Impact / Procedures Using This Table

**Reads (3):**
- [[OT_ImportNewCompetitiveItems]]
- [[Pro_NewCompetitiveItems]]
- [[SalesmanInfo]]

**Writes (1):**
- [[OT_ImportNewCompetitiveItems]]

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
