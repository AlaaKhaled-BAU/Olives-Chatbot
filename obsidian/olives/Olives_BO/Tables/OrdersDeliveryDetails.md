---
type: table
database: Olives_BO
name: OrdersDeliveryDetails
schema: dbo
tags: [#backoffice, #order]
foreign_keys:
  - [[Companies]]
  - [[DeliveryCars]]
  - [[OrdersDetails]]
referenced_by:
  - [[OT_SendCustomersInfo]]
support_relevance: high
last_verified: 2026-07-05
---
# OrdersDeliveryDetails


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores ordersdeliverydetails records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[OrdersDetails]] |
| DeliveryYear | smallint | NO | ✓ |  |  |
| DeliveryNo | int | NO | ✓ |  |  |
| OrderYear | int | NO | ✓ | ✓ | [[OrdersDetails]] |
| OrderNo | int | NO | ✓ | ✓ | [[OrdersDetails]] |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[OrdersDetails]] |
| UnitCode | nvarchar | YES | ✓ | ✓ | [[OrdersDetails]] |
| Qty | float | YES |  |  |  |
| Bonus | float | YES |  |  |  |
| UPrice | float | YES |  |  |  |
| ItemDiscPerc | float | YES |  |  |  |
| TaxPerc | float | YES |  |  |  |
| TaxType | smallint | YES |  |  |  |
| TransferOrderYear | smallint | YES |  |  |  |
| TransferOrderNo | int | YES |  |  |  |
| DeliveryDate | smalldatetime | YES |  |  |  |
| UserID | nvarchar | YES |  |  |  |
| IsDelivered | bit | YES |  |  |  |
| DeliveredDateTime | smalldatetime | YES |  |  |  |
| CarID | int | YES |  | ✓ | [[DeliveryCars]] |
## Primary Key
CompanyID
DeliveryYear
DeliveryNo
OrderYear
OrderNo
ItemCode
UnitCode
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CarID -> [[DeliveryCars]](CompanyID, ID)
CompanyID, OrderYear, OrderNo, ItemCode, UnitCode -> [[OrdersDetails]](CompanyID, OrderYear, OrderNo, ItemCode, UnitID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OT_SendCustomersInfo]]

**Writes (0):**
_None_

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
