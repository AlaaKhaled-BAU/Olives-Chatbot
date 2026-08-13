---
type: procedure
database: Olives_BO
name: Rpt_RouteScoreBySalesman
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[CustomersFinancialDetails]]
  - Fun_GetCompanyBranchesByUser
  - [[LogActionTransaction]]
  - [[OrdersHeaders]]
  - [[Receipts]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
  - [[Customers]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_RouteScoreBySalesman


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersFinancialDetails, Fun_GetCompanyBranchesByUser, LogActionTransaction, OrdersHeaders, Receipts, RoutesInformation, SalesPersons, TransactionsHeaders, Customers. Invoked by 2 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = null
- @FromDate smalldatetime = null
- @FromSalesmanNo int = 0
- @ToSalesmanNo int = 999999
- @UserID nvarchar(50) = null
## Tables Read
- [[CustomersFinancialDetails]]
- Fun_GetCompanyBranchesByUser
- [[LogActionTransaction]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- [[Customers]]
## Tables Written
_None_
## Callers
- [[Rpt_RouteScoreBySalesmanCombine]]
- [[Rpt_SalesOrdersSummaryBySalesman]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomersFinancialDetails]]
- Fun_GetCompanyBranchesByUser
- [[LogActionTransaction]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- [[customers]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
- [[Rpt_RouteScoreBySalesmanCombine]]
- [[Rpt_SalesOrdersSummaryBySalesman]]


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Olives_BO/Procedures/Rpt_VoidOrder]]
- [[Olives_BO/Procedures/Rpt_Hakkak_TargetReportFromAlpha]]
