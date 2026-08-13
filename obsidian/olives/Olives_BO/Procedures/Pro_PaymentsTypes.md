---
type: procedure
database: Olives_BO
name: Pro_PaymentsTypes
schema: dbo
tags: [#backoffice, #billing, #reference]
reads_from:
  - [[PaymentsTypes]]
writes_to:
  - [[PaymentsTypes]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_PaymentsTypes


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads PaymentsTypes. Writes PaymentsTypes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID smallint = null
- @Name nvarchar (200)=null
- @ShortName nvarchar (100)=null
- @Reference1 nvarchar (40)=null
- @Reference2 nvarchar (40)=null
- @cmdType varchar(50)=null
## Tables Read
- [[PaymentsTypes]]
## Tables Written
- [[PaymentsTypes]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[PaymentsTypes]]

**Tables Written**
- [[PaymentsTypes]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
