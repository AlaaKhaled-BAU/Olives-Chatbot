---
type: procedure
database: Olives_BO
name: Rpt_TransactionsVisitsBySalesPersonID
schema: dbo
tags: [#reporting]
reads_from:
  - Checks
  - CustomerStockTacking
  - CustomerStockTackingDetails
  - Customers
  - Items
  - ItemsUnits
  - LogActionTransaction
  - OrdersDetails
  - OrdersHeaders
  - Receipts
  - ReturnOrdersDetails
  - ReturnOrdersHeaders
  - SalesPersons
  - TransactionsDetails
  - TransactionsHeaders
  - TransactionsTypes
writes_to:
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# Rpt_TransactionsVisitsBySalesPersonID

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 16 table(s). See sections below for the full dependency map.
## Parameters
- @FromSalesPersonID int
- @ToSalesPersonID int
- @CompanyID int
- @TransactionYear int
- @TransactionTypeID int
- @TransactionNo bigint
- @FromDate smalldatetime
- @ToDate smalldatetime
- @domain nvarchar(200)
- @cmdType nvarchar(200)
## Tables Read
- [[Checks]]
- [[CustomerStockTacking]]
- [[CustomerStockTackingDetails]]
- [[Customers]]
- [[Items]]
- [[ItemsUnits]]
- [[LogActionTransaction]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[ReturnOrdersDetails]]
- [[ReturnOrdersHeaders]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransactionsTypes]]
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
