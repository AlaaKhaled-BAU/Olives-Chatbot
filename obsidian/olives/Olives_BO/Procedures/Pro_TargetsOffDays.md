---
type: procedure
database: Olives_BO
name: Pro_TargetsOffDays
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[SalesPersonTargetsOffDays]]
  - [[SalesPersons]]
writes_to:
  - [[SalesPersonTargetsOffDays]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_TargetsOffDays


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalesPersonTargetsOffDays, SalesPersons. Writes SalesPersonTargetsOffDays. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID                    INT =null
- @SalespersonID                INT =null
- @TargetYear                   INT =null
- @TargetMonth                  INT =null
- @OffDay                       SmallDateTime =null
- @OldDay                       SmallDateTime =null
- @CMD                          NVARCHAR(MAX) =null
- @OldMonth                     INT=null
- @OldYear                      INT=null
## Tables Read
- [[SalesPersonTargetsOffDays]]
- [[SalesPersons]]
## Tables Written
- [[SalesPersonTargetsOffDays]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalesPersonTargetsOffDays]]
- [[SalesPersons]]

**Tables Written**
- [[SalesPersonTargetsOffDays]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
