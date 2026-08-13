---
type: procedure
database: Olives_BO
name: AlWafi_GetSettlementInvoiceInfo
schema: dbo
tags: [#backoffice, #billing]
reads_from:
  - DB
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# AlWafi_GetSettlementInvoiceInfo


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads DB. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
- @VouYear smallint = 2023
- @VouNo int = 1000025
## Tables Read
- DB
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- DB

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
