---
type: procedure
database: Olives_BO
name: Rpt_SalesmanRouteEfficiency_SV_LV_TV2
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[ClientsActive]]
  - [[CustomersFinancialDetails]]
  - [[LogActionTransaction]]
  - [[OrdersHeaders]]
  - [[Receipts]]
  - SV_LV_TV
  - [[SalesPersons]]
  - [[SalesPersonsRoutes]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
  - [[Rpt_RouteSummaryBySalesmanCombineForEFF]]
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanRouteEfficiency_SV_LV_TV2


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, CustomersFinancialDetails, LogActionTransaction, OrdersHeaders, Receipts, SV_LV_TV, SalesPersons, SalesPersonsRoutes, TransactionsHeaders. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
- @Year smallint = 2018
- @Month smallint = 3
- @FromSalesman int = 0
- @ToSalesman int = 9999
- @FromBranch int = 0
- @ToBranch int = 999999
## Tables Read
- [[ClientsActive]]
- [[CustomersFinancialDetails]]
- [[LogActionTransaction]]
- [[OrdersHeaders]]
- [[Receipts]]
- SV_LV_TV
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- [[Rpt_RouteSummaryBySalesmanCombineForEFF]]
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[CustomersFinancialDetails]]
- [[LogActionTransaction]]
- [[OrdersHeaders]]
- [[Receipts]]
- SV_LV_TV
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- [[TransactionsHeaders]]

**Tables Written**
_None_

**Callers**
- [[Rpt_RouteSummaryBySalesmanCombineForEFF]]

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
