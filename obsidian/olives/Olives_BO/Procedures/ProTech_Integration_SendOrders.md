---
type: procedure
database: Olives_BO
name: ProTech_Integration_SendOrders
schema: dbo
tags: [#backoffice, #integration, #order]
reads_from:
  - [[Companies]]
  - [[Currencies]]
  - [[Customers]]
  - Header
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - artrans_detl
  - artrans_mstr
  - [[OrdersHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# ProTech_Integration_SendOrders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Companies, Currencies, Customers, Header, OrdersDetails, OrdersHeaders, SalesPersons, dbo. Writes artrans_detl, artrans_mstr, OrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[Companies]]
- [[Currencies]]
- [[Customers]]
- Header
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- artrans_detl
- artrans_mstr
- [[OrdersHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Companies]]
- [[Currencies]]
- [[Customers]]
- Header
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- dbo

**Tables Written**
- artrans_detl
- artrans_mstr
- [[OrdersHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
