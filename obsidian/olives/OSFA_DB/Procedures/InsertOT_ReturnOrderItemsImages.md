---
type: procedure
database: OSFA_DB
name: InsertOT_ReturnOrderItemsImages
schema: dbo
tags: [#inventory, #mobile, #order]
reads_from:
  - `dbo`
writes_to:
  - OT_ReturnOrderItemsImages
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# InsertOT_ReturnOrderItemsImages


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads dbo. Writes OT_ReturnOrderItemsImages. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint =1
- @VouYear smallint =1
- @VouNo int=1
- @ItemNo nvarchar(100) ='11'
- @ImageData image=null
## Tables Read
- `dbo`
## Tables Written
- OT_ReturnOrderItemsImages
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- dbo

**Tables Written**
- OT_ReturnOrderItemsImages

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
