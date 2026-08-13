---
type: procedure
database: Olives_BO
name: Rpt_BackOrder
schema: dbo
tags: [#backoffice, #order, #reporting]
reads_from:
  - [[Customers]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_BackOrder


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Items, ItemsUnits, OrdersDetails, OrdersHeaders, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @FromDate  smalldatetime = null
- @ToDate  smalldatetime = null
- @SalesPersonID int = null
- @FromItem varchar(100) = '-1'
- @ToItem varchar(100) = '-1'
- @FromCustomer bigint = -1
- @ToCustomer bigint = -1
- @UserID nvarchar(50)=null
## Tables Read
- [[Customers]]
- [[Items]]
- [[ItemsUnits]]
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
- [[Items]]
- [[ItemsUnits]]
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
