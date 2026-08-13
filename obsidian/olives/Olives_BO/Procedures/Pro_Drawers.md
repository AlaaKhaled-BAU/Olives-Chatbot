---
type: procedure
database: Olives_BO
name: Pro_Drawers
schema: dbo
tags: [#backoffice]
reads_from:
  - [[Customers]]
  - [[Drawers]]
  - `dbo`
writes_to:
  - [[Drawers]]
  - DrawersLog
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_Drawers


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Drawers, dbo. Writes Drawers, DrawersLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID smallint = null
- @Name nvarchar (200)=null
- @ShortName nvarchar (100)=null
- @Reference1 nvarchar (40)=null
- @Reference2 nvarchar (40)=null
- @CustomerID bigint = null
- @cmdType varchar(50)=null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
- @UserID nvarchar(100)=null
## Tables Read
- [[Customers]]
- [[Drawers]]
- `dbo`
## Tables Written
- [[Drawers]]
- DrawersLog
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[Drawers]]
- dbo

**Tables Written**
- [[Drawers]]
- DrawersLog

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
