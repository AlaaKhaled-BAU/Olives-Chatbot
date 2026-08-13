---
type: procedure
database: Olives_BO
name: Rpt_SalesmanSales_ByMonths
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - [[Customers]]
  - [[Locations]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanSales_ByMonths


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Locations, SalesPersons, SalesPersonsGroups, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID SMALLINT
- @TransactionYear INT
- @FromSalesman INT
- @ToSalesman INT
- @FromLocation INT
- @ToLocation INT
- @FromGroup int = 0
- @ToGroup int = 99999999
- @UserID NVARCHAR(50)
## Tables Read
- [[Customers]]
- [[Locations]]
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
- [[Customers]]
- [[Locations]]
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
