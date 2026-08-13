---
type: procedure
database: Olives_BO
name: Rpt_Price
schema: dbo
tags: [#backoffice, #billing, #reporting]
reads_from:
  - [[Customers]]
  - [[Items]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - cte
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_Price


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Items, SalesPersons, TransactionsDetails, TransactionsHeaders, cte. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=1
- @FromSalesperson int =1
- @ToSalesperson int =99999999
- @FromCustomers bigint =1
- @ToCustomers bigint =99999999
## Tables Read
- [[Customers]]
- [[Items]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- cte
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
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- cte

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
