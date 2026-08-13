---
type: procedure
database: Olives_BO
name: SalesPersonItemBounceTarget
schema: dbo
tags: [#backoffice, #inventory, #sales]
reads_from:
  - [[Items]]
  - [[SalesPersonItemBonusTarget]]
  - [[SalesPersons]]
writes_to:
  - [[SalesPersonItemBonusTarget]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# SalesPersonItemBounceTarget


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, SalesPersonItemBonusTarget, SalesPersons. Writes SalesPersonItemBonusTarget. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @SalesPersonID int = null
- @TargetYear int = null
- @ItemCode varchar(50)=null
- @UnitID varchar(50)=null
- @M1 int = null,@M2 int = null
- @M3 int = null,@M4 int = null
- @M5 int = null,@M6 int = null
- @M7 int = null,@M8 int = null
- @M9 int = null,@M10 int = null
- @M11 int = null,@M12 int = null
- @cmdType varchar(50)=null
## Tables Read
- [[Items]]
- [[SalesPersonItemBonusTarget]]
- [[SalesPersons]]
## Tables Written
- [[SalesPersonItemBonusTarget]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Items]]
- [[SalesPersonItemBonusTarget]]
- [[SalesPersons]]

**Tables Written**
- [[SalesPersonItemBonusTarget]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
