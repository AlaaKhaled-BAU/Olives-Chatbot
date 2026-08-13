---
type: procedure
database: Olives_BO
name: OT_ImportCompetitveItemsData
schema: dbo
tags: [#backoffice, #inventory, #mobile]
reads_from:
  - Header
  - [[ProspectiveCustomers]]
  - `dbo`
writes_to:
  - [[CompetitveItemsDataDF]]
  - [[CompetitveItemsDataHF]]
  - [[OT_CompetitveItemsDataHF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportCompetitveItemsData


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Header, ProspectiveCustomers, dbo. Writes CompetitveItemsDataDF, CompetitveItemsDataHF, OT_CompetitveItemsDataHF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- Header
- [[ProspectiveCustomers]]
- `dbo`
## Tables Written
- [[CompetitveItemsDataDF]]
- [[CompetitveItemsDataHF]]
- [[OT_CompetitveItemsDataHF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Header
- [[ProspectiveCustomers]]
- dbo

**Tables Written**
- [[CompetitveItemsDataDF]]
- [[CompetitveItemsDataHF]]
- [[OT_CompetitveItemsDataHF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
