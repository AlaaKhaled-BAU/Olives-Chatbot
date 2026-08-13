---
type: procedure
database: Olives_BO
name: OT_SENDSALESMANDATAFROMORDERS
schema: dbo
tags: [#backoffice, #mobile, #order, #sales]
reads_from:
  - [[ClientsActive]]
  - [[OT_SendLog]]
  - [[SalespersonsSendOrders]]
  - SendOrders
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_SENDSALESMANDATAFROMORDERS


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, OT_SendLog, SalespersonsSendOrders, SendOrders, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
_None_
## Tables Read
- [[ClientsActive]]
- [[OT_SendLog]]
- [[SalespersonsSendOrders]]
- SendOrders
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[OT_SendLog]]
- [[SalespersonsSendOrders]]
- SendOrders
- [[TransactionsHeaders]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
