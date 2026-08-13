---
type: procedure
database: OSFA_DB
name: OT_RequestToExceedCustomerCreditLimitInOrder_Insert
schema: dbo
tags: [#billing, #customer, #mobile, #order, #workflow]
reads_from:
  - [[OT_RequestToExceedCustomerCreditLimitInOrder]]
writes_to:
  - [[OT_RequestToExceedCustomerCreditLimitInOrder]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToExceedCustomerCreditLimitInOrder_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_RequestToExceedCustomerCreditLimitInOrder. Writes OT_RequestToExceedCustomerCreditLimitInOrder. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesPersonNo int
- @CustomerNo bigint
- @InvoiceAmount float
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @TabletSysID varchar(50)=null
- @CustomerCreditLimit float =0
- @CustomerBanalce float=0
- @CustomerChqBanalce float =0
- @ExceedAmount float=0
- @ErrNo smallint output
- @NewAutoID numeric(30,0) output
## Tables Read
- [[OT_RequestToExceedCustomerCreditLimitInOrder]]
## Tables Written
- [[OT_RequestToExceedCustomerCreditLimitInOrder]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_RequestToExceedCustomerCreditLimitInOrder]]

**Tables Written**
- [[OT_RequestToExceedCustomerCreditLimitInOrder]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
