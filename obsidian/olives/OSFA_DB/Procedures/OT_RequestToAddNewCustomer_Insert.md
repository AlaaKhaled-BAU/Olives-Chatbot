---
type: procedure
database: OSFA_DB
name: OT_RequestToAddNewCustomer_Insert
schema: dbo
tags: [#customer, #mobile, #workflow]
reads_from:
  - [[OT_RequestToAddNewCustomer]]
writes_to:
  - [[OT_RequestToAddNewCustomer]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToAddNewCustomer_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_RequestToAddNewCustomer. Writes OT_RequestToAddNewCustomer. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesPersonNo int
- @Notes nvarchar(max)
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @TabletSysID varchar(50)=null
- @ErrNo smallint output
- @NewAutoID numeric(30,0) output
## Tables Read
- [[OT_RequestToAddNewCustomer]]
## Tables Written
- [[OT_RequestToAddNewCustomer]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_RequestToAddNewCustomer]]

**Tables Written**
- [[OT_RequestToAddNewCustomer]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
