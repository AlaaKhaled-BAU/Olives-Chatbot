---
type: procedure
database: Olives_BO
name: Pro_UsersCloseDate
schema: dbo
tags: [#auth, #backoffice]
reads_from:
  - [[UsersCloseDate]]
writes_to:
  - [[UsersCloseDate]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_UsersCloseDate


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads UsersCloseDate. Writes UsersCloseDate. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	= null
- @UserID	nvarchar(50)	= null
- @TrasnDateClose	smalldatetime	= null
- @cmdType nvarchar(50) = null
## Tables Read
- [[UsersCloseDate]]
## Tables Written
- [[UsersCloseDate]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[UsersCloseDate]]

**Tables Written**
- [[UsersCloseDate]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
