---
type: procedure
database: Olives_BO
name: Customers_By_Type
schema: dbo
tags: [#backoffice, #customer, #reference]
reads_from:
  - [[Customers]]
  - [[CustomersTypes]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Customers_By_Type


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersTypes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CustomersType int=null
- @CompanyID int=null
- @cmdType nvarchar(100)=null
## Tables Read
- [[Customers]]
- [[CustomersTypes]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersTypes]]

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
