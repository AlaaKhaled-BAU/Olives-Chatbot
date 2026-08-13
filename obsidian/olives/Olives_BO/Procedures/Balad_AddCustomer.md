---
type: procedure
database: Olives_BO
name: Balad_AddCustomer
schema: dbo
tags: [#backoffice, #customer]
reads_from:
  - [[Balad_Add_Customer_Table]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - Flag
  - [[SalesPersons]]
writes_to:
  - [[Balad_Add_Customer_Table]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Balad_AddCustomer


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Balad_Add_Customer_Table, Customers, CustomersFinancialDetails, Flag, SalesPersons. Writes Balad_Add_Customer_Table, Customers, CustomersFinancialDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
## Tables Read
- [[Balad_Add_Customer_Table]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Flag
- [[SalesPersons]]
## Tables Written
- [[Balad_Add_Customer_Table]]
- [[Customers]]
- [[CustomersFinancialDetails]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Balad_Add_Customer_Table]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Flag
- [[SalesPersons]]

**Tables Written**
- [[Balad_Add_Customer_Table]]
- [[customers]]
- [[CustomersFinancialDetails]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
