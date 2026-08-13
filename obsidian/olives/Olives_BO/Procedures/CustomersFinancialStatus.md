---
type: procedure
database: Olives_BO
name: CustomersFinancialStatus
schema: dbo
tags: [#backoffice, #customer]
reads_from:
  - [[OLV_PDC]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# CustomersFinancialStatus


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads OLV_PDC. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @compno int=1
- @FromDate smalldatetime='2022-08-20'
- @Todate smalldatetime='2024-08-20'
- @FromSalesman int
## Tables Read
- [[OLV_PDC]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OLV_PDC]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
