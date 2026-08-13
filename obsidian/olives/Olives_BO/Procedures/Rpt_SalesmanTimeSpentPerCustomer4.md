---
type: procedure
database: Olives_BO
name: Rpt_SalesmanTimeSpentPerCustomer4
schema: dbo
tags: [#backoffice, #customer, #reporting, #sales]
reads_from:
  - CSales
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - Fun_GetCompanyBranchesByUser
  - [[LogActionTransaction]]
  - [[NoTransactionsReasons]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanTimeSpentPerCustomer4


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CSales, Customers, CustomersFinancialDetails, CustomersTypes, Fun_GetCompanyBranchesByUser, LogActionTransaction, NoTransactionsReasons, OrdersDetails, OrdersHeaders, SalesPersons, TransactionsDetails, TransactionsHeaders. Invoked by 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = null
- @FromDate smallDateTime = null
- @FromSalesman int = null
- @UserID nvarchar(50) = null
## Tables Read
- CSales
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- Fun_GetCompanyBranchesByUser
- [[LogActionTransaction]]
- [[NoTransactionsReasons]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
- [[Rpt_SalesmanTimeSpentPerCustomer4Combine]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- CSales
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- Fun_GetCompanyBranchesByUser
- [[LogActionTransaction]]
- [[NoTransactionsReasons]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
- [[Rpt_SalesmanTimeSpentPerCustomer4Combine]]


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
