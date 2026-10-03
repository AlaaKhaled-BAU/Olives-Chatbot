---
type: table
database: Olives_BO
name: SalesPersonStockTacking
schema: dbo
tags: [#backoffice, #inventory, #sales]
foreign_keys:
  - [[Companies]]
  - [[SalesPersons]]
referenced_by:
  - [[OT_ImportSalesmanStockTacking]]
  - [[OT_ImportUnloadOrderForSalesmanStock]]
  - [[Pro_CompanyParameters]]
  - [[Pro_SalesPersonStockTacking]]
  - [[Pro_SalesPersonStockTackingDetails]]
  - [[Rpt_ReasonReprint]]
  - [[Rpt_ReprintCount]]
  - [[Rpt_SalesPersonStockTackingDetails]]
  - [[Rpt_StockTakingReport]]
  - [[Rpt_StockTakingReportWithPrices]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesPersonStockTacking


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersonstocktacking records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersons]] |
| OrderYear | smallint | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| OrderDate | smalldatetime | YES |  |  |  |
| SalesPersonID | int | YES |  | ✓ | [[SalesPersons]] |
| Notes | nvarchar | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| RouteID | int | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| PrintOriginalCount | int | YES |  |  |  |
| PrintCopyCount | int | YES |  |  |  |
| ServerDate | smalldatetime | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| PostedToERP | bit | YES |  |  |  |
| IsApproved | bit | YES |  |  |  |
| ExtraNote | nvarchar | YES |  |  |  |
| UnloadOrderNo | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
OrderYear
OrderNo
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, SalesPersonID -> [[SalesPersons]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (11):**
- [[OT_ImportSalesmanStockTacking]]
- [[Pro_CompanyParameters]]
- [[Pro_SalesPersonStockTacking]]
- [[Pro_SalesPersonStockTackingDetails]]
- [[Rpt_ReasonReprint]]
- [[Rpt_ReprintCount]]
- [[Rpt_SalesPersonStockTackingDetails]]
- [[Rpt_StockTakingReport]]
- [[Rpt_StockTakingReportWithPrices]]

**Writes (5):**
- [[OT_ImportSalesmanStockTacking]]
- [[OT_ImportUnloadOrderForSalesmanStock]]
- [[Pro_SalesPersonStockTacking]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
