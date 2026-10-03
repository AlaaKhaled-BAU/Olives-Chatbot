---
type: table
database: Olives_BO
name: SalesPersonsGroups
schema: dbo
tags: [#backoffice, #reference, #sales]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OSFA_SP_Api]]
  - [[OSFA_SP_Api_Jawad]]
  - [[Pro_ApproveImagesApp]]
  - [[Pro_Dashboard_Almalak]]
  - [[Pro_ImportData]]
  - [[Pro_Positions]]
  - [[Pro_SalesPersonGroupItemBonusTarget]]
  - [[Pro_SalesPersons]]
  - [[Pro_SalesPersonsGroups]]
  - [[Pro_SalesPersonsMessages]]
  - [[Pro_SalespersonsSendOrders]]
  - [[Pro_TransLock]]
  - [[Pro_WF_SetupHeader]]
  - [[RG_Rpt_PromotionInformation]]
  - [[Rpt_AnnualTargetAnalysis]]
  - [[Rpt_AreaSalesAndSalesmanTarget]]
  - [[Rpt_CustomerDailySales]]
  - [[Rpt_CustomerMonthlySales]]
  - [[Rpt_CustomerMonthlySalesByArea]]
  - [[Rpt_CustomerNotSold]]
  - [[Rpt_CustomerNotSoldBySalemanGroup]]
  - [[Rpt_CustomerSalesByItems]]
  - [[Rpt_CustomersAvgPerClass]]
  - [[Rpt_CustomersOrdersSummary]]
  - [[Rpt_CustomersSalesReturnCollectionMatching]]
  - [[Rpt_DailyDriver]]
  - [[Rpt_DailyUnit]]
  - [[Rpt_GpsLocationForTransaction]]
  - [[Rpt_MonthlyCompareSalesTargetWithSales]]
  - [[Rpt_MonthlySalesTargetBySalesman]]
  - [[Rpt_NetSalesItems]]
  - [[Rpt_NoSalesReasons]]
  - [[Rpt_NumericDistribution]]
  - [[Rpt_ProposedOrder]]
  - [[Rpt_Receipts]]
  - [[Rpt_SalesAndCollectionTargetByLocation]]
  - [[Rpt_SalesAndOrders]]
  - [[Rpt_SalesAreaAndCategoryByCust]]
  - [[Rpt_SalesAreaByCategory]]
  - [[Rpt_SalesByLocationsAndRoute]]
  - [[Rpt_SalesPersonItemBonusTarget]]
  - [[Rpt_SalesmanCashPayments]]
  - [[Rpt_SalesmanChequePayments]]
  - [[Rpt_SalesmanCoverage]]
  - [[Rpt_SalesmanGroupsByPromType]]
  - [[Rpt_SalesmanOrdersSummary]]
  - [[Rpt_SalesmanOrdersSummaryByCategory]]
  - [[Rpt_SalesmanRouteSummary]]
  - [[Rpt_SalesmanRouteTargetDetails]]
  - [[Rpt_SalesmanSalesByCategory]]
  - [[Rpt_SalesmanSalesByItems]]
  - [[Rpt_SalesmanSalesTargetByDay]]
  - [[Rpt_SalesmanSalesTotal_BO]]
  - [[Rpt_SalesmanSales_ByMonths]]
  - [[Rpt_SalesmanSoldAndNoSoldCustomers_BO]]
  - [[Rpt_SalesmanSummaryRoute]]
  - [[Rpt_TowerTargets]]
  - [[Rpt_TowerTargetsBO]]
  - [[Rpt_YearlySalesTarget]]
  - [[Rpt_YearlySalesTargetBySalesman]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Promotion-Setup
  - Salesman-Onboarding
  - Workflow-Approval-Setup
---
# SalesPersonsGroups


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersonsgroups records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| SalesPersonID | int | YES |  |  |  |
| CompanyBranchID | int | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (73):**
- [[Pro_ApproveImagesApp]]
- [[Pro_Dashboard_Almalak]]
- [[Pro_Positions]]
- [[Pro_SalesPersonGroupItemBonusTarget]]
- [[Pro_SalesPersonsGroups]]
- [[Pro_SalesPersonsMessages]]
- [[Pro_SalespersonsSendOrders]]
- [[Pro_TransLock]]
- [[Pro_WF_SetupHeader]]
- [[RG_Rpt_PromotionInformation]]
- [[Rpt_AnnualTargetAnalysis]]
- [[Rpt_AreaSalesAndSalesmanTarget]]
- [[Rpt_CustomerDailySales]]
- [[Rpt_CustomerMonthlySales]]
- [[Rpt_CustomerMonthlySalesByArea]]
- [[Rpt_CustomerNotSold]]
- [[Rpt_CustomerNotSoldBySalemanGroup]]
- [[Rpt_CustomerSalesByItems]]
- [[Rpt_CustomersAvgPerClass]]
- [[Rpt_CustomersOrdersSummary]]
- [[Rpt_CustomersSalesReturnCollectionMatching]]
- [[Rpt_DailyDriver]]
- [[Rpt_DailyUnit]]
- [[Rpt_GpsLocationForTransaction]]
- [[Rpt_MonthlyCompareSalesTargetWithSales]]
- [[Rpt_MonthlySalesTargetBySalesman]]
- [[Rpt_NetSalesItems]]
- [[Rpt_NoSalesReasons]]
- [[Rpt_NumericDistribution]]
- [[Rpt_ProposedOrder]]
- [[Rpt_Receipts]]
- [[Rpt_SalesAndCollectionTargetByLocation]]
- [[Rpt_SalesAndOrders]]
- [[Rpt_SalesAreaAndCategoryByCust]]
- [[Rpt_SalesAreaByCategory]]
- [[Rpt_SalesByLocationsAndRoute]]
- [[Rpt_SalesPersonItemBonusTarget]]
- [[Rpt_SalesmanCashPayments]]
- [[Rpt_SalesmanChequePayments]]
- [[Rpt_SalesmanCoverage]]
- [[Rpt_SalesmanGroupsByPromType]]
- [[Rpt_SalesmanOrdersSummary]]
- [[Rpt_SalesmanOrdersSummaryByCategory]]
- [[Rpt_SalesmanRouteSummary]]
- [[Rpt_SalesmanRouteTargetDetails]]
- [[Rpt_SalesmanSalesByCategory]]
- [[Rpt_SalesmanSalesByItems]]
- [[Rpt_SalesmanSalesTargetByDay]]
- [[Rpt_SalesmanSalesTotal_BO]]
- [[Rpt_SalesmanSales_ByMonths]]
- [[Rpt_SalesmanSoldAndNoSoldCustomers_BO]]
- [[Rpt_SalesmanSummaryRoute]]
- [[Rpt_TowerTargets]]
- [[Rpt_TowerTargetsBO]]
- [[Rpt_YearlySalesTarget]]
- [[Rpt_YearlySalesTargetBySalesman]]

**Writes (37):**
- [[OSFA_SP_Api]]
- [[OSFA_SP_Api_Jawad]]
- [[Pro_ImportData]]
- [[Pro_SalesPersons]]
- [[Pro_SalesPersonsGroups]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
