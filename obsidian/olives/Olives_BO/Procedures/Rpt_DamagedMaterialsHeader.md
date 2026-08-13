---
type: procedure
database: Olives_BO
name: Rpt_DamagedMaterialsHeader
schema: dbo
tags: [#reporting]
reads_from:
  - Items
  - ItemsUnits
  - SalesPersons
  - TransactionsDetails
  - TransactionsHeaders
  - TransfersOrdersDetails
  - TransfersOrdersHeaders
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Rpt_DamagedMaterialsHeader

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 7 table(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromSalesmanNo nvarchar(100)
- @ToSalesmanNo nvarchar(100)
- @fromDate smalldatetime
- @UserID nvarchar(MAX)
## Tables Read
- [[Items]]
- [[ItemsUnits]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
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
