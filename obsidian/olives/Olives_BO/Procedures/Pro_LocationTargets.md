---
type: procedure
database: Olives_BO
name: Pro_LocationTargets
schema: dbo
tags: [#backoffice, #gps, #sales]
reads_from:
  - [[LocationTargets]]
  - [[LocationTargetsDetails]]
  - [[Locations]]
  - [[TargetsTypes]]
writes_to:
  - [[LocationTargets]]
  - [[LocationTargetsDetails]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_LocationTargets


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads LocationTargets, LocationTargetsDetails, Locations, TargetsTypes. Writes LocationTargets, LocationTargetsDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @LocationID int = null
- @TargetYear int = null
- @TargetMonth int = null
- @TargetTypeID int = null
- @Amount float = null
- @FromLocationID int = null
- @ToLocationID int = null
- @FromTargetMonth int = null
- @ToTargetMonth int = null
- @cmdType varchar(50)=null
## Tables Read
- [[LocationTargets]]
- [[LocationTargetsDetails]]
- [[Locations]]
- [[TargetsTypes]]
## Tables Written
- [[LocationTargets]]
- [[LocationTargetsDetails]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[LocationTargets]]
- [[LocationTargetsDetails]]
- [[Locations]]
- [[TargetsTypes]]

**Tables Written**
- [[LocationTargets]]
- [[LocationTargetsDetails]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
