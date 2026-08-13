---
type: procedure
database: Olives_BO
name: TechnicalInsertItemsassignment_invoicehistory
schema: dbo
tags: [#maintenance]
reads_from:
  - SalesPersons
writes_to:
  - SalesPersonItemsAssignment
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# TechnicalInsertItemsassignment_invoicehistory

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 1 table(s); writes 1. See sections below for the full dependency map.
## Parameters
- @compno int
- @salesmanno int
## Tables Read
- [[SalesPersons]]
## Tables Written
- [[SalesPersonItemsAssignment]]
## Cross-DB Tables
References tables in **OSFA_DB** (qualified as `OSFA_DB.dbo.*`):
- [[OSFA_DB/Tables/OT_InvoiceHistoryDF|OT_InvoiceHistoryDF]]
- [[OSFA_DB/Tables/OT_InvoiceHistoryHF|OT_InvoiceHistoryHF]]
## Callers
_None_
## Callees
_None_
## When to Run

Maintenance/one-off fix: run under DBA supervision; verify row counts before and after.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
