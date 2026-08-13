---
type: table
database: Olives_BO
name: Excel
schema: dbo
tags: [#backoffice]
foreign_keys:
referenced_by:
  - [[Fill_In_Missing_PositionRoute]]
  - [[Pro_ImportRouteInfoFromExcel]]
  - [[Technical_CreateRouteBasedonID]]
  - [[Technical_CreateRouteBasedonID_ForPageOnly]]
  - [[Technical_CreateRouteBasedonReference1]]
  - [[Technical_CreateRouteBasedonReference1_UpdateOnly]]
  - [[Technical_UpdateTempCFD_temp_forRouteCreation]]
support_relevance: high
last_verified: 2026-07-05
---
# Excel


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores excel records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| ID | int | YES |  |  |  |
| CustID1 | nvarchar | YES |  |  |  |
| Salesman | nvarchar | YES |  |  |  |
| Day | nvarchar | YES |  |  |  |
| Week | nvarchar | YES |  |  |  |
## Primary Key
(none)
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (7):**
- [[Fill_In_Missing_PositionRoute]]
- [[Pro_ImportRouteInfoFromExcel]]
- [[Technical_CreateRouteBasedonID]]
- [[Technical_CreateRouteBasedonID_ForPageOnly]]
- [[Technical_CreateRouteBasedonReference1]]
- [[Technical_CreateRouteBasedonReference1_UpdateOnly]]
- [[Technical_UpdateTempCFD_temp_forRouteCreation]]

**Writes (1):**
- [[Pro_ImportRouteInfoFromExcel]]

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
