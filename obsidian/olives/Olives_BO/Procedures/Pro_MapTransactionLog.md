---
type: procedure
database: Olives_BO
name: Pro_MapTransactionLog
schema: dbo
tags: [#backoffice, #log]
reads_from:
  - CSales
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersTypes]]
  - [[LogActionTransaction]]
  - [[NoTransactionsReasons]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[PriceLists]]
  - [[Receipts]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
  - [[SalesPersonsRoutes]]
  - [[SurveyCustomers]]
  - [[Surveys]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Data-Sync-Cycle
---
# Pro_MapTransactionLog


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CSales, Customers, CustomersFinancialDetails, CustomersTypes, LogActionTransaction, NoTransactionsReasons, OrdersDetails, OrdersHeaders, PriceLists, Receipts, RoutesInformation, SalesPersons, SalesPersonsRoutes, SurveyCustomers, Surveys. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = null
- @SalesmanNo int = null
- @TrType int = null
- @TrDate smalldatetime = null
## Tables Read
- CSales
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[LogActionTransaction]]
- [[NoTransactionsReasons]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[PriceLists]]
- [[Receipts]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- [[SurveyCustomers]]
- [[Surveys]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- CSales
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersTypes]]
- [[LogActionTransaction]]
- [[NoTransactionsReasons]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[PriceLists]]
- [[Receipts]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- [[SurveyCustomers]]
- [[Surveys]]

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
