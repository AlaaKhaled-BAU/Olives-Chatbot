---
type: procedure
database: Olives_BO
name: Rpt_OrdersSalesReport
schema: dbo
tags: [#backoffice, #order, #reporting, #sales]
reads_from:
  - Fun_GetCompanyBranchesByUser
  - [[Items]]
  - [[ItemsUnits]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_OrdersSalesReport


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_GetCompanyBranchesByUser, Items, ItemsUnits, OrdersDetails, OrdersHeaders, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @SalesPersonID int = null
- @FromDate DateTime = null
- @ToDate DateTime = null
- @StoreID int = null
- @UserID nvarchar(50)=null
- @Clientactive Smallint = null
## Tables Read
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[ItemsUnits]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
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
- [[Items]]
- [[ItemsUnits]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
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
