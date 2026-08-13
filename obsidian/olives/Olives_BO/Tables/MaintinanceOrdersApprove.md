---
type: table
database: Olives_BO
name: MaintinanceOrdersApprove
schema: dbo
tags: [#integration]
foreign_keys: 0
procedures_reading: 2
support_relevance: medium
last_verified: 2026-08-05
---
# MaintinanceOrdersApprove

## Business Purpose

Back-office table in Olives_BO.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric(30,0) | NO | ✓ |  |  |
| CompanyID | smallint | NO | ✓ |  |  |
| UserID | nvarchar(50) | YES |  |  |  |
| AssignDate | smalldatetime | YES |  |  |  |
| Approve | bit | YES |  |  |  |
| ApproveDate | smalldatetime | YES |  |  |  |
| Note | nvarchar(MAX) | YES |  |  |  |
| IsPosted | bit | YES |  |  |  |
| Lineserial | int | NO | ✓ |  |  |
## Primary Key
AutoID CompanyID Lineserial
## Foreign Keys
(none)
## Impact / Procedures Using This Table

Referenced by 2 procedure(s): 2 writing, 0 reading.
**Writers (2):**
- [[MaintinanceOrders_Insert]]
- [[Pro_MaintinanceOrders]]

## Estimated Size / Volatility
~3 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
