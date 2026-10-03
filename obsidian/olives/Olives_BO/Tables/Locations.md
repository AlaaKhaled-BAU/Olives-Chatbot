---
type: table
database: Olives_BO
name: Locations
schema: dbo
tags: [#backoffice, #gps]
foreign_keys:
  - [[Companies]]
  - [[Locations]]
referenced_by:
  - [[AppDashBoard]]
  - [[OSFA_SP_Api]]
  - [[OSFA_SP_Api_Jawad]]
  - [[OT_SendCustomersInfo]]
  - [[Pro_AssetTransfer]]
  - [[Pro_CarAndSalespersonLink]]
  - [[Pro_CustomersAndAssets]]
  - [[Pro_CustomersClass]]
  - [[Pro_CustomersFinancialDetails]]
  - [[Pro_CustomersGPS]]
  - [[Pro_DeliveryAssigning]]
  - [[Pro_DeliveryCar]]
  - [[Pro_DeliveryInvoiceAssigning]]
  - [[Pro_ImportData]]
  - [[Pro_IssueAssets]]
  - [[Pro_LocationTargets]]
  - [[Pro_LocationTargetsDetails]]
  - [[Pro_Locations]]
  - [[Pro_LocationsAndSalespersonsLink]]
  - [[Pro_NewCustomers]]
  - [[Pro_OrdersHeaders]]
  - [[Pro_ProspectiveCustomers]]
  - [[Pro_ReceiptRequestsSchedule]]
  - [[Pro_SalesTrans]]
  - [[Pro_TransactionsHeaders]]
  - [[Pro_WithdrawAssets]]
  - [[RPT_LOCATIONSMAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
  - [[RPT_LOCATIONS_CUSTOMERTYPE_MAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
  - [[RPT_NIROUKHLOCATIONTARGET]]
  - [[Rpt_ApprovedOrder]]
  - [[Rpt_AreaSalesAnalysis]]
  - [[Rpt_AreaSalesAndSalesmanTarget]]
  - [[Rpt_AssetsByLocation]]
  - [[Rpt_CalculateGPSDifference]]
  - [[Rpt_CustGpsWithVisits]]
  - [[Rpt_CustomerFullLocation]]
  - [[Rpt_CustomerMonthlySalesByArea]]
  - [[Rpt_CustomerNameByLocation]]
  - [[Rpt_CustomerNotSold]]
  - [[Rpt_CustomerSupervisorVisitsCount]]
  - [[Rpt_CustomersVisitsPerRoute]]
  - [[Rpt_CustomersVisitsPerRoute_SUP]]
  - [[Rpt_DriversDeliverySummary]]
  - [[Rpt_LocationWithSalesmanSummary]]
  - [[Rpt_LocationsName]]
  - [[Rpt_NewCustomer]]
  - [[Rpt_NewCustomers]]
  - [[Rpt_NotSoldPerCateg]]
  - [[Rpt_ProspectiveCustomer]]
  - [[Rpt_ReturnOrder]]
  - [[Rpt_SalesAndCollectionTargetByLocation]]
  - [[Rpt_SalesAreaAndCategoryByCust]]
  - [[Rpt_SalesAreaByCategory]]
  - [[Rpt_SalesByLocationsAndRoute]]
  - [[Rpt_SalesPerRoute]]
  - [[Rpt_SalesPerRouteWithSalesman]]
  - [[Rpt_SalesmanCustRoutes]]
  - [[Rpt_SalesmanItemSalesPerRoute]]
  - [[Rpt_SalesmanRouteAssignment]]
  - [[Rpt_SalesmanRouteDetails]]
  - [[Rpt_SalesmanSales_ByMonths]]
  - [[Rpt_SoldUnsoldPerRoute]]
  - [[Rpt_StandView]]
  - [[Rpt_TransactionByDate]]
  - [[Rpt_UnloadCustomersPerRoute]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Company-Setup
---
# Locations


## Business Purpose

Geographic location hierarchy (country → region → city → area) for route planning.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Locations]] |
| ID | int | NO | ✓ |  |  |
| Parent | int | YES |  | ✓ | [[Locations]] |
| Name | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| Loc_Level | int | YES |  |  |  |
| PopulationNo | bigint | YES |  |  |  |
| ForeignName | nvarchar | YES |  |  |  |
| PostedToERP | bit | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, Parent -> [[Locations]](CompanyID, ID)
## Known Circular Dependencies
- Self-referencing FK (parent location hierarchy via Parent).
## Impact / Procedures Using This Table

**Reads (99):**
- [[AppDashBoard]]
- [[OT_SendCustomersInfo]]
- [[Pro_AssetTransfer]]
- [[Pro_CarAndSalespersonLink]]
- [[Pro_CustomersAndAssets]]
- [[Pro_CustomersClass]]
- [[Pro_CustomersFinancialDetails]]
- [[Pro_CustomersGPS]]
- [[Pro_DeliveryAssigning]]
- [[Pro_DeliveryCar]]
- [[Pro_DeliveryInvoiceAssigning]]
- [[Pro_ImportData]]
- [[Pro_IssueAssets]]
- [[Pro_LocationTargets]]
- [[Pro_LocationTargetsDetails]]
- [[Pro_Locations]]
- [[Pro_LocationsAndSalespersonsLink]]
- [[Pro_NewCustomers]]
- [[Pro_OrdersHeaders]]
- [[Pro_ProspectiveCustomers]]
- [[Pro_ReceiptRequestsSchedule]]
- [[Pro_SalesTrans]]
- [[Pro_TransactionsHeaders]]
- [[Pro_WithdrawAssets]]
- [[RPT_LOCATIONSMAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
- [[RPT_LOCATIONS_CUSTOMERTYPE_MAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
- [[RPT_NIROUKHLOCATIONTARGET]]
- [[Rpt_ApprovedOrder]]
- [[Rpt_AreaSalesAnalysis]]
- [[Rpt_AreaSalesAndSalesmanTarget]]
- [[Rpt_AssetsByLocation]]
- [[Rpt_CalculateGPSDifference]]
- [[Rpt_CustGpsWithVisits]]
- [[Rpt_CustomerFullLocation]]
- [[Rpt_CustomerMonthlySalesByArea]]
- [[Rpt_CustomerNameByLocation]]
- [[Rpt_CustomerNotSold]]
- [[Rpt_CustomerSupervisorVisitsCount]]
- [[Rpt_CustomersVisitsPerRoute]]
- [[Rpt_CustomersVisitsPerRoute_SUP]]
- [[Rpt_DriversDeliverySummary]]
- [[Rpt_LocationWithSalesmanSummary]]
- [[Rpt_LocationsName]]
- [[Rpt_NewCustomer]]
- [[Rpt_NewCustomers]]
- [[Rpt_NotSoldPerCateg]]
- [[Rpt_ProspectiveCustomer]]
- [[Rpt_ReturnOrder]]
- [[Rpt_SalesAndCollectionTargetByLocation]]
- [[Rpt_SalesAreaAndCategoryByCust]]
- [[Rpt_SalesAreaByCategory]]
- [[Rpt_SalesByLocationsAndRoute]]
- [[Rpt_SalesPerRoute]]
- [[Rpt_SalesPerRouteWithSalesman]]
- [[Rpt_SalesmanCustRoutes]]
- [[Rpt_SalesmanItemSalesPerRoute]]
- [[Rpt_SalesmanRouteAssignment]]
- [[Rpt_SalesmanRouteDetails]]
- [[Rpt_SalesmanSales_ByMonths]]
- [[Rpt_SoldUnsoldPerRoute]]
- [[Rpt_StandView]]
- [[Rpt_TransactionByDate]]
- [[Rpt_UnloadCustomersPerRoute]]

**Writes (36):**
- [[OSFA_SP_Api]]
- [[OSFA_SP_Api_Jawad]]
- [[Pro_ImportData]]
- [[Pro_Locations]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing GPS data**: No coordinates recorded — route planning and distance calc broken
- **Invalid coordinates**: GPSX/GPSY outside expected range — verify device GPS setting
- **Stale locations**: Old coordinates not updated — customer moved but records not refreshed

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
