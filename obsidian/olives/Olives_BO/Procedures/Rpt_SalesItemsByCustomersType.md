---
type: procedure
database: Olives_BO
name: Rpt_SalesItemsByCustomersType
schema: dbo
tags: [#backoffice, #customer, #inventory, #reference, #reporting, #sales]
reads_from:
  - [[Customers]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesItemsByCustomersType


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersTypes, Items, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @FromItem nvarchar(50) = '0'
- @ToItem nvarchar(50) = 'zzzzzzzzzzzzzzzz'
- @FromDate smalldatetime = '2021-01-01'
- @ToDate smalldatetime = '2022-09-01'
- @FromCustType int = 0
- @ToCustType int = 9999
## Tables Read
- [[Customers]]
- [[CustomersTypes]]
- [[Items]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersTypes]]
- [[Items]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

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
