---
type: table
database: Olives_BO
name: ProcedureChangeLog
schema: dbo
tags: [#backoffice, #log]
foreign_keys:
referenced_by:
support_relevance: low
last_verified: 2026-07-05
---
# ProcedureChangeLog


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores procedurechangelog records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| Id | int | YES |  |  |  |
| ObjectName | nvarchar | YES |  |  |  |
| ObjectSchema | nvarchar | YES |  |  |  |
| EventType | nvarchar | YES |  |  |  |
| OldDefinition | nvarchar | YES |  |  |  |
| NewDefinition | nvarchar | YES |  |  |  |
| LoginName | nvarchar | YES |  |  |  |
| HostName | nvarchar | YES |  |  |  |
| IPAddress | nvarchar | YES |  |  |  |
| ChangeTime | datetime | YES |  |  |  |
| ProcDefinition | nvarchar | YES |  |  |  |
## Primary Key
(none)
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Rapid growth**: Table size growing fast — archive old records periodically
- **Orphan log entries**: No corresponding source transaction — investigate data source
- **No cleanup**: No purge job configured — disk space may fill up

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
