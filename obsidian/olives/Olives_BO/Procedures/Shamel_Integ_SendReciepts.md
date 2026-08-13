---
type: procedure
database: Olives_BO
name: Shamel_Integ_SendReciepts
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Branches]]
  - [[Checks]]
  - Curs_Vou
  - [[Customers]]
  - Fun_GetReceiptsChecksTotal
  - [[IntegrationErrorLog]]
  - OPENJSON
  - [[Receipts]]
  - [[SalesPersons]]
writes_to:
called_by:
  - [[Shamel_Integ_GetDataFromAPI]]
  - sp_OACreate
  - sp_OADestroy
  - sp_OAGetProperty
  - sp_OAMethod
support_relevance: high
last_verified: 2026-07-05
---
# Shamel_Integ_SendReciepts


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Branches, Checks, Curs_Vou, Customers, Fun_GetReceiptsChecksTotal, IntegrationErrorLog, OPENJSON, Receipts, SalesPersons. Calls 5 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
## Tables Read
- [[Branches]]
- [[Checks]]
- Curs_Vou
- [[Customers]]
- Fun_GetReceiptsChecksTotal
- [[IntegrationErrorLog]]
- OPENJSON
- [[Receipts]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- [[Shamel_Integ_GetDataFromAPI]]
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod
## Impact / Dependencies

**Tables Read**
- [[Branches]]
- [[Checks]]
- Curs_Vou
- [[Customers]]
- Fun_GetReceiptsChecksTotal
- [[IntegrationErrorLog]]
- OPENJSON
- [[Receipts]]
- [[SalesPersons]]

**Tables Written**
_None_

**Callers**
- [[Shamel_Integ_GetDataFromAPI]]
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
