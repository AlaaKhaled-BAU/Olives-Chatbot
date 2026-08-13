---
type: procedure
database: Olives_BO
name: Rpt_SalesOrdersApprovalEnmaa
schema: dbo
tags: [#integration, #reporting]
reads_from:
  - Customers
  - CustomersBalanceAging
  - CustomersBalanceAging_Inmaa
  - CustomersFinancialDetails
  - Items
  - ItemsUnits
  - OrdersDetails
  - OrdersHeaders
  - PaymentsTypes
  - SalesPersons
  - TransactionsBatchsItemsInfo
writes_to:
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# Rpt_SalesOrdersApprovalEnmaa

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 11 table(s). See sections below for the full dependency map.
## Parameters
- @CompNo int
- @OrderYear int
- @OrderNo bigint
- @CustomerID bigint
## Tables Read
- [[Customers]]
- [[CustomersBalanceAging]]
- [[CustomersBalanceAging_Inmaa]]
- [[CustomersFinancialDetails]]
- [[Items]]
- [[ItemsUnits]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[PaymentsTypes]]
- [[SalesPersons]]
- [[TransactionsBatchsItemsInfo]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
_None_
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
