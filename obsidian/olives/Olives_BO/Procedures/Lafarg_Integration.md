---
type: procedure
database: Olives_BO
name: Lafarg_Integration
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - Balance
  - [[Banks]]
  - [[Branches]]
  - [[BusinessUnits]]
  - [[CompanyBranches]]
  - [[CustomerStatmentOfAccount]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - OPENQUERY
  - [[Positions]]
  - Runining
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - cccc
writes_to:
  - [[CustomerStatmentOfAccount]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Lafarg_Integration


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Balance, Banks, Branches, BusinessUnits, CompanyBranches, CustomerStatmentOfAccount, Customers, CustomersFinancialDetails, CustomersTypes, OPENQUERY, Positions, Runining, SalesPersons, SalesPersonsGroups, cccc. Writes CustomerStatmentOfAccount. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- Balance
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- OPENQUERY
- [[Positions]]
- Runining
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- cccc
## Tables Written
- [[CustomerStatmentOfAccount]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Balance
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- OPENQUERY
- [[Positions]]
- Runining
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- cccc

**Tables Written**
- [[CustomerStatmentOfAccount]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
