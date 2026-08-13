---
type: procedure
database: Olives_BO
name: Rpt_SalesmanRouteTargetDetails
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[CustomersFinancialDetails]]
  - Fun_GetInvoiceTotalAmount
  - GetSalesOrderTotalAmount
  - [[LogActionTransaction]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[SalesPersonsRoutes]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanRouteTargetDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersFinancialDetails, Fun_GetInvoiceTotalAmount, GetSalesOrderTotalAmount, LogActionTransaction, OrdersHeaders, SalesPersons, SalesPersonsGroups, SalesPersonsRoutes, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int= 2
- @Salesman int= 37
- @FromDate Smalldatetime='2025-04-01'
- @ToDate Smalldatetime='2025-04-14'
- @FromGroup    int = 0
- @ToGroup int =99999
## Tables Read
- [[CustomersFinancialDetails]]
- Fun_GetInvoiceTotalAmount
- GetSalesOrderTotalAmount
- [[LogActionTransaction]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[SalesPersonsRoutes]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomersFinancialDetails]]
- Fun_GetInvoiceTotalAmount
- GetSalesOrderTotalAmount
- [[LogActionTransaction]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[SalesPersonsRoutes]]
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
