---
type: procedure
database: Olives_BO
name: Rpt_DailyReceiptsDetails
schema: dbo
tags: [#backoffice, #billing, #reporting]
reads_from:
  - [[Checks]]
  - [[Customers]]
  - Fun_GetCompanyBranchesByUser
  - [[Receipts]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_DailyReceiptsDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Checks, Customers, Fun_GetCompanyBranchesByUser, Receipts, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint =1
- @FromDate smalldatetime = '2016-01-01'
- @ToDate smalldatetime  = '2017-10-31'
- @FromSalesmanNo int = 0
- @ToSalesmanNo int = 9999
- @FromClass int = 0
- @ToClass int = 9999
- @UserID nvarchar(50) = 'admin'
- @FromCustType int=0
- @ToCustType int =99999
## Tables Read
- [[Checks]]
- [[Customers]]
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
- [[Checks]]
- [[Customers]]
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
