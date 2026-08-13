---
type: table
database: Olives_BO
name: SalesPersonsRoutes
schema: dbo
tags: [#backoffice, #gps, #sales]
foreign_keys:
  - [[Companies]]
  - [[Positions]]
  - [[RoutesInformation]]
referenced_by:
  - [[All_Visits]]
  - [[Alpha_SalesmanCustRoute]]
  - [[Fill_In_Missing_PositionRoute]]
  - [[OT_WF_SalesmanVisits]]
  - [[Pro_Dashboard_Almalak]]
  - [[Pro_ImportRouteInfoFromExcel]]
  - [[Pro_ImportRouteInfoFromExcel2]]
  - [[Pro_MapTransactionLog]]
  - [[Pro_SalesPersonsAdditionalRoutes]]
  - [[Pro_SalesPersonsRoutes]]
  - [[Pro_SalesmanDetailsDashboard]]
  - [[RPT_Salesman_Routes_Customers_MonthlyCountandVisits]]
  - [[RPT_ZalloumReportONE]]
  - [[RPT_ZheimanRouteSummaryForExcel]]
  - [[Rpt_ActiveAndInactiveCustomers]]
  - [[Rpt_Coverage]]
  - [[Rpt_CustomerInfoAndRouteDetails]]
  - [[Rpt_DUR]]
  - [[Rpt_DaliyRouteForExcel]]
  - [[Rpt_RouteSummaryByDelivery]]
  - [[Rpt_RouteSummaryBySalesmanByCustomerClass]]
  - [[Rpt_RouteSummaryBySalesman_Delivery]]
  - [[Rpt_RouteSummaryBySalesman_Merchandisers]]
  - [[Rpt_RouteSummaryDeatils]]
  - [[Rpt_RoutesAvg]]
  - [[Rpt_RoutesforExcel]]
  - [[Rpt_SalesAndOrders]]
  - [[Rpt_SalesPersonSpecialTargets]]
  - [[Rpt_SalesTargetByCustCount_Telegraph]]
  - [[Rpt_SalesmanDailyRoute]]
  - [[Rpt_SalesmanRouteAvg]]
  - [[Rpt_SalesmanRouteDetails]]
  - [[Rpt_SalesmanRouteDetails_SendToBarcodePrinter]]
  - [[Rpt_SalesmanRouteEfficiency]]
  - [[Rpt_SalesmanRouteEfficiency_SV_LV_TV2]]
  - [[Rpt_SalesmanRouteEfficiency_Zoumt]]
  - [[Rpt_SalesmanRouteSummary]]
  - [[Rpt_SalesmanRouteTargetDetails]]
  - [[Rpt_SalesmanSummaryRoute]]
  - [[Rpt_SalesmanSummaryRoute_60]]
  - [[Rpt_SalesmanSummaryRoute_Atieh]]
  - [[Rpt_SalesmanSummaryRoute_Dandana]]
  - [[Rpt_SalesmanSummaryRoute_zz]]
  - [[Rpt_SalesmanVisitAnalysis]]
  - [[Rpt_SalesmanVisitsRoute]]
  - [[Rpt_TotalSalesmanRouteSummary]]
  - [[Rpt_TowerTargets]]
  - [[Rpt_TowerTargetsBO]]
  - [[Rpt_TransactionRouteAnalysis]]
  - [[Rpt_UnvisitedCustomersByDate]]
  - [[Rpt_WF_SalesmanVisits]]
  - [[Rpt_WF_UnvisitedCustomer]]
  - [[Rpt_WeeklySalesmanVisits]]
  - [[Sama_GPS_Integ]]
  - [[Tablet_GetSalesmanRoute]]
  - [[Technical_CreateRouteBasedonID]]
  - [[Technical_CreateRouteBasedonID_ForPageOnly]]
  - [[Technical_CreateRouteBasedonReference1]]
  - [[Technical_CreateRouteBasedonReference1_UpdateOnly]]
support_relevance: high
last_verified: 2026-07-05
related_workflows: [[Route-Planning]]
---
# SalesPersonsRoutes


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersonsroutes records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[RoutesInformation]] |
| PositionsID | int | NO | ✓ | ✓ | [[Positions]] |
| WeekDay | int | NO | ✓ |  |  |
| Week1 | int | YES |  | ✓ | [[RoutesInformation]] |
| Week2 | int | YES |  | ✓ | [[RoutesInformation]] |
| Week3 | int | YES |  | ✓ | [[RoutesInformation]] |
| Week4 | int | YES |  | ✓ | [[RoutesInformation]] |
| Day | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
PositionsID
WeekDay
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, PositionsID -> [[Positions]](CompanyID, ID)
CompanyID, Week1 -> [[RoutesInformation]](CompanyID, ID)
CompanyID, Week2 -> [[RoutesInformation]](CompanyID, ID)
CompanyID, Week3 -> [[RoutesInformation]](CompanyID, ID)
CompanyID, Week4 -> [[RoutesInformation]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (59):**
- [[All_Visits]]
- [[Alpha_SalesmanCustRoute]]
- [[Fill_In_Missing_PositionRoute]]
- [[OT_WF_SalesmanVisits]]
- [[Pro_Dashboard_Almalak]]
- [[Pro_ImportRouteInfoFromExcel]]
- [[Pro_ImportRouteInfoFromExcel2]]
- [[Pro_MapTransactionLog]]
- [[Pro_SalesPersonsAdditionalRoutes]]
- [[Pro_SalesPersonsRoutes]]
- [[Pro_SalesmanDetailsDashboard]]
- [[RPT_Salesman_Routes_Customers_MonthlyCountandVisits]]
- [[RPT_ZalloumReportONE]]
- [[RPT_ZheimanRouteSummaryForExcel]]
- [[Rpt_ActiveAndInactiveCustomers]]
- [[Rpt_Coverage]]
- [[Rpt_CustomerInfoAndRouteDetails]]
- [[Rpt_DUR]]
- [[Rpt_DaliyRouteForExcel]]
- [[Rpt_RouteSummaryByDelivery]]
- [[Rpt_RouteSummaryBySalesmanByCustomerClass]]
- [[Rpt_RouteSummaryBySalesman_Delivery]]
- [[Rpt_RouteSummaryBySalesman_Merchandisers]]
- [[Rpt_RouteSummaryDeatils]]
- [[Rpt_RoutesAvg]]
- [[Rpt_RoutesforExcel]]
- [[Rpt_SalesAndOrders]]
- [[Rpt_SalesPersonSpecialTargets]]
- [[Rpt_SalesTargetByCustCount_Telegraph]]
- [[Rpt_SalesmanDailyRoute]]
- [[Rpt_SalesmanRouteAvg]]
- [[Rpt_SalesmanRouteDetails]]
- [[Rpt_SalesmanRouteDetails_SendToBarcodePrinter]]
- [[Rpt_SalesmanRouteEfficiency]]
- [[Rpt_SalesmanRouteEfficiency_SV_LV_TV2]]
- [[Rpt_SalesmanRouteEfficiency_Zoumt]]
- [[Rpt_SalesmanRouteSummary]]
- [[Rpt_SalesmanRouteTargetDetails]]
- [[Rpt_SalesmanSummaryRoute]]
- [[Rpt_SalesmanSummaryRoute_60]]
- [[Rpt_SalesmanSummaryRoute_Atieh]]
- [[Rpt_SalesmanSummaryRoute_Dandana]]
- [[Rpt_SalesmanSummaryRoute_zz]]
- [[Rpt_SalesmanVisitAnalysis]]
- [[Rpt_SalesmanVisitsRoute]]
- [[Rpt_TotalSalesmanRouteSummary]]
- [[Rpt_TowerTargets]]
- [[Rpt_TowerTargetsBO]]
- [[Rpt_TransactionRouteAnalysis]]
- [[Rpt_UnvisitedCustomersByDate]]
- [[Rpt_WF_SalesmanVisits]]
- [[Rpt_WF_UnvisitedCustomer]]
- [[Rpt_WeeklySalesmanVisits]]
- [[Sama_GPS_Integ]]
- [[Tablet_GetSalesmanRoute]]
- [[Technical_CreateRouteBasedonID]]
- [[Technical_CreateRouteBasedonID_ForPageOnly]]
- [[Technical_CreateRouteBasedonReference1]]
- [[Technical_CreateRouteBasedonReference1_UpdateOnly]]

**Writes (8):**
- [[Alpha_SalesmanCustRoute]]
- [[Fill_In_Missing_PositionRoute]]
- [[Pro_ImportRouteInfoFromExcel2]]
- [[Pro_SalesPersonsRoutes]]
- [[Technical_CreateRouteBasedonID]]
- [[Technical_CreateRouteBasedonID_ForPageOnly]]
- [[Technical_CreateRouteBasedonReference1]]
- [[Technical_CreateRouteBasedonReference1_UpdateOnly]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
