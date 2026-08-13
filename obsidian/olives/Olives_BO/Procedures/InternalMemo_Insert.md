---
type: procedure
database: Olives_BO
name: InternalMemo_Insert
schema: dbo
tags: [#backoffice]
reads_from:
  - [[IntenalMemoApprove]]
  - [[InternalMemo]]
  - [[SalesPersons]]
writes_to:
  - [[IntenalMemoApprove]]
  - [[InternalMemo]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# InternalMemo_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads IntenalMemoApprove, InternalMemo, SalesPersons. Writes IntenalMemoApprove, InternalMemo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @TrDateTime datetime
- @SalesmanNo int
- @MemoSubject nvarchar (1000)
- @MemoDepartment nvarchar (1000)
- @MemoDescription nvarchar (MAX)
- @FirstApproval bit=0
- @FirstApprovalDescription nvarchar (MAX)=''
- @FirstApprovalUserID varchar (50)=''
- @SecondApproval bit=0
- @SecondApprovalDescription nvarchar (MAX)=''
- @SecondApprovalUserID varchar (50)=''
- @DeviceSysID varchar (50)
- @CustID varchar (50)
- @ErrNo SmallInt Output
## Tables Read
- [[IntenalMemoApprove]]
- [[InternalMemo]]
- [[SalesPersons]]
## Tables Written
- [[IntenalMemoApprove]]
- [[InternalMemo]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[IntenalMemoApprove]]
- [[InternalMemo]]
- [[SalesPersons]]

**Tables Written**
- [[IntenalMemoApprove]]
- [[InternalMemo]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
