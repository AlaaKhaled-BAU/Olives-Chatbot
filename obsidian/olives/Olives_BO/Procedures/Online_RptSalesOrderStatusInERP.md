---
type: procedure
database: Olives_BO
name: Online_RptSalesOrderStatusInERP
schema: dbo
tags: [#backoffice, #integration, #order, #sales]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - DB
  - [[SalesOrderHistoryDF]]
  - [[SalesOrderHistoryHF]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Online_RptSalesOrderStatusInERP


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, CustomersFinancialDetails, DB, SalesOrderHistoryDF, SalesOrderHistoryHF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int =1
- @SalesmanNo int =1
- @FromDate smalldatetime ='2020-01-01'
- @ToDate smalldatetime ='2022-01-31'
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- DB
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
- [[CustomersFinancialDetails]]
- DB
- [[SalesOrderHistoryDF]]
- [[SalesOrderHistoryHF]]

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
