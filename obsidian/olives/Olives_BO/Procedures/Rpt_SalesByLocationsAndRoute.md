---
type: procedure
database: Olives_BO
name: Rpt_SalesByLocationsAndRoute
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - Fun_GetCompanyBranchesByUser
  - [[Locations]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesByLocationsAndRoute


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, Fun_GetCompanyBranchesByUser, Locations, SalesPersons, SalesPersonsGroups, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int =null
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromSalesman int =Null
- @ToSalesman int = Null
- @FromLocations int = Null
- @ToLocations int=Null
- @FromGroup int = 0
- @ToGroup int = 99999999
- @UserID NVARCHAR(50)=null
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- Fun_GetCompanyBranchesByUser
- [[Locations]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
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
- [[Customers]]
- Fun_GetCompanyBranchesByUser
- [[Locations]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
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
