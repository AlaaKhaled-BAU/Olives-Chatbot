---
type: procedure
database: Olives_BO
name: CL_Integration
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[BusinessUnits]]
  - CLCL
  - [[Companies]]
  - [[CompanyBranches]]
  - Cur_ItemsCategories
  - [[CustomersTypes]]
  - [[IntegrationErrorLog]]
  - [[ItemsCategories]]
writes_to:
  - [[Customers]]
called_by:
  - [[SP_IntegrationErrorLog]]
support_relevance: high
last_verified: 2026-07-05
---
# CL_Integration


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads BusinessUnits, CLCL, Companies, CompanyBranches, Cur_ItemsCategories, CustomersTypes, IntegrationErrorLog, ItemsCategories. Writes Customers. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID nvarchar(50) = 1
## Tables Read
- [[BusinessUnits]]
- CLCL
- [[Companies]]
- [[CompanyBranches]]
- Cur_ItemsCategories
- [[CustomersTypes]]
- [[IntegrationErrorLog]]
- [[ItemsCategories]]
## Tables Written
- [[Customers]]
## Callers
_None (no known callers)_
## Callees
- [[SP_IntegrationErrorLog]]
## Impact / Dependencies

**Tables Read**
- [[BusinessUnits]]
- CLCL
- [[Companies]]
- [[CompanyBranches]]
- Cur_ItemsCategories
- [[CustomersTypes]]
- [[IntegrationErrorLog]]
- [[ItemsCategories]]

**Tables Written**
- [[Customers]]

**Callers**
- [[SP_IntegrationErrorLog]]

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
