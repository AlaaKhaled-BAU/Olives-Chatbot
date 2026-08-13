---
type: procedure
database: Olives_BO
name: Spartan_SAP_Integ_UpdateCustomerChqList
schema: dbo
tags: [#backoffice, #customer, #integration]
reads_from:
  - [[CustomerChqList]]
  - [[Customers]]
  - OPENJSON
  - `dbo`
writes_to:
  - [[CustomerChqList]]
called_by:
  - sp_OACreate
  - sp_OADestroy
  - sp_OAGetProperty
  - sp_OAMethod
support_relevance: high
last_verified: 2026-07-05
---
# Spartan_SAP_Integ_UpdateCustomerChqList


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerChqList, Customers, OPENJSON, dbo. Writes CustomerChqList. Calls 4 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
## Tables Read
- [[CustomerChqList]]
- [[Customers]]
- OPENJSON
- `dbo`
## Tables Written
- [[CustomerChqList]]
## Callers
_None (no known callers)_
## Callees
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod
## Impact / Dependencies

**Tables Read**
- [[CustomerChqList]]
- [[Customers]]
- OPENJSON
- dbo

**Tables Written**
- [[CustomerChqList]]

**Callers**
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
