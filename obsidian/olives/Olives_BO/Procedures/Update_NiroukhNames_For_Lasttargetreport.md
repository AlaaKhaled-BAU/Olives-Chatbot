---
type: procedure
database: Olives_BO
name: Update_NiroukhNames_For_Lasttargetreport
schema: dbo
tags: [#reporting, #maintenance]
reads_from:
  - ClientsActive
  - Customers
writes_to:
  - Companies
  - SpecialCustomerTarget
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Update_NiroukhNames_For_Lasttargetreport

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 2 table(s); writes 2. See sections below for the full dependency map.
## Parameters
- @CompanyID int
## Tables Read
- [[ClientsActive]]
- [[Customers]]
## Tables Written
- [[Companies]]
- [[SpecialCustomerTarget]]
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
