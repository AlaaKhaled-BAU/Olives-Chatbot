---
type: procedure
database: Olives_BO
name: Pro_CustomerStockTacking
schema: dbo
tags: [#backoffice, #customer, #inventory]
reads_from:
  - [[CustomerStockTacking]]
  - [[Customers]]
  - Fun_GetCompanyBranchesByUser
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_CustomerStockTacking


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerStockTacking, Customers, Fun_GetCompanyBranchesByUser, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @FromDate smalldatetime=null
- @ToDate smalldatetime=null
- @UserID nvarchar(50) = null
- @cmdType varchar(50)=null
## Tables Read
- [[CustomerStockTacking]]
- [[Customers]]
- Fun_GetCompanyBranchesByUser
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomerStockTacking]]
- [[Customers]]
- Fun_GetCompanyBranchesByUser
- [[SalesPersons]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
