---
type: procedure
database: OSFA_DB
name: OT_TransBatchsInfo_Insert
schema: dbo
tags: [#inventory, #mobile]
reads_from:
  - [[OT_TransBatchsInfo]]
writes_to:
  - [[OT_TransBatchsInfo]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_TransBatchsInfo_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_TransBatchsInfo. Writes OT_TransBatchsInfo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @VouType smallint
- @VouYear smallint
- @VouNo int
- @ItemNo varchar (100)
- @Unit varchar (50)
- @BatchNo varchar (100)
- @ExpireDate smalldatetime
- @Qty money
- @Bonus money
- @ErrNo SmallInt Output
## Tables Read
- [[OT_TransBatchsInfo]]
## Tables Written
- [[OT_TransBatchsInfo]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_TransBatchsInfo]]

**Tables Written**
- [[OT_TransBatchsInfo]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
