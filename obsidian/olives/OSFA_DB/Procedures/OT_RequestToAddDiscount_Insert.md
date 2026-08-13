---
type: procedure
database: OSFA_DB
name: OT_RequestToAddDiscount_Insert
schema: dbo
tags: [#billing, #mobile, #workflow]
reads_from:
  - [[OT_RequestToAddDiscount]]
writes_to:
  - [[OT_RequestToAddDiscount]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToAddDiscount_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_RequestToAddDiscount. Writes OT_RequestToAddDiscount. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesPersonNo int
- @CustomerNo bigint
- @InvoiceAmount float
- @DiscountAmount float
- @DiscountPercent float
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @Notes nvarchar(Max)
- @TabletSysID varchar(50)=null
- @ErrNo smallint output
## Tables Read
- [[OT_RequestToAddDiscount]]
## Tables Written
- [[OT_RequestToAddDiscount]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_RequestToAddDiscount]]

**Tables Written**
- [[OT_RequestToAddDiscount]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
