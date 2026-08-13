---
type: procedure
database: Olives_BO
name: Rpt_Receipts
schema: dbo
tags: [#backoffice, #billing, #reporting]
reads_from:
  - [[Checks]]
  - [[ClientsActive]]
  - [[Customers]]
  - Fun_GetCompanyBranchesByUser
  - [[Receipts]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_Receipts


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Checks, ClientsActive, Customers, Fun_GetCompanyBranchesByUser, Receipts, SalesPersons, SalesPersonsGroups. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromSales int
- @ToSales int
- @FromDate smalldatetime
- @ToDate smalldatetime
- @UserID nvarchar(50)=null
- @TrDate bit = 0
- @IsVoid bit = 0
- @PostedStatus int = 1
- @FromCustType int
- @ToCustType int
- @FromGroup int = 0
- @ToGroup int = 99999999
## Tables Read
- [[Checks]]
- [[ClientsActive]]
- [[Customers]]
- Fun_GetCompanyBranchesByUser
- [[Receipts]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Checks]]
- [[ClientsActive]]
- [[Customers]]
- Fun_GetCompanyBranchesByUser
- [[Receipts]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]

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
