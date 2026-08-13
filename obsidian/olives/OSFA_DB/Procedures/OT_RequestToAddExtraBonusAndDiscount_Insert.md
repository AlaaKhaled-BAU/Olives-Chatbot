---
type: procedure
database: OSFA_DB
name: OT_RequestToAddExtraBonusAndDiscount_Insert
schema: dbo
tags: [#billing, #mobile, #workflow]
reads_from:
  - [[OT_RequestToAddExtraBonusAndDiscount]]
writes_to:
  - [[OT_RequestToAddExtraBonusAndDiscount]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToAddExtraBonusAndDiscount_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_RequestToAddExtraBonusAndDiscount. Writes OT_RequestToAddExtraBonusAndDiscount. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesPersonNo int
- @TrType int
- @CustomerNo bigint
- @ApprovePercent float
- @InvoiceAmount float
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @Notes nvarchar(Max)
- @TabletSysID varchar(50)=null
- @ErrNo smallint output
- @NewAutoID numeric(30,0) output
## Tables Read
- [[OT_RequestToAddExtraBonusAndDiscount]]
## Tables Written
- [[OT_RequestToAddExtraBonusAndDiscount]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_RequestToAddExtraBonusAndDiscount]]

**Tables Written**
- [[OT_RequestToAddExtraBonusAndDiscount]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
