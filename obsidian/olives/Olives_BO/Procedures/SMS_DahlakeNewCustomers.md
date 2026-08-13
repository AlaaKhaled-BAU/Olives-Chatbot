---
type: procedure
database: Olives_BO
name: SMS_DahlakeNewCustomers
schema: dbo
tags: [#backoffice, #customer]
reads_from:
  - Cur_SendSMS
  - OSFA_DB
  - parseJSON
writes_to:
  - [[OT_NewCustomers]]
called_by:
  - sp_OACreate
  - sp_OADestroy
  - sp_OAMethod
  - sp_OASetProperty
support_relevance: high
last_verified: 2026-07-05
---
# SMS_DahlakeNewCustomers


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Cur_SendSMS, OSFA_DB, parseJSON. Writes OT_NewCustomers. Calls 4 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
## Tables Read
- Cur_SendSMS
- OSFA_DB
- parseJSON
## Tables Written
- [[OT_NewCustomers]]
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
- OSFA_DB
- parseJSON

**Tables Written**
- [[OT_NewCustomers]]

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
