---
type: procedure
database: Olives_BO
name: Rpt_NetsalesAndLoadOrderAndRate_Waffir
schema: dbo
tags: [#reporting]
reads_from:
  - Customers
  - Items
  - SalesPersons
  - TransactionsDetails
  - TransactionsHeaders
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Rpt_NetsalesAndLoadOrderAndRate_Waffir

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 5 table(s); calls 3 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromSalesman int
- @ToSalesman int
## Tables Read
- [[Customers]]
- [[Items]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `Fun_GetDetailsLoadAndUnloadOrder`
- `Fun_GetSalesAndRetAmountPerItem`
- `Fun_GetSalesAndRetAmountPerItemWithoutTax`
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
