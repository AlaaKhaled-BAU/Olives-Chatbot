---
type: procedure
database: Olives_BO
name: Rpt_CustomerSalesOrderByClassTablet
schema: dbo
tags: [#backoffice, #customer, #mobile, #order, #reference, #reporting, #sales]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[CustomersClasses]]
  - [[Items]]
  - [[Locations]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CustomerSalesOrderByClassTablet


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, CustomersClasses, Items, Locations, OrdersDetails, OrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @SalesmanNo int=3003
- @FromDate smalldatetime = '2020-01-01'
- @ToDate smalldatetime = '2025-12-31'
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[CustomersClasses]]
- [[Items]]
- [[Locations]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
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
- [[CustomersClasses]]
- [[Items]]
- [[Locations]]
- [[OrdersDetails]]
- [[OrdersHeaders]]

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
