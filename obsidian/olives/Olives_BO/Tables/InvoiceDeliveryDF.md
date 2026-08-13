---
type: table
database: Olives_BO
name: InvoiceDeliveryDF
schema: dbo
tags: [#backoffice, #billing, #order]
foreign_keys:
referenced_by:
  - [[Alpha_GetItemBalance_Zoumt]]
  - [[Alpha_InvoiceDeliveryHF_BD]]
  - [[ConvertReturnOrderToInvoiceDelivery]]
  - [[OSFA_MobileDeliveryAPI]]
  - [[Online_RptInvoiceDeliveryByDriver]]
  - [[Online_RptInvoiceDeliveryCountBySalesman]]
  - [[Pro_DeliveryCar]]
  - [[Pro_DeliveryCarSummaryReport]]
  - [[Pro_DeliveryDashboard]]
  - [[Pro_DeliveryInvoiceAssigning]]
  - [[Pro_DriverDetailsDashboard]]
  - [[Pro_UnCloseOrder]]
  - [[RptOnlineRpt_DeliveryInvoiceStoresQty]]
  - [[Rpt_ConcreteVehicleTransactions]]
  - [[Rpt_DailyConcrete]]
  - [[Rpt_DailyConcreteSalesAndCollection]]
  - [[Rpt_DeliveryAndroidreport]]
  - [[Rpt_DeliveryCarSummaryReport]]
  - [[Rpt_DeliveryInvoiceTransaction]]
  - [[Rpt_DriverDeliveryCounts]]
  - [[Rpt_DriverNotDeliveryCounts]]
  - [[Rpt_DriversDeliverySummary]]
  - [[Rpt_InvoicesDelivery]]
  - [[Rpt_MasterOrders]]
  - [[Rpt_SalesmanDeliverySummary]]
  - [[SalesmanInfo]]
  - [[Spartan_SAP_Integ]]
  - [[Tablet_GetSalesmanDeliveryTrans]]
  - [[X3_Integ_DeliveryInvoice]]
support_relevance: high
last_verified: 2026-07-05
---
# InvoiceDeliveryDF


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores invoicedeliverydf records.

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
| TotWeight | float | YES |  |  |  |
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

**Reads (28):**
- [[Alpha_GetItemBalance_Zoumt]]
- [[Alpha_InvoiceDeliveryHF_BD]]
- [[OSFA_MobileDeliveryAPI]]
- [[Online_RptInvoiceDeliveryByDriver]]
- [[Online_RptInvoiceDeliveryCountBySalesman]]
- [[Pro_DeliveryCar]]
- [[Pro_DeliveryCarSummaryReport]]
- [[Pro_DeliveryDashboard]]
- [[Pro_DeliveryInvoiceAssigning]]
- [[Pro_DriverDetailsDashboard]]
- [[Pro_UnCloseOrder]]
- [[RptOnlineRpt_DeliveryInvoiceStoresQty]]
- [[Rpt_ConcreteVehicleTransactions]]
- [[Rpt_DailyConcrete]]
- [[Rpt_DailyConcreteSalesAndCollection]]
- [[Rpt_DeliveryAndroidreport]]
- [[Rpt_DeliveryCarSummaryReport]]
- [[Rpt_DeliveryInvoiceTransaction]]
- [[Rpt_DriverDeliveryCounts]]
- [[Rpt_DriverNotDeliveryCounts]]
- [[Rpt_DriversDeliverySummary]]
- [[Rpt_InvoicesDelivery]]
- [[Rpt_MasterOrders]]
- [[Rpt_SalesmanDeliverySummary]]
- [[SalesmanInfo]]
- [[Spartan_SAP_Integ]]
- [[Tablet_GetSalesmanDeliveryTrans]]
- [[X3_Integ_DeliveryInvoice]]

**Writes (4):**
- [[Alpha_GetItemBalance_Zoumt]]
- [[Alpha_InvoiceDeliveryHF_BD]]
- [[ConvertReturnOrderToInvoiceDelivery]]
- [[OSFA_MobileDeliveryAPI]]

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
