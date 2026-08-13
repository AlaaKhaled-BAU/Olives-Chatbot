---
type: procedure
database: Olives_BO
name: Technical_InssertintFinancialfromFirstFinancialLink
schema: dbo
tags: [#maintenance]
reads_from:
  - TechnicalFinancialInsertTable_Temp
writes_to:
  - CustomersFinancialDetails
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Technical_InssertintFinancialfromFirstFinancialLink

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 1 table(s); writes 1. See sections below for the full dependency map.
## Parameters
- @compno int
## Tables Read
- [[TechnicalFinancialInsertTable_Temp]]
## Tables Written
- [[CustomersFinancialDetails]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
_None_
## When to Run

Maintenance/one-off fix: run under DBA supervision; verify row counts before and after.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
