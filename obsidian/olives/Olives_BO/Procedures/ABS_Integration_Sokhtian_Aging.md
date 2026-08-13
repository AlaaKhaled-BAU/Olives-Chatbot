---
type: procedure
database: Olives_BO
name: ABS_Integration_Sokhtian_Aging
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Customers]]
  - [[CustomersBalanceAging]]
  - openjson
writes_to:
  - [[CustomersBalanceAging]]
called_by:
  - ABS_Integ_GetDataFromAPI_Sokhtian
support_relevance: high
last_verified: 2026-07-05
---
# ABS_Integration_Sokhtian_Aging


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersBalanceAging, openjson. Writes CustomersBalanceAging. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID nvarchar(50) = 1
## Tables Read
- [[Customers]]
- [[CustomersBalanceAging]]
- openjson
## Tables Written
- [[CustomersBalanceAging]]
## Callers
_None (no known callers)_
## Callees
- ABS_Integ_GetDataFromAPI_Sokhtian
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersBalanceAging]]
- openjson

**Tables Written**
- [[CustomersBalanceAging]]

**Callers**
- ABS_Integ_GetDataFromAPI_Sokhtian

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
