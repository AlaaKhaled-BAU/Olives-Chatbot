---
type: procedure
database: Olives_BO
name: PRO_PreProductionLoadingOrderApproval
schema: dbo
tags: [#backoffice]
reads_from:
  - ClientsActive
  - CompanyParameters
  - ERPStores
  - Items
  - ItemsStoreByUser
  - ItemsUnits
  - PriceListDetails
  - SalesPersonTransactionsSerials
  - SalesPersons
  - TransfersOrdersDetails
writes_to:
  - OrdersDetails_Log
  - TransactionsSerials
  - TransfersOrdersHeaders
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# PRO_PreProductionLoadingOrderApproval

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 10 table(s); writes 3; calls 3 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @OrderYear smallint
- @OrderNo int
- @ItemCode nvarchar(100)
- @UnitID nvarchar(50)
- @salesmanID int
- @NewItemCode nvarchar(100)
- @NewUnitID nvarchar(50)
- @Quantity float
- @cmdType varchar(50)
- @VouType int
- @UserID nvarchar(50)
- @IsDeleteHeader bit
- @IsEdit bit
- @MacAddress nvarchar(100)
- @IPAddress nvarchar(100)
- @PCName varchar(100)
- @TrType int
- @fromDate datetime
- @TransferOrders transferordertype
- @toDate datetime
- @SalesPersonIDs nvarchar(200)
- @CategCode nvarchar(200)
- @StoreID nvarchar(100)
- @SalesmanNo int
- @OrderType int
- @fillter int
- @TransType int
- @SalesPersonID int
- @Supervisor int
- @ItemClass nvarchar(100)
- @StoreNo nvarchar(100)
- @OrderDate smalldatetime
- @Notes nvarchar(500)
- @DocType int
## Tables Read
- [[ClientsActive]]
- [[CompanyParameters]]
- [[ERPStores]]
- [[Items]]
- [[ItemsStoreByUser]]
- [[ItemsUnits]]
- [[PriceListDetails]]
- [[SalesPersonTransactionsSerials]]
- [[SalesPersons]]
- [[TransfersOrdersDetails]]
## Tables Written
- [[OrdersDetails_Log]]
- [[TransactionsSerials]]
- [[TransfersOrdersHeaders]]
## Cross-DB Tables
References tables in **OSFA_DB** (qualified as `OSFA_DB.dbo.*`):
- [[CompanyParameters]]
## Callers
_None_
## Callees
- `Fun_GetCompanyBranchesByUser`
- `Fun_GetFromDate`
- `GetItemOrgUnitQty`
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
