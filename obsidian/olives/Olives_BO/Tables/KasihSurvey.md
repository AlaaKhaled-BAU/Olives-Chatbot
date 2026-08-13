---
type: table
database: Olives_BO
name: KasihSurvey
schema: dbo
tags: [#backoffice, #survey]
foreign_keys:
referenced_by:
  - [[KasihSurvey_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# KasihSurvey


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores kasihsurvey records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CustomerName | nvarchar | YES |  |  |  |
| CustomerImage | image | YES |  |  |  |
| CustomerImage1 | image | YES |  |  |  |
| CustomerImage2 | image | YES |  |  |  |
| CustomerImage3 | image | YES |  |  |  |
| CustomerImage4 | image | YES |  |  |  |
| ShelfImageBefore | image | YES |  |  |  |
| ShelfImageBefore1 | image | YES |  |  |  |
| ShelfImageBefore2 | image | YES |  |  |  |
| ShelfImageBefore3 | image | YES |  |  |  |
| ShelfImageBefore4 | image | YES |  |  |  |
| ShelfImageAfter | image | YES |  |  |  |
| ShelfImageAfter1 | image | YES |  |  |  |
| ShelfImageAfter2 | image | YES |  |  |  |
| ShelfImageAfter3 | image | YES |  |  |  |
| ShelfImageAfter4 | image | YES |  |  |  |
| ExistingPlace | nvarchar | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| ItemAvailability | nvarchar | YES |  |  |  |
| ItemMovement | nvarchar | YES |  |  |  |
| NeedOrder | nvarchar | YES |  |  |  |
| ItemShownByTransmed | nvarchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[KasihSurvey_Insert]]

**Writes (1):**
- [[KasihSurvey_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Incomplete surveys**: Questions not answered — survey results incomplete
- **Orphan answers**: Answer records without matching survey header — data integrity issue
- **Wrong survey assigned**: Customer received wrong survey version — reporting mismatch

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
