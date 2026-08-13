---
type: table
database: Olives_BO
name: OWGM_Gates
schema: dbo
tags: [#backoffice]
foreign_keys:
referenced_by:
  - [[OWGM_AUTOGATESASSIGMENT]]
  - [[OWGM_AppService]]
  - [[Pro_OWGM_Gates]]
  - [[Pro_OWGM_Transactions]]
support_relevance: high
last_verified: 2026-07-05
---
# OWGM_Gates


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores owgm gates records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| GateID | int | NO | ✓ |  |  |
| GateName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| IsWorking | bit | YES |  |  |  |
## Primary Key
CompanyID
GateID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (4):**
- [[OWGM_AUTOGATESASSIGMENT]]
- [[OWGM_AppService]]
- [[Pro_OWGM_Gates]]
- [[Pro_OWGM_Transactions]]

**Writes (2):**
- [[OWGM_AppService]]
- [[Pro_OWGM_Gates]]

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
