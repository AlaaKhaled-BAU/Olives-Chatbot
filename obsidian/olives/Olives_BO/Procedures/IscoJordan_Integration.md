---
type: procedure
database: Olives_BO
name: IscoJordan_Integration
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[BusinessUnits]]
  - CheckCustFinDet
  - [[CompanyBranches]]
  - [[CustomerStatmentOfAccount]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - DATA
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[Locations]]
writes_to:
  - [[Customers]]
  - [[CustomerStatmentOfAccount]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# IscoJordan_Integration


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, BusinessUnits, CheckCustFinDet, CompanyBranches, CustomerStatmentOfAccount, Customers, CustomersFinancialDetails, CustomersTypes, DATA, Items, ItemsCategories, ItemsUnits, ItemsUnitsDetails, Locations. Writes Customers, CustomerStatmentOfAccount. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 2
## Tables Read
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- CheckCustFinDet
- [[CompanyBranches]]
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- DATA
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]
## Tables Written
- [[Customers]]
- [[CustomerStatmentOfAccount]]
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
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- DATA
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Locations]]

**Tables Written**
- [[Customers]]
- [[CustomerStatmentOfAccount]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
