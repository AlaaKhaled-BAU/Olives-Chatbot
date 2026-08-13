---
type: procedure
database: Olives_BO
name: SMS_AnwarMakesTransfer
schema: dbo
tags: [#backoffice, #order]
reads_from:
  - [[SalesPersons]]
  - parseJSON
writes_to:
called_by:
  - sp_OACreate
  - sp_OADestroy
  - sp_OAMethod
  - sp_OASetProperty
support_relevance: high
last_verified: 2026-07-05
---
# SMS_AnwarMakesTransfer


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalesPersons, parseJSON. Invoked by 1 procedure(s). Calls 4 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint=600
- @SalesmanID int=5
- @OrderNo int =12238552
## Tables Read
- [[SalesPersons]]
- parseJSON
## Tables Written
_None_
## Callers
- [[OT_ImportUploadOrders]]
## Callees
- sp_OACreate
- sp_OADestroy
- sp_OAMethod
- sp_OASetProperty
## Impact / Dependencies

**Tables Read**
- [[SalesPersons]]
- parseJSON

**Tables Written**
_None_

**Callers**
- sp_OACreate
- sp_OADestroy
- sp_OAMethod
- sp_OASetProperty

**Callees**
- [[OT_ImportUploadOrders]]


## When to Run This

SMS notification procedure. Called when the system needs to send SMS alerts. Check SMS configuration if messages aren't being delivered.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
