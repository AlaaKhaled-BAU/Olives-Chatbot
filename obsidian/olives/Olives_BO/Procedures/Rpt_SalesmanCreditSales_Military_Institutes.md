---
type: procedure
database: Olives_BO
name: Rpt_SalesmanCreditSales_Military_Institutes
schema: dbo
tags: [#reporting]
reads_from:
  - Customers
  - SalesPersons
  - TransactionsDetails
  - TransactionsHeaders
  - TransactionsTypes
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Rpt_SalesmanCreditSales_Military_Institutes

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 5 table(s); calls 2 proc(s). See sections below for the full dependency map.
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
- [[Customers]]
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
- `Fun_GetCompanyBranchesByUser`
- `Fun_GetFromDate`
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
