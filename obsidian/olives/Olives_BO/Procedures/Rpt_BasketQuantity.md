---
type: procedure
database: Olives_BO
name: Rpt_BasketQuantity
schema: dbo
tags: [#reporting]
reads_from:
  - Items
  - RoutesInformation
  - SalesPersonItemsBalance
  - SalesPersons
  - SalesPersonsRoutes
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Rpt_BasketQuantity

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 5 table(s); calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @SalesmanNo int
- @FromDate smalldatetime
## Tables Read
- [[Items]]
- [[RoutesInformation]]
- [[SalesPersonItemsBalance]]
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
