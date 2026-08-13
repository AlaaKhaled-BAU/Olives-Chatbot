---
type: procedure
database: Olives_BO
name: Alpha_Integ_IncreaseCustomerCreditlimit
schema: dbo
tags: [#backoffice, #billing, #customer, #integration]
reads_from:
  - IncreaseLimitLog
  - [[RequestToIncreaseCustomerCreditlimit]]
  - limit
writes_to:
  - customer
  - Cust_CrLimit
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Alpha_Integ_IncreaseCustomerCreditlimit


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads IncreaseLimitLog, RequestToIncreaseCustomerCreditlimit, limit. Writes customer, Cust_CrLimit. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @CustomerNo bigint
- @AddedValue float
- @SalesmanNo int
- @OrderYear smallint
- @OrderNo int
## Tables Read
- IncreaseLimitLog
- [[RequestToIncreaseCustomerCreditlimit]]
- limit
## Tables Written
- customer
- Cust_CrLimit
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- IncreaseLimitLog
- [[RequestToIncreaseCustomerCreditlimit]]
- limit

**Tables Written**
- customer
- Cust_CrLimit

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
