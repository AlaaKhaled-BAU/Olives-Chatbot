---
type: procedure
database: Olives_BO
name: SN_Integration
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[BusinessUnits]]
  - [[CompanyBranches]]
  - Cur_Banks
  - Cur_ItemsCategories
  - [[CustomersTypes]]
  - [[IntegrationErrorLog]]
  - [[ItemsCategories]]
  - [[Locations]]
  - [[PaymentsTypes]]
  - SN
  - [[SalesPersonsGroups]]
writes_to:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
called_by:
  - [[SP_IntegrationErrorLog]]
support_relevance: high
last_verified: 2026-07-05
---
# SN_Integration


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, BusinessUnits, CompanyBranches, Cur_Banks, Cur_ItemsCategories, CustomersTypes, IntegrationErrorLog, ItemsCategories, Locations, PaymentsTypes, SN, SalesPersonsGroups. Writes Customers, CustomersFinancialDetails. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID nvarchar(50) = 1
## Tables Read
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- Cur_Banks
- Cur_ItemsCategories
- [[CustomersTypes]]
- [[IntegrationErrorLog]]
- [[ItemsCategories]]
- [[Locations]]
- [[PaymentsTypes]]
- SN
- [[SalesPersonsGroups]]
## Tables Written
- [[Customers]]
- [[CustomersFinancialDetails]]
## Callers
_None (no known callers)_
## Callees
- [[SP_IntegrationErrorLog]]
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- Cur_Banks
- Cur_ItemsCategories
- [[CustomersTypes]]
- [[IntegrationErrorLog]]
- [[ItemsCategories]]
- [[Locations]]
- [[PaymentsTypes]]
- SN
- [[SalesPersonsGroups]]

**Tables Written**
- [[Customers]]
- [[CustomersFinancialDetails]]

**Callers**
- [[SP_IntegrationErrorLog]]

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
