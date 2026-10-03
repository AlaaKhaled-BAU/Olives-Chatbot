---
type: table
database: Olives_BO
name: TargetsReferences
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[BO_Online_RptCustomerSalesTargetDetails]]
  - [[Da_SalesperRep]]
  - [[Da_YearlyCompanyTargetAndSales]]
  - [[NiroukhMonthlyandQuarter]]
  - [[NiroukhMonthlyandQuarter_Month]]
  - [[NiroukhTargetPerDay]]
  - [[OT_NiroukhMonthlyandQuarter_Month]]
  - [[Pro_CustomerTargetsDetails]]
  - [[Pro_LocationTargetsDetails]]
  - [[Pro_SalesPersonCollectionTargetsDetails]]
  - [[Pro_SalesPersonTargetsDetails]]
  - [[Pro_TargetsReferences]]
  - [[RPT_CUSTOMERSMAIN_SUBTARGETREPORT_COLLECTIONS]]
  - [[RPT_CUSTOMERSMAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
  - [[RPT_LOCATIONSMAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
  - [[RPT_LOCATIONS_CUSTOMERTYPE_MAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
  - [[RPT_NEWNIROUKH_MONTHTARGET]]
  - [[RPT_NIROUKHCUSTOMERCLASSTARGET]]
  - [[RPT_NIROUKHCUSTOMERSMAIN_SUBTARGETREPORT]]
  - [[RPT_NIROUKHLOCATIONTARGET]]
  - [[RPT_ZalloumReportTWO]]
  - [[Rpt_AnnualTargetAnalysis]]
  - [[Rpt_AreaSalesAndSalesmanTarget]]
  - [[Rpt_AssistantsSales]]
  - [[Rpt_AssistantsSalesDaily]]
  - [[Rpt_CompareCustSalesByCategAndTargetRef]]
  - [[Rpt_MonthlyCompareSalesTargetWithCustomer]]
  - [[Rpt_MonthlyCompareSalesTargetWithSales]]
  - [[Rpt_MonthlySalesTargetBySalesman]]
  - [[Rpt_NiroukhMonths_Q_Target]]
  - [[Rpt_SalesAndCollectionTargetByLocation]]
  - [[Rpt_SalesCollcetionsTargets]]
  - [[Rpt_SalesPersonTarget]]
  - [[Rpt_SalesmanOrdersSummaryByTargetRef]]
  - [[Rpt_SalesmanSalesTargetByDay]]
  - [[Rpt_SalesmanTargetCommission]]
  - [[Rpt_SalespersonTargetComparison]]
  - [[Rpt_TargetSpartan]]
  - [[Rpt_TowerTargetsBO]]
  - [[Rpt_YearlySalesTarget]]
  - [[Rpt_YearlySalesTargetBySalesman]]
  - [[Rpt_newNiroukh_monthTarget_comm]]
support_relevance: high
last_verified: 2026-07-05
---
# TargetsReferences


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores targetsreferences records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| IsFocusItems | bit | YES |  |  |  |
| RefWieght | float | YES |  |  |  |
| RefPaidTargetAmt | float | YES |  |  |  |
| UnitCode | nvarchar | YES |  |  |  |
| Qty | float | YES |  |  |  |
| IsFocusItemsProductivity | bit | YES |  |  |  |
| TargetPercentage | float | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (48):**
- [[BO_Online_RptCustomerSalesTargetDetails]]
- [[Da_SalesperRep]]
- [[Da_YearlyCompanyTargetAndSales]]
- [[NiroukhMonthlyandQuarter]]
- [[NiroukhMonthlyandQuarter_Month]]
- [[NiroukhTargetPerDay]]
- [[OT_NiroukhMonthlyandQuarter_Month]]
- [[Pro_CustomerTargetsDetails]]
- [[Pro_LocationTargetsDetails]]
- [[Pro_SalesPersonCollectionTargetsDetails]]
- [[Pro_SalesPersonTargetsDetails]]
- [[Pro_TargetsReferences]]
- [[RPT_CUSTOMERSMAIN_SUBTARGETREPORT_COLLECTIONS]]
- [[RPT_CUSTOMERSMAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
- [[RPT_LOCATIONSMAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
- [[RPT_LOCATIONS_CUSTOMERTYPE_MAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
- [[RPT_NEWNIROUKH_MONTHTARGET]]
- [[RPT_NIROUKHCUSTOMERCLASSTARGET]]
- [[RPT_NIROUKHCUSTOMERSMAIN_SUBTARGETREPORT]]
- [[RPT_NIROUKHLOCATIONTARGET]]
- [[RPT_ZalloumReportTWO]]
- [[Rpt_AnnualTargetAnalysis]]
- [[Rpt_AreaSalesAndSalesmanTarget]]
- [[Rpt_AssistantsSales]]
- [[Rpt_AssistantsSalesDaily]]
- [[Rpt_CompareCustSalesByCategAndTargetRef]]
- [[Rpt_MonthlyCompareSalesTargetWithCustomer]]
- [[Rpt_MonthlyCompareSalesTargetWithSales]]
- [[Rpt_MonthlySalesTargetBySalesman]]
- [[Rpt_NiroukhMonths_Q_Target]]
- [[Rpt_SalesAndCollectionTargetByLocation]]
- [[Rpt_SalesCollcetionsTargets]]
- [[Rpt_SalesPersonTarget]]
- [[Rpt_SalesmanOrdersSummaryByTargetRef]]
- [[Rpt_SalesmanSalesTargetByDay]]
- [[Rpt_SalesmanTargetCommission]]
- [[Rpt_SalespersonTargetComparison]]
- [[Rpt_TargetSpartan]]
- [[Rpt_TowerTargetsBO]]
- [[Rpt_YearlySalesTarget]]
- [[Rpt_YearlySalesTargetBySalesman]]
- [[Rpt_newNiroukh_monthTarget_comm]]

**Writes (1):**
- [[Pro_TargetsReferences]]

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
- [[Olives_BO/Tables/CustomerTypeTargetsDetails]]
