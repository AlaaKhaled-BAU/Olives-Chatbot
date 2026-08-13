---
type: procedure
database: OSFA_DB
name: OT_OrderDeliveryInfo_UpdateAttach
schema: dbo
tags: [#mobile, #order]
reads_from:
  - [[OT_OrderDeliveryInfo]]
  - `dbo`
writes_to:
  - [[OrdersDeliveryInfo]]
  - [[OT_OrderDeliveryInfo]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_OrderDeliveryInfo_UpdateAttach


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_OrderDeliveryInfo, dbo. Writes OrdersDeliveryInfo, OT_OrderDeliveryInfo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @OrderYear smallint
- @OrderNo int
- @FileExt nvarchar(10)
## Tables Read
- [[OT_OrderDeliveryInfo]]
- `dbo`
## Tables Written
- [[OrdersDeliveryInfo]]
- [[OT_OrderDeliveryInfo]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_OrderDeliveryInfo]]
- dbo

**Tables Written**
- [[OrdersDeliveryInfo]]
- [[OT_OrderDeliveryInfo]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
