---
type: procedure
database: OSFA_DB
name: OT_RequestToChangeInvoicePaymentType_Insert
schema: dbo
tags: [#billing, #legal, #mobile, #reference, #workflow]
reads_from:
  - [[OT_RequestToChangeInvoicePaymentType]]
writes_to:
  - [[OT_RequestToChangeInvoicePaymentType]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToChangeInvoicePaymentType_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_RequestToChangeInvoicePaymentType. Writes OT_RequestToChangeInvoicePaymentType. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesPersonNo int
- @CustomerNo bigint
- @InvoiceAmount float
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @TabletSysID varchar(50)=null
- @InvDueDays int=null
- @ErrNo smallint output
## Tables Read
- [[OT_RequestToChangeInvoicePaymentType]]
## Tables Written
- [[OT_RequestToChangeInvoicePaymentType]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_RequestToChangeInvoicePaymentType]]

**Tables Written**
- [[OT_RequestToChangeInvoicePaymentType]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
