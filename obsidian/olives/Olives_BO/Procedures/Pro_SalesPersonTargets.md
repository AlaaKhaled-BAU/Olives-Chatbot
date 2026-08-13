---
type: procedure
database: Olives_BO
name: Pro_SalesPersonTargets
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - Sales
  - [[SalesPersonTargets]]
  - [[SalesPersonTargetsDetails]]
  - [[SalesPersons]]
  - [[TargetsTypes]]
writes_to:
  - [[SalesPersonTargets]]
  - [[SalesPersonTargetsDetails]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesPersonTargets


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Sales, SalesPersonTargets, SalesPersonTargetsDetails, SalesPersons, TargetsTypes. Writes SalesPersonTargets, SalesPersonTargetsDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @SalesPersonID int = null
- @TargetYear int = null
- @TargetMonth int = null
- @TargetTypeID int = null
- @DaysNumber int = null
- @Amount float = null
- @FromSalesPersonID int = null
- @ToSalesPersonID int = null
- @FromTargetMonth int = null
- @ToTargetMonth int = null
- @cmdType varchar(50)=null
## Tables Read
- Sales
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersons]]
- [[TargetsTypes]]
## Tables Written
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Sales
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersons]]
- [[TargetsTypes]]

**Tables Written**
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
