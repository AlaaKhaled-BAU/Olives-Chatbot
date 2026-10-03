---
type: table
database: Olives_BO
name: LogActionTransaction
schema: dbo
tags: [#backoffice, #log, #sales, #visit]
foreign_keys:
referenced_by:
  - [[All_Visits]]
  - [[AppDashBoard]]
  - [[DA_SalesTarget]]
  - [[MedicalEfficiencyOnlineReport]]
  - [[OT_FixActionLog]]
  - [[OT_ImportActionLog]]
  - [[OT_WF_SalesmanVisits]]
  - [[POAOnlineReport]]
  - [[PRO_GETCUSTVISITEXITNOTES]]
  - [[Pro_ApproveImagesApp]]
  - [[Pro_CompanyParameters]]
  - [[Pro_DeliveryDashboard]]
  - [[Pro_DriverDetailsDashboard]]
  - [[Pro_GetCashCloseTotals]]
  - [[Pro_MapTransactionLog]]
  - [[Pro_SalesPersons]]
  - [[Pro_SalesmanDetailsDashboard]]
  - [[Pro_SalesmanImages]]
  - [[RPT_RoutesummarybysalesmancompineExcel2]]
  - [[RPT_Salesman_Routes_Customers_MonthlyCountandVisits]]
  - [[RPT_ZalloumReportONE]]
  - [[RPT_ZalloumReportTHREE]]
  - [[RPT_ZheimanRouteSummaryForExcel]]
  - [[RouteCoverageSummary_New_Excel]]
  - [[RptOnlineRpt_SalesmanJournySummary]]
  - [[Rpt_CalculateGPSDifference]]
  - [[Rpt_ConcreteVehicleTransactions]]
  - [[Rpt_Coverage]]
  - [[Rpt_CustGpsWithVisits]]
  - [[Rpt_CustomerLatsVistsAndInvoice]]
  - [[Rpt_CustomerSupervisorVisitsCount]]
  - [[Rpt_CustomersCountVisitByWeek]]
  - [[Rpt_CustomersExpansion]]
  - [[Rpt_CustomersSalesAndVisits2]]
  - [[Rpt_CustomersVisitsCount]]
  - [[Rpt_CustomersVisitsCountByCategory]]
  - [[Rpt_CustomersVisitsCountByClass]]
  - [[Rpt_CustomersVisitsPerRoute]]
  - [[Rpt_CustomersVisitsPerRoute_SUP]]
  - [[Rpt_DUR]]
  - [[Rpt_DailyConcrete]]
  - [[Rpt_DeliveryAndroidreport]]
  - [[Rpt_DeliveryInvoiceTransaction]]
  - [[Rpt_DetectDataUpdate]]
  - [[Rpt_GA_SalesmanAnalysis]]
  - [[Rpt_LastInvoiceByRoute]]
  - [[Rpt_MerchSummary_Excel]]
  - [[Rpt_NetVisitsTime]]
  - [[Rpt_NoSalesReasons]]
  - [[Rpt_RoutePerformanceAnalysis]]
  - [[Rpt_RouteScoreBySalesman]]
  - [[Rpt_RouteScoreBySalesman123]]
  - [[Rpt_RouteScoreBySalesmanCombine]]
  - [[Rpt_RouteScoreBySalesmanFromDateToDate]]
  - [[Rpt_RouteSummaryByDelivery]]
  - [[Rpt_RouteSummaryByDeliveryCombine]]
  - [[Rpt_RouteSummaryBySalesman]]
  - [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
  - [[Rpt_RouteSummaryBySalesmanByCustomerClass]]
  - [[Rpt_RouteSummaryBySalesmanByCustomerClassCombine]]
  - [[Rpt_RouteSummaryBySalesmanByCustomerClassCombine2]]
  - [[Rpt_RouteSummaryBySalesmanCombine]]
  - [[Rpt_RouteSummaryBySalesmanCombineForEFF]]
  - [[Rpt_RouteSummaryBySalesmanCombine_Merchandisers]]
  - [[Rpt_RouteSummaryBySalesmanCombine_New]]
  - [[Rpt_RouteSummaryBySalesmanCombine_Sukhtian]]
  - [[Rpt_RouteSummaryBySalesmanCombine_Sukhtian_Totals]]
  - [[Rpt_RouteSummaryBySalesmanCombineforExcel]]
  - [[Rpt_RouteSummaryBySalesmanCombineforExcel_Bushnaq]]
  - [[Rpt_RouteSummaryBySalesman_Delivery]]
  - [[Rpt_RouteSummaryBySalesman_Merchandisers]]
  - [[Rpt_RouteSummaryBySalesman_Sukhtian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
  - [[Rpt_RouteSummaryDeatils]]
  - [[Rpt_RouteVisitsByWeekDay]]
  - [[Rpt_RouteVisitsByWeekDayforExcel]]
  - [[Rpt_RoutesAvg]]
  - [[Rpt_RoutesByPeriod]]
  - [[Rpt_SalesAndOrders]]
  - [[Rpt_SalesManVisitsVerification]]
  - [[Rpt_SalesPersonSpecialTargets]]
  - [[Rpt_SalesmanActivity]]
  - [[Rpt_SalesmanAppVersion]]
  - [[Rpt_SalesmanDailyActivities]]
  - [[Rpt_SalesmanDaySummary]]
  - [[Rpt_SalesmanDaySummaryCombine]]
  - [[Rpt_SalesmanGeneralDailyVisitsScore]]
  - [[Rpt_SalesmanJourneyPerformance]]
  - [[Rpt_SalesmanJourneyPerformanceDetails]]
  - [[Rpt_SalesmanRouteAvg]]
  - [[Rpt_SalesmanRouteEfficiency]]
  - [[Rpt_SalesmanRouteEfficiency_SV_LV_TV2]]
  - [[Rpt_SalesmanRoutePerformance]]
  - [[Rpt_SalesmanRouteSummary]]
  - [[Rpt_SalesmanRouteTargetDetails]]
  - [[Rpt_SalesmanSummaryRoute]]
  - [[Rpt_SalesmanSummaryRoute_60]]
  - [[Rpt_SalesmanSummaryRoute_Atieh]]
  - [[Rpt_SalesmanSummaryRoute_Dandana]]
  - [[Rpt_SalesmanSummaryRoute_zz]]
  - [[Rpt_SalesmanTimeSpentPerCustomer]]
  - [[Rpt_SalesmanTimeSpentPerCustomer2]]
  - [[Rpt_SalesmanTimeSpentPerCustomer3]]
  - [[Rpt_SalesmanTimeSpentPerCustomer3Combine]]
  - [[Rpt_SalesmanTimeSpentPerCustomer3CombinePerCustomer]]
  - [[Rpt_SalesmanTimeSpentPerCustomer4]]
  - [[Rpt_SalesmanTimeSpentPerCustomer4Combine]]
  - [[Rpt_SalesmanTimeSpentPerCustomer6_QimaH]]
  - [[Rpt_SalesmanTimeSpentPerCustomer6_QimaHCombine]]
  - [[Rpt_SalesmanTimeSpentPerCustomerCombineQima7]]
  - [[Rpt_SalesmanTimeSpentPerCustomerCombineQima9]]
  - [[Rpt_SalesmanTimeSpentPerCustomerQima7]]
  - [[Rpt_SalesmanTimeSpentPerCustomerQima8]]
  - [[Rpt_SalesmanVisitAnalysis]]
  - [[Rpt_SalesmanVisitTimeAverage]]
  - [[Rpt_SalesmanVisitsByPeriod]]
  - [[Rpt_SalesmanVisitsByPeriodSummary]]
  - [[Rpt_SalesmanVisitsRoute]]
  - [[Rpt_SalesmenVisitsByCustomers]]
  - [[Rpt_SalesmenVisitsDetails]]
  - [[Rpt_SalespersonsDailyVisits]]
  - [[Rpt_SecurityLog]]
  - [[Rpt_TargetSpartan]]
  - [[Rpt_TimeManagement]]
  - [[Rpt_TotalSalesmanRouteSummary]]
  - [[Rpt_TowerTargets]]
  - [[Rpt_TowerTargetsBO]]
  - [[Rpt_TransactionRouteAnalysis]]
  - [[Rpt_TransactionsPrintStatusLog]]
  - [[Rpt_UnvisitedCustomer_WF]]
  - [[Rpt_UnvisitedCustomersByDate]]
  - [[Rpt_UnvisitedRouteCustomers]]
  - [[Rpt_UnvisitedRouteCustomers_FromDateToDate]]
  - [[Rpt_WFCustomersVisits]]
  - [[Rpt_WF_SalesmanVisits]]
  - [[Rpt_WF_UnvisitedCustomer]]
  - [[Rpt_WeeklySalesmanVisits]]
  - [[Rpt_first_last_visit_Invoice_TowerExcel]]
  - [[SalesmanInfo]]
  - [[SalesmenRoutesummery_Range_forExcel]]
  - [[Tech_No_Gps_Check_for_second_Visit]]
  - [[Technical_RestoreRoutefromlogaction]]
  - [[Tower_Visits_Coverage_Percentage]]
support_relevance: high
last_verified: 2026-08-28
---
# LogActionTransaction


## Business Purpose

**The field-activity log** — every salesman tablet action that `OT_ImportActionLog` copied from OSFA `OT_ActionLog` into BO (`OSFA_AutoID` is the tablet row). This is the source of truth for **actual** visits and for stamping GPS/location onto documents. Query `t.LogActionTransaction` (tenant via `CompNo`). `lookup_hot` loads the ActionID codebook (`LogActions`), not these fact rows.

**Data1/Data2 meaning depends on ActionID — never treat Data1 as always a customer:**
- `0` CustEntry / `3` CustLeave: `Data1` = customer id (visit). Count visits as `ActionID = N'0'`, not `7` (SystemLogin).
- `8` NoSaleExit: `Data1` = customer. `14`/`15` prospective entry/leave. `21` will-not-visit. `31` postpone.
- `4` InvoiceIssue, `5` OrderIssue, `9` ReturnInvoiceIssue, `12` PaymentIssue: `Data1` = **document year**, `Data2` = **document number**.
- `10` StartJourney / `11` EndJourney: no customer. `45`/`46` open/close cash. `49` pending-invoice JSON in Data1 — exclude from visit counts.
- SalesmanID is nvarchar; `TRY_CAST` to `SalesPersons.ID`. Not the route calendar (that is `SalesPersonsRoutes`).

## ActionID codebook

Decode `ActionID` via [[LogActions]] (`lookup_hot("LogActions")` or `lookup_hot("LogActionTransaction")` — same codebook). Full id list + visit vs login rules: [[LogActions]].

**Workflow approvals** (موافقة تابلت، رفض، معلّق) are **not** `ActionID` — they live in [[WF_MasterLog]] / [[WF_SubLog]]; see [[Workflow_Approval_Codes]].

Visit-related: 0 CustEntry, 3 CustLeave, 8 NoSaleExit, 14/15 prospective, 21 will-not-visit, 31 postpone, 38 no-visit reason import. Journey: 10 Start, 11 End. Documents: 4 invoice, 5 order, 9 return invoice, 12 payment. **7 SystemLogin = app login, not a customer visit.**

## Chatbot semantics
(Query `t.LogActionTransaction` — scoped by session CompNo/CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule |
|----------------------|-----------|---------------|
| عدد الزيارات الفعلية للعميل | `ActionID`, `Data1`, `SalesmanID`, `TimeStamp` | `ActionID = N'0' AND TRY_CAST(Data1 AS bigint) = @CustomerID` |
| زيارات المندوب اليومية الفعلية | `ActionID`, `SalesmanID`, `TimeStamp` | `ActionID = N'0' AND TRY_CAST(SalesmanID AS int) = @SalesmanID AND CAST(TimeStamp AS date) = @Date` |
| وقت دخول وخروج العميل (مدة الزيارة) | `ActionID = N'0'` (دخول) vs `ActionID = N'3'` (خروج) | حساب الفارق الزمني `DATEDIFF(minute, t0.TimeStamp, t3.TimeStamp)` |
| عدم بيع / خروج بدون حركة | `ActionID = N'8'` | خروج من زيارة عميل دون إصدار فاتورة أو طلبية |
| عدم زيارة مع ذكر السبب | `ActionID = N'21'` أو `N'38'` | عدم زيارة عميل مجدول مع توثيق السبب |
| بداية ونهاية الجولة للمندوب | `ActionID = N'10'` (بداية) و `ActionID = N'11'` (نهاية) | توقيت بدء وانتهاء يوم العمل الميداني |
| تسجيل الدخول للتطبيق (ليس زيارة) | `ActionID = N'7'` | `ActionID = N'7'` هو تسجيل دخول للنظام ولا يمثل زيارة عميل |
| إحداثيات وموقع الزيارة | `GpsX`, `GpsY` | خطوط الطول والعرض للتحقق من التواجد الجغرافي |

## Grain & keys
- **Grain**: One row per recorded field action / event on the mobile device (`AutoID`).
- **PK**: `AutoID`.
- **Tenant Key**: `CompNo`.

## Pipeline
Mobile Device Action Log (`OSFA_DB.dbo.OT_ActionLog`) → `OT_ImportActionLog` → `LogActionTransaction` → Reconciled before reports via `OT_FixActionLog`.

## Related
- [[LogActions]]
- [[SalesPersonsRoutes]]
- [[CustomersFinancialDetails]]
- [[Customers]]
- [[SalesPersons]]

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompNo | smallint | NO |  |  |  |
| ActionID | nvarchar | YES |  |  |  |
| TimeStamp | datetime | NO |  |  |  |
| SalesmanID | nvarchar | YES |  |  |  |
| Data1 | nvarchar | YES |  |  |  |
| Data2 | nvarchar | YES |  |  |  |
| Data3 | nvarchar | YES |  |  |  |
| Data4 | nvarchar | YES |  |  |  |
| Data5 | nvarchar | YES |  |  |  |
| GpsX | nchar | YES |  |  |  |
| GpsY | nchar | YES |  |  |  |
| RouteID | int | YES |  |  |  |
| OSFA_AutoID | numeric | YES |  |  |  |
| PostedByEmail | bit | YES |  |  |  |
| VehicleId | varchar | YES |  |  |  |
| CarCounter | bigint | YES |  |  |  |
| IsSMSSend | bit | YES |  |  |  |
| GPSOn | bit | YES |  |  |  |
| NetworkOn | bit | YES |  |  |  |
| InternetOn | bit | YES |  |  |  |
| AppVersion | varchar | YES |  |  |  |
| IsProcced | bit | YES |  |  |  |
| CustLocLineID | varchar | YES |  |  |  |
| AssistantsIDs | varchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (161):**
- [[All_Visits]]
- [[AppDashBoard]]
- [[DA_SalesTarget]]
- [[MedicalEfficiencyOnlineReport]]
- [[OT_FixActionLog]]
- [[OT_ImportActionLog]]
- [[OT_WF_SalesmanVisits]]
- [[POAOnlineReport]]
- [[PRO_GETCUSTVISITEXITNOTES]]
- [[Pro_ApproveImagesApp]]
- [[Pro_CompanyParameters]]
- [[Pro_DeliveryDashboard]]
- [[Pro_DriverDetailsDashboard]]
- [[Pro_GetCashCloseTotals]]
- [[Pro_MapTransactionLog]]
- [[Pro_SalesPersons]]
- [[Pro_SalesmanDetailsDashboard]]
- [[Pro_SalesmanImages]]
- [[RPT_RoutesummarybysalesmancompineExcel2]]
- [[RPT_Salesman_Routes_Customers_MonthlyCountandVisits]]
- [[RPT_ZalloumReportONE]]
- [[RPT_ZalloumReportTHREE]]
- [[RPT_ZheimanRouteSummaryForExcel]]
- [[RouteCoverageSummary_New_Excel]]
- [[RptOnlineRpt_SalesmanJournySummary]]
- [[Rpt_CalculateGPSDifference]]
- [[Rpt_ConcreteVehicleTransactions]]
- [[Rpt_Coverage]]
- [[Rpt_CustGpsWithVisits]]
- [[Rpt_CustomerLatsVistsAndInvoice]]
- [[Rpt_CustomerSupervisorVisitsCount]]
- [[Rpt_CustomersCountVisitByWeek]]
- [[Rpt_CustomersExpansion]]
- [[Rpt_CustomersSalesAndVisits2]]
- [[Rpt_CustomersVisitsCount]]
- [[Rpt_CustomersVisitsCountByCategory]]
- [[Rpt_CustomersVisitsCountByClass]]
- [[Rpt_CustomersVisitsPerRoute]]
- [[Rpt_CustomersVisitsPerRoute_SUP]]
- [[Rpt_DUR]]
- [[Rpt_DailyConcrete]]
- [[Rpt_DeliveryAndroidreport]]
- [[Rpt_DeliveryInvoiceTransaction]]
- [[Rpt_DetectDataUpdate]]
- [[Rpt_GA_SalesmanAnalysis]]
- [[Rpt_LastInvoiceByRoute]]
- [[Rpt_MerchSummary_Excel]]
- [[Rpt_NetVisitsTime]]
- [[Rpt_NoSalesReasons]]
- [[Rpt_RoutePerformanceAnalysis]]
- [[Rpt_RouteScoreBySalesman]]
- [[Rpt_RouteScoreBySalesman123]]
- [[Rpt_RouteScoreBySalesmanCombine]]
- [[Rpt_RouteScoreBySalesmanFromDateToDate]]
- [[Rpt_RouteSummaryByDelivery]]
- [[Rpt_RouteSummaryByDeliveryCombine]]
- [[Rpt_RouteSummaryBySalesman]]
- [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
- [[Rpt_RouteSummaryBySalesmanByCustomerClass]]
- [[Rpt_RouteSummaryBySalesmanByCustomerClassCombine]]
- [[Rpt_RouteSummaryBySalesmanByCustomerClassCombine2]]
- [[Rpt_RouteSummaryBySalesmanCombine]]
- [[Rpt_RouteSummaryBySalesmanCombineForEFF]]
- [[Rpt_RouteSummaryBySalesmanCombine_Merchandisers]]
- [[Rpt_RouteSummaryBySalesmanCombine_New]]
- [[Rpt_RouteSummaryBySalesmanCombine_Sukhtian]]
- [[Rpt_RouteSummaryBySalesmanCombine_Sukhtian_Totals]]
- [[Rpt_RouteSummaryBySalesmanCombineforExcel]]
- [[Rpt_RouteSummaryBySalesmanCombineforExcel_Bushnaq]]
- [[Rpt_RouteSummaryBySalesman_Delivery]]
- [[Rpt_RouteSummaryBySalesman_Merchandisers]]
- [[Rpt_RouteSummaryBySalesman_Sukhtian]]
- [[Rpt_RouteSummaryBySalesman_Suktian]]
- [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
- [[Rpt_RouteSummaryDeatils]]
- [[Rpt_RouteVisitsByWeekDay]]
- [[Rpt_RouteVisitsByWeekDayforExcel]]
- [[Rpt_RoutesAvg]]
- [[Rpt_RoutesByPeriod]]
- [[Rpt_SalesAndOrders]]
- [[Rpt_SalesManVisitsVerification]]
- [[Rpt_SalesPersonSpecialTargets]]
- [[Rpt_SalesmanActivity]]
- [[Rpt_SalesmanAppVersion]]
- [[Rpt_SalesmanDailyActivities]]
- [[Rpt_SalesmanDaySummary]]
- [[Rpt_SalesmanDaySummaryCombine]]
- [[Rpt_SalesmanGeneralDailyVisitsScore]]
- [[Rpt_SalesmanJourneyPerformance]]
- [[Rpt_SalesmanJourneyPerformanceDetails]]
- [[Rpt_SalesmanRouteAvg]]
- [[Rpt_SalesmanRouteEfficiency]]
- [[Rpt_SalesmanRouteEfficiency_SV_LV_TV2]]
- [[Rpt_SalesmanRoutePerformance]]
- [[Rpt_SalesmanRouteSummary]]
- [[Rpt_SalesmanRouteTargetDetails]]
- [[Rpt_SalesmanSummaryRoute]]
- [[Rpt_SalesmanSummaryRoute_60]]
- [[Rpt_SalesmanSummaryRoute_Atieh]]
- [[Rpt_SalesmanSummaryRoute_Dandana]]
- [[Rpt_SalesmanSummaryRoute_zz]]
- [[Rpt_SalesmanTimeSpentPerCustomer]]
- [[Rpt_SalesmanTimeSpentPerCustomer2]]
- [[Rpt_SalesmanTimeSpentPerCustomer3]]
- [[Rpt_SalesmanTimeSpentPerCustomer3Combine]]
- [[Rpt_SalesmanTimeSpentPerCustomer3CombinePerCustomer]]
- [[Rpt_SalesmanTimeSpentPerCustomer4]]
- [[Rpt_SalesmanTimeSpentPerCustomer4Combine]]
- [[Rpt_SalesmanTimeSpentPerCustomer6_QimaH]]
- [[Rpt_SalesmanTimeSpentPerCustomer6_QimaHCombine]]
- [[Rpt_SalesmanTimeSpentPerCustomerCombineQima7]]
- [[Rpt_SalesmanTimeSpentPerCustomerCombineQima9]]
- [[Rpt_SalesmanTimeSpentPerCustomerQima7]]
- [[Rpt_SalesmanTimeSpentPerCustomerQima8]]
- [[Rpt_SalesmanVisitAnalysis]]
- [[Rpt_SalesmanVisitTimeAverage]]
- [[Rpt_SalesmanVisitsByPeriod]]
- [[Rpt_SalesmanVisitsByPeriodSummary]]
- [[Rpt_SalesmanVisitsRoute]]
- [[Rpt_SalesmenVisitsByCustomers]]
- [[Rpt_SalesmenVisitsDetails]]
- [[Rpt_SalespersonsDailyVisits]]
- [[Rpt_SecurityLog]]
- [[Rpt_TargetSpartan]]
- [[Rpt_TimeManagement]]
- [[Rpt_TotalSalesmanRouteSummary]]
- [[Rpt_TowerTargets]]
- [[Rpt_TowerTargetsBO]]
- [[Rpt_TransactionRouteAnalysis]]
- [[Rpt_TransactionsPrintStatusLog]]
- [[Rpt_UnvisitedCustomer_WF]]
- [[Rpt_UnvisitedCustomersByDate]]
- [[Rpt_UnvisitedRouteCustomers]]
- [[Rpt_UnvisitedRouteCustomers_FromDateToDate]]
- [[Rpt_WFCustomersVisits]]
- [[Rpt_WF_SalesmanVisits]]
- [[Rpt_WF_UnvisitedCustomer]]
- [[Rpt_WeeklySalesmanVisits]]
- [[Rpt_first_last_visit_Invoice_TowerExcel]]
- [[SalesmanInfo]]
- [[SalesmenRoutesummery_Range_forExcel]]
- [[Tech_No_Gps_Check_for_second_Visit]]
- [[Technical_RestoreRoutefromlogaction]]
- [[Tower_Visits_Coverage_Percentage]]

**Writes (11):**
- [[OT_FixActionLog]]
- [[OT_ImportActionLog]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Data1 is overloaded**: customer id on 0/3/8; year+doc on 4/5/9/12 — joining Data1 to Customers on invoice rows is wrong
- **Visit count**: `ActionID = N'0'` only; `7` SystemLogin is more frequent and is not a visit
- **OSFA vs BO**: tablet writes `OT_ActionLog`; BO facts appear only after `OT_ImportActionLog` (Posted=1, OSFA_AutoID set)
- **Action 49**: JSON payload, not a visit; import also fills `PendingInvoices`

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
