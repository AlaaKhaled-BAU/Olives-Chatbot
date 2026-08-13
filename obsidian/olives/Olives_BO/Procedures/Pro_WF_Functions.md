---
type: procedure
database: Olives_BO
name: Pro_WF_Functions
schema: dbo
tags: [#auth, #backoffice, #workflow]
reads_from:
  - [[WF_Functions]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_WF_Functions


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads WF_Functions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @ID smallint = null
- @ArName nvarchar (200)=null
- @EngName nvarchar (200)=null
- @cmdType varchar(50)=null
## Tables Read
- [[WF_Functions]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[WF_Functions]]

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
