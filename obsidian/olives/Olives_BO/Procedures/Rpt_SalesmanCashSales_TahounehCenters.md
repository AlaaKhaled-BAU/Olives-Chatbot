---
type: procedure
database: Olives_BO
name: Rpt_SalesmanCashSales_TahounehCenters
schema: dbo
tags: [#reporting]
reads_from:
  - ClientsActive
  - Customers
  - DocumentsTypes
  - ERPStores
  - SalesPersons
  - TransactionsDetails
  - TransactionsHeaders
  - TransactionsTypes
  - TransfersOrdersHeaders
writes_to:
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# Rpt_SalesmanCashSales_TahounehCenters

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 9 table(s); calls 2 proc(s). See sections below for the full dependency map.
## Parameters
- @CompNo smallint
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromSalesman int
- @ToSalesman int
- @FromCustomer bigint
- @ToCustomer bigint
- @UserID nvarchar(50)
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[DocumentsTypes]]
- [[ERPStores]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransactionsTypes]]
- [[TransfersOrdersHeaders]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `Fun_GetCompanyBranchesByUser`
- `Fun_GetFromDate`
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
