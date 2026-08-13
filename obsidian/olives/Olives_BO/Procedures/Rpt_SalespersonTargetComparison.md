---
type: procedure
database: Olives_BO
name: Rpt_SalespersonTargetComparison
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - Fun_ConvArrayToTable
  - [[Items]]
  - [[SalesPersons]]
  - [[TargetsReferences]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalespersonTargetComparison


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_ConvArrayToTable, Items, SalesPersons, TargetsReferences, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=1
- @FirstComparisonYear int=2023
- @SecondComparisonYear int=2024
- @FirstComparisonMonth int=12
- @SecondComparisonMonth int=1
- @SalesmanArray VARCHAR(MAX) = '1001,1017,'
- @TargetRef VARCHAR(MAX) = '1,26,'
## Tables Read
- Fun_ConvArrayToTable
- [[Items]]
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
- Fun_ConvArrayToTable
- [[Items]]
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
