---
type: procedure
database: Olives_BO
name: Rpt_RouteScoreBySalesmanCombine
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[LogActionTransaction]]
writes_to:
called_by:
  - [[Rpt_RouteScoreBySalesman]]
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_RouteScoreBySalesmanCombine


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads LogActionTransaction. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = null
- @FromDate smalldatetime = null
- @ToDate smalldatetime= null
- @FromSalesmanNo int = 0
- @ToSalesmanNo int = 999999
- @UserID nvarchar(50) = null
## Tables Read
- [[LogActionTransaction]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- [[Rpt_RouteScoreBySalesman]]
## Impact / Dependencies

**Tables Read**
- [[LogActionTransaction]]

**Tables Written**
_None_

**Callers**
- [[Rpt_RouteScoreBySalesman]]

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
