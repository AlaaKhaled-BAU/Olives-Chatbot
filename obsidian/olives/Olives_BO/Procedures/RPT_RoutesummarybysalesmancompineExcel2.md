---
type: procedure
database: Olives_BO
name: RPT_RoutesummarybysalesmancompineExcel2
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[ClientsActive]]
  - [[Companies]]
  - [[LogActionTransaction]]
  - [[RequestToVisitCustomerNotInRoute]]
writes_to:
called_by:
  - [[Rpt_RouteSummaryBySalesman]]
support_relevance: medium
last_verified: 2026-07-05
---
# RPT_RoutesummarybysalesmancompineExcel2


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Companies, LogActionTransaction, RequestToVisitCustomerNotInRoute. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @Date smalldatetime
## Tables Read
- [[ClientsActive]]
- [[Companies]]
- [[LogActionTransaction]]
- [[RequestToVisitCustomerNotInRoute]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- [[Rpt_RouteSummaryBySalesman]]
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Companies]]
- [[LogActionTransaction]]
- [[RequestToVisitCustomerNotInRoute]]

**Tables Written**
_None_

**Callers**
- [[Rpt_RouteSummaryBySalesman]]

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
