---
type: procedure
database: Olives_BO
name: Rpt_CustomerStatmentOfAccount
schema: dbo
tags: [#backoffice, #customer, #reporting]
reads_from:
  - [[CustomerStatmentOfAccount]]
  - [[Customers]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CustomerStatmentOfAccount


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerStatmentOfAccount, Customers. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=1
- @CustomerID int=314
- @FromDate datetime='2023-02-05'
- @ToDate datetime='2024-02-05'
## Tables Read
- [[CustomerStatmentOfAccount]]
- [[Customers]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomerStatmentOfAccount]]
- [[Customers]]

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
