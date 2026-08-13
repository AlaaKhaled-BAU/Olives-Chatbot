---
type: procedure
database: Olives_BO
name: Rpt_DeliverySales
schema: dbo
tags: [#backoffice, #order, #reporting, #sales]
reads_from:
  - [[CarAndSalespersonLink]]
  - [[DeliveryCars]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_DeliverySales


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CarAndSalespersonLink, DeliveryCars, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @FromDate smalldatetime = '2020-08-19'
- @ToDate smalldatetime = '2024-08-19'
- @FromSalesman int =3003
- @ToSalesman int =3003
## Tables Read
- [[CarAndSalespersonLink]]
- [[DeliveryCars]]
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
- [[CarAndSalespersonLink]]
- [[DeliveryCars]]
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
