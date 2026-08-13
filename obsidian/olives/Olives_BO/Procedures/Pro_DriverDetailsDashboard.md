---
type: procedure
database: Olives_BO
name: Pro_DriverDetailsDashboard
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - CSales
  - [[ClientsActive]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - [[InvoiceDeliveryDF]]
  - [[InvoiceDeliveryHF]]
  - [[LogActionTransaction]]
  - [[NoTransactionsReasons]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[PriceLists]]
  - [[Receipts]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_DriverDetailsDashboard


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CSales, ClientsActive, Customers, CustomersFinancialDetails, CustomersTypes, InvoiceDeliveryDF, InvoiceDeliveryHF, LogActionTransaction, NoTransactionsReasons, OrdersDetails, OrdersHeaders, PriceLists, Receipts, RoutesInformation, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @SalesmanNo int = 3003
- @FromDate smalldatetime = '2021-01-01'
- @Todate smalldatetime='2022-01-01'
- @WithTax bit = 0
## Tables Read
- CSales
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[LogActionTransaction]]
- [[NoTransactionsReasons]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[PriceLists]]
- [[Receipts]]
- [[RoutesInformation]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- CSales
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[LogActionTransaction]]
- [[NoTransactionsReasons]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[PriceLists]]
- [[Receipts]]
- [[RoutesInformation]]
- [[SalesPersons]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
