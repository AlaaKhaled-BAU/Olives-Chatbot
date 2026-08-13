---
type: procedure
database: Olives_BO
name: FixCustomerMFDuplicateError3
schema: dbo
tags: [#backoffice, #customer, #log]
reads_from:
  - [[CustomersFinancialDetails]]
writes_to:
  - [[CustomersFinancialDetails]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# FixCustomerMFDuplicateError3


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersFinancialDetails. Writes CustomersFinancialDetails. Invoked by 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
- @Salesmanposition int
## Tables Read
- [[CustomersFinancialDetails]]
## Tables Written
- [[CustomersFinancialDetails]]
## Callers
- [[OT_SendSalesmanData]]
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
- [[OT_SendSalesmanData]]


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
