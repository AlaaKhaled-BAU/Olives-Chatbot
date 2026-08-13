---
type: procedure
database: Olives_BO
name: Technical_Activate_DeactivateLoginbybarcode_Atieh
schema: dbo
tags: [#auth, #backoffice, #inventory, #log, #reference]
reads_from:
  - `dbo`
writes_to:
  - [[CopySystemOptions]]
called_by:
  - OSFA_DB
support_relevance: high
last_verified: 2026-07-05
---
# Technical_Activate_DeactivateLoginbybarcode_Atieh


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads dbo. Writes CopySystemOptions. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @SourceSalesman int
- @distinationSalesman int
## Tables Read
- `dbo`
## Tables Written
- [[CopySystemOptions]]
## Callers
_None (no known callers)_
## Callees
- OSFA_DB
## Impact / Dependencies

**Tables Read**
- dbo

**Tables Written**
- [[CopySystemOptions]]

**Callers**
- OSFA_DB

**Callees**
_None_


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
