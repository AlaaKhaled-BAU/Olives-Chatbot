---
type: table
database: Olives_BO
name: SalesOrderDeliveryHF
schema: dbo
tags: [#backoffice, #order, #sales]
foreign_keys:
referenced_by:
  - [[Integ_Normal_DeliveryOrder]]
  - [[OT_ImportSalesInvoices]]
  - [[OT_SendCustomersInfo]]
  - [[Pro_DeliveryCar]]
  - [[Pro_DeliveryCarSummaryReport]]
  - [[Rpt_OrderLink]]
  - [[Rpt_OrdersDeliveryDrivers]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesOrderDeliveryHF


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salesorderdeliveryhf records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| OrderYear | smallint | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| OrderDate | smalldatetime | YES |  |  |  |
| SalesmanNo | smallint | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| OrderState | smallint | YES |  |  |  |
| Reason | smallint | YES |  |  |  |
| OrderStateDesc | varchar | YES |  |  |  |
| ReasonDesc | varchar | YES |  |  |  |
| PO_No | varchar | YES |  |  |  |
| DiscountAmount | float | YES |  |  |  |
| DiscountPercent | float | YES |  |  |  |
| CustomerDiscountPerc | float | YES |  |  |  |
| CustomerDiscountAmount | float | YES |  |  |  |
| OrderDeliveryDate | smalldatetime | YES |  |  |  |
| CarID | int | YES |  |  |  |
| IsDelivered | bit | YES |  |  |  |
| DeliveredDateTime | smalldatetime | YES |  |  |  |
| PostedToERP | bit | YES |  |  |  |
## Primary Key
CompNo
OrderYear
OrderNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (6):**
- [[Integ_Normal_DeliveryOrder]]
- [[OT_SendCustomersInfo]]
- [[Pro_DeliveryCar]]
- [[Pro_DeliveryCarSummaryReport]]
- [[Rpt_OrderLink]]
- [[Rpt_OrdersDeliveryDrivers]]

**Writes (3):**
- [[Integ_Normal_DeliveryOrder]]
- [[OT_ImportSalesInvoices]]
- [[Pro_DeliveryCar]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
