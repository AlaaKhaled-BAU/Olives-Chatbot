---
type: table
database: Olives_BO
name: SalesOrderDeliveryDF
schema: dbo
tags: [#backoffice, #order, #sales]
foreign_keys:
referenced_by:
  - [[Integ_Normal_DeliveryOrder]]
  - [[Pro_DeliveryCarSummaryReport]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesOrderDeliveryDF


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salesorderdeliverydf records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| OrderYear | smallint | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| ItemNo | varchar | YES | ✓ |  |  |
| UnitCode | varchar | YES | ✓ |  |  |
| OrderdQty | money | YES |  |  |  |
| Bonus | money | YES |  |  |  |
| DeliveredQty | money | YES |  |  |  |
| OutstandingQty | money | YES |  |  |  |
| SellValue | float | YES |  |  |  |
| DiscPerc | money | YES |  |  |  |
| DiscValue | float | YES |  |  |  |
| TaxPerc | money | YES |  |  |  |
| TaxValue | float | YES |  |  |  |
| QtyOH | money | YES |  |  |  |
| ItemDesc | varchar | YES |  |  |  |
| InvQty | money | YES |  |  |  |
| VoucherDiscount | float | YES |  |  |  |
| TaxType | smallint | YES |  |  |  |
| UPrice | float | YES |  |  |  |
| Manual_Bonus | float | YES |  |  |  |
| TotWieght | float | YES |  |  |  |
| PickedQty | float | YES |  |  |  |
## Primary Key
CompNo
OrderYear
OrderNo
ItemNo
UnitCode
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Integ_Normal_DeliveryOrder]]
- [[Pro_DeliveryCarSummaryReport]]

**Writes (1):**
- [[Integ_Normal_DeliveryOrder]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
