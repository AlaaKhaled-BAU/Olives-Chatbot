---
type: procedure
database: Olives_BO
name: POAOnlineReport
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[Customers]]
  - [[CustomersClasses]]
  - [[CustomersGroups]]
  - [[LogActionTransaction]]
  - [[POADetails]]
  - [[POAHeader]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# POAOnlineReport


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersClasses, CustomersGroups, LogActionTransaction, POADetails, POAHeader, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint=1
- @SalesmanNo int=3003
- @POAYear smallint=2024
- @POAMonth smallint=12
## Tables Read
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersGroups]]
- [[LogActionTransaction]]
- [[POADetails]]
- [[POAHeader]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersGroups]]
- [[LogActionTransaction]]
- [[POADetails]]
- [[POAHeader]]
- [[SalesPersons]]

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
