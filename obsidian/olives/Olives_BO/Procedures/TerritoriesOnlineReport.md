---
type: procedure
database: Olives_BO
name: TerritoriesOnlineReport
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[SystemCodes]]
  - [[Territories]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# TerritoriesOnlineReport


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SystemCodes, Territories. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint=1
- @SalesmanNo int=3003
- @FromDate smalldatetime='2024-1-1'
- @ToDate smalldatetime='2025-12-1'
## Tables Read
- [[SystemCodes]]
- [[Territories]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SystemCodes]]
- [[Territories]]

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
