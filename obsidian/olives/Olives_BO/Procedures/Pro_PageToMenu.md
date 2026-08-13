---
type: procedure
database: Olives_BO
name: Pro_PageToMenu
schema: dbo
tags: [#backoffice]
reads_from:
writes_to:
  - OlivesMenu
  - OlivesPages
  - OlivesUserPermissions
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Pro_PageToMenu

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — writes 3. See sections below for the full dependency map.
## Parameters
- @ArName nvarchar(255)
- @EngName nvarchar(255)
- @PageName nvarchar(255)
- @SubParent int
- @Parent int
- @MasterMenu int
- @CompanyID int
- @UserName nvarchar(100)
- @SearchTerm nvarchar(255)
- @Master int
- @cmdType nvarchar(200)
## Tables Read
_None_
## Tables Written
- [[OlivesMenu]]
- [[OlivesPages]]
- [[OlivesUserPermissions]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
_None_
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
