---
type: procedure
database: Olives_BO
name: OT_Send_StatmentOfAccount
schema: dbo
tags: [#backoffice, #mobile]
reads_from:
  - [[Customers]]
  - Fun_GetSalesmanStatmentOfAccount
  - XBT
  - cccc
  - `dbo`
writes_to:
  - [[Customers]]
  - [[OT_StateAccBalance]]
  - XBT
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_Send_StatmentOfAccount


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Fun_GetSalesmanStatmentOfAccount, XBT, cccc, dbo. Writes Customers, OT_StateAccBalance, XBT. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
- @SalesmanNo int = 1
- @SendDate smalldatetime = '2024-01-17'
## Tables Read
- [[Customers]]
- Fun_GetSalesmanStatmentOfAccount
- XBT
- cccc
- `dbo`
## Tables Written
- [[Customers]]
- [[OT_StateAccBalance]]
- XBT
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- Fun_GetSalesmanStatmentOfAccount
- XBT
- cccc
- dbo

**Tables Written**
- [[Customers]]
- [[OT_StateAccBalance]]
- XBT

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
