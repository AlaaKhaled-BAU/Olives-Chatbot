---
type: procedure
database: Olives_BO
name: Rpt_SalesmanSummaryRoute
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - Fun_ConvArrayToTable
  - [[LogActionTransaction]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[Receipts]]
  - [[Receipts_Currency]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[SalesPersonsRoutes]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
  - [[Rpt_SalesmanSummaryRoute_Atieh]]
  - Rpt_SalesmanSummaryRoute_Sparten
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanSummaryRoute


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, CustomersFinancialDetails, Fun_ConvArrayToTable, LogActionTransaction, OrdersDetails, OrdersHeaders, Receipts, Receipts_Currency, SalesPersons, SalesPersonsGroups, SalesPersonsRoutes, TransactionsDetails, TransactionsHeaders. Calls 2 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint=1
- @FromDate smalldatetime='2023-10-03'
- @FromSalesman int=1
- @ToSalesman int=999999
- @FromGroup int = 0
- @ToGroup int = 99999999
- @Salesman nvarchar(max)= '104,105,106,107,108,109,110,111,112,113,37,138,139,140,141,'
- @ToDate smalldatetime = NULL
- @GPSVisit BIT =NULL
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_ConvArrayToTable
- [[LogActionTransaction]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[Receipts_Currency]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[SalesPersonsRoutes]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- [[Rpt_SalesmanSummaryRoute_Atieh]]
- Rpt_SalesmanSummaryRoute_Sparten
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_ConvArrayToTable
- [[LogActionTransaction]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[Receipts_Currency]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[SalesPersonsRoutes]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

**Tables Written**
_None_

**Callers**
- [[Rpt_SalesmanSummaryRoute_Atieh]]
- Rpt_SalesmanSummaryRoute_Sparten

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
