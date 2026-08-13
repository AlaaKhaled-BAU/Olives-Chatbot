---
type: procedure
database: Olives_BO
name: JoTax_Integ_SendTransaction
schema: dbo
tags: [#backoffice, #billing, #integration, #legal]
reads_from:
  - [[JOTaxSettings]]
writes_to:
called_by:
  - sp_OACreate
  - sp_OADestroy
  - sp_OAGetProperty
  - sp_OAMethod
support_relevance: high
last_verified: 2026-07-05
---
# JoTax_Integ_SendTransaction


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads JOTaxSettings. Invoked by 1 procedure(s). Calls 4 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID INT
- @TransactionNo INT
- @TransactionTypeID INT
- @TransactionYear INT
- @JSONResult NVARCHAR(MAX) OUTPUT
## Tables Read
- [[JOTaxSettings]]
## Tables Written
_None_
## Callers
- [[Pro_JoTaxResend]]
## Callees
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod
## Impact / Dependencies

**Tables Read**
- [[JOTaxSettings]]

**Tables Written**
_None_

**Callers**
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod

**Callees**
- [[Pro_JoTaxResend]]


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
