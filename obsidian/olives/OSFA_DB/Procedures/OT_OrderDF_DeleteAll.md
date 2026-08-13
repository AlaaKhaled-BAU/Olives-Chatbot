---
type: procedure
database: OSFA_DB
name: OT_OrderDF_DeleteAll
schema: dbo
tags: [#mobile, #order]
reads_from:
  - Olives_BO
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_OrderDF_DeleteAll


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads Olives_BO. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @OrderYear smallint
- @OrderNo int
## Tables Read
- Olives_BO
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Olives_BO

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Cleanup procedure — removes stale or temporary data. Run during maintenance windows only.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
