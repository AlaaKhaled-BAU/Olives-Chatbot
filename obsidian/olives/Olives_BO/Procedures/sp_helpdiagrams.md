---
type: procedure
database: Olives_BO
name: sp_helpdiagrams
schema: dbo
tags: [#backoffice]
reads_from:
  - sysdiagrams
writes_to:
called_by:
  - AS
support_relevance: high
last_verified: 2026-07-05
---
# sp_helpdiagrams


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads sysdiagrams. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @diagramname sysname = NULL
- @owner_id int = NULL ) WITH EXECUTE AS N'dbo'
## Tables Read
- sysdiagrams
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- AS
## Impact / Dependencies

**Tables Read**
- sysdiagrams

**Tables Written**
_None_

**Callers**
- AS

**Callees**
_None_


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
