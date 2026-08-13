---
type: procedure
database: Olives_BO
name: AcBack_Integ_GetItemBalance
schema: dbo
tags: [#backoffice, #integration, #inventory]
reads_from:
  - [[Items]]
  - [[SalesPersonItemsAssignment]]
  - [[SalesPersons]]
writes_to:
  - [[OT_StoreItemsQty]]
called_by:
  - [[Acback_Integ_PostTransactionsData]]
support_relevance: high
last_verified: 2026-07-05
---
# AcBack_Integ_GetItemBalance


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, SalesPersonItemsAssignment, SalesPersons. Writes OT_StoreItemsQty. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int = 1
- @SalesmanNo int = 1
- @sendDate smalldatetime = null
## Tables Read
- [[Items]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]
## Tables Written
- [[OT_StoreItemsQty]]
## Callers
_None (no known callers)_
## Callees
- [[Acback_Integ_PostTransactionsData]]
## Impact / Dependencies

**Tables Read**
- [[Items]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]

**Tables Written**
- [[OT_StoreItemsQty]]

**Callers**
- [[Acback_Integ_PostTransactionsData]]

**Callees**
_None_


## When to Run This

Run when pulling data from an external API/system. Called during sync cycles or on-demand data refresh.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
