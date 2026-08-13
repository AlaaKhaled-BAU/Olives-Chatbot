---
type: procedure
database: Olives_BO
name: Rpt_OutStandingInvoices_online
schema: dbo
tags: [#backoffice, #billing, #reporting]
reads_from:
  - [[RecLinkInv]]
  - [[Customers]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_OutStandingInvoices_online


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads RecLinkInv, Customers. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @Compno int
- @CustomerID bigint
## Tables Read
- [[RecLinkInv]]
- [[Customers]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[RecLinkInv]]
- [[customers]]

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
