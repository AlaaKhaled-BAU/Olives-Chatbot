---
type: procedure
database: Olives_BO
name: Pro_LocationTargetsDetails
schema: dbo
tags: [#backoffice, #gps, #sales]
reads_from:
  - [[LocationTargetsDetails]]
  - [[Locations]]
  - ON
  - [[TargetsReferences]]
writes_to:
  - [[LocationTargetsDetails]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_LocationTargetsDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads LocationTargetsDetails, Locations, ON, TargetsReferences. Writes LocationTargetsDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @LocationID int = null
- @TargetYear int = null
- @TargetMonth int = null
- @TargetTypeID int = null
- @TargetReferenceID int = null
- @Amount float = null
- @Quantity float = null
- @cmdType varchar(50)=null
## Tables Read
- [[LocationTargetsDetails]]
- [[Locations]]
- ON
- [[TargetsReferences]]
## Tables Written
- [[LocationTargetsDetails]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[LocationTargetsDetails]]
- [[Locations]]
- ON
- [[TargetsReferences]]

**Tables Written**
- [[LocationTargetsDetails]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
