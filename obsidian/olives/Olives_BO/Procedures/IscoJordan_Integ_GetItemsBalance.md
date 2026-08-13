---
type: procedure
database: Olives_BO
name: IscoJordan_Integ_GetItemsBalance
schema: dbo
tags: [#backoffice, #integration, #inventory]
reads_from:
  - DATA
  - [[SalesPersonItemsAssignment]]
  - [[SalesPersonItemsBalance]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[SalesPersonItemsBalance]]
  - [[SalesPersons]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# IscoJordan_Integ_GetItemsBalance


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads DATA, SalesPersonItemsAssignment, SalesPersonItemsBalance, SalesPersons, dbo. Writes SalesPersonItemsBalance, SalesPersons. Invoked by 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesmanNo int
- @PositionsID int
- @ErrorNo int = 0 output
## Tables Read
- DATA
- [[SalesPersonItemsAssignment]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
## Callers
- [[OT_SendSalesmanData]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- DATA
- [[SalesPersonItemsAssignment]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- dbo

**Tables Written**
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]

**Callers**
_None_

**Callees**
- [[OT_SendSalesmanData]]


## When to Run This

Run when pulling data from an external API/system. Called during sync cycles or on-demand data refresh.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
