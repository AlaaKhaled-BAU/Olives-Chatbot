---
type: procedure
database: OSFA_DB
name: Technical_OT_CopySystemOption
schema: dbo
tags: [#mobile]
reads_from:
  - [[CopySystemOptions]]
  - Cur_Op_ID
  - [[OT_SystemOptions]]
  - cur_Salesman
  - sysobjects
writes_to:
  - [[OT_SystemOptions]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Technical_OT_CopySystemOption


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads CopySystemOptions, Cur_Op_ID, OT_SystemOptions, cur_Salesman, sysobjects. Writes OT_SystemOptions. Invoked by 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @FromSalesman int
- @CopyOption varchar(50)
## Tables Read
- [[CopySystemOptions]]
- Cur_Op_ID
- [[OT_SystemOptions]]
- cur_Salesman
- sysobjects
## Tables Written
- [[OT_SystemOptions]]
## Callers
- [[Technical_CopySystemoptionsForSeveralSalespersons]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CopySystemOptions]]
- Cur_Op_ID
- [[OT_SystemOptions]]
- cur_Salesman
- sysobjects

**Tables Written**
- [[OT_SystemOptions]]

**Callers**
_None_

**Callees**
- [[Technical_CopySystemoptionsForSeveralSalespersons]]


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
