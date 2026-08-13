---
type: procedure
database: Olives_BO
name: Technical_CreateCustomersTransferQuery
schema: dbo
tags: [#maintenance]
reads_from:
  - Customers
  - CustomersFinancialDetails
  - RoutesInformation
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Technical_CreateCustomersTransferQuery

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 3 table(s). See sections below for the full dependency map.
## Parameters
_None_
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[RoutesInformation]]
## Tables Written
_None_
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
