---
type: procedure
database: Olives_BO
name: Rpt_ItemSalesCommissionsBySalesman
schema: dbo
tags: [#reporting]
reads_from:
  - ItemCommissions
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
# Rpt_ItemSalesCommissionsBySalesman

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 5 table(s). See sections below for the full dependency map.
## Parameters
- @CompanyId int
- @FromSalesmanNo int
- @ToSalesmanNo int
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromCateg nvarchar(20)
- @ToCateg nvarchar(20)
- @FromItem nvarchar(100)
- @ToItem nvarchar(100)
## Tables Read
- [[ItemCommissions]]
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
_None_
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
