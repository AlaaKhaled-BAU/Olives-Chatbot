---
type: procedure
database: Olives_BO
name: Rpt_UnvisitedRouteCustomers_FromDateToDate
schema: dbo
tags: [#backoffice, #customer, #gps, #reporting, #sales]
reads_from:
  - [[LogActionTransaction]]
  - [[SalesPersons]]
writes_to:
called_by:
  - [[Rpt_UnvisitedRouteCustomers]]
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_UnvisitedRouteCustomers_FromDateToDate


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads LogActionTransaction, SalesPersons. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = null
- @FromDate smalldatetime = null
- @ToDate smalldatetime= null
- @SalespersonID int
- @UserID nvarchar(50) = 'admin'
## Tables Read
- [[LogActionTransaction]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- [[Rpt_UnvisitedRouteCustomers]]
## Impact / Dependencies

**Tables Read**
- [[LogActionTransaction]]
- [[SalesPersons]]

**Tables Written**
_None_

**Callers**
- [[Rpt_UnvisitedRouteCustomers]]

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
