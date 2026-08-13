---
type: procedure
database: Olives_BO
name: Rpt_TimeManagement
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[ClientsActive]]
  - Fun_ConvArrayToTable
  - Fun_GetCustomersPromotionsAppliedCount
  - [[LogActionTransaction]]
  - [[NoTransactionsReasons]]
  - [[SalesPersons]]
writes_to:
called_by:
  - [[Rpt_RouteSummaryBySalesman]]
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_TimeManagement


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Fun_ConvArrayToTable, Fun_GetCustomersPromotionsAppliedCount, LogActionTransaction, NoTransactionsReasons, SalesPersons. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = null
- @FromDate smalldatetime = null
- @ToDate smalldatetime= null
- @SalesmanArray VARCHAR(MAX) = null
- @UserID nvarchar(50) = null
- @WithTax bit = 1
## Tables Read
- [[ClientsActive]]
- Fun_ConvArrayToTable
- Fun_GetCustomersPromotionsAppliedCount
- [[LogActionTransaction]]
- [[NoTransactionsReasons]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- [[Rpt_RouteSummaryBySalesman]]
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- Fun_ConvArrayToTable
- Fun_GetCustomersPromotionsAppliedCount
- [[LogActionTransaction]]
- [[NoTransactionsReasons]]
- [[Salespersons]]

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
