---
type: procedure
database: Olives_BO
name: Rpt_SalesPersonCarLink
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - [[CarAndSalespersonLink]]
  - [[DeliveryCars]]
  - [[SalesPersons]]
  - [[SystemCodes]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesPersonCarLink


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CarAndSalespersonLink, DeliveryCars, SalesPersons, SystemCodes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @FromCarNo int=1
- @ToCarNo int=999999
- @FromSalesman bigint=1
- @ToSalesman bigint=999999999
- @CompanyID int=1
- @FromDate smalldatetime ='2023-01-5'
- @ToDate smalldatetime = '2024-03-5'
## Tables Read
- [[CarAndSalespersonLink]]
- [[DeliveryCars]]
- [[SalesPersons]]
- [[SystemCodes]]
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
- [[SystemCodes]]

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
