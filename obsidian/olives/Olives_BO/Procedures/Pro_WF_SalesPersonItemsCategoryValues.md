---
type: procedure
database: Olives_BO
name: Pro_WF_SalesPersonItemsCategoryValues
schema: dbo
tags: [#auth, #backoffice, #inventory, #reference, #sales, #workflow]
reads_from:
  - [[WF_SalesPersonItemsCategoryValues]]
writes_to:
  - [[WF_SalesPersonItemsCategoryValues]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_WF_SalesPersonItemsCategoryValues


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads WF_SalesPersonItemsCategoryValues. Writes WF_SalesPersonItemsCategoryValues. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @cmdType  nvarchar(max)='INSERT'
- @CompanyID smallint=1
- @SalesPersonID int = 6
- @ItemCode nvarchar(20) ='120032'
- @AllowValue float =22
## Tables Read
- [[WF_SalesPersonItemsCategoryValues]]
## Tables Written
- [[WF_SalesPersonItemsCategoryValues]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[WF_SalesPersonItemsCategoryValues]]

**Tables Written**
- [[WF_SalesPersonItemsCategoryValues]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
