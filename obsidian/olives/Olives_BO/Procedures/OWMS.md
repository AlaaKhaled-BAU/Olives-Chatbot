---
type: procedure
database: Olives_BO
name: OWMS
schema: dbo
tags: [#backoffice]
reads_from:
  - ApprovedByHandHeld
  - GLCRBMF
  - GLDEPMF
  - GLN_UsersDept
  - InvBatchsMF
  - InvItemsMF
  - InvSItemsMF
  - InvStoreUsers
  - InvStoresMF
  - InvUnitCodes
  - Invt_TransferOrderDF
  - Invt_TransferOrderHF
  - OrdRecDF
  - OrdRecHF
  - OrderDF
writes_to:
  - ApprovedByHandHeld
  - InvBatchsMF
  - Invt_TransferOrderHF
  - TransactionsByHandHeld
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OWMS


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ApprovedByHandHeld, GLCRBMF, GLDEPMF, GLN_UsersDept, InvBatchsMF, InvItemsMF, InvSItemsMF, InvStoreUsers, InvStoresMF, InvUnitCodes, Invt_TransferOrderDF, Invt_TransferOrderHF, OrdRecDF, OrdRecHF, OrderDF. Writes ApprovedByHandHeld, InvBatchsMF, Invt_TransferOrderHF, TransactionsByHandHeld. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint=null
- @CmdType nvarchar(100)
- @UserName nvarchar(100)=null
- @StoreNo int=null
- @ItemNo varchar(100)=null
- @BatchNo varchar(100)='1'
- @DeptNo int=null
- @TrDate smalldatetime=null
- @VouYear smallint = null
- @VouType smallint = null
- @VouNo int = null
- @DocNo nvarchar(100) = null
- @OrderNo  int= null
- @OrdYear smallint= null
- @TawreedNo varchar(20)= null
- @ExtraRecPer Int=0
- @ChkNewItemCount int = 0
- @Qty money =0
- @DeviceID nvarchar(100)=null
- @ActionID int = null
## Tables Read
- ApprovedByHandHeld
- GLCRBMF
- GLDEPMF
- GLN_UsersDept
- InvBatchsMF
- InvItemsMF
- InvSItemsMF
- InvStoreUsers
- InvStoresMF
- InvUnitCodes
- Invt_TransferOrderDF
- Invt_TransferOrderHF
- OrdRecDF
- OrdRecHF
- OrderDF
## Tables Written
- ApprovedByHandHeld
- InvBatchsMF
- Invt_TransferOrderHF
- TransactionsByHandHeld
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- ApprovedByHandHeld
- GLCRBMF
- GLDEPMF
- GLN_UsersDept
- InvBatchsMF
- InvItemsMF
- InvSItemsMF
- InvStoreUsers
- InvStoresMF
- InvUnitCodes
- Invt_TransferOrderDF
- Invt_TransferOrderHF
- OrdRecDF
- OrdRecHF
- OrderDF

**Tables Written**
- ApprovedByHandHeld
- InvBatchsMF
- Invt_TransferOrderHF
- TransactionsByHandHeld

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
