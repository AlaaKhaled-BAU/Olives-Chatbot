---
type: procedure
database: OSFA_DB
name: OT_RequestToExceedCustomerCreditLimit_Insert
schema: dbo
tags: [#billing, #customer, #mobile, #workflow]
reads_from:
  - [[OT_RequestToExceedCustomerCreditLimit]]
writes_to:
  - [[OT_RequestToExceedCustomerCreditLimit]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToExceedCustomerCreditLimit_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_RequestToExceedCustomerCreditLimit. Writes OT_RequestToExceedCustomerCreditLimit. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesPersonNo int
- @CustomerNo bigint
- @InvoiceAmount float
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @Notes nvarchar(4000)
- @TabletSysID varchar(50)=null
- @CustomerCreditLimit float =0
- @CustomerBanalce float=0
- @CustomerChqBanalce float =0
- @ExceedAmount float=0
- @ErrNo smallint output
## Tables Read
- [[OT_RequestToExceedCustomerCreditLimit]]
## Tables Written
- [[OT_RequestToExceedCustomerCreditLimit]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_RequestToExceedCustomerCreditLimit]]

**Tables Written**
- [[OT_RequestToExceedCustomerCreditLimit]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
