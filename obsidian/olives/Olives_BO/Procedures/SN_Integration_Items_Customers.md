---
type: procedure
database: Olives_BO
name: SN_Integration_Items_Customers
schema: dbo
tags: [#backoffice, #customer, #integration, #inventory]
reads_from:
  - Cur_Items
  - [[ItemsCategories]]
  - SN
writes_to:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
called_by:
  - [[SP_IntegrationErrorLog]]
support_relevance: high
last_verified: 2026-07-05
---
# SN_Integration_Items_Customers


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Cur_Items, ItemsCategories, SN. Writes Customers, CustomersFinancialDetails. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID nvarchar(50) = 1
## Tables Read
- Cur_Items
- [[ItemsCategories]]
- SN
## Tables Written
- [[Customers]]
- [[CustomersFinancialDetails]]
## Callers
_None (no known callers)_
## Callees
- [[SP_IntegrationErrorLog]]
## Impact / Dependencies

**Tables Read**
- Cur_Items
- [[ItemsCategories]]
- SN

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
