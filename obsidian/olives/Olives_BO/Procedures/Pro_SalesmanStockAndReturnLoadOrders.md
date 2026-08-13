---
type: procedure
database: Olives_BO
name: Pro_SalesmanStockAndReturnLoadOrders
schema: dbo
tags: [#backoffice, #inventory, #order, #sales]
reads_from:
  - Fun_GetCompanyBranchesByUser
  - [[Items]]
  - [[ItemsUnits]]
  - OPENJSON
  - [[Receipts]]
  - [[SalesPersonTransactionsSerials]]
  - [[SalesPersons]]
  - [[StockSettelmentCollection]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - [[TransfersOrdersDetails]]
  - [[TransfersOrdersHeaders]]
  - `dbo`
writes_to:
  - [[OT_ConsOrderDF]]
  - [[OT_ConsOrderHF]]
  - [[StockSettelmentCollection]]
  - [[TransfersOrdersDetails]]
  - [[TransfersOrdersHeaders]]
called_by:
  - [[Pro_SalesmanStockAndReturnLoadOrders]]
  - sp_OACreate
  - sp_OADestroy
  - sp_OAGetProperty
  - sp_OAMethod
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesmanStockAndReturnLoadOrders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_GetCompanyBranchesByUser, Items, ItemsUnits, OPENJSON, Receipts, SalesPersonTransactionsSerials, SalesPersons, StockSettelmentCollection, TransactionsDetails, TransactionsHeaders, TransfersOrdersDetails, TransfersOrdersHeaders, dbo. Writes OT_ConsOrderDF, OT_ConsOrderHF, StockSettelmentCollection, TransfersOrdersDetails, TransfersOrdersHeaders. Invoked by 1 procedure(s). Calls 5 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo SmallInt = 1
- @CompBranch Int = 0
- @SalesmanID Int = 3003
- @TrDate SmallDateTime = '2021-12-01'
- @UserID Nvarchar(50) = NULL
- @CmdType Nvarchar(50) = 'SelectAll'
- @OrderNo Int = NULL
- @OrderYear SmallInt = NULL
- @ItemCode Nvarchar(100) = 'P3'
- @LineID Int = NULL
- @CollectedAmout float = NULL
- @SalesmanCollectedAmout float = NULL
- @UnitID Nvarchar(100) = 'cartn'
- @SettlmentDate smalldatetime = '2021-12-01'
- @ItemStatus int = 0
- @Qty Float = 44
## Tables Read
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[ItemsUnits]]
- OPENJSON
- [[Receipts]]
- [[SalesPersonTransactionsSerials]]
- [[SalesPersons]]
- [[StockSettelmentCollection]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
- `dbo`
## Tables Written
- [[OT_ConsOrderDF]]
- [[OT_ConsOrderHF]]
- [[StockSettelmentCollection]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
## Callers
- [[Pro_SalesmanStockAndReturnLoadOrders]]
## Callees
- [[Pro_SalesmanStockAndReturnLoadOrders]]
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod
## Impact / Dependencies

**Tables Read**
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[ItemsUnits]]
- OPENJSON
- [[Receipts]]
- [[SalesPersonTransactionsSerials]]
- [[SalesPersons]]
- [[StockSettelmentCollection]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
- dbo

**Tables Written**
- [[OT_ConsOrderDF]]
- [[OT_ConsOrderHF]]
- [[StockSettelmentCollection]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]

**Callers**
- [[Pro_SalesmanStockAndReturnLoadOrders]]
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod

**Callees**
- [[Pro_SalesmanStockAndReturnLoadOrders]]


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Shared/Runbooks/Van-Stock-Mismatch]]
