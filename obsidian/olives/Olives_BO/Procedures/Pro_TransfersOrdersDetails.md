---
type: procedure
database: Olives_BO
name: Pro_TransfersOrdersDetails
schema: dbo
tags: [#backoffice, #order]
reads_from:
  - [[ClientsActive]]
  - [[CompanyParameters]]
  - Fun_GetCompanyBranchesByUser
  - Fun_GetPreviousDayUnloadedItems
  - Fun_GetPreviousDayUnloadedItems_New
  - [[Items]]
  - [[ItemsUnits]]
  - [[PriceListDetails]]
  - [[SalesPersonItemsAssignment]]
  - [[SalesPersonItemsBalance]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
  - [[TransfersOrdersDetails]]
  - [[TransfersOrdersHeaders]]
  - `dbo`
writes_to:
  - [[OT_ConsOrderDF]]
  - [[TransfersOrdersDetails]]
  - TransfersOrdersDetailsLog
called_by:
  - [[BaladInsertrtLoadDetailsintoTransactionstyp6]]
support_relevance: high
last_verified: 2026-07-05
---
# Pro_TransfersOrdersDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, CompanyParameters, Fun_GetCompanyBranchesByUser, Fun_GetPreviousDayUnloadedItems, Fun_GetPreviousDayUnloadedItems_New, Items, ItemsUnits, PriceListDetails, SalesPersonItemsAssignment, SalesPersonItemsBalance, SalesPersons, TransactionsHeaders, TransfersOrdersDetails, TransfersOrdersHeaders, dbo. Writes OT_ConsOrderDF, TransfersOrdersDetails, TransfersOrdersDetailsLog. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @OrderYear smallint=2021
- @OrderNo INT=2021200303
- @ItemCode nvarchar(100)=NULL
- @UnitID nvarchar(50)=NULL
- @NewItemCode nvarchar(100)=NULL
- @NewUnitID nvarchar(50)=NULL
- @Quantity float= null
- @cmdType varchar(50)='Select All'
- @VouType int=1
- @UserID nvarchar(50) = null
- @IsDeleteHeader bit = null
- @IsEdit bit = 0
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
- @TrType int = null
## Tables Read
- [[ClientsActive]]
- [[CompanyParameters]]
- Fun_GetCompanyBranchesByUser
- Fun_GetPreviousDayUnloadedItems
- Fun_GetPreviousDayUnloadedItems_New
- [[Items]]
- [[ItemsUnits]]
- [[PriceListDetails]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
- `dbo`
## Tables Written
- [[OT_ConsOrderDF]]
- [[TransfersOrdersDetails]]
- TransfersOrdersDetailsLog
## Callers
_None (no known callers)_
## Callees
- [[BaladInsertrtLoadDetailsintoTransactionstyp6]]
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[CompanyParameters]]
- Fun_GetCompanyBranchesByUser
- Fun_GetPreviousDayUnloadedItems
- Fun_GetPreviousDayUnloadedItems_New
- [[Items]]
- [[ItemsUnits]]
- [[PriceListDetails]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
- dbo

**Tables Written**
- [[OT_ConsOrderDF]]
- [[TransfersOrdersDetails]]
- TransfersOrdersDetailsLog

**Callers**
- [[BaladInsertrtLoadDetailsintoTransactionstyp6]]

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
