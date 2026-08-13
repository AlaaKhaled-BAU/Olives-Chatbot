---
type: procedure
database: Olives_BO
name: Pro_ImportExcelDataRoutes_59
schema: dbo
tags: [#backoffice]
reads_from:
writes_to:
  - Excel
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# Pro_ImportExcelDataRoutes_59

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — writes 1; calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @Tbl_Excel_DataRoutes excel_dataroutes_59
- @CompNo int
## Tables Read
_None_
## Tables Written
- [[Excel]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- [[Technical_CreateRouteBasedonID]]
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
