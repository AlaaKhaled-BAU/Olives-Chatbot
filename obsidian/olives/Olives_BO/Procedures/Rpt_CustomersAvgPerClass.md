---
type: procedure
database: Olives_BO
name: Rpt_CustomersAvgPerClass
schema: dbo
tags: [#backoffice, #customer, #reference, #reporting]
reads_from:
  - [[CustomersFinancialDetails]]
  - [[Items]]
  - [[Positions]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CustomersAvgPerClass


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersFinancialDetails, Items, Positions, SalesPersons, SalesPersonsGroups, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @FromDate smalldatetime = '2022-04-01'
- @ToDate smalldatetime = '2022-05-19'
- @FromSalesmanGroup int = 0
- @ToSalesmanGroup int = 99999
- @FromSalesman int = 30
- @ToSalesman int = 31
- @FromItemNo nvarchar(100) = 'MP5071'
- @ToItemNo nvarchar(100) = 'MP5071'
## Tables Read
- [[CustomersFinancialDetails]]
- [[Items]]
- [[Positions]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
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
- [[Positions]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
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
