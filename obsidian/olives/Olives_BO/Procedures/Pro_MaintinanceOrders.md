---
type: procedure
database: Olives_BO
name: Pro_MaintinanceOrders
schema: dbo
tags: [#backoffice, #order]
reads_from:
  - [[Customers]]
  - [[MaintinanceOrders]]
  - `dbo`
writes_to:
  - [[MaintinanceOrders]]
  - OT_TransAttachment
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MaintinanceOrders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, MaintinanceOrders, dbo. Writes MaintinanceOrders, OT_TransAttachment. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @AutoID int  = null
- @FirstApproval bit =null
- @FirstApprovalDescription nvarchar(MAX)=null
- @FirstApprovalUserID nvarchar(40) =null
- @SecondApproval bit =null
- @SecondApprovalDescription nvarchar(MAX)=null
- @SecondApprovalUserID nvarchar(40) =null
- @cmdType nvarchar(50)=null
- @FileName nvarchar(200)=null
- @SendToUserID nvarchar(50)=null
- @Attachment image=null
- @UserID   nvarchar(50)=null
## Tables Read
- [[Customers]]
- [[MaintinanceOrders]]
- `dbo`
## Tables Written
- [[MaintinanceOrders]]
- OT_TransAttachment
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[MaintinanceOrders]]
- dbo

**Tables Written**
- [[MaintinanceOrders]]
- OT_TransAttachment

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
