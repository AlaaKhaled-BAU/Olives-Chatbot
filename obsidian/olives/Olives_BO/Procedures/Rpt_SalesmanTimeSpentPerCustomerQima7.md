---
type: procedure
database: Olives_BO
name: Rpt_SalesmanTimeSpentPerCustomerQima7
schema: dbo
tags: [#backoffice, #customer, #reporting, #sales]
reads_from:
  - CSales
  - [[ClientsActive]]
  - [[CompanyBranches]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - [[LogActionTransaction]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[Receipts]]
  - [[Receipts_Currency]]
  - [[Report5CustomersExcemptions]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanTimeSpentPerCustomerQima7


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CSales, ClientsActive, CompanyBranches, Customers, CustomersFinancialDetails, CustomersTypes, LogActionTransaction, OrdersDetails, OrdersHeaders, Receipts, Receipts_Currency, Report5CustomersExcemptions, SalesPersons, TransactionsDetails, TransactionsHeaders. Invoked by 2 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromDate smalldatetime
- @SalesmanNo int
## Tables Read
- CSales
- [[ClientsActive]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[LogActionTransaction]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[Receipts_Currency]]
- [[Report5CustomersExcemptions]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
- [[Rpt_SalesmanTimeSpentPerCustomerCombineQima7]]
- [[Rpt_SalesmanTimeSpentPerCustomerCombineQima9]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- CSales
- [[ClientsActive]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[LogActionTransaction]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[Receipts_Currency]]
- [[Report5CustomersExcemptions]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
- [[Rpt_SalesmanTimeSpentPerCustomerCombineQima7]]
- [[Rpt_SalesmanTimeSpentPerCustomerCombineQima9]]


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
