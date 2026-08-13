---
type: procedure
database: Olives_BO
name: rpt_OlivesApp_Export_ByUser
schema: dbo
tags: [#integration, #reporting]
reads_from:
  - ItemsCategories
writes_to:
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# rpt_OlivesApp_Export_ByUser

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 1 table(s); calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @Username nvarchar(100)
- @CompanyID int
- @FromDate date
- @ToDate date
## Tables Read
- [[ItemsCategories]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- [[rpt_OlivesApp_Export]]
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
