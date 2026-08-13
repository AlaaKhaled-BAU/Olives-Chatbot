---
type: table
database: Olives_BO
name: Vacations
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[Pro_Vacations]]
  - [[Rpt_Vacations]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-07-05
---
# Vacations


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores vacations records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| VacID | bigint | NO | ✓ |  |  |
| SalesPersonID | int | YES |  |  |  |
| VacType | nvarchar | YES |  |  |  |
| FromDate | smalldatetime | YES |  |  |  |
| ToDate | smalldatetime | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| Approved | bit | YES |  |  |  |
## Primary Key
CompanyID
VacID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_Vacations]]
- [[Rpt_Vacations]]

**Writes (3):**
- [[Pro_Vacations]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]

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
