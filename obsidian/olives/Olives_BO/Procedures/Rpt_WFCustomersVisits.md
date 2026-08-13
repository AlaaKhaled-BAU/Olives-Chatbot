---
type: procedure
database: Olives_BO
name: Rpt_WFCustomersVisits
schema: dbo
tags: [#backoffice, #customer, #reporting, #sales]
reads_from:
  - CSales
  - [[CompanyBranches]]
  - [[Customers]]
  - [[LogActionTransaction]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[RequestToLoginToCustomerWithoutVerficiation]]
  - [[RequestToVisitCustomerNotInRoute]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - [[WF_Functions]]
  - [[WF_MasterLog]]
  - [[WF_SubLog]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_WFCustomersVisits


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CSales, CompanyBranches, Customers, LogActionTransaction, OrdersDetails, OrdersHeaders, RequestToLoginToCustomerWithoutVerficiation, RequestToVisitCustomerNotInRoute, SalesPersons, TransactionsDetails, TransactionsHeaders, WF_Functions, WF_MasterLog, WF_SubLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromSalesmanNo int
- @ToSalesmanNo int
- @FromCustomerNo bigint
- @ToCustomerNo bigint
- @FromDate smalldatetime
- @ToDate smalldatetime
## Tables Read
- CSales
- [[CompanyBranches]]
- [[Customers]]
- [[LogActionTransaction]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[RequestToLoginToCustomerWithoutVerficiation]]
- [[RequestToVisitCustomerNotInRoute]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[WF_Functions]]
- [[WF_MasterLog]]
- [[WF_SubLog]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- CSales
- [[CompanyBranches]]
- [[Customers]]
- [[LogActionTransaction]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[RequestToLoginToCustomerWithoutVerficiation]]
- [[RequestToVisitCustomerNotInRoute]]
- [[Salespersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[WF_Functions]]
- [[WF_MasterLog]]
- [[WF_SubLog]]

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
