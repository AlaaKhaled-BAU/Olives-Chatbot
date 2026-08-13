---
type: table
database: Olives_BO
name: PlanogramMedia
schema: dbo
tags: [#backoffice]
foreign_keys:
referenced_by:
  - [[PlanogramMediabyAssets]]
  - [[Pro_PlanogramMedia]]
  - [[Rpt_PlanogramPhotos]]
support_relevance: high
last_verified: 2026-07-05
---
# PlanogramMedia


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores planogrammedia records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | NO |  |  |  |
| Name | nvarchar | YES |  |  |  |
| FilePath | nvarchar | YES |  |  |  |
| Ref1 | varchar | YES |  |  |  |
| Ref2 | varchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (3):**
- [[PlanogramMediabyAssets]]
- [[Pro_PlanogramMedia]]
- [[Rpt_PlanogramPhotos]]

**Writes (2):**
- [[PlanogramMediabyAssets]]
- [[Pro_PlanogramMedia]]

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
