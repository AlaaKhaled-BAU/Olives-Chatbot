---
type: procedure
database: Olives_BO
name: Pro_SalesPersonCollectionTargetsDetails
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - SalesPersonCollectionTargetsDetails
  - [[SalesPersons]]
  - [[TargetsReferences]]
writes_to:
  - SalesPersonCollectionTargetsDetails
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesPersonCollectionTargetsDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalesPersonCollectionTargetsDetails, SalesPersons, TargetsReferences. Writes SalesPersonCollectionTargetsDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @SalesPersonID int = null
- @TargetYear int = null
- @TargetMonth int = null
- @TargetTypeID int = null
- @TargetReferenceID int = null
- @Amount float = null
- @Quantity float = null
- @cmdType varchar(50)=null
## Tables Read
- SalesPersonCollectionTargetsDetails
- [[SalesPersons]]
- [[TargetsReferences]]
## Tables Written
- SalesPersonCollectionTargetsDetails
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- SalesPersonCollectionTargetsDetails
- [[SalesPersons]]
- [[TargetsReferences]]

**Tables Written**
- SalesPersonCollectionTargetsDetails

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
