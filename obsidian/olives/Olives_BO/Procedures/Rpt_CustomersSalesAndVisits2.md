---
type: procedure
database: Olives_BO
name: Rpt_CustomersSalesAndVisits2
schema: dbo
tags: [#backoffice, #customer, #reporting, #sales]
reads_from:
  - [[Customers]]
  - Fun_GetCustomerVisitsCountByRoute
  - Fun_GetCustomersRouteByDate
  - [[LogActionTransaction]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CustomersSalesAndVisits2


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Fun_GetCustomerVisitsCountByRoute, Fun_GetCustomersRouteByDate, LogActionTransaction, RoutesInformation, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int = 1
- @FromDate smalldatetime= '2023-08-17'
- @ToDate smalldatetime = '2023-08-17'
- @FromCustomer bigint = 1
- @ToCustomer bigint =99999999999
- @fromsalesman int=6
- @tosalesmanno int=6
- @fromrouteID int=0
- @torouteID int=99999999
## Tables Read
- [[Customers]]
- Fun_GetCustomerVisitsCountByRoute
- Fun_GetCustomersRouteByDate
- [[LogActionTransaction]]
- [[RoutesInformation]]
- [[SalesPersons]]
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
- [[Customers]]
- Fun_GetCustomerVisitsCountByRoute
- Fun_GetCustomersRouteByDate
- [[LogActionTransaction]]
- [[RoutesInformation]]
- [[SalesPersons]]
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
