---
type: procedure
database: Olives_BO
name: Rpt_CustomersSalesAndVisits
schema: dbo
tags: [#backoffice, #customer, #reporting, #sales]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - Fun_GetCustomerVisitsCountByRoute
  - Fun_GetCustomersRouteByDate
  - [[RoutesInformation]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CustomersSalesAndVisits


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, Fun_GetCustomerVisitsCountByRoute, Fun_GetCustomersRouteByDate, RoutesInformation, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int = 1
- @FromDate smalldatetime = '2019-01-01'
- @ToDate smalldatetime = '2019-01-01'
- @FromCustomer bigint = 1
- @ToCustomer bigint =99999999999
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- Fun_GetCustomerVisitsCountByRoute
- Fun_GetCustomersRouteByDate
- [[RoutesInformation]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Customers]]
- Fun_GetCustomerVisitsCountByRoute
- Fun_GetCustomersRouteByDate
- [[RoutesInformation]]
- [[TransactionsDetails]]
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
