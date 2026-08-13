---
type: procedure
database: Olives_BO
name: Rpt_RouteScoreBySalesman123
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[CustomersFinancialDetails]]
  - Fun_GetCompanyBranchesByUser
  - [[LogActionTransaction]]
  - [[OrdersHeaders]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_RouteScoreBySalesman123


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersFinancialDetails, Fun_GetCompanyBranchesByUser, LogActionTransaction, OrdersHeaders, RoutesInformation, SalesPersons, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = null
- @FromDate smalldatetime = null
- @ToDate smalldatetime = null
- @FromSalesmanNo int = 0
- @ToSalesmanNo int = 999999
- @UserID nvarchar(50) = null
## Tables Read
- [[CustomersFinancialDetails]]
- Fun_GetCompanyBranchesByUser
- [[LogActionTransaction]]
- [[OrdersHeaders]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomersFinancialDetails]]
- Fun_GetCompanyBranchesByUser
- [[LogActionTransaction]]
- [[OrdersHeaders]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[TransactionsHeaders]]

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
