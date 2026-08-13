---
type: table
database: Olives_BO
name: SalesAcheivmentGrades
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[Pro_SalesAcheivmentGrades]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesAcheivmentGrades


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salesacheivmentgrades records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| MinValue | float | YES |  |  |  |
| MaxValue | float | YES |  |  |  |
| Factor | float | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_SalesAcheivmentGrades]]

**Writes (1):**
- [[Pro_SalesAcheivmentGrades]]

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
