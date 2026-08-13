---
type: procedure
database: OSFA_DB
name: OT_TransSuggestedItems_Insert
schema: dbo
tags: [#inventory, #mobile]
reads_from:
  - [[OT_TransSuggestedItems]]
writes_to:
  - [[OT_TransSuggestedItems]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_TransSuggestedItems_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_TransSuggestedItems. Writes OT_TransSuggestedItems. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @VouType smallint
- @VouYear smallint
- @VouNo int
- @ItemNo varchar (100)
- @Unit varchar (100)
- @Qty float
- @UnitPrice float
- @Ref1 varchar (100)
- @Ref2 varchar (100)
- @ErrNo SmallInt Output
## Tables Read
- [[OT_TransSuggestedItems]]
## Tables Written
- [[OT_TransSuggestedItems]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_TransSuggestedItems]]

**Tables Written**
- [[OT_TransSuggestedItems]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
