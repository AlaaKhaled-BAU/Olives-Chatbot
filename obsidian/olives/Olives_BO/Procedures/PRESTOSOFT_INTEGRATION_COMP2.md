---
type: procedure
database: Olives_BO
name: PRESTOSOFT_INTEGRATION_COMP2
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[BusinessUnits]]
  - CheckCustFinDet
  - [[CompanyBranches]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[Locations]]
  - PRESTOSOFT
  - [[Positions]]
  - [[PriceListDetails]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# PRESTOSOFT_INTEGRATION_COMP2


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, BusinessUnits, CheckCustFinDet, CompanyBranches, Customers, CustomersFinancialDetails, CustomersTypes, Items, ItemsCategories, ItemsUnits, Locations, PRESTOSOFT, Positions, PriceListDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
_None_
## Tables Read
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- CheckCustFinDet
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[Locations]]
- PRESTOSOFT
- [[Positions]]
- [[PriceListDetails]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- CheckCustFinDet
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[Locations]]
- PRESTOSOFT
- [[Positions]]
- [[PriceListDetails]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
