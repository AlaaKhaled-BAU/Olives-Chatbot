---
type: procedure
database: Olives_BO
name: Pro_OT_Layout_Setting
schema: dbo
tags: [#backoffice, #mobile]
reads_from:
  - [[SystemCodes]]
  - `dbo`
writes_to:
  - [[OT_Layout_Setting]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_OT_Layout_Setting


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SystemCodes, dbo. Writes OT_Layout_Setting. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo	smallint	= null
- @LayoutId	int	= null
- @PropertyID	int	= null
- @LayoutName	nvarchar(500)	= null
- @Description	nvarchar(500)	= null
- @Value1	nvarchar(100)	= null
- @Value2	nvarchar(100)	= null
- @cmdType nvarchar(50) = null
## Tables Read
- [[SystemCodes]]
- `dbo`
## Tables Written
- [[OT_Layout_Setting]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SystemCodes]]
- dbo

**Tables Written**
- [[OT_Layout_Setting]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Cross-Database
Also exists in the other database: [[OSFA_DB/Procedures/Pro_OT_Layout_Setting]] (OSFA).

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
