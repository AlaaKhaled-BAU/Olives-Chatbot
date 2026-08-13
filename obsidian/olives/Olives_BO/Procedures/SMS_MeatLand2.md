---
type: procedure
database: Olives_BO
name: SMS_MeatLand2
schema: dbo
tags: [#backoffice]
reads_from:
  - Cur_SendSMS
  - [[Customers]]
  - [[LogActionTransaction]]
  - [[OrdersHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# SMS_MeatLand2


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Cur_SendSMS, Customers, LogActionTransaction, OrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
## Tables Read
- Cur_SendSMS
- [[Customers]]
- [[LogActionTransaction]]
- [[OrdersHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Cur_SendSMS
- [[Customers]]
- [[LogActionTransaction]]
- [[OrdersHeaders]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

SMS notification procedure. Called when the system needs to send SMS alerts. Check SMS configuration if messages aren't being delivered.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
