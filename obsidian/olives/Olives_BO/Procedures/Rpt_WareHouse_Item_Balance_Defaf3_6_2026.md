---
type: procedure
database: Olives_BO
name: Rpt_WareHouse_Item_Balance_Defaf3_6_2026
schema: dbo
tags: [#reporting]
reads_from:
  - ClientsActive
  - Items
  - ItemsCategories
  - SalesPersons
  - TransactionsDetails
  - TransactionsHeaders
writes_to:
called_by:
  - Rpt_WareHouse_Item_Balance
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Rpt_WareHouse_Item_Balance_Defaf3_6_2026

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 6 table(s); called by 1 proc(s); calls 3 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromSalesPerson int
- @ToSalesPerson int
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromItem nvarchar(100)
- @ToItem nvarchar(100)
- @FromCateg nvarchar(100)
- @ToCateg nvarchar(100)
- @UserID nvarchar(50)
## Tables Read
- [[ClientsActive]]
- [[Items]]
- [[ItemsCategories]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
- [[Rpt_WareHouse_Item_Balance]]
## Callees
- `Fun_GetFromDate`
- `Fun_GetItemOpenBalBySalesman`
- `Fun_GetItemOpenBalBySalesman_DefafCo1`
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
