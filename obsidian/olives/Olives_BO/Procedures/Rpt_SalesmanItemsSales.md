---
type: procedure
database: Olives_BO
name: Rpt_SalesmanItemsSales
schema: dbo
tags: [#backoffice, #inventory, #reporting, #sales]
reads_from:
  - [[ClientsActive]]
  - Fun_GetCompanyBranchesByUser
  - [[Items]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanItemsSales


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Fun_GetCompanyBranchesByUser, Items, PriceListDetails, PriceLists, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromSalesPerson int
- @ToSalesPerson int
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromType int
- @ToType int
- @UserID nvarchar(50)=null
- @InvoiceType int=1
## Tables Read
- [[ClientsActive]]
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[PriceListDetails]]
- [[PriceLists]]
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
- [[ClientsActive]]
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[PriceListDetails]]
- [[PriceLists]]
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
