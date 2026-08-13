---
type: procedure
database: Olives_BO
name: Awtar_Integ_SendReceipts
schema: dbo
tags: [#backoffice, #billing, #integration]
reads_from:
  - [[Banks]]
  - [[Checks]]
  - [[Companies]]
  - Curs_Payment
  - [[Customers]]
  - [[Drawers]]
  - Fun_GetReceiptsChecksTotal
  - [[IntegrationErrorLog]]
  - [[Receipts]]
  - [[SalesPersons]]
writes_to:
  - [[Receipts]]
called_by:
  - sp_OACreate
  - sp_OADestroy
  - sp_OAGetProperty
  - sp_OAMethod
support_relevance: high
last_verified: 2026-07-05
---
# Awtar_Integ_SendReceipts


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Checks, Companies, Curs_Payment, Customers, Drawers, Fun_GetReceiptsChecksTotal, IntegrationErrorLog, Receipts, SalesPersons. Writes Receipts. Calls 4 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Banks]]
- [[Checks]]
- [[Companies]]
- Curs_Payment
- [[Customers]]
- [[Drawers]]
- Fun_GetReceiptsChecksTotal
- [[IntegrationErrorLog]]
- [[Receipts]]
- [[SalesPersons]]
## Tables Written
- [[Receipts]]
## Callers
_None (no known callers)_
## Callees
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Checks]]
- [[Companies]]
- Curs_Payment
- [[Customers]]
- [[Drawers]]
- Fun_GetReceiptsChecksTotal
- [[IntegrationErrorLog]]
- [[Receipts]]
- [[SalesPersons]]

**Tables Written**
- [[Receipts]]

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
