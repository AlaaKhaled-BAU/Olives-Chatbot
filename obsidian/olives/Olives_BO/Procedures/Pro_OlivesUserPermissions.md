---
type: procedure
database: Olives_BO
name: Pro_OlivesUserPermissions
schema: dbo
tags: [#auth, #backoffice, #integration]
reads_from:
  - [[OlivesMenu]]
  - [[OlivesPages]]
  - [[OlivesUserPermissions]]
  - [[Users]]
  - `dbo`
writes_to:
  - [[OlivesUserPermissions]]
  - OlivesUserPermissionsLog
  - WHERE
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_OlivesUserPermissions


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads OlivesMenu, OlivesPages, OlivesUserPermissions, Users, dbo. Writes OlivesUserPermissions, OlivesUserPermissionsLog, WHERE. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=null
- @UserID nvarchar(50)=null
- @PrID int=null
- @CanAccess bit=null
- @CanAdd bit=null
- @CanEdit bit=null
- @CanDelete bit=null
- @FromUser nvarchar(50)=null
- @ToUser nvarchar(50)=null
- @cmdType varchar(50)=null
- @ID int = Null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
- @UserIDLog nvarchar(100)=null
## Tables Read
- [[OlivesMenu]]
- [[OlivesPages]]
- [[OlivesUserPermissions]]
- [[Users]]
- `dbo`
## Tables Written
- [[OlivesUserPermissions]]
- OlivesUserPermissionsLog
- WHERE
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OlivesMenu]]
- [[OlivesPages]]
- [[OlivesUserPermissions]]
- [[Users]]
- dbo

**Tables Written**
- [[OlivesUserPermissions]]
- OlivesUserPermissionsLog
- WHERE

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
