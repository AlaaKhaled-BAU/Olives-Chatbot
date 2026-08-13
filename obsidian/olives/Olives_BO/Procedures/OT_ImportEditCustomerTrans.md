---
type: procedure
database: Olives_BO
name: OT_ImportEditCustomerTrans
schema: dbo
tags: [#backoffice, #customer, #mobile]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - Header
  - `dbo`
writes_to:
  - customer
  - [[Customers]]
  - [[OT_EditCustomerTrans]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportEditCustomerTrans


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, Header, dbo. Writes customer, Customers, OT_EditCustomerTrans. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- Header
- `dbo`
## Tables Written
- customer
- [[Customers]]
- [[OT_EditCustomerTrans]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Customers]]
- Header
- dbo

**Tables Written**
- customer
- [[customers]]
- [[OT_EditCustomerTrans]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
