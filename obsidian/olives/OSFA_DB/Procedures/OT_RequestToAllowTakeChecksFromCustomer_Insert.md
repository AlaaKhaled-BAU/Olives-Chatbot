---
type: procedure
database: OSFA_DB
name: OT_RequestToAllowTakeChecksFromCustomer_Insert
schema: dbo
tags: [#customer, #mobile, #workflow]
reads_from:
  - [[OT_RequestToAllowTakeChecksFromCustomer]]
writes_to:
  - [[OT_RequestToAllowTakeChecksFromCustomer]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToAllowTakeChecksFromCustomer_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_RequestToAllowTakeChecksFromCustomer. Writes OT_RequestToAllowTakeChecksFromCustomer. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesPersonNo int
- @CustomerNo bigint
- @ReceiptAmount float
- @ChecksInfo nvarchar(max)
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @TabletSysID varchar(50)=null
- @ErrNo smallint output
- @NewAutoID numeric(30,0) output
## Tables Read
- [[OT_RequestToAllowTakeChecksFromCustomer]]
## Tables Written
- [[OT_RequestToAllowTakeChecksFromCustomer]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_RequestToAllowTakeChecksFromCustomer]]

**Tables Written**
- [[OT_RequestToAllowTakeChecksFromCustomer]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
