---
type: procedure
database: Olives_BO
name: Pro_InternalMemo
schema: dbo
tags: [#backoffice]
reads_from:
  - BEGIN
  - Blue
  - Fun_ConvArrayToTable
  - Fun_GetCompanyBranchesByUser
  - [[IntenalMemoApprove]]
  - [[InternalMemo]]
  - [[OlivesUserPermissions]]
  - [[SalesPersons]]
  - [[Users]]
  - `dbo`
  - if
writes_to:
  - [[IntenalMemoApprove]]
  - [[InternalMemo]]
  - OT_TransAttachment
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_InternalMemo


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads BEGIN, Blue, Fun_ConvArrayToTable, Fun_GetCompanyBranchesByUser, IntenalMemoApprove, InternalMemo, OlivesUserPermissions, SalesPersons, Users, dbo, if. Writes IntenalMemoApprove, InternalMemo, OT_TransAttachment. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @AutoID int  = null
- @FirstApproval bit =null
- @FirstApprovalDescription nvarchar(MAX)=null
- @FirstApprovalUserID nvarchar(40) =null
- @SecondApproval bit =null
- @SecondApprovalDescription nvarchar(MAX)=null
- @SecondApprovalUserID nvarchar(40) =null
- @cmdType nvarchar(50)='Select All First Approve'
- @SendToUserID nvarchar(50) = null
- @UserID nvarchar(50)='admin'
- @FromDate smalldatetime=NULL
- @ToDate smalldatetime=NULL
- @InternalMemoAutoID int=NULL
- @PostedLst nvarchar(1000)=null
- @MemoDescription nvarchar(Max)=null
- @MemoDepartment nvarchar(500)=null
- @MemoSubject nvarchar(500)=null
- @SalesmanNo int=null
- @Attachment image=null
- @FileName nvarchar(200)=null
- @DeviceSysID varchar(50) = null
- @FDate DateTime=null
- @TDate DateTime = null
## Tables Read
- BEGIN
- Blue
- Fun_ConvArrayToTable
- Fun_GetCompanyBranchesByUser
- [[IntenalMemoApprove]]
- [[InternalMemo]]
- [[OlivesUserPermissions]]
- [[SalesPersons]]
- [[Users]]
- `dbo`
- if
## Tables Written
- [[IntenalMemoApprove]]
- [[InternalMemo]]
- OT_TransAttachment
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- BEGIN
- Blue
- Fun_ConvArrayToTable
- Fun_GetCompanyBranchesByUser
- [[IntenalMemoApprove]]
- [[InternalMemo]]
- [[OlivesUserPermissions]]
- [[SalesPersons]]
- [[Users]]
- dbo
- if

**Tables Written**
- [[IntenalMemoApprove]]
- [[InternalMemo]]
- OT_TransAttachment

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
