---
type: procedure
database: OSFA_DB
name: OT_RequestToExceedCustomerInvoiceDueDaysInOrder_Insert
schema: dbo
tags: [#billing, #customer, #mobile, #order, #workflow]
reads_from:
  - [[OT_RequestToExceedCustomerInvoiceDueDaysInOrder]]
writes_to:
  - [[OT_RequestToExceedCustomerInvoiceDueDaysInOrder]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToExceedCustomerInvoiceDueDaysInOrder_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_RequestToExceedCustomerInvoiceDueDaysInOrder. Writes OT_RequestToExceedCustomerInvoiceDueDaysInOrder. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesPersonNo int
- @CustomerNo bigint
- @InvoiceAmount float
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @TabletSysID varchar(50)=null
- @ErrNo smallint output
- @NewAutoID numeric(30,0) output
- @Notes varchar(MAX)
## Tables Read
- [[OT_RequestToExceedCustomerInvoiceDueDaysInOrder]]
## Tables Written
- [[OT_RequestToExceedCustomerInvoiceDueDaysInOrder]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_RequestToExceedCustomerInvoiceDueDaysInOrder]]

**Tables Written**
- [[OT_RequestToExceedCustomerInvoiceDueDaysInOrder]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
