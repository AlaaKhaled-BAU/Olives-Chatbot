---
type: procedure
database: Olives_BO
name: RPT_ZalloumReportTWO
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[Customers]]
  - [[CustomersClasses]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[SalesPersons]]
  - [[TargetsReferences]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-07-05
---
# RPT_ZalloumReportTWO


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersClasses, Items, ItemsCategories, SalesPersons, TargetsReferences, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompID int
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromSalesman int
- @ToSalesman int
- @FromCustomerID bigint
- @ToCustomerID bigint
## Tables Read
- [[Customers]]
- [[CustomersClasses]]
- [[Items]]
- [[ItemsCategories]]
- [[SalesPersons]]
- [[TargetsReferences]]
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
- [[CustomersClasses]]
- [[Items]]
- [[ItemsCategories]]
- [[SalesPersons]]
- [[TargetsReferences]]
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
