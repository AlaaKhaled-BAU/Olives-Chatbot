---
type: procedure
database: Olives_BO
name: Niroukh_Integ_SendReturnOrder
schema: dbo
tags: [#backoffice, #integration, #order]
reads_from:
  - Curs_Vou
  - [[Customers]]
  - [[IntegrationErrorLog]]
  - [[Items]]
  - [[ReturnOrdersDetails]]
  - [[ReturnOrdersHeaders]]
  - [[SalesPersons]]
writes_to:
  - [[ReturnOrdersHeaders]]
called_by:
  - sp_OACreate
  - sp_OADestroy
  - sp_OAGetProperty
  - sp_OAMethod
support_relevance: high
last_verified: 2026-07-05
---
# Niroukh_Integ_SendReturnOrder


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Curs_Vou, Customers, IntegrationErrorLog, Items, ReturnOrdersDetails, ReturnOrdersHeaders, SalesPersons. Writes ReturnOrdersHeaders. Calls 4 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
## Tables Read
- Curs_Vou
- [[Customers]]
- [[IntegrationErrorLog]]
- [[Items]]
- [[ReturnOrdersDetails]]
- [[ReturnOrdersHeaders]]
- [[SalesPersons]]
## Tables Written
- [[ReturnOrdersHeaders]]
## Callers
_None (no known callers)_
## Callees
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod
## Impact / Dependencies

**Tables Read**
- Curs_Vou
- [[Customers]]
- [[IntegrationErrorLog]]
- [[Items]]
- [[ReturnOrdersDetails]]
- [[ReturnOrdersHeaders]]
- [[SalesPersons]]

**Tables Written**
- [[ReturnOrdersHeaders]]

**Callers**
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
