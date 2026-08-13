---
type: procedure
database: OSFA_DB
name: WF_Attachment_Insert
schema: dbo
tags: [#auth, #mobile, #workflow]
reads_from:
  - `dbo`
writes_to:
  - WF_Attachment
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# WF_Attachment_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads dbo. Writes WF_Attachment. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FunctionID smallint
- @TabletSysID varchar (50)
- @ImageData image
- @ErrNo SmallInt Output
- @FileName	varchar(500)
- @Ref1	varchar(500)
- @Ref2	varchar(500)
## Tables Read
- `dbo`
## Tables Written
- WF_Attachment
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- dbo

**Tables Written**
- WF_Attachment

**Callers**
_None_

**Callees**
_None_


## When to Run This

Workflow procedure — called automatically by the WF engine when processing approval chains. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
