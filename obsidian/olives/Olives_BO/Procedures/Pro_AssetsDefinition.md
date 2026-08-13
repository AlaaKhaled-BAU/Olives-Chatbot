---
type: procedure
database: Olives_BO
name: Pro_AssetsDefinition
schema: dbo
tags: [#assets, #backoffice]
reads_from:
  - [[Assets]]
  - [[AssetsCustomerLink]]
  - [[AssetsWarehouseTransactions]]
  - [[CustomersContactPersons]]
  - Fun_GetAssetsBalance
  - [[SystemCodes]]
writes_to:
  - [[Assets]]
  - [[AssetsWarehouseTransactions]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_AssetsDefinition


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Assets, AssetsCustomerLink, AssetsWarehouseTransactions, CustomersContactPersons, Fun_GetAssetsBalance, SystemCodes. Writes Assets, AssetsWarehouseTransactions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @AssetID smallint = null
- @AssetName varchar(500) =null
- @AssetType int = null
- @CustomerID bigint = null
- @StoreNo int = null
- @AssetSerial nvarchar(50)=null
- @Status int = null
- @Notes nvarchar(500)= null
- @AssetValue float = null
- @AssetVolume float = null
- @Reference1 nvarchar (50)=null
- @Reference2 nvarchar (50)=null
- @cmdType varchar(50)=null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
- @UserID nvarchar(100)=null
## Tables Read
- [[Assets]]
- [[AssetsCustomerLink]]
- [[AssetsWarehouseTransactions]]
- [[CustomersContactPersons]]
- Fun_GetAssetsBalance
- [[SystemCodes]]
## Tables Written
- [[Assets]]
- [[AssetsWarehouseTransactions]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Assets]]
- [[AssetsCustomerLink]]
- [[AssetsWarehouseTransactions]]
- [[CustomersContactPersons]]
- Fun_GetAssetsBalance
- [[SystemCodes]]

**Tables Written**
- [[Assets]]
- [[AssetsWarehouseTransactions]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
