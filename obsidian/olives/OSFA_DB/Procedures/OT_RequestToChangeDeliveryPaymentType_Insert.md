---
type: procedure
database: OSFA_DB
name: OT_RequestToChangeDeliveryPaymentType_Insert
schema: dbo
tags: [#billing, #mobile, #order, #reference, #workflow]
reads_from:
  - [[OT_RequestToChangeDeliveryPaymentType]]
writes_to:
  - [[OT_RequestToChangeDeliveryPaymentType]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToChangeDeliveryPaymentType_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_RequestToChangeDeliveryPaymentType. Writes OT_RequestToChangeDeliveryPaymentType. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesPersonNo int
- @OriginalSalespersonNo int
- @CustomerNo bigint
- @TrTypeID smallint
- @TrTypeYear smallint
- @TrTypeNo int
- @InvoiceAmount float
- @OldPaymentType int
- @NewPaymentType int
- @IsPosted bit=0
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @ErrNo smallint output
- @NewAutoID numeric(30,0) output
## Tables Read
- [[OT_RequestToChangeDeliveryPaymentType]]
## Tables Written
- [[OT_RequestToChangeDeliveryPaymentType]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_RequestToChangeDeliveryPaymentType]]

**Tables Written**
- [[OT_RequestToChangeDeliveryPaymentType]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
