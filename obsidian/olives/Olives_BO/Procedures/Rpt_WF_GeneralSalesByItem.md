---
type: procedure
database: Olives_BO
name: Rpt_WF_GeneralSalesByItem
schema: dbo
tags: [#auth, #backoffice, #inventory, #reporting, #sales, #workflow]
reads_from:
  - [[ClientsActive]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
writes_to:
called_by:
  - 192
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_WF_GeneralSalesByItem


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Items, ItemsCategories, OrdersDetails, OrdersHeaders, SalesPersons. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = null
- @FromCustomer bigint
- @ToCustomer bigint
- @FromCateg varchar (10)
- @ToCateg varchar(10)
- @FromDate smalldatetime
- @ToDate smalldatetime
- @Parent int = NULL
- @FromSales int
- @ToSales int
## Tables Read
- [[ClientsActive]]
- [[Items]]
- [[ItemsCategories]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- 192
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Items]]
- [[ItemsCategories]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]

**Tables Written**
_None_

**Callers**
- 192

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
