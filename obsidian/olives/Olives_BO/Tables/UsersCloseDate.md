---
type: table
database: Olives_BO
name: UsersCloseDate
schema: dbo
tags: [#auth, #backoffice]
foreign_keys:
  - [[Companies]]
  - [[Users]]
referenced_by:
  - [[Pro_Users]]
  - [[Pro_UsersCloseDate]]
support_relevance: high
last_verified: 2026-07-05
---
# UsersCloseDate


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores usersclosedate records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| UserID | nvarchar | YES | ✓ | ✓ | [[Users]] |
| TrasnDateClose | smalldatetime | YES |  |  |  |
## Primary Key
CompanyID
UserID
## Foreign Keys
CompanyID -> [[Companies]](ID)
UserID -> [[Users]](UserID)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_Users]]
- [[Pro_UsersCloseDate]]

**Writes (1):**
- [[Pro_UsersCloseDate]]

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
