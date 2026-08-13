---
type: table
database: Olives_BO
name: Contracts
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[Companies]]
  - [[Customers]]
referenced_by:
  - [[Pro_Contracts]]
  - [[Pro_SalesPersonContractsAssignment]]
support_relevance: high
last_verified: 2026-07-05
---
# Contracts


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores contracts records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Customers]] |
| ContractID | nvarchar | YES | ✓ |  |  |
| ContractName | nvarchar | YES |  |  |  |
| StartDate | smalldatetime | YES |  |  |  |
| EndDate | smalldatetime | YES |  |  |  |
| CustomerID | bigint | YES |  | ✓ | [[Customers]] |
| IsSuspended | bit | YES |  |  |  |
## Primary Key
CompanyID
ContractID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_Contracts]]
- [[Pro_SalesPersonContractsAssignment]]

**Writes (1):**
- [[Pro_Contracts]]

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
- See also (OSFA counterpart): [[OSFA_DB/Tables/OT_Contracts]]
