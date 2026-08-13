---
type: procedure
database: Olives_BO
name: Rpt_RouteVisitsByWeekDayforExcel
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[Companies]]
  - [[LogActionTransaction]]
  - [[SalesPersons]]
  - [[Customers]]
writes_to:
called_by:
  - [[Rpt_RouteSummaryBySalesman]]
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_RouteVisitsByWeekDayforExcel


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Companies, LogActionTransaction, SalesPersons, Customers. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = null
- @FromDate smalldatetime = null
- @ToDate smalldatetime= null
- @Fromsalesman int=null
- @Tosalesman int=null
- @FromCustomer bigint
- @Tocustomer bigint
- @UserID nvarchar(50) = null
- @WithTax bit = 1
## Tables Read
- [[Companies]]
- [[LogActionTransaction]]
- [[SalesPersons]]
- [[Customers]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- [[Rpt_RouteSummaryBySalesman]]
## Impact / Dependencies

**Tables Read**
- [[Companies]]
- [[LogActionTransaction]]
- [[SalesPersons]]
- [[customers]]

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
