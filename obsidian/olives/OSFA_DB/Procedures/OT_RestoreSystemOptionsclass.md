---
type: procedure
database: OSFA_DB
name: OT_RestoreSystemOptionsclass
schema: dbo
tags: [#mobile, #reference]
reads_from:
  - [[OT_SystemOptions]]
  - `dbo`
writes_to:
  - [[OT_SystemOptions]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_RestoreSystemOptionsclass


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_SystemOptions, dbo. Writes OT_SystemOptions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[OT_SystemOptions]]
- `dbo`
## Tables Written
- [[OT_SystemOptions]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_SystemOptions]]
- dbo

**Tables Written**
- [[OT_SystemOptions]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
