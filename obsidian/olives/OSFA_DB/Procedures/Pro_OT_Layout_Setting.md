---
type: procedure
database: OSFA_DB
name: Pro_OT_Layout_Setting
schema: dbo
tags: [#mobile]
reads_from:
  - [[OT_Layout_Setting]]
writes_to:
  - [[OT_Layout_Setting]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_OT_Layout_Setting


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_Layout_Setting. Writes OT_Layout_Setting. See Tables Read/Written and Callers/Callees below for the full dependency map.
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
- [[OT_Layout_Setting]]
## Tables Written
- [[OT_Layout_Setting]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_Layout_Setting]]

**Tables Written**
- [[OT_Layout_Setting]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Cross-Database
Also exists in the other database: [[Olives_BO/Procedures/Pro_OT_Layout_Setting]] (BO).

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
