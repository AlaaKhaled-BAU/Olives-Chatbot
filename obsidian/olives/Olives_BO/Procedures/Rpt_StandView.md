---
type: procedure
database: Olives_BO
name: Rpt_StandView
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[Locations]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_StandView


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersFinancialDetails, Locations, RoutesInformation, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID  smallint =1
- @Fromcustomer int=1
- @Tocustomer int=999
- @FromSalesperson int=1
- @ToSalesperson int=9999
- @FromDate datetime = '2021-03-01 '
- @ToDate datetime = '2023-03-11 '
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Locations]]
- [[RoutesInformation]]
- [[SalesPersons]]
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
- [[CustomersFinancialDetails]]
- [[Locations]]
- [[RoutesInformation]]
- [[SalesPersons]]
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
