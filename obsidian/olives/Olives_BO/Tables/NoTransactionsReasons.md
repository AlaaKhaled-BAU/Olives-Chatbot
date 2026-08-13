---
type: table
database: Olives_BO
name: NoTransactionsReasons
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[ABS_Integ_SendPayment_Jebrene]]
  - [[ABS_Integ_SendPayment_Sokhtian]]
  - [[ECO_Land_SAP_Integ]]
  - [[Galaxy_Integ_SendSalesInvoices]]
  - [[Online_RptInvoiceDeliveryByDriver]]
  - [[Pro_ApproveImagesApp]]
  - [[Pro_DeliveryCar]]
  - [[Pro_DriverDetailsDashboard]]
  - [[Pro_MapTransactionLog]]
  - [[Pro_NoTransactionsReasons]]
  - [[Pro_SalesmanDetailsDashboard]]
  - [[Pro_UnCloseOrder]]
  - [[Rpt_DeliveryInvoiceTransaction]]
  - [[Rpt_DriverNotDeliveryCounts]]
  - [[Rpt_DriversDeliverySummary]]
  - [[Rpt_NoSalesReasons]]
  - [[Rpt_RouteSummaryByDelivery]]
  - [[Rpt_RouteSummaryBySalesman]]
  - [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
  - [[Rpt_RouteSummaryBySalesman_Delivery]]
  - [[Rpt_RouteSummaryBySalesman_Merchandisers]]
  - [[Rpt_RouteSummaryBySalesman_Spartan]]
  - [[Rpt_RouteSummaryBySalesman_Sukhtian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
  - [[Rpt_SalesmanTimeSpentPerCustomer]]
  - [[Rpt_SalesmanTimeSpentPerCustomer2]]
  - [[Rpt_SalesmanTimeSpentPerCustomer3]]
  - [[Rpt_SalesmanTimeSpentPerCustomer4]]
  - [[Rpt_SalesmanTimeSpentPerCustomer6_QimaH]]
  - [[Rpt_TimeManagement]]
  - [[Spartan_SAP_Integ_draft]]
support_relevance: high
last_verified: 2026-07-05
---
# NoTransactionsReasons


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores notransactionsreasons records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| ID | int | NO | ✓ |  |  |
| ReasonType | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| IsNeedNote | bit | YES |  |  |  |
## Primary Key
CompanyID
ID
ReasonType
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (31):**
- [[ABS_Integ_SendPayment_Jebrene]]
- [[ABS_Integ_SendPayment_Sokhtian]]
- [[Galaxy_Integ_SendSalesInvoices]]
- [[Online_RptInvoiceDeliveryByDriver]]
- [[Pro_ApproveImagesApp]]
- [[Pro_DeliveryCar]]
- [[Pro_DriverDetailsDashboard]]
- [[Pro_MapTransactionLog]]
- [[Pro_NoTransactionsReasons]]
- [[Pro_SalesmanDetailsDashboard]]
- [[Pro_UnCloseOrder]]
- [[Rpt_DeliveryInvoiceTransaction]]
- [[Rpt_DriverNotDeliveryCounts]]
- [[Rpt_DriversDeliverySummary]]
- [[Rpt_NoSalesReasons]]
- [[Rpt_RouteSummaryByDelivery]]
- [[Rpt_RouteSummaryBySalesman]]
- [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
- [[Rpt_RouteSummaryBySalesman_Delivery]]
- [[Rpt_RouteSummaryBySalesman_Merchandisers]]
- [[Rpt_RouteSummaryBySalesman_Spartan]]
- [[Rpt_RouteSummaryBySalesman_Sukhtian]]
- [[Rpt_RouteSummaryBySalesman_Suktian]]
- [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
- [[Rpt_SalesmanTimeSpentPerCustomer]]
- [[Rpt_SalesmanTimeSpentPerCustomer2]]
- [[Rpt_SalesmanTimeSpentPerCustomer3]]
- [[Rpt_SalesmanTimeSpentPerCustomer4]]
- [[Rpt_SalesmanTimeSpentPerCustomer6_QimaH]]
- [[Rpt_TimeManagement]]
- [[Spartan_SAP_Integ_draft]]

**Writes (2):**
- [[ECO_Land_SAP_Integ]]
- [[Pro_NoTransactionsReasons]]

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
