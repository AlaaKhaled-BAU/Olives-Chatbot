---
type: procedure
database: Olives_BO
name: Soft_Integration_Comp1
schema: dbo
tags: [#integration]
reads_from:
writes_to:
  - Banks
  - Branches
  - BusinessUnits
  - CompanyBranches
  - Customers
  - CustomersFinancialDetails
  - CustomersGroups
  - CustomersPromotionsGroups
  - CustomersTypes
  - Items
  - ItemsCategories
  - ItemsUnits
  - Locations
  - NewCustomerDefaultValue
  - PaymentsTypes
  - Positions
  - PriceListDetails
  - PriceLists
  - SalesPersonItemsAssignment
  - SalesPersons
  - SalesPersonsGroups
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# Soft_Integration_Comp1

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — writes 21; calls 1 proc(s). See sections below for the full dependency map.
## Parameters
_None_
## Tables Read
_None_
## Tables Written
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersGroups]]
- [[CustomersPromotionsGroups]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[Locations]]
- [[NewCustomerDefaultValue]]
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
## Cross-DB Tables
References tables in **OSFA_DB** (qualified as `OSFA_DB.dbo.*`):
- [[OSFA_DB/Tables/OT_NewCustomers|OT_NewCustomers]]
## Callers
_None_
## Callees
- `Fun_GetSalesmanRouteByDate`
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
