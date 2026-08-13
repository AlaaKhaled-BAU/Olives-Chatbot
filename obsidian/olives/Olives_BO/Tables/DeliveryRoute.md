---
type: table
database: Olives_BO
name: DeliveryRoute
schema: dbo
tags: [#backoffice, #gps, #order, #sales]
foreign_keys:
referenced_by:
  - [[Falcons_Integ]]
  - [[OT_SendCustomersInfo]]
  - [[Rpt_RouteSummaryByDelivery]]
support_relevance: high
last_verified: 2026-07-05
---
# DeliveryRoute


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores deliveryroute records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| SalesmanNo | int | NO | ✓ |  |  |
| CustomerID | bigint | NO | ✓ |  |  |
| RouteDate | smalldatetime | NO | ✓ |  |  |
## Primary Key
CompNo
SalesmanNo
CustomerID
RouteDate
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (3):**
- [[Falcons_Integ]]
- [[OT_SendCustomersInfo]]
- [[Rpt_RouteSummaryByDelivery]]

**Writes (1):**
- [[OT_SendCustomersInfo]]

## Estimated Size / Volatility
Typical business table
## Common Issues
> [!warning] AUTO-GENERATED — verify before trusting

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
