---
type: procedure
database: Olives_BO
name: Niroukh_Integ_AllUsers_SOA
schema: dbo
tags: [#auth, #backoffice, #integration]
reads_from:
  - Cur_Users
  - [[Customers]]
  - [[CustomersPromotionsGroupsLink]]
  - [[SalesPersons]]
writes_to:
  - [[CustomersPromotionsGroupsLink]]
called_by:
  - [[Niroukh_Integration_SOA]]
  - [[SP_IntegrationErrorLog]]
support_relevance: high
last_verified: 2026-07-05
---
# Niroukh_Integ_AllUsers_SOA


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Cur_Users, Customers, CustomersPromotionsGroupsLink, SalesPersons. Writes CustomersPromotionsGroupsLink. Calls 2 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int=1
## Tables Read
- Cur_Users
- [[Customers]]
- [[CustomersPromotionsGroupsLink]]
- [[SalesPersons]]
## Tables Written
- [[CustomersPromotionsGroupsLink]]
## Callers
_None (no known callers)_
## Callees
- [[Niroukh_Integration_SOA]]
- [[SP_IntegrationErrorLog]]
## Impact / Dependencies

**Tables Read**
- Cur_Users
- [[Customers]]
- [[CustomersPromotionsGroupsLink]]
- [[SalesPersons]]

**Tables Written**
- [[CustomersPromotionsGroupsLink]]

**Callers**
- [[Niroukh_Integration_SOA]]
- [[SP_IntegrationErrorLog]]

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
