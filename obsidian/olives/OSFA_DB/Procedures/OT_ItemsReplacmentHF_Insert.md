---
type: procedure
database: OSFA_DB
name: OT_ItemsReplacmentHF_Insert
schema: dbo
tags: [#inventory, #mobile]
reads_from:
  - [[OT_ItemsReplacmentHF]]
writes_to:
  - [[OT_ItemsReplacmentHF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ItemsReplacmentHF_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_ItemsReplacmentHF. Writes OT_ItemsReplacmentHF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @VouYear smallint
- @VouNo int
- @SalesmanNo smallint
- @CustomerNo bigint
- @VouType int
- @VouDate smalldatetime
- @GPSX varchar (50)
- @GPSY varchar (50)
- @Notes varchar (200)
- @ErrNo SmallInt Output
- @TrDateTime smalldatetime = null
- @RouteID	int
## Tables Read
- [[OT_ItemsReplacmentHF]]
## Tables Written
- [[OT_ItemsReplacmentHF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_ItemsReplacmentHF]]

**Tables Written**
- [[OT_ItemsReplacmentHF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
