---
type: procedure
database: Olives_BO
name: Rpt_GpsLocationForTransaction
schema: dbo
tags: [#backoffice, #gps, #reporting]
reads_from:
  - [[Companies]]
  - [[Customers]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_GpsLocationForTransaction


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Companies, Customers, SalesPersons, SalesPersonsGroups, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int
- @FromSalesman int
- @ToSalesman int
- @FromCustomer bigint
- @ToCustomer bigint
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromGroup int = 0
- @ToGroup int = 99999999
## Tables Read
- [[Companies]]
- [[Customers]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Companies]]
- [[Customers]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
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
