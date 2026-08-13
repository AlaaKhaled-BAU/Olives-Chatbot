---
type: procedure
database: Olives_BO
name: OWGM_AppService
schema: dbo
tags: [#backoffice]
reads_from:
  - [[OWGM_Gates]]
  - [[OWGM_GatesUsers]]
  - [[OWGM_LockLog]]
  - [[OWGM_Transactions]]
  - `dbo`
writes_to:
  - [[OWGM_Gates]]
  - [[OWGM_GatesUsers]]
  - [[OWGM_LockLog]]
  - [[OWGM_Transactions]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OWGM_AppService


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads OWGM_Gates, OWGM_GatesUsers, OWGM_LockLog, OWGM_Transactions, dbo. Writes OWGM_Gates, OWGM_GatesUsers, OWGM_LockLog, OWGM_Transactions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @CmdType nvarchar(200)
- @GateUserID int = null
- @AdminUserID nvarchar(200) = null
- @Barcode nvarchar(200) = null
- @TransType int =null
- @MacAddress nvarchar(200) = null
- @OpType int = null
## Tables Read
- [[OWGM_Gates]]
- [[OWGM_GatesUsers]]
- [[OWGM_LockLog]]
- [[OWGM_Transactions]]
- `dbo`
## Tables Written
- [[OWGM_Gates]]
- [[OWGM_GatesUsers]]
- [[OWGM_LockLog]]
- [[OWGM_Transactions]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OWGM_Gates]]
- [[OWGM_GatesUsers]]
- [[OWGM_LockLog]]
- [[OWGM_Transactions]]
- dbo

**Tables Written**
- [[OWGM_Gates]]
- [[OWGM_GatesUsers]]
- [[OWGM_LockLog]]
- [[OWGM_Transactions]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
