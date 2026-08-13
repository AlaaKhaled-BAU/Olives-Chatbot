---
type: procedure
database: OSFA_DB
name: OT_ItemsReplacmentDF_Insert
schema: dbo
tags: [#inventory, #mobile]
reads_from:
  - [[OT_ItemsReplacmentDF]]
writes_to:
  - [[OT_ItemsReplacmentDF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ItemsReplacmentDF_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_ItemsReplacmentDF. Writes OT_ItemsReplacmentDF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @VouYear smallint
- @VouNo int
- @VouType int
- @LineSerial int
- @ItemNo varchar (200)
- @Unit varchar (100)
- @Qty money
- @Notes nvarchar(300)=''
- @ErrNo SmallInt Output
## Tables Read
- [[OT_ItemsReplacmentDF]]
## Tables Written
- [[OT_ItemsReplacmentDF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_ItemsReplacmentDF]]

**Tables Written**
- [[OT_ItemsReplacmentDF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
