---
type: procedure
database: Olives_BO
name: FixDuplicate_All
schema: dbo
tags: [#backoffice]
reads_from:
  - [[BusinessUnits]]
  - CTE
  - [[CustomersFinancialDetails]]
  - [[SalesPersons]]
writes_to:
  - CTE
  - [[CustomersFinancialDetails]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# FixDuplicate_All


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads BusinessUnits, CTE, CustomersFinancialDetails, SalesPersons. Writes CTE, CustomersFinancialDetails. Invoked by 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @compno int
- @SALESMANNO int
## Tables Read
- [[BusinessUnits]]
- CTE
- [[CustomersFinancialDetails]]
- [[SalesPersons]]
## Tables Written
- CTE
- [[CustomersFinancialDetails]]
## Callers
- [[OT_SendSalesmanData]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[BusinessUnits]]
- CTE
- [[CustomersFinancialDetails]]
- [[salespersons]]

**Tables Written**
- CTE
- [[CustomersFinancialDetails]]

**Callers**
_None_

**Callees**
- [[OT_SendSalesmanData]]


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
