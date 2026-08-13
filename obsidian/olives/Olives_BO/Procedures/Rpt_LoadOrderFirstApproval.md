---
type: procedure
database: Olives_BO
name: Rpt_LoadOrderFirstApproval
schema: dbo
tags: [#backoffice, #order, #reporting, #workflow]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[Checks]]
  - [[ClientsActive]]
  - [[Companies]]
  - [[Currencies]]
  - [[Customers]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[PriceLists]]
  - [[Receipts]]
  - [[ReturnOrdersDetails]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_LoadOrderFirstApproval


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, Checks, ClientsActive, Companies, Currencies, Customers, Items, ItemsUnits, ItemsUnitsDetails, OrdersDetails, OrdersHeaders, PriceLists, Receipts, ReturnOrdersDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @InvNo bigint
- @TransactionYear smalldatetime
- @TransactionTypeID smallint
## Tables Read
- [[Banks]]
- [[Branches]]
- [[Checks]]
- [[ClientsActive]]
- [[Companies]]
- [[Currencies]]
- [[Customers]]
- [[Items]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[PriceLists]]
- [[Receipts]]
- [[ReturnOrdersDetails]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- [[Checks]]
- [[ClientsActive]]
- [[Companies]]
- [[Currencies]]
- [[Customers]]
- [[Items]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[PriceLists]]
- [[Receipts]]
- [[ReturnOrdersDetails]]

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
