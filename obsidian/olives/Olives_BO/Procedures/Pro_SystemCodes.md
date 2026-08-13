---
type: procedure
database: Olives_BO
name: Pro_SystemCodes
schema: dbo
tags: [#backoffice, #reference]
reads_from:
  - [[SystemCodes]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SystemCodes


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SystemCodes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @SysCodeTypeID	nvarchar(100)	 = null
- @SysCode	nvarchar(100)	= null
- @Name	nvarchar(100)	= null
- @cmdType varchar(50)=null
## Tables Read
- [[SystemCodes]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SystemCodes]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
