---
type: procedure
database: Olives_BO
name: Rpt_WF_SalesOrderStatus
schema: dbo
tags: [#auth, #backoffice, #order, #reporting, #sales, #workflow]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[OrdersHeaders]]
  - [[Positions]]
  - Rep_Cursor
  - [[SalesPersons]]
  - [[WF_MasterLog]]
  - [[WF_SubLog]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_WF_SalesOrderStatus


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, OrdersHeaders, Positions, Rep_Cursor, SalesPersons, WF_MasterLog, WF_SubLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @PositionID int = 647
- @FromDate smalldatetime='2022-12-01'
- @ToDate smalldatetime  ='2022-12-12'
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[OrdersHeaders]]
- [[Positions]]
- Rep_Cursor
- [[SalesPersons]]
- [[WF_MasterLog]]
- [[WF_SubLog]]
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
- [[OrdersHeaders]]
- [[Positions]]
- Rep_Cursor
- [[SalesPersons]]
- [[WF_MasterLog]]
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
