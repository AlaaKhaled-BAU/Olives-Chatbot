---
type: procedure
database: Olives_BO
name: Rpt_RouteSummaryBySalesmanCombine_Spartan
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[Checks]]
  - [[ClientsActive]]
  - [[Companies]]
  - Fun_ConvArrayToTable
  - Fun_GetCompanyBranchesByUser
  - [[LogActionTransaction]]
  - [[Receipts]]
  - [[SalesPersons]]
  - [[Banks]]
  - [[Customers]]
writes_to:
called_by:
  - [[Rpt_RouteSummaryBySalesman_Spartan]]
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_RouteSummaryBySalesmanCombine_Spartan


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Checks, ClientsActive, Companies, Fun_ConvArrayToTable, Fun_GetCompanyBranchesByUser, LogActionTransaction, Receipts, SalesPersons, Banks, Customers. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @FromDate smalldatetime = '2024-10-01'
- @ToDate smalldatetime= '2024-10-21'
- @SalesmanArray VARCHAR(MAX) = '3,16,35,7052,13,15,18,55'
- @UserID nvarchar(50) = ''
- @WithTax bit = 1
## Tables Read
- [[Checks]]
- [[ClientsActive]]
- [[Companies]]
- Fun_ConvArrayToTable
- Fun_GetCompanyBranchesByUser
- [[LogActionTransaction]]
- [[Receipts]]
- [[SalesPersons]]
- [[Banks]]
- [[Customers]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- [[Rpt_RouteSummaryBySalesman_Spartan]]
## Impact / Dependencies

**Tables Read**
- [[Checks]]
- [[ClientsActive]]
- [[Companies]]
- Fun_ConvArrayToTable
- Fun_GetCompanyBranchesByUser
- [[LogActionTransaction]]
- [[Receipts]]
- [[SalesPersons]]
- [[banks]]
- [[customers]]

**Tables Written**
_None_

**Callers**
- [[Rpt_RouteSummaryBySalesman_spartan]]

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
