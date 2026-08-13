---
type: procedure
database: Olives_BO
name: Rpt_RouteSummaryBySalesmanCombine_New
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[ClientsActive]]
  - [[Companies]]
  - Fun_ConvArrayToTable
  - Fun_GetCompanyBranchesByUser
  - [[LogActionTransaction]]
  - [[SalesPersons]]
writes_to:
called_by:
  - Rpt_RouteSummaryBySalesman_New
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_RouteSummaryBySalesmanCombine_New


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Companies, Fun_ConvArrayToTable, Fun_GetCompanyBranchesByUser, LogActionTransaction, SalesPersons. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = null
- @FromDate smalldatetime = null
- @ToDate smalldatetime= null
- @SalesmanArray VARCHAR(MAX) = null
- @UserID nvarchar(50) = ''
- @WithTax bit = 1
## Tables Read
- [[ClientsActive]]
- [[Companies]]
- Fun_ConvArrayToTable
- Fun_GetCompanyBranchesByUser
- [[LogActionTransaction]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- Rpt_RouteSummaryBySalesman_New
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Companies]]
- Fun_ConvArrayToTable
- Fun_GetCompanyBranchesByUser
- [[LogActionTransaction]]
- [[SalesPersons]]

**Tables Written**
_None_

**Callers**
- Rpt_RouteSummaryBySalesman_New

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
