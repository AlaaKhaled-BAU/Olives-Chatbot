---
type: procedure
database: Olives_BO
name: Rpt_ReprintCount
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[CustomerStockTacking]]
  - [[OrdersHeaders]]
  - [[Receipts]]
  - [[ReprintedTransactions]]
  - [[SalesPersonStockTacking]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
  - [[TransactionsTypes]]
  - [[TransfersOrdersHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_ReprintCount


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerStockTacking, OrdersHeaders, Receipts, ReprintedTransactions, SalesPersonStockTacking, SalesPersons, TransactionsHeaders, TransactionsTypes, TransfersOrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint =null
- @FromDate smalldatetime =null
- @ToDate smalldatetime =null
- @FromTransactionType  smallint =null
- @ToTransactionType smallint =null
- @FromTransactionNo int =null
- @ToTransactionNo int=null
- @FromSalesman int =null
- @Tosalesman int = null
- @UserID nvarchar(50) = null
## Tables Read
- [[CustomerStockTacking]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[ReprintedTransactions]]
- [[SalesPersonStockTacking]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- [[TransactionsTypes]]
- [[TransfersOrdersHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomerStockTacking]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[ReprintedTransactions]]
- [[SalesPersonStockTacking]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- [[TransactionsTypes]]
- [[TransfersOrdersHeaders]]

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
