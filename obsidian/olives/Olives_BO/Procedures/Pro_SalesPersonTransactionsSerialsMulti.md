---
type: procedure
database: Olives_BO
name: Pro_SalesPersonTransactionsSerialsMulti
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[SalesPersonTransactionsSerialsMulti]]
writes_to:
  - [[SalesPersonTransactionsSerialsMulti]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesPersonTransactionsSerialsMulti


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalesPersonTransactionsSerialsMulti. Writes SalesPersonTransactionsSerialsMulti. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	 = null
- @SalesPersonID	int	= null
- @SerYear	smallint	= null
- @RefLink	varchar(200)	= null
- @OrderTakingNextSerial	bigint	= null
- @TransferOrderNextSerial	bigint	= null
- @SalesInvoiceNextSerial	bigint	= null
- @ReturnSalesNextSerial	bigint	= null
- @ReceiptNextSerial	bigint	= null
- @ConsNextSerial	bigint	= null
- @CustStockNextSerial	bigint	= null
- @CompetitiveItemsInfoNextSerial	bigint	= null
- @UnLoadOrdersNextSerials	bigint	= null
- @SalesmanStockNextSerial	bigint	= null
- @ReturnOrderNextSerial	bigint	= null
- @VanTransferNextSerial	bigint	= null
- @SalesQuotationNextSerial	bigint	= null
- @cmdType varchar(50)=null
## Tables Read
- [[SalesPersonTransactionsSerialsMulti]]
## Tables Written
- [[SalesPersonTransactionsSerialsMulti]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalesPersonTransactionsSerialsMulti]]

**Tables Written**
- [[SalesPersonTransactionsSerialsMulti]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
