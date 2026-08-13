---
type: procedure
database: Olives_BO
name: OT_ImportSalesmanDoneProcedures
schema: dbo
tags: [#backoffice, #mobile, #sales]
reads_from:
  - [[SalesPersons]]
  - [[SalespersonsProcedures]]
  - `dbo`
writes_to:
  - [[OT_SalesmanDoneProcedures]]
  - [[SalespersonsProcedures]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportSalesmanDoneProcedures


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalesPersons, SalespersonsProcedures, dbo. Writes OT_SalesmanDoneProcedures, SalespersonsProcedures. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[SalesPersons]]
- [[SalespersonsProcedures]]
- `dbo`
## Tables Written
- [[OT_SalesmanDoneProcedures]]
- [[SalespersonsProcedures]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalesPersons]]
- [[SalespersonsProcedures]]
- dbo

**Tables Written**
- [[OT_SalesmanDoneProcedures]]
- [[SalespersonsProcedures]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
