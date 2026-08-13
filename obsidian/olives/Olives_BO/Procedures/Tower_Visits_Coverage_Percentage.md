---
type: procedure
database: Olives_BO
name: Tower_Visits_Coverage_Percentage
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[CustomersFinancialDetails]]
  - [[LogActionTransaction]]
  - [[SalesPersons]]
writes_to:
called_by:
  - [[FixCustomerMFDuplicateError]]
support_relevance: high
last_verified: 2026-07-05
---
# Tower_Visits_Coverage_Percentage


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersFinancialDetails, LogActionTransaction, SalesPersons. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @companyid int
- @salesmanno int
- @Fromdate smalldatetime
- @ToDate smalldatetime
## Tables Read
- [[CustomersFinancialDetails]]
- [[LogActionTransaction]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- [[FixCustomerMFDuplicateError]]
## Impact / Dependencies

**Tables Read**
- [[CustomersFinancialDetails]]
- [[LogActionTransaction]]
- [[SalesPersons]]

**Tables Written**
_None_

**Callers**
- [[FixCustomerMFDuplicateError]]

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
