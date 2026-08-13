---
type: procedure
database: Olives_BO
name: Pro_ErrorLog_BO
schema: dbo
tags: [#backoffice, #log]
reads_from:
  - [[ErrorLog]]
writes_to:
  - [[ErrorLog]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ErrorLog_BO


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ErrorLog. Writes ErrorLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @MacAddress	nvarchar(100)	 = null
- @IPAddress	nvarchar(100)	 = null
- @PCName	nvarchar(100)	 = null
- @UserID	nvarchar(100)	 = null
- @CompanyID	smallint	 = null
- @Uri	nvarchar(500)	 = null
- @ErrorDescription	nvarchar(MAX)	 = null
- @cmdType  nvarchar(50) = null
## Tables Read
- [[ErrorLog]]
## Tables Written
- [[ErrorLog]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ErrorLog]]

**Tables Written**
- [[ErrorLog]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
