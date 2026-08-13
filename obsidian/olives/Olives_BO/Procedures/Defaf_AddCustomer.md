---
type: procedure
database: Olives_BO
name: Defaf_AddCustomer
schema: dbo
tags: [#backoffice, #customer]
reads_from:
  - [[Add_Customer]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersPromotionsGroupsLink]]
  - Flag
  - [[SalesPersons]]
writes_to:
  - [[Add_Customer]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersPromotionsGroupsLink]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Defaf_AddCustomer


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Add_Customer, Customers, CustomersFinancialDetails, CustomersPromotionsGroupsLink, Flag, SalesPersons. Writes Add_Customer, Customers, CustomersFinancialDetails, CustomersPromotionsGroupsLink. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
- @addstatus bit
## Tables Read
- [[Add_Customer]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPromotionsGroupsLink]]
- Flag
- [[SalesPersons]]
## Tables Written
- [[Add_Customer]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPromotionsGroupsLink]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Add_Customer]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPromotionsGroupsLink]]
- Flag
- [[SalesPersons]]

**Tables Written**
- [[Add_Customer]]
- [[customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPromotionsGroupsLink]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
