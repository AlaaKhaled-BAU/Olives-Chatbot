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
  - [[Technical_CreateRouteBasedonID]]
  - [[Technical_CreateRouteBasedonID_ForPageOnly]]
  - [[Technical_CreateRouteBasedonReference1]]
  - [[Technical_CreateRouteBasedonReference1_UpdateOnly]]
support_relevance: high
last_verified: 2026-10-03
related_workflows: [[Route-Planning]]
---
# SalesPersonsRoutes

## Business Purpose
**Planned / future salesman visits** — weekly route schedule **template** defining which route ID a sales position covers on each day of the week across 4 monthly cycle weeks (`Week1`..`Week4`). Queryable via `t.SalesPersonsRoutes`.

- `WeekDay` 1–7 = Saturday–Friday (`Day` column confirms Arabic name: السبت, الأحد, ...).
- `Week1`–`Week4` = route id per **week-of-month slot** — resolved with `Fun_GetWeekNo` / BO week logic.
- **Never query this table alone** for customer visit plans: customer-to-route assignment lives in [[CustomersFinancialDetails]].

## Chatbot semantics
(Query `t.SalesPersonsRoutes` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| خطة المسار الأسبوعية للمندوب | `PositionsID`, `WeekDay`, `Week1`..`Week4` | Filter by position | Returns route IDs for each day |
| مسار اليوم للمندوب | `WeekDay`, `Day` | Match weekday (1=السبت..7=الجمعة) | Pick corresponding `WeekN` route ID |
| الزبائن المخطط زيارتهم في المسار | Join `t.CustomersFinancialDetails` | `c.RouteID = r.WeekN AND c.PositionsID = r.PositionsID` | Customer list ordered by `c.VisitOrder` |
| اسم المسار | Join `t.RoutesInformation` | `RoutesInformation.ID = r.WeekN` | Name of the route |

**Do not confuse with:**
- `LogActionTransaction`: Actual visits performed in the field (`ActionID = N'0'`).
- `SalespersonRouteByDate`: Date-specific route overrides (used by some clients).
- `SalesmanVisitsSummary`: Hidden table in gate; do not route queries here.

## Grain & keys
- **Composite PK**: (`CompanyID`, `PositionsID`, `WeekDay`)
- **Tenant key**: `CompanyID`
- **FKs**: `PositionsID` → [[Positions]](ID), `Week1`..`Week4` → [[RoutesInformation]](ID)

## Pipeline (how rows get here)
Defined in Back Office route planning UI (`Pro_SalesPersonsRoutes`). Read by `OT_SendSalesmanData` to generate daily journey plans sent to salesman tablets.

## Related
- [[RoutesInformation]]
- [[CustomersFinancialDetails]]
- [[SalesPersons]]
- [[LogActionTransaction]]
- [[SalespersonRouteByDate]]


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
- [[Technical_CreateRouteBasedonID]]
- [[Technical_CreateRouteBasedonID_ForPageOnly]]
- [[Technical_CreateRouteBasedonReference1]]
- [[Technical_CreateRouteBasedonReference1_UpdateOnly]]

**Writes (8):**
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
