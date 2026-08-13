---
type: procedure
database: OSFA_DB
name: OT_Hakkak_ShipmentOrders
schema: dbo
tags: [#mobile, #order]
reads_from:
  - `dbo`
writes_to:
  - ShippingOrderAttach
  - ShippingOrderDF
  - ShippingOrderSman
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_Hakkak_ShipmentOrders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads dbo. Writes ShippingOrderAttach, ShippingOrderDF, ShippingOrderSman. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CmdType nvarchar(500) = null
- @CompNo smallint = null
- @SalesmanNo int = null
- @ID int = null
- @ShipOrderNo nvarchar(150) = null
- @Serial int = null
- @CustNumber bigint = null
- @ItemNo nvarchar(120) = null
- @QtyRec float = null
- @TransFees float = null
- @ManifestNo nvarchar(120) = null
- @Notes nvarchar(200) = null
- @AttachName nvarchar(150) = null
- @AttachLink nvarchar(max) = null
- @EditID int = null
## Tables Read
- `dbo`
## Tables Written
- ShippingOrderAttach
- ShippingOrderDF
- ShippingOrderSman
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- dbo

**Tables Written**
- ShippingOrderAttach
- ShippingOrderDF
- ShippingOrderSman

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
