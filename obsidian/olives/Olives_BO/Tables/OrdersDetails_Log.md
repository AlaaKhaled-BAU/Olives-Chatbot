---
type: table
database: Olives_BO
name: OrdersDetails_Log
schema: dbo
tags: [#backoffice]
foreign_keys: 0
procedures_reading: 4
support_relevance: medium
last_verified: 2026-08-05
---
# OrdersDetails_Log

## Business Purpose

Back-office table in Olives_BO.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| OrderYear | smallint | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| ItemCode | nvarchar(100) | NO | ✓ |  |  |
| UnitID | nvarchar(50) | NO | ✓ |  |  |
| UserId | nvarchar(100) | NO | ✓ |  |  |
| Quantity | float | YES |  |  |  |
## Primary Key
CompanyID OrderYear OrderNo ItemCode UnitID UserId
## Foreign Keys
(none)
## Impact / Procedures Using This Table

Referenced by 4 procedure(s): 4 writing, 0 reading.
**Writers (4):**
- [[PRO_PostProductionLoadingOrderApproval]]
- [[PRO_PreProductionLoadingOrderApproval]]
- [[Pro_ItemsOrderList]]
- [[Pro_TransfersOrdersDetails]]

## Estimated Size / Volatility
~13 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
