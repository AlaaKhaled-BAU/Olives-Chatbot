---
type: procedure
database: Olives_BO
name: AccPack_Integ_LuxuryItems_StatmentOfAccount
schema: dbo
tags: [#backoffice, #integration, #inventory]
reads_from:
  - [[CustomerStatmentOfAccount]]
  - [[Customers]]
  - TMPAccStat
  - XBT
  - cccc
  - `dbo`
  - where
writes_to:
  - [[CustomerStatmentOfAccount]]
  - XBT
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# AccPack_Integ_LuxuryItems_StatmentOfAccount


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerStatmentOfAccount, Customers, TMPAccStat, XBT, cccc, dbo, where. Writes CustomerStatmentOfAccount, XBT. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- TMPAccStat
- XBT
- cccc
- `dbo`
- where
## Tables Written
- [[CustomerStatmentOfAccount]]
- XBT
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- TMPAccStat
- XBT
- cccc
- dbo
- where

**Tables Written**
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
