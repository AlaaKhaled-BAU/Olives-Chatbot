---
type: table
database: Olives_BO
name: InvoiceDeliveryHF
schema: dbo
tags: [#backoffice, #billing, #order]
foreign_keys:
referenced_by:
  - [[Alpha_GetItemBalance_Zoumt]]
  - [[Alpha_Integ_SendInvoicesDelivery]]
  - [[Alpha_InvoiceDeliveryHF_BD]]
  - [[ConvertReturnOrderToInvoiceDelivery]]
  - [[Falcons_Integ]]
  - [[OSFA_MobileDeliveryAPI]]
  - [[OT_ImportInvoicesDelivery]]
  - [[OT_SendCustomersInfo]]
  - [[Online_RptInvoiceDeliveryByDriver]]
  - [[Online_RptInvoiceDeliveryCountBySalesman]]
  - [[Pro_AssignOrderDeliveryToCar]]
  - [[Pro_DeliveryCar]]
  - [[Pro_DeliveryCarSummaryReport]]
  - [[Pro_DeliveryDashboard]]
  - [[Pro_DeliveryInvoiceAssigning]]
  - [[Pro_DriverDetailsDashboard]]
  - [[Pro_SelectDeliveryBatchID]]
  - [[Pro_UnCloseOrder]]
  - [[RptOnlineRpt_DeliveryInvoiceStoresQty]]
  - [[Rpt_ConcreteVehicleTransactions]]
  - [[Rpt_DailyConcrete]]
  - [[Rpt_DailyConcreteSalesAndCollection]]
  - [[Rpt_DeliveryAndroidreport]]
  - [[Rpt_DeliveryCarSummaryReport]]
  - [[Rpt_DeliveryDetails]]
  - [[Rpt_DeliveryInvoiceTransaction]]
  - [[Rpt_DriverDeliveryCounts]]
  - [[Rpt_DriverNotDeliveryCounts]]
  - [[Rpt_DriversDeliverySummary]]
  - [[Rpt_InvoicesDelivery]]
  - [[Rpt_MasterOrders]]
  - [[Rpt_RouteSummaryByDelivery]]
  - [[Rpt_RouteSummaryBySalesman_Delivery]]
  - [[Rpt_SalesmanDeliverySummary]]
  - [[SalesmanInfo]]
  - [[Tablet_GetSalesmanDeliveryTrans]]
  - [[X3_Integ_DeliveryInvoice]]
support_relevance: high
last_verified: 2026-07-05
---
# InvoiceDeliveryHF


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores invoicedeliveryhf records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| VouYear | smallint | NO | ✓ |  |  |
| VouNo | int | NO | ✓ |  |  |
| VouType | smallint | NO | ✓ |  |  |
| VouDate | smalldatetime | YES |  |  |  |
| SalesmanNo | smallint | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| Ref1 | varchar | YES |  |  |  |
| Ref2 | varchar | YES |  |  |  |
| Notes | varchar | YES |  |  |  |
| IsDelivered | bit | YES |  |  |  |
| DeliveredDateTime | smalldatetime | YES |  |  |  |
| DeliveredSalesmanNo | int | YES |  |  |  |
| PostedToERP | bit | YES |  |  |  |
| VouDiscPerc | float | YES |  |  |  |
| CustomerDiscPerc | float | YES |  |  |  |
| AssignDateTime | smalldatetime | YES |  |  |  |
| CancelReasonID | int | YES |  |  |  |
| DeliveredStoreNo | nvarchar | YES |  |  |  |
| RouteName | nvarchar | YES |  |  |  |
| NumberOfPackages | int | YES |  |  |  |
| CreditCash | smallint | YES |  |  |  |
| AssistantSalesmanNo | int | YES |  |  |  |
| ShippingDate | smalldatetime | YES |  |  |  |
| DeliveryCarID | int | YES |  |  |  |
| ManifestID | int | YES |  |  |  |
| ERPVouNo | nvarchar | YES |  |  |  |
| ProvaNo | bigint | YES |  |  |  |
| Amount | float | YES |  |  |  |
| PaymentTypeID | int | YES |  |  |  |
| RouteID | int | YES |  |  |  |
| DeliveryBatchID | int | YES |  |  |  |
| RefOrderYear | smallint | YES |  |  |  |
| RefOrderNo | int | YES |  |  |  |
## Primary Key
CompNo
VouYear
VouNo
VouType
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (37):**
- [[Alpha_GetItemBalance_Zoumt]]
- [[Alpha_Integ_SendInvoicesDelivery]]
- [[Alpha_InvoiceDeliveryHF_BD]]
- [[ConvertReturnOrderToInvoiceDelivery]]
- [[Falcons_Integ]]
- [[OSFA_MobileDeliveryAPI]]
- [[OT_ImportInvoicesDelivery]]
- [[OT_SendCustomersInfo]]
- [[Online_RptInvoiceDeliveryByDriver]]
- [[Online_RptInvoiceDeliveryCountBySalesman]]
- [[Pro_AssignOrderDeliveryToCar]]
- [[Pro_DeliveryCar]]
- [[Pro_DeliveryCarSummaryReport]]
- [[Pro_DeliveryDashboard]]
- [[Pro_DeliveryInvoiceAssigning]]
- [[Pro_DriverDetailsDashboard]]
- [[Pro_SelectDeliveryBatchID]]
- [[Pro_UnCloseOrder]]
- [[RptOnlineRpt_DeliveryInvoiceStoresQty]]
- [[Rpt_ConcreteVehicleTransactions]]
- [[Rpt_DailyConcrete]]
- [[Rpt_DailyConcreteSalesAndCollection]]
- [[Rpt_DeliveryAndroidreport]]
- [[Rpt_DeliveryCarSummaryReport]]
- [[Rpt_DeliveryDetails]]
- [[Rpt_DeliveryInvoiceTransaction]]
- [[Rpt_DriverDeliveryCounts]]
- [[Rpt_DriverNotDeliveryCounts]]
- [[Rpt_DriversDeliverySummary]]
- [[Rpt_InvoicesDelivery]]
- [[Rpt_MasterOrders]]
- [[Rpt_RouteSummaryByDelivery]]
- [[Rpt_RouteSummaryBySalesman_Delivery]]
- [[Rpt_SalesmanDeliverySummary]]
- [[SalesmanInfo]]
- [[Tablet_GetSalesmanDeliveryTrans]]
- [[X3_Integ_DeliveryInvoice]]

**Writes (11):**
- [[Alpha_GetItemBalance_Zoumt]]
- [[Alpha_Integ_SendInvoicesDelivery]]
- [[Alpha_InvoiceDeliveryHF_BD]]
- [[ConvertReturnOrderToInvoiceDelivery]]
- [[OSFA_MobileDeliveryAPI]]
- [[OT_ImportInvoicesDelivery]]
- [[Pro_AssignOrderDeliveryToCar]]
- [[Pro_DeliveryCar]]
- [[Pro_DeliveryCarSummaryReport]]
- [[Pro_DeliveryInvoiceAssigning]]
- [[Pro_UnCloseOrder]]

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
