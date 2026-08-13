---
type: procedure
database: Olives_BO
name: Pro_Territories
schema: dbo
tags: [#backoffice]
reads_from:
  - [[SystemCodes]]
  - [[Territories]]
writes_to:
  - [[Territories]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_Territories


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SystemCodes, Territories. Writes Territories. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @CmdType nvarchar(200)='SelectAll'
- @SalesmanNo int=null
- @TerritoryType nvarchar(50)=null
- @TrDate smalldatetime=null
- @Notes nvarchar(300) = null
## Tables Read
- [[SystemCodes]]
- [[Territories]]
## Tables Written
- [[Territories]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SystemCodes]]
- [[Territories]]

**Tables Written**
- [[Territories]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
