---
type: procedure
database: Olives_BO
name: Rpt_SalesmanJourneyPerformanceDetails
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - Fun_GetCompanyBranchesByUser
  - [[LogActionTransaction]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanJourneyPerformanceDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_GetCompanyBranchesByUser, LogActionTransaction, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = null
- @FromDate datetime = null
- @ToDate datetime = null
- @FromSalesmanNo int = 0
- @ToSalesmanNo int = 999999
- @UserID nvarchar(50) = null
## Tables Read
- Fun_GetCompanyBranchesByUser
- [[LogActionTransaction]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Fun_GetCompanyBranchesByUser
- [[LogActionTransaction]]
- [[SalesPersons]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
