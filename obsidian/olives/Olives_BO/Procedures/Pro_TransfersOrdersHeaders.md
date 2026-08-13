---
type: procedure
database: Olives_BO
name: Pro_TransfersOrdersHeaders
schema: dbo
tags: [#backoffice, #order]
reads_from:
  - Approval
  - [[ClientsActive]]
  - [[CompanyParameters]]
  - [[ERPStores]]
  - ErrorInQty
  - Fun_GetCompanyBranchesByUser
  - [[Items]]
  - [[OT_SendLog]]
  - [[SalesPersonItemsBalance]]
  - [[SalesPersonTransactionsSerials]]
  - [[SalesPersons]]
  - [[SalespersonsMessages]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - [[TransactionsSerials]]
writes_to:
  - [[OT_SendLog]]
  - [[SalesPersonItemsBalance]]
  - [[SalespersonsMessages]]
  - [[TransactionsSerials]]
  - TransfersOrdersDetailsLog
  - [[TransfersOrdersHeaders]]
  - TransfersOrdersHeadersLog
called_by:
  - [[BaladInsertrtLoadHeadersintoTransactionstyp6]]
  - [[Pro_ConvertLoadOrderToTransaction]]
  - [[Pro_ConvertUnloadOrderToTransaction]]
  - [[Zoumt_Integ]]
support_relevance: high
last_verified: 2026-07-05
---
# Pro_TransfersOrdersHeaders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Approval, ClientsActive, CompanyParameters, ERPStores, ErrorInQty, Fun_GetCompanyBranchesByUser, Items, OT_SendLog, SalesPersonItemsBalance, SalesPersonTransactionsSerials, SalesPersons, SalespersonsMessages, TransactionsDetails, TransactionsHeaders, TransactionsSerials. Writes OT_SendLog, SalesPersonItemsBalance, SalespersonsMessages, TransactionsSerials, TransfersOrdersDetailsLog, TransfersOrdersHeaders, TransfersOrdersHeadersLog. Calls 4 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @OrderYear smallint=null
- @OrderNo bigint=null
- @SalesPersonID int=null
- @OrderDate smalldatetime=null
- @Notes nvarchar(500)=null
- @cmdType varchar(50)=null
- @VouType int=null
- @DocType int=null
- @FromDate smalldatetime=null
- @ToDate smalldatetime=null
- @ErrorNo smallint = 0 output
- @OrderApproveCount  tinyint=0
- @UserID nvarchar(50) = null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
- @TrType int = null
## Tables Read
- Approval
- [[ClientsActive]]
- [[CompanyParameters]]
- [[ERPStores]]
- ErrorInQty
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[OT_SendLog]]
- [[SalesPersonItemsBalance]]
- [[SalesPersonTransactionsSerials]]
- [[SalesPersons]]
- [[SalespersonsMessages]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransactionsSerials]]
## Tables Written
- [[OT_SendLog]]
- [[SalesPersonItemsBalance]]
- [[SalespersonsMessages]]
- [[TransactionsSerials]]
- TransfersOrdersDetailsLog
- [[TransfersOrdersHeaders]]
- TransfersOrdersHeadersLog
## Callers
_None (no known callers)_
## Callees
- [[BaladInsertrtLoadHeadersintoTransactionstyp6]]
- [[Pro_ConvertLoadOrderToTransaction]]
- [[Pro_ConvertUnloadOrderToTransaction]]
- [[Zoumt_Integ]]
## Impact / Dependencies

**Tables Read**
- Approval
- [[ClientsActive]]
- [[CompanyParameters]]
- [[ERPStores]]
- ErrorInQty
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[OT_SendLog]]
- [[SalesPersonItemsBalance]]
- [[SalesPersonTransactionsSerials]]
- [[SalesPersons]]
- [[SalespersonsMessages]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransactionsSerials]]

**Tables Written**
- [[OT_SendLog]]
- [[SalesPersonItemsBalance]]
- [[SalespersonsMessages]]
- [[TransactionsSerials]]
- TransfersOrdersDetailsLog
- [[TransfersOrdersHeaders]]
- TransfersOrdersHeadersLog

**Callers**
- [[BaladInsertrtLoadHeadersintoTransactionstyp6]]
- [[Pro_ConvertLoadOrderToTransaction]]
- [[Pro_ConvertUnloadOrderToTransaction]]
- [[Zoumt_Integ]]

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
