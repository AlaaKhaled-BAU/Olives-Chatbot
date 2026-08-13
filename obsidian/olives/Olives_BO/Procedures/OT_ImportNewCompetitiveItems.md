---
type: procedure
database: Olives_BO
name: OT_ImportNewCompetitiveItems
schema: dbo
tags: [#backoffice, #inventory, #mobile]
reads_from:
  - [[NewCompetitiveItems]]
  - `dbo`
writes_to:
  - [[NewCompetitiveItems]]
  - [[OT_NewCompetitiveItems]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportNewCompetitiveItems


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads NewCompetitiveItems, dbo. Writes NewCompetitiveItems, OT_NewCompetitiveItems. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[NewCompetitiveItems]]
- `dbo`
## Tables Written
- [[NewCompetitiveItems]]
- [[OT_NewCompetitiveItems]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[NewCompetitiveItems]]
- dbo

**Tables Written**
- [[NewCompetitiveItems]]
- [[OT_NewCompetitiveItems]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
