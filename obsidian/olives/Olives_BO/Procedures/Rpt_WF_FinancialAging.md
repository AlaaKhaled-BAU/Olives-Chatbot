---
type: procedure
database: Olives_BO
name: Rpt_WF_FinancialAging
schema: dbo
tags: [#auth, #backoffice, #reporting, #workflow]
reads_from:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - OPENQUERY
  - [[SalesPersons]]
writes_to:
called_by:
  - db
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_WF_FinancialAging


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersFinancialDetails, OPENQUERY, SalesPersons. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = null
- @Parent int = NULL
- @FromSales int
- @ToSales int
- @FromDep int
- @ToDep int
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- OPENQUERY
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- db
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersFinancialDetails]]
- OPENQUERY
- [[SalesPersons]]

**Tables Written**
_None_

**Callers**
- db

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
