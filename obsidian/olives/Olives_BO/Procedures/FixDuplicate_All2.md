---
type: procedure
database: Olives_BO
name: FixDuplicate_All2
schema: dbo
tags: [#maintenance]
reads_from:
  - BusinessUnits
  - SalesPersons
writes_to:
  - Customers
  - CustomersFinancialDetails
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# FixDuplicate_All2

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 2 table(s); writes 2. See sections below for the full dependency map.
## Parameters
- @compno int
- @SALESMANNO int
## Tables Read
- [[BusinessUnits]]
- [[SalesPersons]]
## Tables Written
- [[Customers]]
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
