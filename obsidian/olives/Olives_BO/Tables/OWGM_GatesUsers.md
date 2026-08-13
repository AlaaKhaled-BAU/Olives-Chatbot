---
type: table
database: Olives_BO
name: OWGM_GatesUsers
schema: dbo
tags: [#auth, #backoffice]
foreign_keys:
referenced_by:
  - [[OWGM_AUTOGATESASSIGMENT]]
  - [[OWGM_AppService]]
  - [[Pro_OWGM_Transactions]]
  - [[Pro_OWGM_UsersGates]]
support_relevance: high
last_verified: 2026-07-05
---
# OWGM_GatesUsers


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores owgm gatesusers records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| GateUserID | int | NO | ✓ |  |  |
| GateUserName | nvarchar | YES |  |  |  |
| GateID | int | NO |  |  |  |
| DevicePassword | varchar | YES |  |  |  |
| MacAddress | nvarchar | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| IsWorking | bit | YES |  |  |  |
| IsBreak | bit | YES |  |  |  |
| AllowPrepare | bit | YES |  |  |  |
| AllowDelivery | bit | YES |  |  |  |
| IsGateAssigment | bit | YES |  |  |  |
## Primary Key
CompanyID
GateUserID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (4):**
- [[OWGM_AUTOGATESASSIGMENT]]
- [[OWGM_AppService]]
- [[Pro_OWGM_Transactions]]
- [[Pro_OWGM_UsersGates]]

**Writes (2):**
- [[OWGM_AppService]]
- [[Pro_OWGM_UsersGates]]

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
