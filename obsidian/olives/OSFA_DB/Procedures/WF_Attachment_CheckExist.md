---
type: procedure
database: OSFA_DB
name: WF_Attachment_CheckExist
schema: dbo
tags: [#auth, #mobile, #workflow]
reads_from:
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# WF_Attachment_CheckExist


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @TabletSysID varchar (50)
- @ErrNo SmallInt Output
- @Exist SmallInt Output
## Tables Read
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- dbo

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Workflow procedure — called automatically by the WF engine when processing approval chains. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
