---
type: table
database: Olives_BO
name: SalesPersonStockTackingDetails
schema: dbo
tags: [#backoffice, #inventory, #sales]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[SalesPersonStockTacking]]
referenced_by:
  - [[OT_ImportSalesmanStockTacking]]
  - [[Pro_ItemsUnitsDetails]]
  - [[Pro_SalesPersonStockTackingDetails]]
  - [[Rpt_SalesPersonStockTackingDetails]]
  - [[Rpt_StockTakingReport]]
  - [[Rpt_StockTakingReportWithPrices]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesPersonStockTackingDetails


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersonstocktackingdetails records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersonStockTacking]] |
| OrderYear | smallint | NO | ✓ | ✓ | [[SalesPersonStockTacking]] |
| OrderNo | int | NO | ✓ | ✓ | [[SalesPersonStockTacking]] |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
| UnitID | nvarchar | YES | ✓ | ✓ | [[ItemsUnits]] |
| BeginQuantity | float | YES |  |  |  |
| CurrQuantity | float | YES |  |  |  |
| Quantity | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
OrderYear
OrderNo
ItemCode
UnitID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, UnitID -> [[ItemsUnits]](CompanyID, ID)
CompanyID, OrderYear, OrderNo -> [[SalesPersonStockTacking]](CompanyID, OrderYear, OrderNo)
## Impact / Procedures Using This Table

**Reads (5):**
- [[Pro_ItemsUnitsDetails]]
- [[Pro_SalesPersonStockTackingDetails]]
- [[Rpt_SalesPersonStockTackingDetails]]
- [[Rpt_StockTakingReport]]
- [[Rpt_StockTakingReportWithPrices]]

**Writes (2):**
- [[OT_ImportSalesmanStockTacking]]
- [[Pro_SalesPersonStockTackingDetails]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
