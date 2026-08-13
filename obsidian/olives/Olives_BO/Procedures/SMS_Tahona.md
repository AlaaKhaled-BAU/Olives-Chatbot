---
type: procedure
database: Olives_BO
name: SMS_Tahona
schema: dbo
tags: [#backoffice]
reads_from:
  - Cur_SendSMS
  - [[Customers]]
  - [[LogActionTransaction]]
  - [[OrdersHeaders]]
  - [[Receipts]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
  - [[LogActionTransaction]]
called_by:
  - sp_OACreate
  - sp_OADestroy
  - sp_OAMethod
  - sp_OASetProperty
support_relevance: high
last_verified: 2026-07-05
---
# SMS_Tahona


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Cur_SendSMS, Customers, LogActionTransaction, OrdersHeaders, Receipts, TransactionsDetails, TransactionsHeaders. Writes LogActionTransaction. Calls 4 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
## Tables Read
- Cur_SendSMS
- [[Customers]]
- [[LogActionTransaction]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
- [[LogActionTransaction]]
## Callers
_None (no known callers)_
## Callees
- sp_OACreate
- sp_OADestroy
- sp_OAMethod
- sp_OASetProperty
## Impact / Dependencies

**Tables Read**
- Cur_SendSMS
- [[Customers]]
- [[LogActionTransaction]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

**Tables Written**
- [[LogActionTransaction]]

**Callers**
- sp_OACreate
- sp_OADestroy
- sp_OAMethod
- sp_OASetProperty

**Callees**
_None_


## When to Run This

SMS notification procedure. Called when the system needs to send SMS alerts. Check SMS configuration if messages aren't being delivered.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
