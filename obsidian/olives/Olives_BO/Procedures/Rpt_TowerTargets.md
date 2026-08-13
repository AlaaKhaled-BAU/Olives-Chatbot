---
type: procedure
database: Olives_BO
name: Rpt_TowerTargets
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - [[CustomerStockTacking]]
  - [[CustomerStockTackingDetails]]
  - [[CustomersFinancialDetails]]
  - Fun_GetInvoiceTotalAmountForHis
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
  - [[Items]]
  - [[LogActionTransaction]]
  - [[SalesPersonTargetsDetails]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[SalesPersonsRoutes]]
  - [[SalespersonCustStockItemsTargetLink]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_TowerTargets


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerStockTacking, CustomerStockTackingDetails, CustomersFinancialDetails, Fun_GetInvoiceTotalAmountForHis, InvoiceHistoryDF, InvoiceHistoryHF, Items, LogActionTransaction, SalesPersonTargetsDetails, SalesPersons, SalesPersonsGroups, SalesPersonsRoutes, SalespersonCustStockItemsTargetLink. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int=1
- @SalesmanNo int
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FotTablet bit=1
## Tables Read
- [[CustomerStockTacking]]
- [[CustomerStockTackingDetails]]
- [[CustomersFinancialDetails]]
- Fun_GetInvoiceTotalAmountForHis
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[LogActionTransaction]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[SalesPersonsRoutes]]
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
- [[CustomersFinancialDetails]]
- Fun_GetInvoiceTotalAmountForHis
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[LogActionTransaction]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[SalesPersonsRoutes]]
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
