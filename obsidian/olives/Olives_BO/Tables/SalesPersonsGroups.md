---
type: table
database: Olives_BO
name: SalesPersonsGroups
schema: dbo
tags: [#backoffice, #reference, #sales]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[Acback_Integration]]
  - [[Alpha_Integ]]
  - [[Alpha_updateRoute]]
  - [[Awael_Integration_WithLog]]
  - [[Awtar_Integration_GetPromotion]]
  - [[Awtar_Integration_WithLog]]
  - [[Darwaza_Integration_WithLog]]
  - [[Ejabi_Integration]]
  - [[GP_Integ]]
  - [[GP_Integ_Wadi]]
  - [[GTS_Integration_WithLog]]
  - [[Galaxy_Integration]]
  - [[Isco_Integration_WithLog]]
  - [[JV_Integ]]
  - [[Lafarg_Integration]]
  - [[MeatLand_Integration]]
  - [[MeatLand_Integrationnew]]
  - [[Mira_Integration_WithLog]]
  - [[Mira_Wales_Integration_WithLog]]
  - [[Niroukh_Integration_GetPromotion]]
  - [[Niroukh_Integration_WithLog]]
  - [[OSFA_SP_Api]]
  - [[OSFA_SP_Api_Jawad]]
  - [[Phenix_Sukhtian_Integ_WithLog]]
  - [[ProTech_Integration]]
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
  - [[Rpt_MonthlyCompareSalesTargetWithSales_Spartan]]
  - [[Rpt_MonthlySalesTargetBySalesman]]
  - [[Rpt_NetSalesItems]]
  - [[Rpt_NoSalesReasons]]
  - [[Rpt_NumericDistribution]]
  - [[Rpt_ProposedOrder]]
  - [[Rpt_Receipts]]
  - [[Rpt_RoutePerformanceAnalysis_Spartan]]
  - [[Rpt_SalesAndCollectionTargetByLocation]]
  - [[Rpt_SalesAndOrders]]
  - [[Rpt_SalesAreaAndCategoryByCust]]
  - [[Rpt_SalesAreaByCategory]]
  - [[Rpt_SalesByLocationsAndRoute]]
  - [[Rpt_SalesPersonItemBonusTarget]]
  - [[Rpt_SalesPersonItemBonusTarget_Tablet]]
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
  - [[SAP_Integ]]
  - [[SAP_Integ_Amazing]]
  - [[SAP_Integ_Hammoudeh]]
  - [[SAP_Integ_Karadsheh]]
  - [[SAP_Integ_Kaylani]]
  - [[SAP_Integ_Lamis]]
  - [[SAP_Integ_MERI]]
  - [[SAP_Integ_Malak]]
  - [[SAP_Integration_WithLog]]
  - [[SAP_Tyconz_Integ]]
  - [[SN_Integration]]
  - [[Shamel_Integration]]
  - [[Tahona_Integration_WithLog]]
  - [[X3_INTEGRATIONPROMOTION_WITHLOG]]
  - [[Yolande_Integ]]
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
- [[Acback_Integration]]
- [[Awael_Integration_WithLog]]
- [[Awtar_Integration_GetPromotion]]
- [[Ejabi_Integration]]
- [[GTS_Integration_WithLog]]
- [[Lafarg_Integration]]
- [[Mira_Integration_WithLog]]
- [[Mira_Wales_Integration_WithLog]]
- [[Niroukh_Integration_GetPromotion]]
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
- [[Rpt_MonthlyCompareSalesTargetWithSales_Spartan]]
- [[Rpt_MonthlySalesTargetBySalesman]]
- [[Rpt_NetSalesItems]]
- [[Rpt_NoSalesReasons]]
- [[Rpt_NumericDistribution]]
- [[Rpt_ProposedOrder]]
- [[Rpt_Receipts]]
- [[Rpt_RoutePerformanceAnalysis_Spartan]]
- [[Rpt_SalesAndCollectionTargetByLocation]]
- [[Rpt_SalesAndOrders]]
- [[Rpt_SalesAreaAndCategoryByCust]]
- [[Rpt_SalesAreaByCategory]]
- [[Rpt_SalesByLocationsAndRoute]]
- [[Rpt_SalesPersonItemBonusTarget]]
- [[Rpt_SalesPersonItemBonusTarget_Tablet]]
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
- [[SAP_Integration_WithLog]]
- [[SN_Integration]]
- [[Shamel_Integration]]
- [[Tahona_Integration_WithLog]]
- [[X3_INTEGRATIONPROMOTION_WITHLOG]]

**Writes (37):**
- [[Acback_Integration]]
- [[Alpha_Integ]]
- [[Alpha_updateRoute]]
- [[Awael_Integration_WithLog]]
- [[Awtar_Integration_WithLog]]
- [[Darwaza_Integration_WithLog]]
- [[Ejabi_Integration]]
- [[GP_Integ]]
- [[GP_Integ_Wadi]]
- [[GTS_Integration_WithLog]]
- [[Galaxy_Integration]]
- [[Isco_Integration_WithLog]]
- [[JV_Integ]]
- [[MeatLand_Integration]]
- [[MeatLand_Integrationnew]]
- [[Mira_Integration_WithLog]]
- [[Mira_Wales_Integration_WithLog]]
- [[Niroukh_Integration_WithLog]]
- [[OSFA_SP_Api]]
- [[OSFA_SP_Api_Jawad]]
- [[Phenix_Sukhtian_Integ_WithLog]]
- [[ProTech_Integration]]
- [[Pro_ImportData]]
- [[Pro_SalesPersons]]
- [[Pro_SalesPersonsGroups]]
- [[SAP_Integ]]
- [[SAP_Integ_Amazing]]
- [[SAP_Integ_Hammoudeh]]
- [[SAP_Integ_Karadsheh]]
- [[SAP_Integ_Kaylani]]
- [[SAP_Integ_Lamis]]
- [[SAP_Integ_MERI]]
- [[SAP_Integ_Malak]]
- [[SAP_Integration_WithLog]]
- [[SAP_Tyconz_Integ]]
- [[Shamel_Integration]]
- [[Yolande_Integ]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
