---
type: procedure
database: Olives_BO
name: Tablet_InvoiceHistoryByDate
schema: dbo
tags: [#backoffice]
reads_from:
  - ClientsActive
  - InvoiceHistoryDF
  - InvoiceHistoryHF
  - Items
  - SalesPersons
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Tablet_InvoiceHistoryByDate

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 5 table(s). See sections below for the full dependency map.
## Parameters
- @CompanyID int
- @SalesmanNo int
- @CustomerNo bigint
- @Header bit
- @FromDate smalldatetime
- @ToDate smalldatetime
## Tables Read
- [[ClientsActive]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[SalesPersons]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
_None_
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
