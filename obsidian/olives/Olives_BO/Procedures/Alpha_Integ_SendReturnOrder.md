---
type: procedure
database: Olives_BO
name: Alpha_Integ_SendReturnOrder
schema: dbo
tags: [#backoffice, #integration, #order]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[ReturnOrdersHeaders]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[OT_ReturnOrderDF]]
  - [[OT_ReturnOrderHF]]
  - [[ReturnOrdersHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Alpha_Integ_SendReturnOrder


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, ReturnOrdersHeaders, SalesPersons, dbo. Writes OT_ReturnOrderDF, OT_ReturnOrderHF, ReturnOrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[ReturnOrdersHeaders]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[OT_ReturnOrderDF]]
- [[OT_ReturnOrderHF]]
- [[ReturnOrdersHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Customers]]
- [[ReturnOrdersHeaders]]
- [[SalesPersons]]
- dbo

**Tables Written**
- [[OT_ReturnOrderDF]]
- [[OT_ReturnOrderHF]]
- [[ReturnOrdersHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
