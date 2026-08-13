---
type: procedure
database: Olives_BO
name: RPT_ZalloumReportONE
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[CustomersFinancialDetails]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[LogActionTransaction]]
  - [[SalesPersons]]
  - [[SalesPersonsRoutes]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-07-05
---
# RPT_ZalloumReportONE


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersFinancialDetails, Items, ItemsCategories, LogActionTransaction, SalesPersons, SalesPersonsRoutes, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromSalesmanID int
- @ToSalesmanID int
- @RouatDate smalldatetime
## Tables Read
- [[CustomersFinancialDetails]]
- [[Items]]
- [[ItemsCategories]]
- [[LogActionTransaction]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
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
- [[CustomersFinancialDetails]]
- [[Items]]
- [[ItemsCategories]]
- [[LogActionTransaction]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
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
