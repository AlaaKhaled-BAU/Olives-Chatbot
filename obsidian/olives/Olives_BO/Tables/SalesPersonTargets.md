---
type: table
database: Olives_BO
name: SalesPersonTargets
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
  - [[Companies]]
  - [[SalesPersons]]
  - [[TargetsTypes]]
referenced_by:
  - [[AppDashBoard]]
  - [[DA_SalesTarget]]
  - [[Da_SalesperRep]]
  - [[Da_YearlyCompanyTargetAndSales]]
  - [[NiroukhMonthlyandQuarter]]
  - [[NiroukhMonthlyandQuarter_Month]]
  - [[NiroukhTargetPerDay]]
  - [[Niroukh_VSQ]]
  - [[OT_NiroukhMonthlyandQuarter_Month]]
  - [[Pro_ImportSalesPersonTargets]]
  - [[Pro_SalesPersonTargets]]
  - [[Pro_SalespersonsTargetDashboard]]
  - [[Rpt_AnnualTargetAnalysis]]
  - [[Rpt_AreaSalesAndSalesmanTarget]]
  - [[Rpt_MonthlyCompareSalesTargetWithSales]]
  - [[Rpt_MonthlyCompareSalesTargetWithSales_Spartan]]
  - [[Rpt_MonthlySalesTargetBySalesman]]
  - [[Rpt_NiroukhMonths_Q_Target]]
  - [[Rpt_PerformanceMetric]]
  - [[Rpt_SalesAndCollectionTargetByLocation]]
  - [[Rpt_SalesAndOrders]]
  - [[Rpt_SalesOrderPerformance]]
  - [[Rpt_SalesPersonTarget]]
  - [[Rpt_SalesmanAnalysisDashBoard]]
  - [[Rpt_SalesmanSalesTargetByDay]]
  - [[Rpt_SalesmanTargetbyParent]]
  - [[Rpt_TargetSpartan]]
  - [[Rpt_YearlySalesTarget]]
  - [[Rpt_YearlySalesTargetBySalesman]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesPersonTargets


## Business Purpose

Sales performance targets and goals for sales measurement.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersons]] |
| SalesPersonID | int | NO | ✓ | ✓ | [[SalesPersons]] |
| TargetYear | smallint | NO | ✓ |  |  |
| TargetMonth | int | NO | ✓ |  |  |
| TargetTypeID | int | YES |  | ✓ | [[TargetsTypes]] |
| Amount | float | YES |  |  |  |
| DaysNumber | int | YES |  |  |  |
| TotalCommissions_1 | float | YES |  |  |  |
| TotalCommissions_2 | float | YES |  |  |  |
| TotalCommissions_3 | float | YES |  |  |  |
| TotalCommissions_4 | float | YES |  |  |  |
| Perc_G1 | float | YES |  |  |  |
| Perc_G2 | float | YES |  |  |  |
| Perc_G3 | float | YES |  |  |  |
| Perc_G4 | float | YES |  |  |  |
| Perc_G3_1234 | float | YES |  |  |  |
| Perc_G4_1234 | float | YES |  |  |  |
## Primary Key
CompanyID
SalesPersonID
TargetYear
TargetMonth
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, SalesPersonID -> [[SalesPersons]](CompanyID, ID)
TargetTypeID -> [[TargetsTypes]](ID)
## Impact / Procedures Using This Table

**Reads (29):**
- [[AppDashBoard]]
- [[DA_SalesTarget]]
- [[Da_SalesperRep]]
- [[Da_YearlyCompanyTargetAndSales]]
- [[NiroukhMonthlyandQuarter]]
- [[NiroukhMonthlyandQuarter_Month]]
- [[NiroukhTargetPerDay]]
- [[Niroukh_VSQ]]
- [[OT_NiroukhMonthlyandQuarter_Month]]
- [[Pro_ImportSalesPersonTargets]]
- [[Pro_SalesPersonTargets]]
- [[Pro_SalespersonsTargetDashboard]]
- [[Rpt_AnnualTargetAnalysis]]
- [[Rpt_AreaSalesAndSalesmanTarget]]
- [[Rpt_MonthlyCompareSalesTargetWithSales]]
- [[Rpt_MonthlyCompareSalesTargetWithSales_Spartan]]
- [[Rpt_MonthlySalesTargetBySalesman]]
- [[Rpt_NiroukhMonths_Q_Target]]
- [[Rpt_PerformanceMetric]]
- [[Rpt_SalesAndCollectionTargetByLocation]]
- [[Rpt_SalesAndOrders]]
- [[Rpt_SalesOrderPerformance]]
- [[Rpt_SalesPersonTarget]]
- [[Rpt_SalesmanAnalysisDashBoard]]
- [[Rpt_SalesmanSalesTargetByDay]]
- [[Rpt_SalesmanTargetbyParent]]
- [[Rpt_TargetSpartan]]
- [[Rpt_YearlySalesTarget]]
- [[Rpt_YearlySalesTargetBySalesman]]

**Writes (2):**
- [[Pro_ImportSalesPersonTargets]]
- [[Pro_SalesPersonTargets]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
