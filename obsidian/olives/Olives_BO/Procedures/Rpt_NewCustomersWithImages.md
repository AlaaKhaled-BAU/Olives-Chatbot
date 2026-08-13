---
type: procedure
database: Olives_BO
name: Rpt_NewCustomersWithImages
schema: dbo
tags: [#backoffice, #customer, #reporting]
reads_from:
  - OSFA_DB
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_NewCustomersWithImages


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads OSFA_DB. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNO int =1
- @FromSalesMan int=0
- @ToSalesMan int=9999
- @FromDate date ='2020-01-01'
- @ToDate date ='2020-08-15'
## Tables Read
- OSFA_DB
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- OSFA_DB

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
