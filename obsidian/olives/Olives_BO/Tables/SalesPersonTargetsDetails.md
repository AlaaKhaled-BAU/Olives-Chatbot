---
type: table
database: Olives_BO
name: SalesPersonTargetsDetails
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
  - [[Companies]]
  - [[SalesPersons]]
  - [[SalesPersonTargets]]
  - [[TargetsReferences]]
referenced_by:
  - [[DA_SalesTarget]]
  - [[Da_SalesperRep]]
  - [[Da_YearlyCompanyTargetAndSales]]
  - [[NiroukhMonthlyandQuarter]]
  - [[NiroukhMonthlyandQuarter_Month]]
  - [[NiroukhTargetPerDay]]
  - [[OT_NiroukhMonthlyandQuarter_Month]]
  - [[Pro_ImportSalesPersonTargets]]
  - [[Pro_SalesPersonTargets]]
  - [[Pro_SalesPersonTargetsDetails]]
  - [[Pro_SalespersonsTargetDashboard]]
  - [[RPT_NEWNIROUKH_MONTHTARGET]]
  - [[Rpt_AnnualTargetAnalysis]]
  - [[Rpt_AreaSalesAndSalesmanTarget]]
  - [[Rpt_MonthlyCompareSalesTargetWithSales]]
  - [[Rpt_MonthlySalesTargetBySalesman]]
  - [[Rpt_NiroukhMonths_Q_Target]]
  - [[Rpt_SalesAndCollectionTargetByLocation]]
  - [[Rpt_SalesAndOrders]]
  - [[Rpt_SalesCollcetionsTargets]]
  - [[Rpt_SalesPersonTarget]]
  - [[Rpt_SalesmanSalesTargetByDay]]
  - [[Rpt_SalesmanTargetCommission]]
  - [[Rpt_SalesmanTargetbyParent]]
  - [[Rpt_TargetSpartan]]
  - [[Rpt_TowerTargets]]
  - [[Rpt_TowerTargetsBO]]
  - [[Rpt_YearlySalesTarget]]
  - [[Rpt_YearlySalesTargetBySalesman]]
  - [[Rpt_newNiroukh_monthTarget_comm]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesPersonTargetsDetails


## Business Purpose
Sales quota and performance target detail table for sales representatives and supervisors. Defines the planned monthly sales targets per representative (`SalesPersonID`), year (`TargetYear`), month (`TargetMonth`), and target reference category (`TargetReferenceID`), measured by target value/amount (`Amount`), physical quantity (`Quantity`), active selling days (`DaysNumber`), and expected commission rates.
- **Quota Tracking**: Used by sales managers and supervisors to monitor target achievement percentages against actual net sales recorded in `TransactionsHeaders` and `TransactionsDetails`.
- **Target Reference**: `TargetReferenceID` links to `TargetsReferences` (e.g. Total Sales target, Focus Category target, New Customers target).

## Chatbot semantics
(Query `t.SalesPersonTargetsDetails` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule |
|----------------------|-----------|---------------|
| أهداف / تارجت المندوب | `Amount`, `Quantity`, `TargetYear`, `TargetMonth` | `SalesPersonID = @SalesmanID AND TargetYear = @Year AND TargetMonth = @Month` |
| تارجت المبيعات الشهري بالدينار / القيمة | `Amount` | القيمة المالية المستهدفة للمبيعات في الشهر |
| تارجت الكميات | `Quantity` | الكمية الإجمالية المستهدفة بالأصناف |
| نسبة العمولة | `Commission` | النسبة المحددة لحساب عمولة المندوب عند تحقيق التارجت |
| اسم المندوب والتارجت | Join `t.SalesPersons` | `td.SalesPersonID = sp.ID` |

**Do not confuse with:**
- `t.TransactionsDetails` (actual realized sales achieved by the salesman).
- `t.CustomerTargetsDetails` (sales target allocated per specific customer).

## Grain & keys
- **Grain**: One row per salesman, year, month, and target reference (`SalesPersonID`, `TargetYear`, `TargetMonth`, `TargetReferenceID`).
- **Composite PK**: `CompanyID`, `SalesPersonID`, `TargetYear`, `TargetMonth`, `TargetReferenceID`.
- **Tenant Key**: `CompanyID`.

## Pipeline
Back Office Sales Ops Management → `Pro_ImportSalesPersonTargets` → `SalesPersonTargetsDetails` → Compared against actual sales in KPI and performance reports (`Rpt_SalespersonTargetComparison`).

## Related
- [[SalesPersons]]
- [[TargetsReferences]]
- [[TransactionsHeaders]]
- [[TransactionsDetails]]

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[TargetsReferences]] |
| SalesPersonID | int | NO | ✓ | ✓ | [[SalesPersonTargets]] |
| TargetYear | smallint | NO | ✓ | ✓ | [[SalesPersonTargets]] |
| TargetMonth | int | NO | ✓ | ✓ | [[SalesPersonTargets]] |
| TargetReferenceID | int | NO | ✓ | ✓ | [[TargetsReferences]] |
| Quantity | float | YES |  |  |  |
| Amount | float | YES |  |  |  |
| DaysNumber | int | YES |  |  |  |
| Commission | float | YES |  |  |  |
| Perc_G1_1 | float | YES |  |  |  |
| Perc_G1_2 | float | YES |  |  |  |
| Perc_G1_3 | float | YES |  |  |  |
| Perc_G1_4 | float | YES |  |  |  |
| Perc_G2_1 | float | YES |  |  |  |
| Perc_G2_2 | float | YES |  |  |  |
| Perc_G2_3 | float | YES |  |  |  |
| Perc_G2_4 | float | YES |  |  |  |
## Primary Key
CompanyID
SalesPersonID
TargetYear
TargetMonth
TargetReferenceID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, SalesPersonID -> [[SalesPersons]](CompanyID, ID)
CompanyID, SalesPersonID, TargetYear, TargetMonth -> [[SalesPersonTargets]](CompanyID, SalesPersonID, TargetYear, TargetMonth)
CompanyID, TargetReferenceID -> [[TargetsReferences]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (33):**
- [[DA_SalesTarget]]
- [[Da_SalesperRep]]
- [[Da_YearlyCompanyTargetAndSales]]
- [[NiroukhMonthlyandQuarter]]
- [[NiroukhMonthlyandQuarter_Month]]
- [[NiroukhTargetPerDay]]
- [[OT_NiroukhMonthlyandQuarter_Month]]
- [[Pro_ImportSalesPersonTargets]]
- [[Pro_SalesPersonTargets]]
- [[Pro_SalesPersonTargetsDetails]]
- [[Pro_SalespersonsTargetDashboard]]
- [[RPT_NEWNIROUKH_MONTHTARGET]]
- [[Rpt_AnnualTargetAnalysis]]
- [[Rpt_AreaSalesAndSalesmanTarget]]
- [[Rpt_MonthlyCompareSalesTargetWithSales]]
- [[Rpt_MonthlySalesTargetBySalesman]]
- [[Rpt_NiroukhMonths_Q_Target]]
- [[Rpt_SalesAndCollectionTargetByLocation]]
- [[Rpt_SalesAndOrders]]
- [[Rpt_SalesCollcetionsTargets]]
- [[Rpt_SalesPersonTarget]]
- [[Rpt_SalesmanSalesTargetByDay]]
- [[Rpt_SalesmanTargetCommission]]
- [[Rpt_SalesmanTargetbyParent]]
- [[Rpt_TargetSpartan]]
- [[Rpt_TowerTargets]]
- [[Rpt_TowerTargetsBO]]
- [[Rpt_YearlySalesTarget]]
- [[Rpt_YearlySalesTargetBySalesman]]
- [[Rpt_newNiroukh_monthTarget_comm]]

**Writes (3):**
- [[Pro_ImportSalesPersonTargets]]
- [[Pro_SalesPersonTargets]]
- [[Pro_SalesPersonTargetsDetails]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
