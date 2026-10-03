---
type: table
database: Olives_BO
name: SalesOrderDeliveryHF
schema: dbo
tags: [#backoffice, #order, #sales]
foreign_keys:
referenced_by:
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
- [[OT_SendCustomersInfo]]
- [[Pro_DeliveryCar]]
- [[Pro_DeliveryCarSummaryReport]]
- [[Rpt_OrderLink]]
- [[Rpt_OrdersDeliveryDrivers]]

**Writes (3):**
- [[OT_ImportSalesInvoices]]
- [[Pro_DeliveryCar]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Stage**: delivery-stage copy of orders; SalesOrderHistoryHF is the archived twin — same shape, different retention
- **State enums**: OrderState/Reason codes have Desc mirror columns (OrderStateDesc/ReasonDesc); only value 1 observed locally — read the Desc columns rather than hard-coding ids
## Tenancy

Both tables surface as `t.` views scoped via their `CompNo` column (= `SESSION_CONTEXT(N'CompanyID')`; proven live: company 1 sees 2 of SalesOrderDeliveryDF's SalesOrderDeliveryHF rows). `CompNo` holds the company id.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
