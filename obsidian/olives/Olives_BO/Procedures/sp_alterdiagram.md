---
type: procedure
database: Olives_BO
name: sp_alterdiagram
schema: dbo
tags: [#backoffice]
reads_from:
  - dds
  - sysdiagrams
writes_to:
  - sysdiagrams
called_by:
  - AS
support_relevance: high
last_verified: 2026-07-05
---
# sp_alterdiagram


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads dds, sysdiagrams. Writes sysdiagrams. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @diagramname 	sysname
- @owner_id	int	= null
- @version 	int
- @definition 	varbinary(max) ) WITH EXECUTE AS 'dbo'
## Tables Read
- dds
- sysdiagrams
## Tables Written
- sysdiagrams
## Callers
_None (no known callers)_
## Callees
- AS
## Impact / Dependencies

**Tables Read**
- dds
- sysdiagrams

**Tables Written**
- sysdiagrams

**Callers**
- AS

**Callees**
_None_


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
