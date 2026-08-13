---
type: procedure
database: Olives_BO
name: Rpt_LuxuryItemsCustTarget
schema: dbo
tags: [#backoffice, #inventory, #reporting, #sales]
reads_from:
  - [[Customers]]
  - [[CustomersMonthlyCollectionTarget]]
  - [[Receipts]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_LuxuryItemsCustTarget


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersMonthlyCollectionTarget, Receipts. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int =1
- @Year int =2020
- @Month int =12
- @SalesmanNo int =27
## Tables Read
- [[Customers]]
- [[CustomersMonthlyCollectionTarget]]
- [[Receipts]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersMonthlyCollectionTarget]]
- [[Receipts]]

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
