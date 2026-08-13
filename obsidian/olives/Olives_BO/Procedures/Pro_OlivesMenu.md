---
type: procedure
database: Olives_BO
name: Pro_OlivesMenu
schema: dbo
tags: [#backoffice]
reads_from:
  - [[ClientsActive]]
  - [[OlivesMenu]]
  - [[OlivesPages]]
  - [[OlivesUserPermissions]]
  - [[UsersFavoriteMenu]]
writes_to:
  - [[OlivesMenu]]
  - [[OlivesPages]]
  - [[OlivesUserPermissions]]
  - [[UsersFavoriteMenu]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_OlivesMenu


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, OlivesMenu, OlivesPages, OlivesUserPermissions, UsersFavoriteMenu. Writes OlivesMenu, OlivesPages, OlivesUserPermissions, UsersFavoriteMenu. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @UserID nvarchar(50) = null
- @cmdType varchar(50) ='Select All With Permissions'
- @Lang varchar(50) = null
- @ArName varchar(200) = null
- @EngName varchar(200) = null
- @UrlName varchar(100) = 'custom'
- @PrID int = null
## Tables Read
- [[ClientsActive]]
- [[OlivesMenu]]
- [[OlivesPages]]
- [[OlivesUserPermissions]]
- [[UsersFavoriteMenu]]
## Tables Written
- [[OlivesMenu]]
- [[OlivesPages]]
- [[OlivesUserPermissions]]
- [[UsersFavoriteMenu]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[OlivesMenu]]
- [[OlivesPages]]
- [[OlivesUserPermissions]]
- [[UsersFavoriteMenu]]

**Tables Written**
- [[OlivesMenu]]
- [[OlivesPages]]
- [[OlivesUserPermissions]]
- [[UsersFavoriteMenu]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
