---
type: table
database: Olives_BO
name: Excel2
schema: dbo
tags: [#backoffice]
foreign_keys:
referenced_by:
  - [[Technical_CreateRouteBasedonID]]
  - [[Technical_CreateRouteBasedonReference1]]
support_relevance: high
last_verified: 2026-07-05
---
# Excel2


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores excel2 records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| ID | int | YES |  |  |  |
| CustID1 | nvarchar | YES |  |  |  |
| Salesman | nvarchar | YES |  |  |  |
| Day | nvarchar | YES |  |  |  |
| Week | nvarchar | YES |  |  |  |
| Routename | nvarchar | YES |  |  |  |
## Primary Key
(none)
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Technical_CreateRouteBasedonID]]
- [[Technical_CreateRouteBasedonReference1]]

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
