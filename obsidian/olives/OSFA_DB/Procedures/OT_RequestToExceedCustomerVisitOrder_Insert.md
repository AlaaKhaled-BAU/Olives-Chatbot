---
type: procedure
database: OSFA_DB
name: OT_RequestToExceedCustomerVisitOrder_Insert
schema: dbo
tags: [#customer, #mobile, #order, #sales, #workflow]
reads_from:
  - [[OT_RequestToExceedCustomerVisitOrder]]
writes_to:
  - [[OT_RequestToExceedCustomerVisitOrder]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToExceedCustomerVisitOrder_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_RequestToExceedCustomerVisitOrder. Writes OT_RequestToExceedCustomerVisitOrder. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesPersonNo int
- @CustomerNo bigint
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @Notes nvarchar(50)
- @ErrNo smallint output
- @NewAutoID numeric(30,0) output
## Tables Read
- [[OT_RequestToExceedCustomerVisitOrder]]
## Tables Written
- [[OT_RequestToExceedCustomerVisitOrder]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_RequestToExceedCustomerVisitOrder]]

**Tables Written**
- [[OT_RequestToExceedCustomerVisitOrder]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
