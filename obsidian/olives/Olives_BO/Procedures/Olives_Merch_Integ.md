---
type: procedure
database: Olives_BO
name: Olives_Merch_Integ
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Customers]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[Locations]]
  - Olives_Merch
  - [[Positions]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[Customers]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[Locations]]
  - [[Positions]]
  - [[SalesPersons]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Olives_Merch_Integ


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersTypes, Items, ItemsCategories, ItemsUnits, ItemsUnitsDetails, Locations, Olives_Merch, Positions, SalesPersons, dbo. Writes Customers, CustomersTypes, Items, ItemsCategories, ItemsUnits, ItemsUnitsDetails, Locations, Positions, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
## Tables Read
- [[Customers]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- Olives_Merch
- [[Positions]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[Customers]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- [[Positions]]
- [[SalesPersons]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- Olives_Merch
- [[Positions]]
- [[SalesPersons]]
- dbo

**Tables Written**
- [[Customers]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
- [[Positions]]
- [[SalesPersons]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
