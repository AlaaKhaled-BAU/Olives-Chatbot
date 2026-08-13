---
type: procedure
database: OSFA_DB
name: OT_GetInvImageCompItem
schema: dbo
tags: [#inventory, #mobile]
reads_from:
  - [[OT_CompetitiveItems]]
  - [[OT_ItemsMF]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_GetInvImageCompItem


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_CompetitiveItems, OT_ItemsMF, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @ItemNo varchar(200)
- @SalesmanNo	smallint
## Tables Read
- [[OT_CompetitiveItems]]
- [[OT_ItemsMF]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_CompetitiveItems]]
- [[OT_ItemsMF]]
- dbo

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

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
