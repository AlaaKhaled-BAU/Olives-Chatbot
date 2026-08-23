---
type: table
database: Olives_BO
name: InvoiceHistoryHF
schema: dbo
tags: [#backoffice, #billing, #log]
foreign_keys:
referenced_by:
  - [[ABS_Integration_Sokhtian]]
  - [[Alpha_Integ]]
  - [[Alpha_Integ_GoldenArrow]]
  - [[Alpha_Integ_HistData]]
  - [[Alpha_updateRoute]]
  - [[Awael_Integ_HisInvoices]]
  - [[BO_Online_RptCustomerSalesTargetDetails]]
  - [[Bajali_SAP_Integ]]
  - [[Falcons_Integ]]
  - [[GArrow_SAP_Integ]]
  - [[Jazeera_Integ]]
  - [[NPF_IntegrationHisData]]
  - [[NiroukhMonthlyandQuarter]]
  - [[Niroukh_SalesPerTeamQ]]
  - [[OT_SendCompData]]
  - [[OT_SendSalesmanData]]
  - [[Pro_ReturnOrdersHeaders]]
  - [[RPT_CUSTOMERSMAIN_SUBTARGETREPORT_COLLECTIONS]]
  - [[RPT_CUSTOMERSMAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
  - [[RPT_LOCATIONSMAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
  - [[RPT_LOCATIONS_CUSTOMERTYPE_MAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
  - [[RPT_NEWNIROUKH_MONTHTARGET]]
  - [[RPT_NIROUKHCUSTOMERCLASSTARGET]]
  - [[RPT_NIROUKHCUSTOMERSMAIN_SUBTARGETREPORT]]
  - [[RPT_NIROUKHLOCATIONTARGET]]
  - [[Rpt_CompareCustSalesByCategAndTargetRef]]
  - [[Rpt_CustomerMonthlySalesByArea]]
  - [[Rpt_CustomerSalesByItems]]
  - [[Rpt_MonthlyCompareSalesTargetWithSales]]
  - [[Rpt_MonthlyCompareSalesTargetWithSales_Spartan]]
  - [[Rpt_NiroukhMonths_Q_Target]]
  - [[Rpt_Niroukh_LocationTarget]]
  - [[Rpt_Niroukh_SalesPerTeamQ]]
  - [[Rpt_SalesmanSalesByItems]]
  - [[Rpt_SalesmanSalesTotal]]
  - [[Rpt_SalesmanSalesTotal_BO]]
  - [[Rpt_SalesmanSoldAndNoSoldCustomers]]
  - [[Rpt_SalesmanSoldAndNoSoldCustomers_BO]]
  - [[Rpt_TargetSpartan]]
  - [[Rpt_TowerTargets]]
  - [[Rpt_newNiroukh_monthTarget_comm]]
  - [[SAMA_SAP_Integ]]
  - [[SalesmanInfo]]
  - [[Tablet_GetInvoiceHistoryFromERP]]
  - [[Tablet_GetPendingOrdersTotals]]
  - [[X3_Integ_HistData]]
support_relevance: high
last_verified: 2026-07-05
---
# InvoiceHistoryHF


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores invoicehistoryhf records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| VouYear | smallint | NO | ✓ |  |  |
| VouNo | int | NO | ✓ |  |  |
| VouType | smallint | NO | ✓ |  |  |
| VouDate | smalldatetime | YES |  |  |  |
| StoreNo | int | YES |  |  |  |
| SalesmanNo | smallint | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| InvStatus | varchar | YES |  |  |  |
| Ref1 | varchar | YES |  |  |  |
| Ref2 | varchar | YES |  |  |  |
| Notes | varchar | YES |  |  |  |
| VouDiscPerc | float | YES |  |  |  |
| CustomerDiscPerc | float | YES |  |  |  |
| ERPVouNo | nvarchar | YES |  |  |  |
| PaymentDiscPerc | float | YES |  |  |  |
| PaymentDiscAmt | float | YES |  |  |  |
## Primary Key
CompNo
VouYear
VouNo
VouType
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (45):**
- [[ABS_Integration_Sokhtian]]
- [[Alpha_Integ]]
- [[Alpha_Integ_GoldenArrow]]
- [[Alpha_Integ_HistData]]
- [[Alpha_updateRoute]]
- [[Awael_Integ_HisInvoices]]
- [[BO_Online_RptCustomerSalesTargetDetails]]
- [[Bajali_SAP_Integ]]
- [[Falcons_Integ]]
- [[GArrow_SAP_Integ]]
- [[Jazeera_Integ]]
- [[NPF_IntegrationHisData]]
- [[NiroukhMonthlyandQuarter]]
- [[Niroukh_SalesPerTeamQ]]
- [[OT_SendCompData]]
- [[OT_SendSalesmanData]]
- [[Pro_ReturnOrdersHeaders]]
- [[RPT_CUSTOMERSMAIN_SUBTARGETREPORT_COLLECTIONS]]
- [[RPT_CUSTOMERSMAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
- [[RPT_LOCATIONSMAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
- [[RPT_LOCATIONS_CUSTOMERTYPE_MAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
- [[RPT_NEWNIROUKH_MONTHTARGET]]
- [[RPT_NIROUKHCUSTOMERCLASSTARGET]]
- [[RPT_NIROUKHCUSTOMERSMAIN_SUBTARGETREPORT]]
- [[RPT_NIROUKHLOCATIONTARGET]]
- [[Rpt_CompareCustSalesByCategAndTargetRef]]
- [[Rpt_CustomerMonthlySalesByArea]]
- [[Rpt_CustomerSalesByItems]]
- [[Rpt_MonthlyCompareSalesTargetWithSales]]
- [[Rpt_MonthlyCompareSalesTargetWithSales_Spartan]]
- [[Rpt_NiroukhMonths_Q_Target]]
- [[Rpt_Niroukh_LocationTarget]]
- [[Rpt_Niroukh_SalesPerTeamQ]]
- [[Rpt_SalesmanSalesByItems]]
- [[Rpt_SalesmanSalesTotal]]
- [[Rpt_SalesmanSalesTotal_BO]]
- [[Rpt_SalesmanSoldAndNoSoldCustomers]]
- [[Rpt_SalesmanSoldAndNoSoldCustomers_BO]]
- [[Rpt_TargetSpartan]]
- [[Rpt_TowerTargets]]
- [[Rpt_newNiroukh_monthTarget_comm]]
- [[SalesmanInfo]]
- [[Tablet_GetInvoiceHistoryFromERP]]
- [[Tablet_GetPendingOrdersTotals]]
- [[X3_Integ_HistData]]

**Writes (6):**
- [[Alpha_Integ_HistData]]
- [[Alpha_updateRoute]]
- [[Awael_Integ_HisInvoices]]
- [[Bajali_SAP_Integ]]
- [[GArrow_SAP_Integ]]
- [[SAMA_SAP_Integ]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Status column**: InvStatus is NULL on essentially all live rows — do not filter on it
- **Doc types**: VouType values observed live: 9 (dominant), 1 — meaning is app-side; never assume 1=invoice
- **Naming**: key is CompNo+VouYear+VouNo+VouType; carrier cols are CustomerNo/SalesmanNo (no underscores)
## Tenancy

Both tables surface as `t.` views scoped via their `CompNo` column (= `SESSION_CONTEXT(N'CompanyID')`; proven live: company 1 sees 2 of InvoiceHistoryDF's InvoiceHistoryHF rows). `CompNo` holds the company id.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
