---
type: table
database: Olives_BO
name: InvoiceDeliveryHF
schema: dbo
tags: [#backoffice, #billing, #order]
foreign_keys:
referenced_by:
  - [[ConvertReturnOrderToInvoiceDelivery]]
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
| DeliveredApproved | bit | YES |  |  |  |
## Primary Key
CompNo
VouYear
VouNo
VouType
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (37):**
- [[ConvertReturnOrderToInvoiceDelivery]]
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

**Writes (11):**
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

- **Order back-link**: RefOrderYear/RefOrderNo point at originating SalesOrderDelivery vouchers — join there for order-to-invoice traceability
- **Lifecycle**: IsDelivered + DeliveredDateTime + DeliveredSalesmanNo track van delivery state; ManifestID groups delivery runs
- **Status column**: InvStatus mostly NULL live; PostedToERP marks ERP export
## Tenancy

Both tables surface as `t.` views scoped via their `CompNo` column (= `SESSION_CONTEXT(N'CompanyID')`; proven live: company 1 sees 2 of InvoiceDeliveryDF's InvoiceDeliveryHF rows). `CompNo` holds the company id.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
