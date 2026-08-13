---
type: procedure
database: Olives_BO
name: SoftInteg_SendNewCustomers
schema: dbo
tags: [#integration]
reads_from:
  - Customers
  - CustomersTypes
  - Locations
  - SalesPersons
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# SoftInteg_SendNewCustomers

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 4 table(s). See sections below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[Customers]]
- [[CustomersTypes]]
- [[Locations]]
- [[SalesPersons]]
## Tables Written
_None_
## Cross-DB Tables
References tables in **OSFA_DB** (qualified as `OSFA_DB.dbo.*`):
- [[OSFA_DB/Tables/OT_NewCustomers|OT_NewCustomers]]
## Callers
_None_
## Callees
_None_
## When to Run

Run during API sync cycles: pulls from or pushes to an external ERP/API when new data is ready or on-demand refresh.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
