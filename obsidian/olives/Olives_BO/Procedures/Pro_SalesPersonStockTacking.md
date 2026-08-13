---
type: procedure
database: Olives_BO
name: Pro_SalesPersonStockTacking
schema: dbo
tags: [#backoffice, #inventory, #sales]
reads_from:
  - Fun_GetCompanyBranchesByUser
  - [[SalesPersonStockTacking]]
  - [[SalesPersons]]
writes_to:
  - [[SalesPersonStockTacking]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesPersonStockTacking


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_GetCompanyBranchesByUser, SalesPersonStockTacking, SalesPersons. Writes SalesPersonStockTacking. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @IsApproved bit=null
- @OrderNo int=null
- @OrderYear smallint=null
- @cmdType varchar(50)=null
- @FromDate smalldatetime=null
- @ToDate smalldatetime =null
- @UserID nvarchar(50) = null
## Tables Read
- Fun_GetCompanyBranchesByUser
- [[SalesPersonStockTacking]]
- [[SalesPersons]]
## Tables Written
- [[SalesPersonStockTacking]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Fun_GetCompanyBranchesByUser
- [[SalesPersonStockTacking]]
- [[SalesPersons]]

**Tables Written**
- [[SalesPersonStockTacking]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
