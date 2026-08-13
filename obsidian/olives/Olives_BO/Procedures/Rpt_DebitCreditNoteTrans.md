---
type: procedure
database: Olives_BO
name: Rpt_DebitCreditNoteTrans
schema: dbo
tags: [#backoffice, #billing, #reporting]
reads_from:
  - [[Customers]]
  - [[DebitCreditNoteTrans]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_DebitCreditNoteTrans


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, DebitCreditNoteTrans, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo SmallInt=1
- @FromSalesman Int=1
- @ToSalesman Int=9999
- @FromDate SmallDateTime = '2021-11-01'
- @ToDate SmallDateTime = '2021-11-30'
## Tables Read
- [[Customers]]
- [[DebitCreditNoteTrans]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[DebitCreditNoteTrans]]
- [[SalesPersons]]

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
