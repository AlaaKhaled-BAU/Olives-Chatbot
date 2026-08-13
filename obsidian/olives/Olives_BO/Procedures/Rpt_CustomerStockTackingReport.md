---
type: procedure
database: Olives_BO
name: Rpt_CustomerStockTackingReport
schema: dbo
tags: [#backoffice, #customer, #inventory, #reporting]
reads_from:
  - [[ClientsActive]]
  - [[CustomerStockTacking]]
  - [[CustomerStockTackingDetails]]
  - [[Customers]]
  - Fun_GetCompanyBranchesByUser
  - [[Items]]
  - [[ItemsUnits]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CustomerStockTackingReport


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, CustomerStockTacking, CustomerStockTackingDetails, Customers, Fun_GetCompanyBranchesByUser, Items, ItemsUnits, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromCustomer bigint
- @ToCustomer bigint
- @FromSalesman int
- @ToSalesman int
- @FromGroup int
- @ToGroup int
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromDoc nvarchar(50)=null
- @ToDoc nvarchar(50)=null
- @UserID nvarchar(50)=null
## Tables Read
- [[ClientsActive]]
- [[CustomerStockTacking]]
- [[CustomerStockTackingDetails]]
- [[Customers]]
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[ItemsUnits]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[CustomerStockTacking]]
- [[CustomerStockTackingDetails]]
- [[Customers]]
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[ItemsUnits]]
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
