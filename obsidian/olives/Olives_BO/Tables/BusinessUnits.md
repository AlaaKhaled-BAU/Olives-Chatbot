---
type: table
database: Olives_BO
name: BusinessUnits
schema: dbo
tags: [#backoffice, #inventory]
foreign_keys:
  - [[Companies]]
  - [[CompanyBranches]]
referenced_by:
  - [[FixDuplicate_All]]
  - [[OT_ImportSalesIssueItems]]
  - [[OT_ImportSalesOrders]]
  - [[OT_SendCompData]]
  - [[Pro_BusinessUnits]]
  - [[Pro_CustomersFinancialDetails]]
  - [[Pro_ImportRouteInfoFromExcel]]
  - [[Pro_ImportRouteInfoFromExcel2]]
  - [[Pro_SalesPersons]]
  - [[Pro_TransLock]]
  - [[Technical_CreateRouteBasedonID]]
  - [[Technical_CreateRouteBasedonID_ForPageOnly]]
  - [[Technical_CreateRouteBasedonReference1]]
  - [[Technical_CreateRouteBasedonReference1_UpdateOnly]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Company-Setup
  - Salesman-Onboarding
---
# BusinessUnits


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores businessunits records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[CompanyBranches]] |
| ID | int | NO | ✓ |  |  |
| Parent | int | YES |  |  |  |
| Name | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| Level | int | YES |  |  |  |
| CompanyBrancheID | int | YES |  | ✓ | [[CompanyBranches]] |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CompanyBrancheID -> [[CompanyBranches]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (68):**
- [[FixDuplicate_All]]
- [[OT_ImportSalesIssueItems]]
- [[OT_ImportSalesOrders]]
- [[OT_SendCompData]]
- [[Pro_BusinessUnits]]
- [[Pro_CustomersFinancialDetails]]
- [[Pro_ImportRouteInfoFromExcel]]
- [[Pro_ImportRouteInfoFromExcel2]]
- [[Pro_SalesPersons]]
- [[Pro_TransLock]]
- [[Technical_CreateRouteBasedonID]]
- [[Technical_CreateRouteBasedonID_ForPageOnly]]
- [[Technical_CreateRouteBasedonReference1]]
- [[Technical_CreateRouteBasedonReference1_UpdateOnly]]

**Writes (43):**
- [[Pro_BusinessUnits]]
- [[Pro_CustomersFinancialDetails]]

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
