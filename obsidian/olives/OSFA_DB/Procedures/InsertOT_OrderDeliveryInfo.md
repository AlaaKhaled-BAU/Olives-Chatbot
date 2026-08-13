---
type: procedure
database: OSFA_DB
name: InsertOT_OrderDeliveryInfo
schema: dbo
tags: [#mobile, #order]
reads_from:
  - [[OT_OrderDeliveryInfo]]
writes_to:
  - [[OT_OrderDeliveryInfo]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# InsertOT_OrderDeliveryInfo


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_OrderDeliveryInfo. Writes OT_OrderDeliveryInfo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @OrderYear int
- @OrderNo int
- @PoNo nvarchar(50)
- @CustName nvarchar(100)
- @CustAddress nvarchar(200)
- @MobNo nvarchar(50)
- @TelNo nvarchar(50)
- @Notes nvarchar(max)
- @Ref1 nvarchar(50)
- @Ref2 nvarchar(50)
- @ErrNo SmallInt Output
## Tables Read
- [[OT_OrderDeliveryInfo]]
## Tables Written
- [[OT_OrderDeliveryInfo]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_OrderDeliveryInfo]]

**Tables Written**
- [[OT_OrderDeliveryInfo]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
