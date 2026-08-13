---
type: table
database: Olives_BO
name: Menu
schema: dbo
tags: [#backoffice]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# Menu


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores menu records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| ID | bigint | NO |  |  |  |
| Desc1 | nvarchar | YES |  |  |  |
| Desc2 | nvarchar | YES |  |  |  |
| PageUrl | nvarchar | YES |  |  |  |
| Width | float | YES |  |  |  |
| Height | float | YES |  |  |  |
| ShowActions | bit | YES |  |  |  |
| ParentID | bigint | YES |  |  |  |
| MenuIcon | nvarchar | YES |  |  |  |
| IsActive | bit | YES |  |  |  |
| SearchBehavior | nvarchar | YES |  |  |  |
| SortNo | bigint | YES |  |  |  |
## Primary Key
(none)
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

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
- [[Olives_BO/Tables/GroupsMenu]]
