---
type: table
database: Olives_BO
name: RoutesInformation
schema: dbo
tags: [#backoffice, #gps, #sales]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[All_Visits]]
  - [[Alpha_SalesmanCustRoute]]
  - [[Pro_DriverDetailsDashboard]]
  - [[Pro_ImportData]]
  - [[Pro_ImportRouteInfoFromExcel]]
  - [[Pro_ImportRouteInfoFromExcel2]]
  - [[Pro_JoTaxApi]]
  - [[Pro_JoTaxApiFromOSFA]]
  - [[Pro_JoTaxApiFromOSFA____]]
  - [[Pro_MapTransactionLog]]
  - [[Pro_RoutesInformation]]
  - [[Pro_SalesPersonsAdditionalRoutes]]
  - [[Pro_SalesPersonsRoutes]]
  - [[Pro_SalesmanDetailsDashboard]]
  - [[Pro_SalespersonRouteByDate]]
  - [[Pro_TransactionsHeaders]]
  - [[Pro_ZatcaIntegrationApi]]
  - [[RPT_Salesman_Routes_Customers_MonthlyCountandVisits]]
  - [[RPT_ZheimanRouteSummaryForExcel]]
  - [[Rpt_CheckCustomers]]
  - [[Rpt_Coverage]]
  - [[Rpt_CustomerClassesByRoute]]
  - [[Rpt_CustomerInfoAndRouteDetails]]
  - [[Rpt_CustomerNotSold]]
  - [[Rpt_CustomerNotSoldBySalemanGroup]]
  - [[Rpt_CustomerSalesByUnit]]
  - [[Rpt_CustomersSalesAndVisits]]
  - [[Rpt_CustomersSalesAndVisits2]]
  - [[Rpt_DaliyRouteForExcel]]
  - [[Rpt_GetAssignedRoutesDataforReport]]
  - [[Rpt_ItemsSalesPerRoute]]
  - [[Rpt_LastInvoiceByRoute]]
  - [[Rpt_RouteScoreBySalesman]]
  - [[Rpt_RouteScoreBySalesman123]]
  - [[Rpt_RouteScoreBySalesmanFromDateToDate]]
  - [[Rpt_RouteSummaryBySalesman]]
  - [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
  - [[Rpt_RouteSummaryBySalesmanByCustomerClass]]
  - [[Rpt_RouteSummaryBySalesman_Delivery]]
  - [[Rpt_RouteSummaryBySalesman_Merchandisers]]
  - [[Rpt_RouteSummaryBySalesman_Sukhtian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
  - [[Rpt_RouteSummaryDeatils]]
  - [[Rpt_RoutesforExcel]]
  - [[Rpt_SalesByRoute]]
  - [[Rpt_SalesManVisitsVerification]]
  - [[Rpt_SalesPersonAndCustomer]]
  - [[Rpt_SalesmanCustRoutes]]
  - [[Rpt_SalesmanDailyRoute]]
  - [[Rpt_SalesmanGeneralDailyVisitsScore]]
  - [[Rpt_SalesmanRouteAssignment]]
  - [[Rpt_SalesmanRouteDetails]]
  - [[Rpt_SalesmanRouteDetails_SendToBarcodePrinter]]
  - [[Rpt_SalesmanSalesRecStatment]]
  - [[Rpt_SalesmanVisitsRoute]]
  - [[Rpt_SalespersonsDailyVisits]]
  - [[Rpt_StandView]]
  - [[Rpt_SuspendedCustomers]]
  - [[Rpt_UnvisitedCustomerDetails]]
  - [[Rpt_UnvisitedRouteCustomers]]
  - [[Rpt_customersbarcodes]]
  - [[Sama_GPS_Integ]]
  - [[Tablet_GetSalesmanRoute]]
  - [[Technical_CreateRouteBasedonID]]
  - [[Technical_CreateRouteBasedonID_ForPageOnly]]
  - [[Technical_CreateRouteBasedonReference1]]
  - [[Technical_CreateRouteBasedonReference1_UpdateOnly]]
support_relevance: high
last_verified: 2026-07-05
---
# RoutesInformation


## Business Purpose

Route definitions — sequences of customer visits assigned to salespersons.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (68):**
- [[All_Visits]]
- [[Alpha_SalesmanCustRoute]]
- [[Pro_DriverDetailsDashboard]]
- [[Pro_ImportData]]
- [[Pro_ImportRouteInfoFromExcel]]
- [[Pro_ImportRouteInfoFromExcel2]]
- [[Pro_JoTaxApi]]
- [[Pro_JoTaxApiFromOSFA]]
- [[Pro_JoTaxApiFromOSFA____]]
- [[Pro_MapTransactionLog]]
- [[Pro_RoutesInformation]]
- [[Pro_SalesPersonsAdditionalRoutes]]
- [[Pro_SalesPersonsRoutes]]
- [[Pro_SalesmanDetailsDashboard]]
- [[Pro_SalespersonRouteByDate]]
- [[Pro_TransactionsHeaders]]
- [[Pro_ZatcaIntegrationApi]]
- [[RPT_Salesman_Routes_Customers_MonthlyCountandVisits]]
- [[RPT_ZheimanRouteSummaryForExcel]]
- [[Rpt_CheckCustomers]]
- [[Rpt_Coverage]]
- [[Rpt_CustomerClassesByRoute]]
- [[Rpt_CustomerInfoAndRouteDetails]]
- [[Rpt_CustomerNotSold]]
- [[Rpt_CustomerNotSoldBySalemanGroup]]
- [[Rpt_CustomerSalesByUnit]]
- [[Rpt_CustomersSalesAndVisits]]
- [[Rpt_CustomersSalesAndVisits2]]
- [[Rpt_DaliyRouteForExcel]]
- [[Rpt_GetAssignedRoutesDataforReport]]
- [[Rpt_ItemsSalesPerRoute]]
- [[Rpt_LastInvoiceByRoute]]
- [[Rpt_RouteScoreBySalesman]]
- [[Rpt_RouteScoreBySalesman123]]
- [[Rpt_RouteScoreBySalesmanFromDateToDate]]
- [[Rpt_RouteSummaryBySalesman]]
- [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
- [[Rpt_RouteSummaryBySalesmanByCustomerClass]]
- [[Rpt_RouteSummaryBySalesman_Delivery]]
- [[Rpt_RouteSummaryBySalesman_Merchandisers]]
- [[Rpt_RouteSummaryBySalesman_Sukhtian]]
- [[Rpt_RouteSummaryBySalesman_Suktian]]
- [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
- [[Rpt_RouteSummaryDeatils]]
- [[Rpt_RoutesforExcel]]
- [[Rpt_SalesByRoute]]
- [[Rpt_SalesManVisitsVerification]]
- [[Rpt_SalesPersonAndCustomer]]
- [[Rpt_SalesmanCustRoutes]]
- [[Rpt_SalesmanDailyRoute]]
- [[Rpt_SalesmanGeneralDailyVisitsScore]]
- [[Rpt_SalesmanRouteAssignment]]
- [[Rpt_SalesmanRouteDetails]]
- [[Rpt_SalesmanRouteDetails_SendToBarcodePrinter]]
- [[Rpt_SalesmanSalesRecStatment]]
- [[Rpt_SalesmanVisitsRoute]]
- [[Rpt_SalespersonsDailyVisits]]
- [[Rpt_StandView]]
- [[Rpt_SuspendedCustomers]]
- [[Rpt_UnvisitedCustomerDetails]]
- [[Rpt_UnvisitedRouteCustomers]]
- [[Rpt_customersbarcodes]]
- [[Sama_GPS_Integ]]
- [[Tablet_GetSalesmanRoute]]
- [[Technical_CreateRouteBasedonID]]
- [[Technical_CreateRouteBasedonID_ForPageOnly]]
- [[Technical_CreateRouteBasedonReference1]]
- [[Technical_CreateRouteBasedonReference1_UpdateOnly]]

**Writes (8):**
- [[Alpha_SalesmanCustRoute]]
- [[Pro_ImportData]]
- [[Pro_ImportRouteInfoFromExcel2]]
- [[Pro_RoutesInformation]]
- [[Technical_CreateRouteBasedonID]]
- [[Technical_CreateRouteBasedonID_ForPageOnly]]
- [[Technical_CreateRouteBasedonReference1]]
- [[Technical_CreateRouteBasedonReference1_UpdateOnly]]

## Estimated Size / Volatility
Typical business table
## Common Issues
> [!warning] AUTO-GENERATED — verify before trusting

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
