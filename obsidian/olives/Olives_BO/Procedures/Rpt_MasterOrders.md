---
type: procedure
database: Olives_BO
name: Rpt_MasterOrders
schema: dbo
tags: [#backoffice, #order, #reporting]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[DeliveryProvaD]]
  - [[DeliveryProvaH]]
  - Fun_GetCompanyBranchesByUser
  - [[InvoiceDeliveryDF]]
  - [[InvoiceDeliveryHF]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[RequestToExceedCheckDueDate]]
  - [[RequestToExceedCustomerCreditLimitInOrder]]
  - [[SalesOrderHistoryDF]]
  - [[SalesOrderHistoryHF]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_MasterOrders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, DeliveryProvaD, DeliveryProvaH, Fun_GetCompanyBranchesByUser, InvoiceDeliveryDF, InvoiceDeliveryHF, Items, ItemsUnits, OrdersDetails, OrdersHeaders, RequestToExceedCheckDueDate, RequestToExceedCustomerCreditLimitInOrder, SalesOrderHistoryDF, SalesOrderHistoryHF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @FromOrdNo bigint=1
- @ToOrdNo bigint=9999999
- @FromDate smalldatetime='2014-01-01'
- @ToDate smalldatetime='2023-09-01'
- @FromSalesman int=1
- @ToSalesman int =9999999
- @UserID nvarchar(50)='admin'
- @InvType smallint = -1
- @FromDeliveyDate smalldatetime='2014-01-01'
- @ToDeliveyDate smalldatetime='2023-09-01'
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[DeliveryProvaD]]
- [[DeliveryProvaH]]
- Fun_GetCompanyBranchesByUser
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[Items]]
- [[ItemsUnits]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[RequestToExceedCheckDueDate]]
- [[RequestToExceedCustomerCreditLimitInOrder]]
- [[SalesOrderHistoryDF]]
- [[SalesOrderHistoryHF]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Customers]]
- [[DeliveryProvaD]]
- [[DeliveryProvaH]]
- Fun_GetCompanyBranchesByUser
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[Items]]
- [[ItemsUnits]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[RequestToExceedCheckDueDate]]
- [[RequestToExceedCustomerCreditLimitInOrder]]
- [[SalesOrderHistoryDF]]
- [[SalesOrderHistoryHF]]

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
