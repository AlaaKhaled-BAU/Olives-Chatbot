---
type: procedure
database: Olives_BO
name: Rpt_SalesmanSalesRecStatment_TahounehCenters
schema: dbo
tags: [#reporting]
reads_from:
  - Checks
  - ClientsActive
  - Customers
  - CustomersFinancialDetails
  - DocumentsTypes
  - PaymentsOrders
  - Receipts
  - Receipts_PaidTrans
  - RoutesInformation
  - SalesPersons
  - TransactionsDetails
  - TransactionsHeaders
  - TransactionsTypes
writes_to:
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# Rpt_SalesmanSalesRecStatment_TahounehCenters

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 13 table(s); calls 5 proc(s). See sections below for the full dependency map.
## Parameters
- @CompNo smallint
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromSalesman int
- @ToSalesman int
- @FromCustomer bigint
- @ToCustomer bigint
- @TrType nvarchar(50)
- @UserID nvarchar(50)
## Tables Read
- [[Checks]]
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[DocumentsTypes]]
- [[PaymentsOrders]]
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransactionsTypes]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `Fun_ConvArrayToTable`
- `Fun_GetCashInvoicesReceipts`
- `Fun_GetCompanyBranchesByUser`
- `Fun_GetFromDate`
- `Fun_GetSalesmanParentName`
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
