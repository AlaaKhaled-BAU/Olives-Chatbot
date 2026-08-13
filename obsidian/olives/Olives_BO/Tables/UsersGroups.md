---
type: table
database: Olives_BO
name: UsersGroups
schema: dbo
tags: [#auth, #backoffice, #reference]
foreign_keys:
  - [[Companies]]
referenced_by:
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Users-and-Permissions
---
# UsersGroups


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores usersgroups records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| ID | bigint | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ForeignName | nvarchar | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| IsSuspend | bit | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
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
- [[Olives_BO/Tables/UsersGroupsLink]]
