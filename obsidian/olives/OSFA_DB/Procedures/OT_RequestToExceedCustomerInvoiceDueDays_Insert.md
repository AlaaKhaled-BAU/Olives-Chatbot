---
type: procedure
database: OSFA_DB
name: OT_RequestToExceedCustomerInvoiceDueDays_Insert
schema: dbo
tags: [#billing, #customer, #mobile, #workflow]
reads_from:
  - [[OT_RequestToExceedCustomerInvoiceDueDays]]
writes_to:
  - [[OT_RequestToExceedCustomerInvoiceDueDays]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToExceedCustomerInvoiceDueDays_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_RequestToExceedCustomerInvoiceDueDays. Writes OT_RequestToExceedCustomerInvoiceDueDays. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesPersonNo int
- @CustomerNo bigint
- @InvoiceAmount float
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @TabletSysID varchar(50)=null
- @ErrNo smallint output
## Tables Read
- [[OT_RequestToExceedCustomerInvoiceDueDays]]
## Tables Written
- [[OT_RequestToExceedCustomerInvoiceDueDays]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_RequestToExceedCustomerInvoiceDueDays]]

**Tables Written**
- [[OT_RequestToExceedCustomerInvoiceDueDays]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
