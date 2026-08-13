---
type: procedure
database: Olives_BO
name: Galaxy_Integ_SendLoadOrder
schema: dbo
tags: [#backoffice, #integration, #order]
reads_from:
  - [[ClientsActive]]
  - [[SalesPersons]]
  - [[TransfersOrdersHeaders]]
  - `dbo`
writes_to:
  - LoadOrderHF
  - LoadOrdersDF
  - [[TransfersOrdersHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Galaxy_Integ_SendLoadOrder


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, SalesPersons, TransfersOrdersHeaders, dbo. Writes LoadOrderHF, LoadOrdersDF, TransfersOrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
## Tables Read
- [[ClientsActive]]
- [[SalesPersons]]
- [[TransfersOrdersHeaders]]
- `dbo`
## Tables Written
- LoadOrderHF
- LoadOrdersDF
- [[TransfersOrdersHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[SalesPersons]]
- [[TransfersOrdersHeaders]]
- dbo

**Tables Written**
- LoadOrderHF
- LoadOrdersDF
- [[TransfersOrdersHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
