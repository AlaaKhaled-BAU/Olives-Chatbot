---
type: procedure
database: Olives_BO
name: BO_Online_RptCustomerSalesTargetDetails
schema: dbo
tags: [#backoffice, #customer, #sales]
reads_from:
  - [[ClientsActive]]
  - [[CustomerTargets]]
  - [[CustomerTargetsDetails]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
  - [[Items]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesOrderHistoryDF]]
  - [[SalesOrderHistoryHF]]
  - [[SalesPersons]]
  - [[TargetsReferences]]
  - [[TransactionsDetails]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# BO_Online_RptCustomerSalesTargetDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, CustomerTargets, CustomerTargetsDetails, Customers, CustomersFinancialDetails, InvoiceHistoryDF, InvoiceHistoryHF, Items, OrdersDetails, OrdersHeaders, SalesOrderHistoryDF, SalesOrderHistoryHF, SalesPersons, TargetsReferences, TransactionsDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint=1
- @SalesmanNo int=43
- @FromSalesman int=1
- @ToSalesman int=99999
- @TargetYear smallint=2023
- @TargetMonth smallint=2
- @TargetType smallint=1
## Tables Read
- [[ClientsActive]]
- [[CustomerTargets]]
- [[CustomerTargetsDetails]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesOrderHistoryDF]]
- [[SalesOrderHistoryHF]]
- [[SalesPersons]]
- [[TargetsReferences]]
- [[TransactionsDetails]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[CustomerTargets]]
- [[CustomerTargetsDetails]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesOrderHistoryDF]]
- [[SalesOrderHistoryHF]]
- [[SalesPersons]]
- [[TargetsReferences]]
- [[TransactionsDetails]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
