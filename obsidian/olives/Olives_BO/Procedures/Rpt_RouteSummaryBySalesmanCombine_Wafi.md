---
type: procedure
database: Olives_BO
name: Rpt_RouteSummaryBySalesmanCombine_Wafi
schema: dbo
tags: [#reporting]
reads_from:
  - ClientsActive
  - LogActionTransaction
  - SalesPersons
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Rpt_RouteSummaryBySalesmanCombine_Wafi

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 3 table(s); calls 3 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromDate smalldatetime
- @ToDate smalldatetime
- @SalesmanArray varchar(MAX)
- @UserID nvarchar(50)
- @WithTax bit
- @VisitStatus int
- @Lang int
- @URL nvarchar(200)
## Tables Read
- [[ClientsActive]]
- [[LogActionTransaction]]
- [[SalesPersons]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `Fun_ConvArrayToTable`
- `Fun_GetCompanyBranchesByUser`
- `Fun_GetFromDate`
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
