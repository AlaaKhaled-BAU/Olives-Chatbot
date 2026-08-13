---
type: procedure
database: Olives_BO
name: PRESTOSOFT_INTEG_SENDORDERS_COMP2
schema: dbo
tags: [#backoffice, #integration, #order]
reads_from:
  - [[Customers]]
  - D
  - [[Items]]
  - M
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - PRESTOSOFT
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# PRESTOSOFT_INTEG_SENDORDERS_COMP2


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, D, Items, M, OrdersDetails, OrdersHeaders, PRESTOSOFT, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
_None_
## Tables Read
- [[Customers]]
- D
- [[Items]]
- M
- [[OrdersDetails]]
- [[OrdersHeaders]]
- PRESTOSOFT
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- D
- [[Items]]
- M
- [[OrdersDetails]]
- [[OrdersHeaders]]
- PRESTOSOFT
- [[SalesPersons]]

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
