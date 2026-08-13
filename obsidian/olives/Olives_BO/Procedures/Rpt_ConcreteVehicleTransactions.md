---
type: procedure
database: Olives_BO
name: Rpt_ConcreteVehicleTransactions
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[Customers]]
  - Fun_GetOrdersDeliveredQtyTot
  - Fun_GetSalesOrderTotalAmount
  - [[InvoiceDeliveryDF]]
  - [[InvoiceDeliveryHF]]
  - [[LogActionTransaction]]
  - Olives_Images
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_ConcreteVehicleTransactions


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Fun_GetOrdersDeliveredQtyTot, Fun_GetSalesOrderTotalAmount, InvoiceDeliveryDF, InvoiceDeliveryHF, LogActionTransaction, Olives_Images, OrdersDetails, OrdersHeaders, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @FromDate smalldatetime='2023-12-18'
- @ToDate smalldatetime='2023-12-26'
- @FromCarNo int=1
- @ToCarNo int=999999
## Tables Read
- [[Customers]]
- Fun_GetOrdersDeliveredQtyTot
- Fun_GetSalesOrderTotalAmount
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[LogActionTransaction]]
- Olives_Images
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- Fun_GetOrdersDeliveredQtyTot
- Fun_GetSalesOrderTotalAmount
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[LogActionTransaction]]
- Olives_Images
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]

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
