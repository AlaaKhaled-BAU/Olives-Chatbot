---
type: procedure
database: Olives_BO
name: OMS
schema: dbo
tags: [#backoffice]
reads_from:
  - GLCRBMF
  - GLDEPMF
  - GLN_UsersDept
  - InvBatchsMF
  - InvItemsMF
  - InvSItemsMF
  - InvStoreUsers
  - InvStoresMF
  - [[Users]]
  - customer
  - glactmf
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OMS


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads GLCRBMF, GLDEPMF, GLN_UsersDept, InvBatchsMF, InvItemsMF, InvSItemsMF, InvStoreUsers, InvStoresMF, Users, customer, glactmf. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint=null
- @CmdType nvarchar(100)=null
- @UserName nvarchar(100)=null
- @StoreNo int=null
- @ItemNo varchar(100)=null
- @BatchNo varchar(100)=null
- @DeptNo int=null
## Tables Read
- GLCRBMF
- GLDEPMF
- GLN_UsersDept
- InvBatchsMF
- InvItemsMF
- InvSItemsMF
- InvStoreUsers
- InvStoresMF
- [[Users]]
- customer
- glactmf
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- GLCRBMF
- GLDEPMF
- GLN_UsersDept
- InvBatchsMF
- InvItemsMF
- InvSItemsMF
- InvStoreUsers
- InvStoresMF
- [[Users]]
- customer
- glactmf

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
