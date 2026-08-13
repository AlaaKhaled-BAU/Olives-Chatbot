---
type: procedure
database: Olives_BO
name: OT_FixDuplicateCustomers
schema: dbo
tags: [#backoffice, #customer, #mobile]
reads_from:
  - [[CustomersFinancialDetails]]
writes_to:
  - [[CustomersFinancialDetails]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_FixDuplicateCustomers


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersFinancialDetails. Writes CustomersFinancialDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesmanNo int
## Tables Read
- [[CustomersFinancialDetails]]
## Tables Written
- [[CustomersFinancialDetails]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomersFinancialDetails]]

**Tables Written**
- [[CustomersFinancialDetails]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
