---
type: procedure
database: Olives_BO
name: Pro_TransfersOrdersHeaders_Nighthammoudeh
schema: dbo
tags: [#backoffice]
reads_from:
  - ClientsActive
  - CompanyParameters
  - ERPStores
  - Items
  - ItemsCategories
  - ItemsUnits
  - PriceListDetails
  - SalesPersonItemsAssignment
  - SalesPersonItemsBalance
  - SalesPersonTransactionsSerials
  - SalesPersons
  - TransactionsHeaders
writes_to:
  - TransactionsSerials
  - TransfersOrdersDetails
  - TransfersOrdersHeaders
  - WF_SubLog
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# Pro_TransfersOrdersHeaders_Nighthammoudeh

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 12 table(s); writes 4; calls 6 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @OrderYear smallint
- @OrderNo bigint
- @SalesPersonID int
- @Supervisor int
- @OrderDate smalldatetime
- @Notes nvarchar(500)
- @cmdType varchar(50)
- @VouType int
- @DocType int
- @FromDate smalldatetime
- @ToDate smalldatetime
- @ErrorNo smallint OUTPUT
- @OrderApproveCount tinyint
- @UserID nvarchar(50)
- @MacAddress nvarchar(100)
- @IPAddress nvarchar(100)
- @PCName varchar(100)
- @TrType int
- @ItemCode nvarchar(200)
- @OrderType int
- @StoreID nvarchar(100)
- @IsEdit bit
- @UnitID nvarchar(50)
- @NewItemCode nvarchar(100)
- @NewUnitID nvarchar(50)
- @Quantity float
- @IsDeleteHeader bit
- @TransferOrders transferordertype
- @SalesPersonIDs nvarchar(200)
- @CategCode nvarchar(200)
- @SalesmanNo int
- @fillter int
- @TransType int
- @ItemClass nvarchar(100)
- @StoreNo nvarchar(100)
## Tables Read
- [[ClientsActive]]
- [[CompanyParameters]]
- [[ERPStores]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[PriceListDetails]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersonItemsBalance]]
- [[SalesPersonTransactionsSerials]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
## Tables Written
- [[TransactionsSerials]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
- [[WF_SubLog]]
## Cross-DB Tables
References tables in **OSFA_DB** (qualified as `OSFA_DB.dbo.*`):
- [[CompanyParameters]]
- [[OSFA_DB/Tables/OT_ConsOrderDF|OT_ConsOrderDF]]
## Callers
_None_
## Callees
- `Fun_GetCompanyBranchesByUser`
- `Fun_GetFromDate`
- `Fun_GetPreviousDayUnloadedItems`
- `Fun_GetPreviousDayUnloadedItems_New`
- `GetItemMasterUnitQty`
- `GetItemOrgUnitQty`
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
