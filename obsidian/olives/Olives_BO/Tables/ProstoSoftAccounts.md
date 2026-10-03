---
type: table
database: Olives_BO
name: ProstoSoftAccounts
schema: dbo
tags: [#backoffice]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# ProstoSoftAccounts


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores prostosoftaccounts records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| S_M | bigint | YES |  |  |  |
| S_M_M | bigint | YES |  |  |  |
| S_D | bigint | YES |  |  |  |
| S_D_M | bigint | YES |  |  |  |
| S_T | bigint | YES |  |  |  |
| S_V | bigint | YES |  |  |  |
## Primary Key
CompanyID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**

**Writes (0):**
_None_

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
