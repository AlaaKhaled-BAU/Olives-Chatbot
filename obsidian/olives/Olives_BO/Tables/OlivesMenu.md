---
type: table
database: Olives_BO
name: OlivesMenu
schema: dbo
tags: [#backoffice]
foreign_keys:
referenced_by:
  - [[Pro_OlivesMenu]]
  - [[Pro_OlivesUserPermissions]]
support_relevance: high
last_verified: 2026-07-05
---
# OlivesMenu


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores olivesmenu records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| ID | int | NO | ✓ |  |  |
| Parent | int | YES |  |  |  |
| ArName | varchar | YES |  |  |  |
| EngName | varchar | YES |  |  |  |
| PageName | varchar | YES |  |  |  |
| PrID | int | YES |  |  |  |
## Primary Key
ID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_OlivesMenu]]
- [[Pro_OlivesUserPermissions]]

**Writes (1):**
- [[Pro_OlivesMenu]]

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
