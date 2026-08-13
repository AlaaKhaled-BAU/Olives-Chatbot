---
type: table
database: Olives_BO
name: UserCompanyBranchesLink
schema: dbo
tags: [#auth, #backoffice]
foreign_keys:
  - [[Companies]]
  - [[CompanyBranches]]
  - [[Users]]
referenced_by:
  - [[Pro_CustomersPromotionsGroupsLink]]
  - [[Pro_UserCompanyBranchesLink]]
support_relevance: high
last_verified: 2026-07-05
---
# UserCompanyBranchesLink


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores usercompanybrancheslink records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[CompanyBranches]] |
| UserID | nvarchar | YES | ✓ | ✓ | [[Users]] |
| CompanyBrancheID | int | NO | ✓ | ✓ | [[CompanyBranches]] |
| HavePermission | bit | YES |  |  |  |
## Primary Key
CompanyID
UserID
CompanyBrancheID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CompanyBrancheID -> [[CompanyBranches]](CompanyID, ID)
UserID -> [[Users]](UserID)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_CustomersPromotionsGroupsLink]]
- [[Pro_UserCompanyBranchesLink]]

**Writes (1):**
- [[Pro_UserCompanyBranchesLink]]

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
