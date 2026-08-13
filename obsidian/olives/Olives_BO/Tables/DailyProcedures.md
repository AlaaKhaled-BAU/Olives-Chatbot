---
type: table
database: Olives_BO
name: DailyProcedures
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[Pro_DailyProcedures]]
  - [[Pro_SalespersonsProcedures]]
support_relevance: high
last_verified: 2026-07-05
---
# DailyProcedures


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores dailyprocedures records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_DailyProcedures]]
- [[Pro_SalespersonsProcedures]]

**Writes (1):**
- [[Pro_DailyProcedures]]

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
