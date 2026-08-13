---
type: procedure
database: OSFA_DB
name: OT_GPSLogImages_Insert
schema: dbo
tags: [#gps, #log, #mobile]
reads_from:
  - `dbo`
writes_to:
  - OT_GPSLogImages
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_GPSLogImages_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads dbo. Writes OT_GPSLogImages. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @TabletSysID varchar (50)
- @ImageData image
- @ErrNo SmallInt Output
## Tables Read
- `dbo`
## Tables Written
- OT_GPSLogImages
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- dbo

**Tables Written**
- OT_GPSLogImages

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
- [[OSFA_DB/Procedures/OT_DirectInvoice]]
