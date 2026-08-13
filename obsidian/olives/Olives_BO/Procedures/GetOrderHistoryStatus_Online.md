---
type: procedure
database: Olives_BO
name: GetOrderHistoryStatus_Online
schema: dbo
tags: [#backoffice, #log, #order]
reads_from:
  - [[ClientsActive]]
  - [[OrdersHeaders]]
writes_to:
called_by:
  - sp_OACreate
  - sp_OADestroy
  - sp_OAMethod
  - sp_OASetProperty
support_relevance: high
last_verified: 2026-07-05
---
# GetOrderHistoryStatus_Online


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, OrdersHeaders. Calls 4 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint=1
- @OrderYear smallint=2021
- @OrderNo bigint =12160156
## Tables Read
- [[ClientsActive]]
- [[OrdersHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- sp_OACreate
- sp_OADestroy
- sp_OAMethod
- sp_OASetProperty
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[OrdersHeaders]]

**Tables Written**
_None_

**Callers**
- sp_OACreate
- sp_OADestroy
- sp_OAMethod
- sp_OASetProperty

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
