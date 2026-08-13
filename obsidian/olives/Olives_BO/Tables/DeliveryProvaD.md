---
type: table
database: Olives_BO
name: DeliveryProvaD
schema: dbo
tags: [#backoffice, #order]
foreign_keys:
referenced_by:
  - [[Pro_DeliveryAssigning]]
  - [[Rpt_MasterOrders]]
support_relevance: high
last_verified: 2026-07-05
---
# DeliveryProvaD


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores deliveryprovad records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| DeliveryProvaNo | bigint | NO | ✓ |  |  |
| OrderYear | smallint | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| ItemCode | varchar | YES | ✓ |  |  |
| UnitID | varchar | YES | ✓ |  |  |
| LoadedQty | float | YES |  |  |  |
| PickedQty | float | YES |  |  |  |
| TotWeight | float | YES |  |  |  |
## Primary Key
CompanyID
DeliveryProvaNo
OrderYear
OrderNo
ItemCode
UnitID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_DeliveryAssigning]]
- [[Rpt_MasterOrders]]

**Writes (1):**
- [[Pro_DeliveryAssigning]]

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
