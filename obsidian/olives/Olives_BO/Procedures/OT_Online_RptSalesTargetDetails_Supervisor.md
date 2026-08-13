---
type: procedure
database: Olives_BO
name: OT_Online_RptSalesTargetDetails_Supervisor
schema: dbo
tags: [#backoffice, #mobile, #sales]
reads_from:
  - AS
  - Fun_GetSalesmanTreeByID
  - ON
  - [[SalesPersons]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_Online_RptSalesTargetDetails_Supervisor


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads AS, Fun_GetSalesmanTreeByID, ON, SalesPersons, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint=1
- @SalesmanNo int=3
- @TargetYear smallint=2023
- @TargetMonth smallint=03
- @TargetType smallint=1
- @IsSummary bit=1
## Tables Read
- AS
- Fun_GetSalesmanTreeByID
- ON
- [[SalesPersons]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- AS
- Fun_GetSalesmanTreeByID
- ON
- [[SalesPersons]]
- dbo

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
