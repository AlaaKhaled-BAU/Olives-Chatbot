---
type: table
database: Olives_BO
name: SalesOrderDeliveryDF
schema: dbo
tags: [#backoffice, #order, #sales]
foreign_keys:
referenced_by:
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
| ItemNo | varchar | NO | ✓ |  |  |
| UnitCode | varchar | NO | ✓ |  |  |
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
- [[Pro_DeliveryCarSummaryReport]]

**Writes (1):**

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Fill rate**: OrderedQty vs DeliveredQty vs OutstandingQty per line; QtyOH = quantity on hand at order time
## Tenancy

Chatbot queries `t.SalesOrderDeliveryDF` only — auto-scoped by `SESSION_CONTEXT(N'CompanyID')`. Raw dbo access is blocked for `chatbot_ro`.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
