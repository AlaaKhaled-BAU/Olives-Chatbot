---
type: procedure
database: Olives_BO
name: Rpt_SalesDifferencePerRoute
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[Customers]]
  - Fun_ConvArrayToTable
  - [[SalesPersonsItemsGroups]]
  - SplitString
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesDifferencePerRoute


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Fun_ConvArrayToTable, SalesPersonsItemsGroups, SplitString, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int = 1
- @LocationID nvarchar(max) = '  3,1,2,4,5,6,7,8,'
- @FromCurantDate smalldatetime = '2015-02-02'
- @ToCurantDate smalldatetime = '2024-02-06'
- @FromPreDate smalldatetime = '2013-02-02'
- @ToPreDate smalldatetime = '2015-02-06'
- @Cutomer nvarchar(max) = '1,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,3003,'
- @ItemCateg nvarchar (20)='  0001,1,100,10000,10000-11001,10000-11002,10000-11003,10000-11004,10000-11005,10000-11006,10000-11007,10000-11008,10000-11009,10000-11010,10000-11011,10000-11012,10000-11013,10000-11014,10000-11015,10000-11016,'
- @ItemGroupID nvarchar (20)=' 2,1,3,4,'
## Tables Read
- [[Customers]]
- Fun_ConvArrayToTable
- [[SalesPersonsItemsGroups]]
- SplitString
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
- [[Customers]]
- Fun_ConvArrayToTable
- [[SalesPersonsItemsGroups]]
- SplitString
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
