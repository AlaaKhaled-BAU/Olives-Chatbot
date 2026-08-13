---
type: procedure
database: Olives_BO
name: GP_Integ_Customer_Wadi
schema: dbo
tags: [#backoffice, #customer, #integration]
reads_from:
  - [[Customers]]
  - [[CustomersTypes]]
  - [[Locations]]
  - `dbo`
writes_to:
  - [[Customers]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# GP_Integ_Customer_Wadi


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersTypes, Locations, dbo. Writes Customers. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Customers]]
- [[CustomersTypes]]
- [[Locations]]
- `dbo`
## Tables Written
- [[Customers]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersTypes]]
- [[Locations]]
- dbo

**Tables Written**
- [[Customers]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
