---
type: procedure
database: OSFA_DB
name: OT_RequestToExceedInvoiceCount_Insert
schema: dbo
tags: [#billing, #mobile, #workflow]
reads_from:
  - [[OT_RequestToExceedInvoiceCount]]
writes_to:
  - [[OT_RequestToExceedInvoiceCount]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToExceedInvoiceCount_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_RequestToExceedInvoiceCount. Writes OT_RequestToExceedInvoiceCount. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesPersonNo int
- @CustomerNo bigint
- @InvoiceCount float
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @Notes nvarchar(4000)
- @TabletSysID varchar(50)=null
- @ErrNo smallint output
- @NewAutoID numeric(30,0) output
## Tables Read
- [[OT_RequestToExceedInvoiceCount]]
## Tables Written
- [[OT_RequestToExceedInvoiceCount]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_RequestToExceedInvoiceCount]]

**Tables Written**
- [[OT_RequestToExceedInvoiceCount]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
