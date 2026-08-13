---
type: procedure
database: Olives_BO
name: OT_GetOrderInvoiceLinkHistory
schema: dbo
tags: [#backoffice, #billing, #log, #mobile, #order]
reads_from:
  - [[Customers]]
  - [[Items]]
  - [[ItemsUnits]]
  - Olives_BO
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
  - [[WF_MasterLog]]
  - [[WF_SubLog]]
  - `dbo`
writes_to:
  - OrderInvoiceLinkHistory
called_by:
  - Alpha_Integration
support_relevance: high
last_verified: 2026-07-05
---
# OT_GetOrderInvoiceLinkHistory


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Items, ItemsUnits, Olives_BO, OrdersDetails, OrdersHeaders, SalesPersons, TransactionsHeaders, WF_MasterLog, WF_SubLog, dbo. Writes OrderInvoiceLinkHistory. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint=1
- @SalesmanNo int=3003
- @FromDate smallDateTime= '2017-01-01'
- @ToDate smallDateTime= '2017-03-01'
## Tables Read
- [[Customers]]
- [[Items]]
- [[ItemsUnits]]
- Olives_BO
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- [[WF_MasterLog]]
- [[WF_SubLog]]
- `dbo`
## Tables Written
- OrderInvoiceLinkHistory
## Callers
_None (no known callers)_
## Callees
- Alpha_Integration
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[Items]]
- [[ItemsUnits]]
- Olives_BO
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- [[WF_MasterLog]]
- [[WF_SubLog]]
- dbo

**Tables Written**
- OrderInvoiceLinkHistory

**Callers**
- Alpha_Integration

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Cross-Database
Also exists in the other database: [[OSFA_DB/Procedures/OT_GetOrderInvoiceLinkHistory]] (OSFA).

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
