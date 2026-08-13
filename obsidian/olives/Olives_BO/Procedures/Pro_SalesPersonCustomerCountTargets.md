---
type: procedure
database: Olives_BO
name: Pro_SalesPersonCustomerCountTargets
schema: dbo
tags: [#backoffice]
reads_from:
  - Excel
  - SalesPersons
  - TargetsReferences
writes_to:
  - SalesPersonCustomerCountTargetsDF
  - SalesPersonCustomerCountTargetsHF
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Pro_SalesPersonCustomerCountTargets

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 3 table(s); writes 2. See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @SalesPersonID int
- @TargetYear int
- @TargetMonth int
- @TargetReferenceID int
- @CustomerCount int
- @cmdType varchar(50)
## Tables Read
- [[Excel]]
- [[SalesPersons]]
- [[TargetsReferences]]
## Tables Written
- [[SalesPersonCustomerCountTargetsDF]]
- [[SalesPersonCustomerCountTargetsHF]]
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
