---
type: procedure
database: Olives_BO
name: Rpt_PrintOrdersBatches
schema: dbo
tags: [#backoffice, #inventory, #order, #reporting]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[Items]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesPersonItemsAssignment]]
  - [[SalesPersons]]
  - [[TransactionsBatchsItemsInfo]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_PrintOrdersBatches


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, Items, OrdersDetails, OrdersHeaders, SalesPersonItemsAssignment, SalesPersons, TransactionsBatchsItemsInfo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @DeliveryBatchID int
- @cmdType varchar(50)=null
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[Items]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]
- [[TransactionsBatchsItemsInfo]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Customers]]
- [[Items]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]
- [[TransactionsBatchsItemsInfo]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
