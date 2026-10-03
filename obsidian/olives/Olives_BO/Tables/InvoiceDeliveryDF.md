---
type: table
database: Olives_BO
name: InvoiceDeliveryDF
schema: dbo
tags: [#backoffice, #billing, #order]
foreign_keys:
referenced_by:
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
| ItemNo | varchar | NO | ✓ |  |  |
| BatchNo | varchar | NO | ✓ |  |  |
| UnitCode | varchar | NO | ✓ |  |  |
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

**Writes (4):**
- [[ConvertReturnOrderToInvoiceDelivery]]
- [[OSFA_MobileDeliveryAPI]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **TotWeight**: carries line weight for load planning; units come from item master config
## Tenancy

Both tables surface as `t.` views scoped via their `CompNo` column (= `SESSION_CONTEXT(N'CompanyID')`; proven live: company 1 sees 2 of InvoiceDeliveryHF's InvoiceDeliveryDF rows). `CompNo` holds the company id.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
