---
type: table
database: Olives_BO
name: TechnicalFinancialInsertTable_Temp
schema: dbo
tags: [#maintenance]
foreign_keys: 0
procedures_reading: 1
support_relevance: low
last_verified: 2026-08-05
---
# TechnicalFinancialInsertTable_Temp

## Business Purpose

Back-office table in Olives_BO.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| Compno | int | YES |  |  |  |
| CustID | bigint | YES |  |  |  |
| Pos | int | YES |  |  |  |
| routeID | nchar(10) | YES |  |  |  |
## Primary Key
(none)
## Foreign Keys
(none)
## Impact / Procedures Using This Table

Referenced by 1 procedure(s): 0 writing, 1 reading.
**Readers (1):**
- [[Technical_InssertintFinancialfromFirstFinancialLink]]

## Estimated Size / Volatility
~0 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
