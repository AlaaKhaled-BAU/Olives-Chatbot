---
type: procedure
database: Olives_BO
name: RPT_NIROUKHLOCATIONTARGET
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[Customers]]
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
  - [[Items]]
  - [[LocationTargetsDetails]]
  - [[Locations]]
  - [[TargetsReferences]]
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-07-05
---
# RPT_NIROUKHLOCATIONTARGET


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, InvoiceHistoryDF, InvoiceHistoryHF, Items, LocationTargetsDetails, Locations, TargetsReferences. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
_None_
## Tables Read
- [[Customers]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[LocationTargetsDetails]]
- [[Locations]]
- [[TargetsReferences]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[LocationTargetsDetails]]
- [[Locations]]
- [[TargetsReferences]]

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
