---
type: procedure
database: Olives_BO
name: X3_Integ_SOA_Batches
schema: dbo
tags: [#backoffice, #integration, #inventory]
reads_from:
  - [[BatchsItemsInfo]]
  - [[Items]]
  - Olives_BO
  - SSMS
  - XBT
  - cccc
  - `dbo`
writes_to:
  - [[BatchsItemsInfo]]
  - [[CustomerStatmentOfAccount]]
  - XBT
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# X3_Integ_SOA_Batches


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads BatchsItemsInfo, Items, Olives_BO, SSMS, XBT, cccc, dbo. Writes BatchsItemsInfo, CustomerStatmentOfAccount, XBT. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
## Tables Read
- [[BatchsItemsInfo]]
- [[Items]]
- Olives_BO
- SSMS
- XBT
- cccc
- `dbo`
## Tables Written
- [[BatchsItemsInfo]]
- [[CustomerStatmentOfAccount]]
- XBT
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[BatchsItemsInfo]]
- [[Items]]
- Olives_BO
- SSMS
- XBT
- cccc
- dbo

**Tables Written**
- [[BatchsItemsInfo]]
- [[CustomerStatmentOfAccount]]
- XBT

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
