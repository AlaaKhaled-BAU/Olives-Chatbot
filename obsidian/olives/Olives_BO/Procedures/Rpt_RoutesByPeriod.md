---
type: procedure
database: Olives_BO
name: Rpt_RoutesByPeriod
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[CustomersFinancialDetails]]
  - Fun_GetCompanyBranchesByUser
  - [[LogActionTransaction]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
  - [[TransactionsPromotions]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_RoutesByPeriod


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersFinancialDetails, Fun_GetCompanyBranchesByUser, LogActionTransaction, OrdersHeaders, SalesPersons, TransactionsHeaders, TransactionsPromotions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint =1
- @FromDate smalldatetime ='2021-01-03'
- @ToDate smalldatetime ='2021-08-03'
- @FromSales int = 1
- @ToSales int =9999
- @UserID nvarchar(50) ='admin'
## Tables Read
- [[CustomersFinancialDetails]]
- Fun_GetCompanyBranchesByUser
- [[LogActionTransaction]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- [[TransactionsPromotions]]
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
- [[SalesPersons]]
- [[TransactionsHeaders]]
- [[TransactionsPromotions]]

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
