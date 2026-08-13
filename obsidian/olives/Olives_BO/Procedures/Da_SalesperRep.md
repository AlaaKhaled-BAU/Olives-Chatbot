---
type: procedure
database: Olives_BO
name: Da_SalesperRep
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[Items]]
  - [[SalesPersonTargets]]
  - [[SalesPersonTargetsDetails]]
  - [[SalesPersons]]
  - [[TargetsReferences]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Da_SalesperRep


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, SalesPersonTargets, SalesPersonTargetsDetails, SalesPersons, TargetsReferences, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromSalesman int
- @ToSalesman int
- @TargetYear smallint
- @FromMonth smallint
- @ToMonth smallint
## Tables Read
- [[Items]]
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersons]]
- [[TargetsReferences]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Items]]
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersons]]
- [[TargetsReferences]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
