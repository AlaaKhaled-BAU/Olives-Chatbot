---
type: procedure
database: Olives_BO
name: NPF_Integration
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Banks]]
  - [[BusinessUnits]]
  - [[Companies]]
  - [[CompanyBranches]]
  - Cur_Banks
  - Cur_Branches
  - [[CustomersTypes]]
  - [[IntegrationErrorLog]]
  - SALESSERVER
writes_to:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[PriceListDetails]]
  - [[PriceLists]]
called_by:
  - [[SP_IntegrationErrorLog]]
support_relevance: high
last_verified: 2026-07-05
---
# NPF_Integration


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, BusinessUnits, Companies, CompanyBranches, Cur_Banks, Cur_Branches, CustomersTypes, IntegrationErrorLog, SALESSERVER. Writes Customers, CustomersFinancialDetails, PriceListDetails, PriceLists. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID nvarchar(50) = 1
## Tables Read
- [[Banks]]
- [[BusinessUnits]]
- [[Companies]]
- [[CompanyBranches]]
- Cur_Banks
- Cur_Branches
- [[CustomersTypes]]
- [[IntegrationErrorLog]]
- SALESSERVER
## Tables Written
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[PriceListDetails]]
- [[PriceLists]]
## Callers
_None (no known callers)_
## Callees
- [[SP_IntegrationErrorLog]]
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[BusinessUnits]]
- [[Companies]]
- [[CompanyBranches]]
- Cur_Banks
- Cur_Branches
- [[CustomersTypes]]
- [[IntegrationErrorLog]]
- SALESSERVER

**Tables Written**
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[PriceListDetails]]
- [[PriceLists]]

**Callers**
- [[SP_IntegrationErrorLog]]

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
