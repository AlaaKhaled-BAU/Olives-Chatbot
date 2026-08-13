---
type: procedure
database: OSFA_DB
name: OT_OrderDeliveryInfo_CheckAttach
schema: dbo
tags: [#mobile, #order]
reads_from:
  - [[OT_OrderDeliveryInfo]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_OrderDeliveryInfo_CheckAttach


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_OrderDeliveryInfo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @OrderYear smallint
- @OrderNo int
## Tables Read
- [[OT_OrderDeliveryInfo]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_OrderDeliveryInfo]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
