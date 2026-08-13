---
type: procedure
database: OSFA_DB
name: OT_RequestToMakeZeroAmountInvoice_Insert
schema: dbo
tags: [#billing, #mobile, #workflow]
reads_from:
  - [[OT_RequestToMakeZeroAmountInvoice]]
writes_to:
  - [[OT_RequestToMakeZeroAmountInvoice]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToMakeZeroAmountInvoice_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_RequestToMakeZeroAmountInvoice. Writes OT_RequestToMakeZeroAmountInvoice. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesPersonNo int
- @CustomerNo bigint
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @Notes nvarchar(4000)
- @TabletSysID varchar(50)=null
- @ErrNo smallint output
- @NewAutoID numeric(30,0) output
## Tables Read
- [[OT_RequestToMakeZeroAmountInvoice]]
## Tables Written
- [[OT_RequestToMakeZeroAmountInvoice]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_RequestToMakeZeroAmountInvoice]]

**Tables Written**
- [[OT_RequestToMakeZeroAmountInvoice]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
