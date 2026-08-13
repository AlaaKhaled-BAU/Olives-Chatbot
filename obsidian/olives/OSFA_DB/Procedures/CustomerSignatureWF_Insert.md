---
type: procedure
database: OSFA_DB
name: CustomerSignatureWF_Insert
schema: dbo
tags: [#auth, #customer, #mobile, #workflow]
reads_from:
  - `dbo`
writes_to:
  - CustomerSignatureWF
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# CustomerSignatureWF_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads dbo. Writes CustomerSignatureWF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=0
- @SID bigint=0
- @SalesmanNo int=0
- @ImageData image=null
## Tables Read
- `dbo`
## Tables Written
- CustomerSignatureWF
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- dbo

**Tables Written**
- CustomerSignatureWF

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
