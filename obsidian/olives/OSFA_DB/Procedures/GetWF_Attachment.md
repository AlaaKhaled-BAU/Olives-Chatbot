---
type: procedure
database: OSFA_DB
name: GetWF_Attachment
schema: dbo
tags: [#auth, #mobile, #workflow]
reads_from:
  - Olives_Images
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# GetWF_Attachment


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads Olives_Images. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint=1
- @ImageAutoID	bigint
- @FunctionID	bigint =22
## Tables Read
- Olives_Images
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Olives_Images

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
