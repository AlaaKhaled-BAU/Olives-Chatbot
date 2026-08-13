---
type: table
database: OSFA_DB
name: OrdersSMSSebd
schema: dbo
tags: [#integration]
foreign_keys: 0
procedures_reading: 1
support_relevance: low
last_verified: 2026-08-05
---
# OrdersSMSSebd

## Business Purpose

Back-office table in OSFA_DB.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| OrderUKey | nvarchar(100) | NO |  |  |  |
| Name | nvarchar(200) | YES |  |  |  |
| MobileNo | nvarchar(30) | YES |  |  |  |
| Amount | float | YES |  |  |  |
| SendDate | datetime | YES |  |  |  |
## Primary Key
(none)
## Foreign Keys
(none)
## Impact / Procedures Using This Table

Referenced by 1 procedure(s): 1 writing, 0 reading.
**Writers (1):**
- [[Pro_SendOrderSMS]]

## Estimated Size / Volatility
~4 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-OSFA_DB|OSFA_DB MOC]]
