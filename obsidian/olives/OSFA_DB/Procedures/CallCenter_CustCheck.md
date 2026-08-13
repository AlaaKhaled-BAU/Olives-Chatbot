---
type: procedure
database: OSFA_DB
name: CallCenter_CustCheck
schema: dbo
tags: [#mobile]
reads_from:
  - Olives_CallCenter
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# CallCenter_CustCheck


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads Olives_CallCenter. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int =1
- @CustID bigint=314
## Tables Read
- Olives_CallCenter
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Olives_CallCenter

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
