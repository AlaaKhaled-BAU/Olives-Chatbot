---
type: procedure
database: OSFA_DB
name: Technical_CopySystemoptionsForSeveralSalespersons
schema: dbo
tags: [#mobile, #sales]
reads_from:
  - [[CopySystemOptions]]
  - [[OT_SystemOptions]]
  - Olives_BO
  - the
writes_to:
  - [[CopySystemOptions]]
called_by:
  - [[Technical_OT_CopySystemOption]]
support_relevance: high
last_verified: 2026-07-05
---
# Technical_CopySystemoptionsForSeveralSalespersons


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads CopySystemOptions, OT_SystemOptions, Olives_BO, the. Writes CopySystemOptions. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @compno int=2
- @SourceSalesman int=4
- @SalespersonIDs VARCHAR(MAX) = '64,25,23'
## Tables Read
- [[CopySystemOptions]]
- [[OT_SystemOptions]]
- Olives_BO
- the
## Tables Written
- [[CopySystemOptions]]
## Callers
_None (no known callers)_
## Callees
- [[Technical_OT_CopySystemOption]]
## Impact / Dependencies

**Tables Read**
- [[CopySystemOptions]]
- [[OT_SystemOptions]]
- Olives_BO
- the

**Tables Written**
- [[CopySystemOptions]]

**Callers**
- [[Technical_OT_CopySystemOption]]

**Callees**
_None_


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
