---
type: table
database: Olives_BO
name: InvoiceHistoryDF
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
  - [[ECO_Land_SAP_Integ]]
  - [[Falcons_GetItemBalance]]
  - [[Falcons_Integ]]
  - [[GArrow_SAP_Integ]]
  - [[Jazeera_Integ]]
  - [[NPF_IntegrationHisData]]
  - [[NiroukhMonthlyandQuarter]]
  - [[Niroukh_SalesPerTeamQ]]
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
  - [[RamPharm_SAP_Integ]]
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
# InvoiceHistoryDF


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores invoicehistorydf records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| VouYear | smallint | NO | ✓ |  |  |
| VouNo | int | NO | ✓ |  |  |
| VouType | smallint | NO | ✓ |  |  |
| ItemNo | varchar | YES | ✓ |  |  |
| BatchNo | varchar | YES | ✓ |  |  |
| UnitCode | varchar | YES | ✓ |  |  |
| Qty | money | YES |  |  |  |
| Bonus | money | YES |  |  |  |
| SellValue | float | YES |  |  |  |
| DiscPerc | money | YES |  |  |  |
| DiscValue | float | YES |  |  |  |
| TaxPerc | money | YES |  |  |  |
| TaxValue | float | YES |  |  |  |
| ItemDesc | varchar | YES |  |  |  |
| UnitPrice | float | YES |  |  |  |
| VouDiscValue | float | YES |  |  |  |
## Primary Key
CompNo
VouYear
VouNo
VouType
ItemNo
BatchNo
UnitCode
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (48):**
- [[ABS_Integration_Sokhtian]]
- [[Alpha_Integ]]
- [[Alpha_Integ_GoldenArrow]]
- [[Alpha_Integ_HistData]]
- [[Alpha_updateRoute]]
- [[Awael_Integ_HisInvoices]]
- [[BO_Online_RptCustomerSalesTargetDetails]]
- [[Bajali_SAP_Integ]]
- [[ECO_Land_SAP_Integ]]
- [[Falcons_GetItemBalance]]
- [[Falcons_Integ]]
- [[GArrow_SAP_Integ]]
- [[Jazeera_Integ]]
- [[NPF_IntegrationHisData]]
- [[NiroukhMonthlyandQuarter]]
- [[Niroukh_SalesPerTeamQ]]
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
- [[RamPharm_SAP_Integ]]
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

**Writes (7):**
- [[ABS_Integration_Sokhtian]]
- [[Alpha_Integ_HistData]]
- [[Alpha_updateRoute]]
- [[Awael_Integ_HisInvoices]]
- [[Bajali_SAP_Integ]]
- [[GArrow_SAP_Integ]]
- [[SAMA_SAP_Integ]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Orphan lines**: Detail rows without matching header — causes sync failures
- **Posting failure**: IsPosted flag stuck false — check ERP integration log
- **Duplicate vouchers**: Same VouNo generated for different transactions — run dedup check
- **Currency mismatch**: ExRate different from CurrenciesRate table — financial reconciliation off
- **Void inconsistency**: IsVoid flag but original transaction still active — check WF approval

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
