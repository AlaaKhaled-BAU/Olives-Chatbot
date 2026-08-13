---
type: procedure
database: Olives_BO
name: Rpt_CustomerStockNotExistByDocType_Summary
schema: dbo
tags: [#backoffice, #customer, #inventory, #reference, #reporting]
reads_from:
  - [[CustomerStockTacking]]
  - [[CustomerStockTackingDetails]]
  - [[Items]]
  - [[ItemsCategories]]
  - OSFA_DB
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
  - [[Customers]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CustomerStockNotExistByDocType_Summary


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerStockTacking, CustomerStockTackingDetails, Items, ItemsCategories, OSFA_DB, OrdersDetails, OrdersHeaders, SalesPersons, Customers. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @FromSalesmanNo bigint=42
- @ToSalesmanNo bigint=42
- @FromCustomerNo  bigint=0
- @ToCustomerNo  bigint=9999999
- @FromDate smalldatetime='2024-04-07 00:00:00'
- @ToDate smalldatetime='2024-04-16 00:00:00'
## Tables Read
- [[CustomerStockTacking]]
- [[CustomerStockTackingDetails]]
- [[Items]]
- [[ItemsCategories]]
- OSFA_DB
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[Customers]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomerStockTacking]]
- [[CustomerStockTackingDetails]]
- [[Items]]
- [[ItemsCategories]]
- OSFA_DB
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[customers]]

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
