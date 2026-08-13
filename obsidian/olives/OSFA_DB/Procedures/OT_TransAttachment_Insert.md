---
type: procedure
database: OSFA_DB
name: OT_TransAttachment_Insert
schema: dbo
tags: [#mobile]
reads_from:
  - `dbo`
writes_to:
  - OT_TransAttachment
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_TransAttachment_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads dbo. Writes OT_TransAttachment. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @TransactionTypeID smallint
- @TransactionYear smallint
- @TransactionNo int
- @LineSerial int
- @TabletSysID varchar (50)
- @ImageData image
- @ErrNo SmallInt Output
- @FileName	varchar(500)
- @Ref1	varchar(500)
- @Ref2	varchar(500)
## Tables Read
- `dbo`
## Tables Written
- OT_TransAttachment
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- dbo

**Tables Written**
- OT_TransAttachment

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
