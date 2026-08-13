---
type: procedure
database: Olives_BO
name: Wings_Integ_Send_StatmentOfAccount
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Customers]]
  - WACC
  - XBT
  - cccc
  - `dbo`
writes_to:
  - [[OT_StateAccBalance]]
  - XBT
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Wings_Integ_Send_StatmentOfAccount


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, WACC, XBT, cccc, dbo. Writes OT_StateAccBalance, XBT. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
- @SalesmanNo int = 21
- @SendDate smalldatetime = '2019-07-20'
## Tables Read
- [[Customers]]
- WACC
- XBT
- cccc
- `dbo`
## Tables Written
- [[OT_StateAccBalance]]
- XBT
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- WACC
- XBT
- cccc
- dbo

**Tables Written**
- [[OT_StateAccBalance]]
- XBT

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
