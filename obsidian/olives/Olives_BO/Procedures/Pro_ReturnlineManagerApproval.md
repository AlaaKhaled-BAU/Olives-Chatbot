---
type: procedure
database: Olives_BO
name: Pro_ReturnlineManagerApproval
schema: dbo
tags: [#backoffice, #order, #workflow]
reads_from:
  - Fun_GetCompanyBranchesByUser
  - [[Items]]
  - [[ItemsCategories]]
  - [[SalesPersonItemsAssignment]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - `dbo`
writes_to:
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - TransactionsHeadersLog
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ReturnlineManagerApproval


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_GetCompanyBranchesByUser, Items, ItemsCategories, SalesPersonItemsAssignment, SalesPersons, TransactionsDetails, TransactionsHeaders, dbo. Writes TransactionsDetails, TransactionsHeaders, TransactionsHeadersLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @cmdType nvarchar (200)=null
- @CompanyID int = null
- @TransYear int  = null
- @TransNo  int  = null
- @fromDate smalldatetime =null
- @ToDate smalldatetime =null
- @CategCode nvarchar (50) =NULL
- @UserID nvarchar(50) = 'admin'
## Tables Read
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[ItemsCategories]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- `dbo`
## Tables Written
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- TransactionsHeadersLog
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[ItemsCategories]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- dbo

**Tables Written**
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- TransactionsHeadersLog

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
