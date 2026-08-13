---
type: procedure
database: OSFA_DB
name: OT_RequestToExceedPayOverBalance_Insert
schema: dbo
tags: [#inventory, #mobile, #workflow]
reads_from:
  - [[OT_RequestToExceedPayOverBalance]]
writes_to:
  - [[OT_RequestToExceedPayOverBalance]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToExceedPayOverBalance_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_RequestToExceedPayOverBalance. Writes OT_RequestToExceedPayOverBalance. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesPersonNo int
- @CustomerNo bigint
- @ReceiptAmount float
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @TabletSysID varchar(50)=null
- @ErrNo smallint output
- @NewAutoID numeric(30,0) output
- @CustomerBanalce float=0
## Tables Read
- [[OT_RequestToExceedPayOverBalance]]
## Tables Written
- [[OT_RequestToExceedPayOverBalance]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_RequestToExceedPayOverBalance]]

**Tables Written**
- [[OT_RequestToExceedPayOverBalance]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
