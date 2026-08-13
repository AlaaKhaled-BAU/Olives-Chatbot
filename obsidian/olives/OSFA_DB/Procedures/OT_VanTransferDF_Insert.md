---
type: procedure
database: OSFA_DB
name: OT_VanTransferDF_Insert
schema: dbo
tags: [#mobile, #order]
reads_from:
  - [[OT_VanTransferDF]]
writes_to:
  - [[OT_VanTransferDF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_VanTransferDF_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_VanTransferDF. Writes OT_VanTransferDF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @OrderYear smallint
- @OrderNo int
- @SalesmanNo int
- @ItemNo varchar (100)
- @UnitCode varchar (50)
- @Qty money
- @Notes nvarchar(300)=''
- @ErrNo SmallInt Output
## Tables Read
- [[OT_VanTransferDF]]
## Tables Written
- [[OT_VanTransferDF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_VanTransferDF]]

**Tables Written**
- [[OT_VanTransferDF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
