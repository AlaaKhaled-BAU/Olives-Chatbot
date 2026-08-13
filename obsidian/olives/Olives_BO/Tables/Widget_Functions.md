---
type: table
database: Olives_BO
name: Widget_Functions
schema: dbo
tags: [#backoffice]
foreign_keys: 0
procedures_reading: 0
support_relevance: low
last_verified: 2026-08-05
---
# Widget_Functions

## Business Purpose

Back-office table in Olives_BO.
No procedures or foreign keys reference it in the dependency graph — likely a temp/utility table.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | int | NO | ✓ |  |  |
| CompanyName | nvarchar(300) | YES |  |  |  |
| FunctionID | int | YES |  |  |  |
| FunctionName | nvarchar(MAX) | YES |  |  |  |
| CalledProcedureName | nvarchar(MAX) | YES |  |  |  |
## Primary Key
CompNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

Referenced by 0 procedure(s): 0 writing, 0 reading.
_No procedures reference this table in the dependency graph._

## Estimated Size / Volatility
~0 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
