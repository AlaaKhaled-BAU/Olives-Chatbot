---
type: procedure
database: Olives_BO
name: GetRouteAndCategoryOnline
schema: dbo
tags: [#backoffice, #gps, #reference, #sales]
reads_from:
  - Olives_BO
  - OverDueV
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# GetRouteAndCategoryOnline


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Olives_BO, OverDueV. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=1,@CmdType nvarchar(200)
- @SalesmanNo int=0
## Tables Read
- Olives_BO
- OverDueV
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Olives_BO
- OverDueV

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
