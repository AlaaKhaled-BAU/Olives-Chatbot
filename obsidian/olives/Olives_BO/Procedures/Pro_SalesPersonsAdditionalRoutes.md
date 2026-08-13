---
type: procedure
database: Olives_BO
name: Pro_SalesPersonsAdditionalRoutes
schema: dbo
tags: [#backoffice, #gps, #sales]
reads_from:
  - [[RoutesInformation]]
  - [[SalesPersonsAdditionalRoutes]]
  - [[SalesPersonsRoutes]]
writes_to:
  - [[SalesPersonsAdditionalRoutes]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesPersonsAdditionalRoutes


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads RoutesInformation, SalesPersonsAdditionalRoutes, SalesPersonsRoutes. Writes SalesPersonsAdditionalRoutes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	= null
- @PositionID	int	= null
- @WeekNo	int	= null
- @DayNo	smallint	= null
- @RouteID	int	= null
- @FromPositionID	int	=null
- @FromWeekNo	int=	null
- @FromDayNo	int=	null
- @cmdType nvarchar(50) = null
## Tables Read
- [[RoutesInformation]]
- [[SalesPersonsAdditionalRoutes]]
- [[SalesPersonsRoutes]]
## Tables Written
- [[SalesPersonsAdditionalRoutes]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[RoutesInformation]]
- [[SalesPersonsAdditionalRoutes]]
- [[SalesPersonsRoutes]]

**Tables Written**
- [[SalesPersonsAdditionalRoutes]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
