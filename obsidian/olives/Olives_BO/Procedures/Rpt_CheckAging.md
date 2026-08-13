---
type: procedure
database: Olives_BO
name: Rpt_CheckAging
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - CTE
  - [[Checks]]
  - [[Customers]]
  - [[CustomersClasses]]
  - Fun_GetCompanyBranchesByUser
  - [[Receipts]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CheckAging


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CTE, Checks, Customers, CustomersClasses, Fun_GetCompanyBranchesByUser, Receipts, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint =1
- @FromYear int =2018
- @ToYear int =2018
- @FromMonth int=1
- @ToMonth int =2
- @FromClass int=1
- @ToClass int =1
- @Aging int =30
- @UserID nvarchar(50) ='admin'
- @FromCustType int = 0
- @ToCustType int = 99999
## Tables Read
- CTE
- [[Checks]]
- [[Customers]]
- [[CustomersClasses]]
- Fun_GetCompanyBranchesByUser
- [[Receipts]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- CTE
- [[Checks]]
- [[Customers]]
- [[CustomersClasses]]
- Fun_GetCompanyBranchesByUser
- [[Receipts]]
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
