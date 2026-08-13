---
type: procedure
database: Olives_BO
name: Rpt_TransactionsPrintStatusLog
schema: dbo
tags: [#backoffice, #log, #reporting]
reads_from:
  - [[LogActionTransaction]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_TransactionsPrintStatusLog


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads LogActionTransaction, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @FromDate smalldatetime='2024-1-1'
- @ToDate smalldatetime ='2025-1-1'
## Tables Read
- [[LogActionTransaction]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[LogActionTransaction]]
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
- [[Olives_BO/Procedures/Rpt_VoidOrder]]
