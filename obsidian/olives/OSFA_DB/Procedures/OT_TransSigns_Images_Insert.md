---
type: procedure
database: OSFA_DB
name: OT_TransSigns_Images_Insert
schema: dbo
tags: [#mobile]
reads_from:
  - [[OT_Cust_Survey_Answers]]
  - `dbo`
writes_to:
  - OT_TransSigns_Images
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_TransSigns_Images_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_Cust_Survey_Answers, dbo. Writes OT_TransSigns_Images. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @TransactionTypeID smallint
- @TransactionYear smallint
- @TransactionNo int
- @LineSerial int
- @TabletSysID varchar (50)
- @ImageData image
- @ErrNo SmallInt Output
## Tables Read
- [[OT_Cust_Survey_Answers]]
- `dbo`
## Tables Written
- OT_TransSigns_Images
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_Cust_Survey_Answers]]
- dbo

**Tables Written**
- OT_TransSigns_Images

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
