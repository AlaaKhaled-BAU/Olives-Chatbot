---
type: procedure
database: Olives_BO
name: SAP_Naouri_Integ
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[CompanyBranches]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersPaidTransList]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[Positions]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - [[SalesPersonItemsAssignment]]
  - `dbo`
writes_to:
  - [[Banks]]
  - [[Branches]]
  - [[CompanyBranches]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersPaidTransList]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - [[SalesPersonItemsAssignment]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# SAP_Naouri_Integ


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, CompanyBranches, Customers, CustomersFinancialDetails, CustomersPaidTransList, CustomersTypes, Items, ItemsUnits, Positions, PriceListDetails, PriceLists, SalesPersonItemsAssignment, dbo. Writes Banks, Branches, CompanyBranches, Customers, CustomersFinancialDetails, CustomersPaidTransList, CustomersTypes, Items, ItemsUnits, PriceListDetails, PriceLists, SalesPersonItemsAssignment. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Banks]]
- [[Branches]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPaidTransList]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsUnits]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersonItemsAssignment]]
- `dbo`
## Tables Written
- [[Banks]]
- [[Branches]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPaidTransList]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsUnits]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersonItemsAssignment]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPaidTransList]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsUnits]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersonItemsAssignment]]
- dbo

**Tables Written**
- [[Banks]]
- [[Branches]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPaidTransList]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsUnits]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersonItemsAssignment]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
