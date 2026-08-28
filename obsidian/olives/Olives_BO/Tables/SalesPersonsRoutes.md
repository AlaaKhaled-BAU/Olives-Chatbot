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

**Planned / future salesman visits** — weekly route **template** (not GPS history, not actual visits).

- `WeekDay` 1–7 = Saturday–Friday (`Day` column confirms Arabic name).
- `Week1`–`Week4` = route id per **week-of-month slot** — resolve with `Fun_GetWeekNo` / BO week logic (same as `OT_SendSalesmanData`); do not assume calendar weeks 1–4 blindly.
- **Never query this table alone** for «زيارات قادمة»: join chain below.

**Push to tablet:** [[OT_SendSalesmanData]] reads this + [[CustomersFinancialDetails]] + [[RoutesInformation]] and builds `OSFA_DB.OT_SalesmanRoute` (daily customer list). Optional override: [[SalespersonRouteByDate]] (sparse, some clients).

**Chatbot planned visits:** `SalesPersons` → `PositionID` → this table for target weekday → pick correct `WeekN` column → `CustomersFinancialDetails` (`RouteID`, `VisitOrder`, same `PositionsID`) → `RoutesInformation.Name`.

**Actual past visits:** [[LogActionTransaction]] (`ActionID = N'0'`), imported via [[OT_ImportActionLog]] — not this table.

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
## Tenancy

Chatbot queries `t.SalesPersonsRoutes` only — auto-scoped by `SESSION_CONTEXT(N'CompanyID')`.

## Common Issues

- **Calendar**: WeekDay integers verified live: 1=السبت(Sat),2=الأحد(Sun),3=الاثنين(Mon),4=الثلاثاء(Tue),5=الأربعاء(Wed),6=الخميس(Thu),7=الجمعة(Fri)
- **Slot selection**: do NOT assume Week1..4 = week-of-month; resolve via app logic (Fun_GetWeekNo usage in Rpt procs)
## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
