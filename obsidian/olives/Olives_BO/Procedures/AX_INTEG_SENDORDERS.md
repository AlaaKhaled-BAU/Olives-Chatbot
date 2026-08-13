---
type: procedure
database: Olives_BO
name: AX_INTEG_SENDORDERS
schema: dbo
tags: [#backoffice, #integration, #order]
reads_from:
  - [[Companies]]
  - [[Customers]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[PaymentsTypes]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# AX_INTEG_SENDORDERS


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Companies, Customers, OrdersDetails, OrdersHeaders, PaymentsTypes, SalesPersons, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
_None_
## Tables Read
- [[Companies]]
- [[Customers]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[PaymentsTypes]]
- [[SalesPersons]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Companies]]
- [[Customers]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[PaymentsTypes]]
- [[SalesPersons]]
- dbo

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
