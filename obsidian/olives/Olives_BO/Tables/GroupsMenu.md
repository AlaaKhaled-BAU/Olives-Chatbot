---
type: table
database: Olives_BO
name: GroupsMenu
schema: dbo
tags: [#backoffice, #reference]
foreign_keys:
  - [[Companies]]
  - [[Menu]]
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# GroupsMenu


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores groupsmenu records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO |  | ✓ | [[Companies]] |
| GroupID | bigint | NO |  |  |  |
| MenuID | bigint | NO |  |  |  |
| CanRead | bit | NO |  |  |  |
| CanAdd | bit | NO |  |  |  |
| CanEdit | bit | NO |  |  |  |
| CanDelete | bit | NO |  |  |  |
## Primary Key
(none)
## Foreign Keys
CompanyID -> [[Companies]](ID)
MenuID -> [[Menu]](ID)
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
