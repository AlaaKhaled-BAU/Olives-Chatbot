---
type: procedure
database: Olives_BO
name: Pro_CustomersAndAssets
schema: dbo
tags: [#assets, #backoffice, #customer]
reads_from:
  - [[Assets]]
  - [[AssetsCustomerLink]]
  - [[AssetsTransactions]]
  - [[AssetsWarehouseTransactions]]
  - [[Customers]]
  - [[CustomersContactPersons]]
  - [[CustomersContactPersonsLink]]
  - [[ERPStores]]
  - Fun_GetOldAssetStoresTbl
  - Fun_GetOldCustomerAssetsTbl
  - [[Locations]]
  - [[SystemCodes]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_CustomersAndAssets


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Assets, AssetsCustomerLink, AssetsTransactions, AssetsWarehouseTransactions, Customers, CustomersContactPersons, CustomersContactPersonsLink, ERPStores, Fun_GetOldAssetStoresTbl, Fun_GetOldCustomerAssetsTbl, Locations, SystemCodes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=2
- @cmdType Varchar(50)='SelectAllCustomersWithAsset'
- @FieldID int = null
- @LocationID int = -1
- @ContactPersonID int = -1
- @AssetID int = -1
- @CustomerID bigint = -1
- @FieldCaption Varchar(100) = null
- @FieldForeignCaption Varchar(100) = null
- @IsRequired bit = null
## Tables Read
- [[Assets]]
- [[AssetsCustomerLink]]
- [[AssetsTransactions]]
- [[AssetsWarehouseTransactions]]
- [[Customers]]
- [[CustomersContactPersons]]
- [[CustomersContactPersonsLink]]
- [[ERPStores]]
- Fun_GetOldAssetStoresTbl
- Fun_GetOldCustomerAssetsTbl
- [[Locations]]
- [[SystemCodes]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Assets]]
- [[AssetsCustomerLink]]
- [[AssetsTransactions]]
- [[AssetsWarehouseTransactions]]
- [[Customers]]
- [[CustomersContactPersons]]
- [[CustomersContactPersonsLink]]
- [[ERPStores]]
- Fun_GetOldAssetStoresTbl
- Fun_GetOldCustomerAssetsTbl
- [[Locations]]
- [[SystemCodes]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
