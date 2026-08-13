---
type: procedure
database: Olives_BO
name: Rpt_SalesmanTimeSpentPerCustomer3PerCustomer
schema: dbo
tags: [#reporting]
reads_from:
  - ClientsActive
  - Customers
  - CustomersFinancialDetails
  - CustomersTypes
  - LogActionTransaction
  - NoTransactionsReasons
  - OrdersDetails
  - OrdersHeaders
  - Receipts
  - Receipts_Currency
  - SalesPersons
  - TransactionsDetails
  - TransactionsHeaders
writes_to:
called_by:
  - Rpt_SalesmanTimeSpentPerCustomer3CombinePerCustomer
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# Rpt_SalesmanTimeSpentPerCustomer3PerCustomer

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 13 table(s); called by 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromDate smalldatetime
- @SalesmanNo int
- @FromCustomer bigint
- @ToCustomer bigint
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[LogActionTransaction]]
- [[NoTransactionsReasons]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[Receipts_Currency]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
- [[Rpt_SalesmanTimeSpentPerCustomer3CombinePerCustomer]]
## Callees
_None_
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
