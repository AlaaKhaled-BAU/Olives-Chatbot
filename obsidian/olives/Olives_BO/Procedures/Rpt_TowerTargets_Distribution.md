---
type: procedure
database: Olives_BO
name: Rpt_TowerTargets_Distribution
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - [[CustomerStockTacking]]
  - [[CustomerStockTackingDetails]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[Items]]
  - [[SalesPersons]]
  - [[SalespersonCustStockItemsTargetLink]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_TowerTargets_Distribution


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerStockTacking, CustomerStockTackingDetails, Customers, CustomersFinancialDetails, Items, SalesPersons, SalespersonCustStockItemsTargetLink. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
- @SalesmanNo int
- @FromDate smalldatetime
- @ToDate smalldatetime
## Tables Read
- [[CustomerStockTacking]]
- [[CustomerStockTackingDetails]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Items]]
- [[SalesPersons]]
- [[SalespersonCustStockItemsTargetLink]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomerStockTacking]]
- [[CustomerStockTackingDetails]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Items]]
- [[SalesPersons]]
- [[SalespersonCustStockItemsTargetLink]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
