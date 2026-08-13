---
type: procedure
database: Olives_BO
name: Rpt_CustomerRouteVistsList_temp
schema: dbo
tags: [#reporting]
reads_from:
  - CustomersFinancialDetails
  - LogActionTransaction
  - SalesPersons
  - SalesPersonsRoutes
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Rpt_CustomerRouteVistsList_temp

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 4 table(s); calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyId int
- @FromSalesman int
- @ToSalesman int
- @FromDate smalldatetime
- @ToDate smalldatetime
## Tables Read
- [[CustomersFinancialDetails]]
- [[LogActionTransaction]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `Fun_GetWeekNo`
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
