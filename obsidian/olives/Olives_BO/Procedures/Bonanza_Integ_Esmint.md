---
type: procedure
database: Olives_BO
name: Bonanza_Integ_Esmint
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[BusinessUnits]]
  - [[CompanyBranches]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[Items]]
  - Olives_BO
  - [[Positions]]
  - SSMS
  - [[SalesPersonItemsAssignment]]
  - [[SalesPersons]]
  - XBT
  - cccc
  - `dbo`
writes_to:
  - [[Banks]]
  - [[Branches]]
  - [[BusinessUnits]]
  - [[CompanyBranches]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomerStatmentOfAccount]]
  - [[Positions]]
  - [[SalesPersonItemsAssignment]]
  - [[SalesPersons]]
  - XBT
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Bonanza_Integ_Esmint


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, BusinessUnits, CompanyBranches, Customers, CustomersFinancialDetails, Items, Olives_BO, Positions, SSMS, SalesPersonItemsAssignment, SalesPersons, XBT, cccc, dbo. Writes Banks, Branches, BusinessUnits, CompanyBranches, Customers, CustomersFinancialDetails, CustomerStatmentOfAccount, Positions, SalesPersonItemsAssignment, SalesPersons, XBT. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Items]]
- Olives_BO
- [[Positions]]
- SSMS
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]
- XBT
- cccc
- `dbo`
## Tables Written
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomerStatmentOfAccount]]
- [[Positions]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]
- XBT
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Items]]
- Olives_BO
- [[Positions]]
- SSMS
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]
- XBT
- cccc
- dbo

**Tables Written**
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomerStatmentOfAccount]]
- [[Positions]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]
- XBT

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
