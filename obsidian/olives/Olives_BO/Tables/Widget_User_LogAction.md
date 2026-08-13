---
type: table
database: Olives_BO
name: Widget_User_LogAction
schema: dbo
tags: [#backoffice]
foreign_keys: 1
procedures_reading: 0
support_relevance: low
last_verified: 2026-08-05
---
# Widget_User_LogAction

## Business Purpose

Back-office table in Olives_BO.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | int | NO | ✓ | ✓ | [[Widget_User_LogAction]] |
| ActionDate | datetime | YES |  |  |  |
| UserID | nvarchar(50) | YES |  |  |  |
| FunctionID | int | YES |  |  |  |
| CalledProcedure | nvarchar(MAX) | YES |  |  |  |
## Primary Key
CompNo
## Foreign Keys
- Widget_User_LogAction.CompNo → [[Widget_User_LogAction]].CompNo
**Referenced by (incoming FKs):**
- [[Widget_User_LogAction]].CompNo → Widget_User_LogAction.CompNo
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
