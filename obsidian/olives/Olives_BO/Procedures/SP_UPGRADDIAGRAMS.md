---
type: procedure
database: Olives_BO
name: SP_UPGRADDIAGRAMS
schema: dbo
tags: [#backoffice]
reads_from:
  - dtproperties
  - sysdiagrams
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# SP_UPGRADDIAGRAMS


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads dtproperties, sysdiagrams. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
_None_
## Tables Read
- dtproperties
- sysdiagrams
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- dtproperties
- sysdiagrams

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
