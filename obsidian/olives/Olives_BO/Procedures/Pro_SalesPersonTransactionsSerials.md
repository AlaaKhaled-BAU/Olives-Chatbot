---
type: procedure
database: Olives_BO
name: Pro_SalesPersonTransactionsSerials
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[SalesPersonTransactionsSerials]]
  - `dbo`
writes_to:
  - [[SalesPersonTransactionsSerials]]
  - SalesPersonTransactionsSerialsLog
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesPersonTransactionsSerials


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalesPersonTransactionsSerials, dbo. Writes SalesPersonTransactionsSerials, SalesPersonTransactionsSerialsLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @SalesPersonID int=null
- @SerYear smallint=null
- @OrderTakingNextSerial bigint=null
- @TransferOrderNextSerial bigint=null
- @SalesInvoiceNextSerial bigint=null
- @ReceiptNextSerial bigint=null
- @ConsNextSerial bigint=null
- @CustStockNextSerial bigint=null
- @ReturnSalesNextSerial bigint=null
- @CompetitiveItemsInfoNextSerial bigint = null
- @cmdType varchar(50)=null
- @UnLoadOrdersNextSerials bigint = null
- @SalesmanStockNextSerial bigint = null
- @ReturnOrderNextSerial bigint = null
- @ItemsReplacementNextSerial  bigint = null
- @IssueItemsNextSerial  bigint = null
- @SalesInvoiceCreditNextSerial bigint = null
- @DebitCreditNoteNextSerial bigint = null
- @PaymentsOrdersNextSerial bigint = null
- @ReceiveItemsNextSerial bigint = null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
- @UserID nvarchar(100)=null
## Tables Read
- [[SalesPersonTransactionsSerials]]
- `dbo`
## Tables Written
- [[SalesPersonTransactionsSerials]]
- SalesPersonTransactionsSerialsLog
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalesPersonTransactionsSerials]]
- dbo

**Tables Written**
- [[SalesPersonTransactionsSerials]]
- SalesPersonTransactionsSerialsLog

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
