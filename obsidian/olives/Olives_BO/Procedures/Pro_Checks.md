---
type: procedure
database: Olives_BO
name: Pro_Checks
schema: dbo
tags: [#backoffice]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[Checks]]
  - [[Currencies]]
  - [[Customers]]
  - [[Drawers]]
  - [[Receipts]]
  - [[Receipts_PaidTrans]]
  - [[TransactionsHeaders]]
  - [[TransactionsTypes]]
  - `dbo`
writes_to:
  - [[Checks]]
  - [[TransactionsHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_Checks


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, Checks, Currencies, Customers, Drawers, Receipts, Receipts_PaidTrans, TransactionsHeaders, TransactionsTypes, dbo. Writes Checks, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @TransactionTypeID int = null
- @TransactionYear smallint = null
- @TransactionNo int  = null
- @cmdType varchar(50)=null
- @BankID int = null
- @BranchID int = null
- @CustomerID int = null
- @ChequeNo int = null
- @DrawerID int = null
- @DueDate datetime = null
- @ChangeStatusDate smalldatetime = null
- @Amount float =null
- @CurrencyID smallint = null
- @ExchangeRate float = null
- @CheckStatus smallint = null
- @VouNo int =null
- @VouYear int =null
- @VouType int=null
- @CustBankAccNo nvarchar  = null
- @IsGero bit =null
## Tables Read
- [[Banks]]
- [[Branches]]
- [[Checks]]
- [[Currencies]]
- [[Customers]]
- [[Drawers]]
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[TransactionsHeaders]]
- [[TransactionsTypes]]
- `dbo`
## Tables Written
- [[Checks]]
- [[TransactionsHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- [[Checks]]
- [[Currencies]]
- [[Customers]]
- [[Drawers]]
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[TransactionsHeaders]]
- [[TransactionsTypes]]
- dbo

**Tables Written**
- [[Checks]]
- [[TransactionsHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
