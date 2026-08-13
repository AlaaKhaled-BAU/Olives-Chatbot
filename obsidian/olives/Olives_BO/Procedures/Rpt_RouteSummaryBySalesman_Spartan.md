---
type: procedure
database: Olives_BO
name: Rpt_RouteSummaryBySalesman_Spartan
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - CSales
  - [[Checks]]
  - [[ClientsActive]]
  - [[Customers]]
  - [[CustomersClasses]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[Locations]]
  - [[LogActionTransaction]]
  - [[NoTransactionsReasons]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[PriceLists]]
  - [[Receipts]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_RouteSummaryBySalesman_Spartan


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CSales, Checks, ClientsActive, Customers, CustomersClasses, CustomersFinancialDetails, CustomersTypes, Items, Locations, LogActionTransaction, NoTransactionsReasons, OrdersDetails, OrdersHeaders, PriceLists, Receipts. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID_ smallint=1
- @FromDate_ smalldatetime='2023-03-06'
- @SalesmanNo_ int=3003
- @WithTax_ bit = 1
## Tables Read
- CSales
- [[Checks]]
- [[ClientsActive]]
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[Locations]]
- [[LogActionTransaction]]
- [[NoTransactionsReasons]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[PriceLists]]
- [[Receipts]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- CSales
- [[Checks]]
- [[ClientsActive]]
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[Items]]
- [[Locations]]
- [[LogActionTransaction]]
- [[NoTransactionsReasons]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[PriceLists]]
- [[Receipts]]

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
