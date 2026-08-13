---
type: procedure
database: OSFA_DB
name: OT_ConsOrderDF_Insert
schema: dbo
tags: [#mobile, #order]
reads_from:
  - [[OT_ConsOrderDF]]
writes_to:
  - [[OT_ConsOrderDF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ConsOrderDF_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_ConsOrderDF. Writes OT_ConsOrderDF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @OrderYear smallint
- @OrderNo int
- @ItemNo varchar (200)
- @Qty money
- @UnitCode varchar (100)
- @VouType int=1
- @Notes nvarchar(300) = ''
- @ErrNo SmallInt Output
## Tables Read
- [[OT_ConsOrderDF]]
## Tables Written
- [[OT_ConsOrderDF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_ConsOrderDF]]

**Tables Written**
- [[OT_ConsOrderDF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
