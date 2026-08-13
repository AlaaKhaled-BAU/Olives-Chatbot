---
type: table
database: OSFA_DB
name: OT_Surveys_Questions_Options
schema: dbo
tags: [#mobile, #survey]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_Surveys_Questions_Options



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| SalesmanNo | int | NO | ✓ |  |  |
| Survey_ID | int | NO | ✓ |  |  |
| Question_No | int | NO | ✓ |  |  |
| Option_No | int | NO | ✓ |  |  |
| Option_Desc | varchar | YES |  |  |  |
| SortID | int | YES |  |  |  |
## Primary Key
CompNo
SalesmanNo
Survey_ID
Question_No
Option_No
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Sync conflict**: Same record modified on tablet and BO simultaneously — last-write-wins may lose data
- **Orphan tablet records**: Row with no linked BO counterpart — check sync log
- **Duplicate TabletSysID**: Same tablet transaction inserted twice — run dedup check
- **Missing IsPosted flag**: Data not synced to BO — check tablet connectivity

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
- [[OT_Cust_Survey]]
- [[OT_Surveys_Questions]]
- [[OT_Salesman_Survey]]

- [[OT_CustomersItemsAssigment]]
- [[OT_Banks]]
- [[OT_CompanyBranches]]
- [[Glossary]]
