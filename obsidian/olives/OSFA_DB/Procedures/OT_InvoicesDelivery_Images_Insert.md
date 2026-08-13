---
type: procedure
database: OSFA_DB
name: OT_InvoicesDelivery_Images_Insert
schema: dbo
tags: [#billing, #mobile, #order]
reads_from:
  - [[OT_ErrorLog]]
  - `dbo`
writes_to:
  - [[OT_ErrorLog]]
  - OT_InvoicesDelivery_Images
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_InvoicesDelivery_Images_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_ErrorLog, dbo. Writes OT_ErrorLog, OT_InvoicesDelivery_Images. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @TransactionTypeID smallint
- @TransactionYear smallint
- @TransactionNo int
- @TabletSysID varchar (50)
- @ImageData image
- @ErrNo SmallInt Output
## Tables Read
- [[OT_ErrorLog]]
- `dbo`
## Tables Written
- [[OT_ErrorLog]]
- OT_InvoicesDelivery_Images
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_ErrorLog]]
- dbo

**Tables Written**
- [[OT_ErrorLog]]
- OT_InvoicesDelivery_Images

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
