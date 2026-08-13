---
type: procedure
database: Olives_BO
name: Rpt_DailyDriver
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[Customers]]
  - [[SalesOrderHistoryDF]]
  - [[SalesOrderHistoryHF]]
  - [[SalesPersonsGroups]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_DailyDriver


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, SalesOrderHistoryDF, SalesOrderHistoryHF, SalesPersonsGroups. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int = 1
- @FromDate smalldatetime ='2019-02-25'
- @ToDate smalldatetime ='2019-02-25'
- @FromSalesmanNo int = 0
- @ToSalesmanNo int = 999999
## Tables Read
- [[Customers]]
- [[SalesOrderHistoryDF]]
- [[SalesOrderHistoryHF]]
- [[SalesPersonsGroups]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[SalesOrderHistoryDF]]
- [[SalesOrderHistoryHF]]
- [[SalesPersonsGroups]]

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
