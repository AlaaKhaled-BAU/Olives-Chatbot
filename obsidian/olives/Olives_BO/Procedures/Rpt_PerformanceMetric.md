---
type: procedure
database: Olives_BO
name: Rpt_PerformanceMetric
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[CustomersFinancialDetails]]
  - [[Items]]
  - [[SalesPersonItemsAssignment]]
  - [[SalesPersonTargets]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_PerformanceMetric


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersFinancialDetails, Items, SalesPersonItemsAssignment, SalesPersonTargets, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @SalesPersonID int=3003
- @FromDate smalldatetime ='2025-01-01'
- @ToDate smalldatetime ='2025-0101'
- @NOS Float
- @NIS Float
- @S Float
- @UserID nvarchar(50) = null
## Tables Read
- [[CustomersFinancialDetails]]
- [[Items]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersonTargets]]
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
- [[CustomersFinancialDetails]]
- [[Items]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersonTargets]]
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
