---
type: table
database: Olives_BO
name: CustomerStockTacking
schema: dbo
tags: [#backoffice, #customer, #inventory]
foreign_keys:
  - [[Companies]]
  - [[Customers]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
referenced_by:
  - [[OT_ImportActionLog]]
  - [[OT_ImportCustStockTacking]]
  - [[Pro_CompanyParameters]]
  - [[Pro_CustomerStockTacking]]
  - [[Rpt_CompareCustomerStockWithOrder]]
  - [[Rpt_CustomerStockByExpire]]
  - [[Rpt_CustomerStockNotExistByDocType]]
  - [[Rpt_CustomerStockNotExistByDocType_Summary]]
  - [[Rpt_CustomerStockTackingReport]]
  - [[Rpt_CustomerStockTackingReportByItems]]
  - [[Rpt_CustomerStockandCompetitveItems]]
  - [[Rpt_ItemsStockStatement]]
  - [[Rpt_ReasonReprint]]
  - [[Rpt_ReprintCount]]
  - [[Rpt_ShelfStockTakingWithImages]]
  - [[Rpt_StockTaking]]
  - [[Rpt_TowerTargets]]
  - [[Rpt_TowerTargetsBO]]
  - [[Rpt_TowerTargets_Distribution]]
  - [[SalesmanInfo]]
support_relevance: high
last_verified: 2026-07-05
---
# CustomerStockTacking


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customerstocktacking records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Customers]] |
| OrderYear | smallint | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| OrderDate | smalldatetime | YES |  |  |  |
| CustomersID | bigint | YES |  | ✓ | [[Customers]] |
| SalesPersonID | int | YES |  | ✓ | [[SalesPersons]] |
| Notes | nvarchar | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| RouteID | int | YES |  | ✓ | [[RoutesInformation]] |
| DocumentTypeID | int | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| PrintOriginalCount | int | YES |  |  |  |
| PrintCopyCount | int | YES |  |  |  |
| ServerDate | smalldatetime | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| LocationLineID | int | YES |  |  |  |
| IsLinkedToSalesOrder | bit | YES |  |  |  |

## Primary Key
CompanyID
OrderYear
OrderNo
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomersID -> [[Customers]](CompanyID, ID)
CompanyID, RouteID -> [[RoutesInformation]](CompanyID, ID)
CompanyID, SalesPersonID -> [[SalesPersons]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (19):**
- [[OT_ImportCustStockTacking]]
- [[Pro_CompanyParameters]]
- [[Pro_CustomerStockTacking]]
- [[Rpt_CompareCustomerStockWithOrder]]
- [[Rpt_CustomerStockByExpire]]
- [[Rpt_CustomerStockNotExistByDocType]]
- [[Rpt_CustomerStockNotExistByDocType_Summary]]
- [[Rpt_CustomerStockTackingReport]]
- [[Rpt_CustomerStockTackingReportByItems]]
- [[Rpt_CustomerStockandCompetitveItems]]
- [[Rpt_ItemsStockStatement]]
- [[Rpt_ReasonReprint]]
- [[Rpt_ReprintCount]]
- [[Rpt_ShelfStockTakingWithImages]]
- [[Rpt_StockTaking]]
- [[Rpt_TowerTargets]]
- [[Rpt_TowerTargetsBO]]
- [[Rpt_TowerTargets_Distribution]]
- [[SalesmanInfo]]

**Writes (2):**
- [[OT_ImportActionLog]]
- [[OT_ImportCustStockTacking]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Duplicate customers**: Multiple records with same name/phone created during sync — support agent sees duplicate entries in dropdowns
- **Orphan references**: Customer records referenced by transactions that were soft-deleted — causes FK violation on cleanup
- **Balance mismatch**: CustomerBalance field diverges from actual calculated balance — run reconciliation proc
- **Suspend stuck**: IsSuspended flag not clearing after payment — check WF approval chain
- **GPS not collected**: IsCollectedGPS flag false — affects route optimization

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
