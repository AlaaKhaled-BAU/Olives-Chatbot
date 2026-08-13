---
type: procedure
database: OSFA_DB
name: OT_ItemsUnitsBarcodes_Insert
schema: dbo
tags: [#inventory, #mobile, #reference]
reads_from:
  - `dbo`
writes_to:
  - [[ItemsBarcodes]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ItemsUnitsBarcodes_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads dbo. Writes ItemsBarcodes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @ItemCode nvarchar(100)
- @Unit nvarchar(100)
- @Barcode nvarchar(100)
## Tables Read
- `dbo`
## Tables Written
- [[ItemsBarcodes]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- dbo

**Tables Written**
- [[ItemsBarcodes]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
