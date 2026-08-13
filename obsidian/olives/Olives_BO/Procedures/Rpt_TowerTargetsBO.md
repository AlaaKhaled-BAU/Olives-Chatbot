---
type: procedure
database: Olives_BO
name: Rpt_TowerTargetsBO
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - [[CustomerStockTacking]]
  - [[CustomerStockTackingDetails]]
  - [[CustomersFinancialDetails]]
  - Fun_GetInvoiceTotalAmount
  - Fun_GetSalesmanTreeByID
  - [[Items]]
  - [[LogActionTransaction]]
  - [[SalesPersonTargetsDetails]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[SalesPersonsRoutes]]
  - [[SalespersonCustStockItemsTargetLink]]
  - [[SalespersonTargetReferenceFocusItem]]
  - Sup_Cur
  - [[TargetsReferences]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_TowerTargetsBO


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerStockTacking, CustomerStockTackingDetails, CustomersFinancialDetails, Fun_GetInvoiceTotalAmount, Fun_GetSalesmanTreeByID, Items, LogActionTransaction, SalesPersonTargetsDetails, SalesPersons, SalesPersonsGroups, SalesPersonsRoutes, SalespersonCustStockItemsTargetLink, SalespersonTargetReferenceFocusItem, Sup_Cur, TargetsReferences. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int=1
- @FromSupNo int=7
- @ToSupNo int=7
- @FromDate smalldatetime='2020-11-01'
- @ToDate smalldatetime='2020-11-30'
## Tables Read
- [[CustomerStockTacking]]
- [[CustomerStockTackingDetails]]
- [[CustomersFinancialDetails]]
- Fun_GetInvoiceTotalAmount
- Fun_GetSalesmanTreeByID
- [[Items]]
- [[LogActionTransaction]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[SalesPersonsRoutes]]
- [[SalespersonCustStockItemsTargetLink]]
- [[SalespersonTargetReferenceFocusItem]]
- Sup_Cur
- [[TargetsReferences]]
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
- [[CustomersFinancialDetails]]
- Fun_GetInvoiceTotalAmount
- Fun_GetSalesmanTreeByID
- [[Items]]
- [[LogActionTransaction]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[SalesPersonsRoutes]]
- [[SalespersonCustStockItemsTargetLink]]
- [[SalespersonTargetReferenceFocusItem]]
- Sup_Cur
- [[TargetsReferences]]

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
