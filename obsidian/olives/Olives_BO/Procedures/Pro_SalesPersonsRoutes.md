---
type: procedure
database: Olives_BO
name: Pro_SalesPersonsRoutes
schema: dbo
tags: [#backoffice, #gps, #sales]
reads_from:
  - [[RoutesInformation]]
  - [[SalesPersonsRoutes]]
writes_to:
  - [[SalesPersonsRoutes]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesPersonsRoutes


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads RoutesInformation, SalesPersonsRoutes. Writes SalesPersonsRoutes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @PositionsID int = null
- @WeekDay int = null
- @Week1 int = null
- @Week2 int = null
- @Week3 int = null
- @Week4 int = null
- @Day nvarchar(50) = null
- @cmdType varchar(50)=null
## Tables Read
- [[RoutesInformation]]
- [[SalesPersonsRoutes]]
## Tables Written
- [[SalesPersonsRoutes]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[RoutesInformation]]
- [[SalesPersonsRoutes]]

**Tables Written**
- [[SalesPersonsRoutes]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
