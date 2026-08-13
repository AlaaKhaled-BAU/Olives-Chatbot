---
type: procedure
database: Olives_BO
name: Pro_SystemCodes_Manage
schema: dbo
tags: [#backoffice, #reference]
reads_from:
  - [[SystemCodes]]
writes_to:
  - [[SystemCodes]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SystemCodes_Manage


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SystemCodes. Writes SystemCodes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @cmdType varchar(50)=null
- @SysCodeTypeID nvarchar(100) = null
- @SysCode  nvarchar(100) = null
- @Name  nvarchar(100) = null
- @CanEdit bit = null
## Tables Read
- [[SystemCodes]]
## Tables Written
- [[SystemCodes]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SystemCodes]]

**Tables Written**
- [[SystemCodes]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
