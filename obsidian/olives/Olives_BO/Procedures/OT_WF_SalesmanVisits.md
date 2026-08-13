---
type: procedure
database: Olives_BO
name: OT_WF_SalesmanVisits
schema: dbo
tags: [#auth, #backoffice, #mobile, #sales, #workflow]
reads_from:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[LogActionTransaction]]
  - [[SalesPersons]]
  - [[SalesPersonsRoutes]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_WF_SalesmanVisits


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersFinancialDetails, LogActionTransaction, SalesPersons, SalesPersonsRoutes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int = 1
- @Date smalldatetime = '2021-06-17'
- @Parent int = 1
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[LogActionTransaction]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[LogActionTransaction]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
