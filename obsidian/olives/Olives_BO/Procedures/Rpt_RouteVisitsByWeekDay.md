---
type: procedure
database: Olives_BO
name: Rpt_RouteVisitsByWeekDay
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[Companies]]
  - [[Customers]]
  - [[LogActionTransaction]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_RouteVisitsByWeekDay


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Companies, Customers, LogActionTransaction, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromSales int
- @ToSales int
- @FromCustomer bigint
- @ToCustomer bigint
- @FromDate smalldatetime
- @ToDate smalldatetime
- @UserID nvarchar(50) = null
## Tables Read
- [[Companies]]
- [[Customers]]
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
- [[Companies]]
- [[Customers]]
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
