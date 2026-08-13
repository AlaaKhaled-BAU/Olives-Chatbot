---
type: procedure
database: Olives_BO
name: Rpt_RouteSummaryBySalesmanCombine_SukhtianForPWPI_22_BO
schema: dbo
tags: [#reporting]
reads_from:
  - ClientsActive
  - LogActionTransaction
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Rpt_RouteSummaryBySalesmanCombine_SukhtianForPWPI_22_BO

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 2 table(s); calls 2 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromDate datetime
- @ToDate datetime
- @SalesmanArray varchar(MAX)
- @UserID nvarchar(50)
- @WithTax bit
## Tables Read
- [[ClientsActive]]
- [[LogActionTransaction]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `Fun_ConvArrayToTable`
- `Fun_GetFromDate`
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
