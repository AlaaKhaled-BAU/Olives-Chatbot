---
type: procedure
database: Olives_BO
name: Rpt_OrdersDeliveryDrivers
schema: dbo
tags: [#backoffice, #order, #reporting]
reads_from:
  - [[Customers]]
  - [[OrdersHeaders]]
  - [[SalesOrderDeliveryHF]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_OrdersDeliveryDrivers


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, OrdersHeaders, SalesOrderDeliveryHF, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @FromDate smalldatetime = '2022-10-01'
- @ToDate smalldatetime= '2024-10-22'
- @FromSalesperosnsID int = 0
- @ToSalesperosnsID int = 999999
- @FromCustID Bigint=0
- @ToCustID Bigint=99999999999999
## Tables Read
- [[Customers]]
- [[OrdersHeaders]]
- [[SalesOrderDeliveryHF]]
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
- [[OrdersHeaders]]
- [[SalesOrderDeliveryHF]]
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
