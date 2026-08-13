---
type: procedure
database: Olives_BO
name: Rpt_SalesmanSalesRecStatment
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - [[Checks]]
  - [[ClientsActive]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[DocumentsTypes]]
  - Fun_ConvArrayToTable
  - Fun_GetCashInvoicesReceipts
  - Fun_GetCompanyBranchesByUser
  - [[PaymentsOrders]]
  - [[Receipts]]
  - [[Receipts_PaidTrans]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanSalesRecStatment


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Checks, ClientsActive, Customers, CustomersFinancialDetails, DocumentsTypes, Fun_ConvArrayToTable, Fun_GetCashInvoicesReceipts, Fun_GetCompanyBranchesByUser, PaymentsOrders, Receipts, Receipts_PaidTrans, RoutesInformation, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromSalesman int
- @ToSalesman int
- @FromCustomer bigint
- @ToCustomer bigint
- @TrType nvarchar(50)=null
- @UserID nvarchar(50)=null
- @IsApprove bit = null
## Tables Read
- [[Checks]]
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[DocumentsTypes]]
- Fun_ConvArrayToTable
- Fun_GetCashInvoicesReceipts
- Fun_GetCompanyBranchesByUser
- [[PaymentsOrders]]
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[RoutesInformation]]
- [[SalesPersons]]
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
- [[Checks]]
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[DocumentsTypes]]
- Fun_ConvArrayToTable
- Fun_GetCashInvoicesReceipts
- Fun_GetCompanyBranchesByUser
- [[PaymentsOrders]]
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[RoutesInformation]]
- [[SalesPersons]]
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
