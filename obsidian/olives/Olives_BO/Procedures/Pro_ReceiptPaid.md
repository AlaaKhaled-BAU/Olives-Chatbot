---
type: procedure
database: Olives_BO
name: Pro_ReceiptPaid
schema: dbo
tags: [#backoffice, #billing]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[Checks]]
  - [[ClientsActive]]
  - [[Customers]]
  - [[Drawers]]
  - [[Receipts]]
  - [[Receipts_PaidTrans]]
  - [[Receipts_PaidTransChecks]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[Checks]]
  - [[Receipts]]
  - ReceiptsLog
  - [[Receipts_PaidTransChecks]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ReceiptPaid


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, Checks, ClientsActive, Customers, Drawers, Receipts, Receipts_PaidTrans, Receipts_PaidTransChecks, SalesPersons, dbo. Writes Checks, Receipts, ReceiptsLog, Receipts_PaidTransChecks. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @TransactionTypeID int = null
- @TransactionYear smallint = null
- @TransactionNo int  = null
- @ReceiptNo int  = null
- @BankID int  = null
- @BranchID int  = null
- @PaidTransYear int  = null
- @PaidTransNo int  = null
- @PaidTransTypeID int  = null
- @ChequeNo int  = null
- @Amount float  = null
- @FilterBy int  = null
- @cmdType varchar(50)=null
- @MacAddress nvarchar(100)=null
- @UserID nvarchar(50) = null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
- @CustomerID bigint = null
- @TransactionDate datetime = null
- @FromDate smalldatetime = null
- @ToDate smalldatetime = null
## Tables Read
- [[Banks]]
- [[Branches]]
- [[Checks]]
- [[ClientsActive]]
- [[Customers]]
- [[Drawers]]
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[Receipts_PaidTransChecks]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[Checks]]
- [[Receipts]]
- ReceiptsLog
- [[Receipts_PaidTransChecks]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- [[Checks]]
- [[ClientsActive]]
- [[Customers]]
- [[Drawers]]
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[Receipts_PaidTransChecks]]
- [[SalesPersons]]
- dbo

**Tables Written**
- [[Checks]]
- [[Receipts]]
- ReceiptsLog
- [[Receipts_PaidTransChecks]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
