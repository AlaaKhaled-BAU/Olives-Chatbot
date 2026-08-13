---
type: procedure
database: Olives_BO
name: Rpt_OrderLink
schema: dbo
tags: [#backoffice, #order, #reporting]
reads_from:
  - [[Customers]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesOrderDeliveryHF]]
  - [[SalesPersons]]
  - [[WF_SubLog]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_OrderLink


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, OrdersDetails, OrdersHeaders, SalesOrderDeliveryHF, SalesPersons, WF_SubLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @FromSales int=0
- @ToSales int=999999999
- @FromOrderNo int=0
- @ToOrderNo int=999999999
- @FromDate smalldatetime='2020-11-08'
- @ToDate smalldatetime ='2025-11-08'
## Tables Read
- [[Customers]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesOrderDeliveryHF]]
- [[SalesPersons]]
- [[WF_SubLog]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesOrderDeliveryHF]]
- [[SalesPersons]]
- [[WF_SubLog]]

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
