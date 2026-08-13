---
type: procedure
database: Olives_BO
name: Pro_SalesmanClassTarget
schema: dbo
tags: [#backoffice, #reference, #sales]
reads_from:
  - [[Customers]]
  - [[CustomersClasses]]
  - [[CustomersFinancialDetails]]
  - [[SalesPersons]]
  - [[SalespersonClassTarget]]
writes_to:
  - [[SalespersonClassTarget]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesmanClassTarget


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersClasses, CustomersFinancialDetails, SalesPersons, SalespersonClassTarget. Writes SalespersonClassTarget. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @SalesmanID int = null
- @ClassID int = null
- @Target int = null
- @cmdType varchar(50)=null
## Tables Read
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- [[SalesPersons]]
- [[SalespersonClassTarget]]
## Tables Written
- [[SalespersonClassTarget]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- [[SalesPersons]]
- [[SalespersonClassTarget]]

**Tables Written**
- [[SalespersonClassTarget]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
