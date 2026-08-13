---
type: procedure
database: Olives_BO
name: Rpt_CustomersVisitsCount
schema: dbo
tags: [#backoffice, #customer, #reporting, #sales]
reads_from:
  - CSales
  - [[Customers]]
  - [[LogActionTransaction]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[Receipts]]
  - [[Receipts_Currency]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CustomersVisitsCount


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CSales, Customers, LogActionTransaction, OrdersDetails, OrdersHeaders, Receipts, Receipts_Currency, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromCust bigint
- @ToCust bigint
- @FromSales int
- @ToSales int
- @FromDate smalldatetime
- @ToDate smalldatetime
- @UserID nvarchar(50)=null
- @WithTax bit = 1
## Tables Read
- CSales
- [[Customers]]
- [[LogActionTransaction]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[Receipts_Currency]]
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
- CSales
- [[Customers]]
- [[LogActionTransaction]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[Receipts_Currency]]
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
