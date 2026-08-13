---
type: procedure
database: Olives_BO
name: Rpt_SalesmanStockAndReturn
schema: dbo
tags: [#backoffice, #inventory, #order, #reporting, #sales]
reads_from:
  - [[Customers]]
  - [[Items]]
  - [[Receipts]]
  - [[SalesPersons]]
  - [[StockSettelmentCollection]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanStockAndReturn


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Items, Receipts, SalesPersons, StockSettelmentCollection, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=1
- @SalesPersonID int=78
- @date smalldatetime='2022-12-14'
- @cmdType varchar(50)='Total Return'
## Tables Read
- [[Customers]]
- [[Items]]
- [[Receipts]]
- [[SalesPersons]]
- [[StockSettelmentCollection]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[Items]]
- [[Receipts]]
- [[SalesPersons]]
- [[StockSettelmentCollection]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

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
