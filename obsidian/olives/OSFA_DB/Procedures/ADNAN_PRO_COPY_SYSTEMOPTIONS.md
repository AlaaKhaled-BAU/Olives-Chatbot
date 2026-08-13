---
type: procedure
database: OSFA_DB
name: ADNAN_PRO_COPY_SYSTEMOPTIONS
schema: dbo
tags: [#mobile]
reads_from:
  - [[AZOT_SystemOptions]]
  - [[OT_SystemOptions]]
  - sysobjects
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# ADNAN_PRO_COPY_SYSTEMOPTIONS


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads AZOT_SystemOptions, OT_SystemOptions, sysobjects. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
_None_
## Tables Read
- [[AZOT_SystemOptions]]
- [[OT_SystemOptions]]
- sysobjects
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[AZOT_SystemOptions]]
- [[OT_SystemOptions]]
- sysobjects

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
