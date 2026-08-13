---
type: procedure
database: Olives_BO
name: Rpt_ItemsSalesmanNotSold
schema: dbo
tags: [#backoffice, #inventory, #reporting, #sales]
reads_from:
  - Fun_GetCompanyBranchesByUser
  - Fun_SalesmanItemSales
  - Fun_SalesmanItemSalesInOrder
  - [[Items]]
  - [[SalesPersonItemsAssignment]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_ItemsSalesmanNotSold


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_GetCompanyBranchesByUser, Fun_SalesmanItemSales, Fun_SalesmanItemSalesInOrder, Items, SalesPersonItemsAssignment, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromSales int
- @ToSales int
- @FromDate smalldatetime
- @ToDate smalldatetime
- @SaleManType smallint
- @UserID nvarchar(50)=null
## Tables Read
- Fun_GetCompanyBranchesByUser
- Fun_SalesmanItemSales
- Fun_SalesmanItemSalesInOrder
- [[Items]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Fun_GetCompanyBranchesByUser
- Fun_SalesmanItemSales
- Fun_SalesmanItemSalesInOrder
- [[Items]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]

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
