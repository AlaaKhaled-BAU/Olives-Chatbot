---
type: table
database: Olives_BO
name: CustomerStockTackingDetails
schema: dbo
tags: [#backoffice, #customer, #inventory]
foreign_keys:
  - [[Companies]]
  - [[CustomerStockTacking]]
  - [[Items]]
  - [[ItemsUnits]]
referenced_by:
  - [[OT_ImportCustStockTacking]]
  - [[Pro_CustomerStockTackingDetails]]
  - [[Pro_ItemsUnitsDetails]]
  - [[Rpt_CompareCustomerStockWithOrder]]
  - [[Rpt_CustomerStockByExpire]]
  - [[Rpt_CustomerStockNotExistByDocType]]
  - [[Rpt_CustomerStockNotExistByDocType_Summary]]
  - [[Rpt_CustomerStockTackingReport]]
  - [[Rpt_CustomerStockTackingReportByItems]]
  - [[Rpt_CustomerStockandCompetitveItems]]
  - [[Rpt_ItemsStockStatement]]
  - [[Rpt_ShelfStockTakingWithImages]]
  - [[Rpt_StockTaking]]
  - [[Rpt_TowerTargets]]
  - [[Rpt_TowerTargetsBO]]
  - [[Rpt_TowerTargets_Distribution]]
  - [[SalesmanInfo]]
support_relevance: high
last_verified: 2026-07-05
---
# CustomerStockTackingDetails


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customerstocktackingdetails records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[ItemsUnits]] |
| OrderYear | smallint | NO | ✓ | ✓ | [[CustomerStockTacking]] |
| OrderNo | int | NO | ✓ | ✓ | [[CustomerStockTacking]] |
| ItemCode | nvarchar | NO | ✓ | ✓ | [[Items]] |
| UnitID | nvarchar | NO | ✓ | ✓ | [[ItemsUnits]] |
| Quantity | float | YES |  |  |  |
| ItemImage | image | YES |  |  |  |
| ExpDate | smalldatetime | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| SP_Qty | float | YES |  |  |  |
| ItemStatus | nvarchar | YES |  |  |  |
| price | nvarchar | YES |  |  |  |
| no_faces | int | YES |  |  |  |

## Primary Key
CompanyID
OrderYear
OrderNo
ItemCode
UnitID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, OrderYear, OrderNo -> [[CustomerStockTacking]](CompanyID, OrderYear, OrderNo)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, UnitID -> [[ItemsUnits]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (16):**
- [[Pro_CustomerStockTackingDetails]]
- [[Pro_ItemsUnitsDetails]]
- [[Rpt_CompareCustomerStockWithOrder]]
- [[Rpt_CustomerStockByExpire]]
- [[Rpt_CustomerStockNotExistByDocType]]
- [[Rpt_CustomerStockNotExistByDocType_Summary]]
- [[Rpt_CustomerStockTackingReport]]
- [[Rpt_CustomerStockTackingReportByItems]]
- [[Rpt_CustomerStockandCompetitveItems]]
- [[Rpt_ItemsStockStatement]]
- [[Rpt_ShelfStockTakingWithImages]]
- [[Rpt_StockTaking]]
- [[Rpt_TowerTargets]]
- [[Rpt_TowerTargetsBO]]
- [[Rpt_TowerTargets_Distribution]]
- [[SalesmanInfo]]

**Writes (1):**
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
