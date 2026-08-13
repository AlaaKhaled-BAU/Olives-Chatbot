---
type: procedure
database: Olives_BO
name: Wings_Integ_SendReturnSales
schema: dbo
tags: [#backoffice, #integration, #order, #sales]
reads_from:
  - [[Customers]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - WACC
writes_to:
  - TEMP_INVENT_VOH_MAS
  - [[TransactionsHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Wings_Integ_SendReturnSales


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, SalesPersons, TransactionsDetails, TransactionsHeaders, WACC. Writes TEMP_INVENT_VOH_MAS, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[Customers]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- WACC
## Tables Written
- TEMP_INVENT_VOH_MAS
- [[TransactionsHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- WACC

**Tables Written**
- TEMP_INVENT_VOH_MAS
- [[TransactionsHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
