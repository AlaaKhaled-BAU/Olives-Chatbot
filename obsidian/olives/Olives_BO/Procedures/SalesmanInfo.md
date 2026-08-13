---
type: procedure
database: Olives_BO
name: SalesmanInfo
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[Checks]]
  - [[CompetitveItemsDataDF]]
  - [[CompetitveItemsDataHF]]
  - [[CustomerStockTacking]]
  - [[CustomerStockTackingDetails]]
  - [[CustomersFinancialDetails]]
  - [[CustomersMonthlyCollectionTarget]]
  - [[InvoiceDeliveryDF]]
  - [[InvoiceDeliveryHF]]
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
  - [[LogActionTransaction]]
  - [[NewCompetitiveItems]]
  - [[NoTransactionsLog]]
  - [[OT_SendLog]]
writes_to:
  - [[SalesPersons]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# SalesmanInfo


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Checks, CompetitveItemsDataDF, CompetitveItemsDataHF, CustomerStockTacking, CustomerStockTackingDetails, CustomersFinancialDetails, CustomersMonthlyCollectionTarget, InvoiceDeliveryDF, InvoiceDeliveryHF, InvoiceHistoryDF, InvoiceHistoryHF, LogActionTransaction, NewCompetitiveItems, NoTransactionsLog, OT_SendLog. Writes SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=0
- @SalesPersonID int=0
- @PositionsID int=0
## Tables Read
- [[Checks]]
- [[CompetitveItemsDataDF]]
- [[CompetitveItemsDataHF]]
- [[CustomerStockTacking]]
- [[CustomerStockTackingDetails]]
- [[CustomersFinancialDetails]]
- [[CustomersMonthlyCollectionTarget]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[LogActionTransaction]]
- [[NewCompetitiveItems]]
- [[NoTransactionsLog]]
- [[OT_SendLog]]
## Tables Written
- [[SalesPersons]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Checks]]
- [[CompetitveItemsDataDF]]
- [[CompetitveItemsDataHF]]
- [[CustomerStockTacking]]
- [[CustomerStockTackingDetails]]
- [[CustomersFinancialDetails]]
- [[CustomersMonthlyCollectionTarget]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[LogActionTransaction]]
- [[NewCompetitiveItems]]
- [[NoTransactionsLog]]
- [[OT_SendLog]]

**Tables Written**
- [[SalesPersons]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
