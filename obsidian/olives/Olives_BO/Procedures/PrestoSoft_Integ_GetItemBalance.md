---
type: procedure
database: Olives_BO
name: PrestoSoft_Integ_GetItemBalance
schema: dbo
tags: [#backoffice, #integration, #inventory]
reads_from:
  - [[SalesPersonItemsAssignment]]
  - [[SalesPersonItemsBalance]]
  - [[SalesPersons]]
  - dual
  - openquery
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# PrestoSoft_Integ_GetItemBalance


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalesPersonItemsAssignment, SalesPersonItemsBalance, SalesPersons, dual, openquery. Invoked by 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
- @SalesmanNo int
## Tables Read
- [[SalesPersonItemsAssignment]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- dual
- openquery
## Tables Written
_None_
## Callers
- [[OT_SendSalesmanData]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalesPersonItemsAssignment]]
- [[SalesPersonItemsBalance]]
- [[Salespersons]]
- dual
- openquery

**Tables Written**
_None_

**Callers**
_None_

**Callees**
- [[OT_SendSalesmanData]]


## When to Run This

Run when pulling data from an external API/system. Called during sync cycles or on-demand data refresh.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
