---
type: table
database: Olives_BO
name: BanksAccounts
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[Banks]]
  - [[Companies]]
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# BanksAccounts


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores banksaccounts records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| BankID | int | NO | ✓ | ✓ | [[Banks]] |
| ID | int | NO | ✓ |  |  |
| AccountNumber | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
BankID
ID
## Foreign Keys
CompanyID, BankID -> [[Banks]](CompanyID, ID)
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (1):**

**Writes (1):**

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
