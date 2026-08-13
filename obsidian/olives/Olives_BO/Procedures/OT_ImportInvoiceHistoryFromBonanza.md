---
type: procedure
database: Olives_BO
name: OT_ImportInvoiceHistoryFromBonanza
schema: dbo
tags: [#maintenance]
reads_from:
  - ClientsActive
  - Customers
writes_to:
  - InvoiceHistoryDF
  - InvoiceHistoryHF
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# OT_ImportInvoiceHistoryFromBonanza

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 2 table(s); writes 2. See sections below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[ClientsActive]]
- [[Customers]]
## Tables Written
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
_None_
## When to Run

Run when importing data from tablets/external files into the back-office (batch or scheduled import).

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
