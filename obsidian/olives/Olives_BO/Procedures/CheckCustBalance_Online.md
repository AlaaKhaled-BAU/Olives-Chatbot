---
type: procedure
database: Olives_BO
name: CheckCustBalance_Online
schema: dbo
tags: [#backoffice, #inventory]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
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
# CheckCustBalance_Online


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, parseJSON. Calls 4 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesmanNo smallint
- @CustNo bigint
- @VouAmount float
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- parseJSON
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
- [[Customers]]
- parseJSON

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

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
