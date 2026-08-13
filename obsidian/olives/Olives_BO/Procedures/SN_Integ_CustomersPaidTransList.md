---
type: procedure
database: Olives_BO
name: SN_Integ_CustomersPaidTransList
schema: dbo
tags: [#backoffice, #customer, #integration]
reads_from:
  - [[Customers]]
  - [[CustomersPaidTransList]]
  - SN
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# SN_Integ_CustomersPaidTransList


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersPaidTransList, SN. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
## Tables Read
- [[Customers]]
- [[CustomersPaidTransList]]
- SN
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersPaidTransList]]
- SN

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
