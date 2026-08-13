---
type: procedure
database: Olives_BO
name: Pro_AssetTransfer
schema: dbo
tags: [#assets, #backoffice, #order]
reads_from:
  - [[Assets]]
  - [[AssetsCustomerLink]]
  - [[AssetsTransactions]]
  - [[AssetsWarehouseTransactions]]
  - [[Customers]]
  - [[CustomersContactPersonsLink]]
  - [[Locations]]
  - [[SystemCodes]]
  - [[Users]]
writes_to:
  - [[AssetsCustomerLink]]
  - [[AssetsTransactions]]
  - [[Customers]]
called_by:
  - [[Pro_AssetsWarehouseTransactionsCalc]]
support_relevance: high
last_verified: 2026-07-05
---
# Pro_AssetTransfer


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Assets, AssetsCustomerLink, AssetsTransactions, AssetsWarehouseTransactions, Customers, CustomersContactPersonsLink, Locations, SystemCodes, Users. Writes AssetsCustomerLink, AssetsTransactions, Customers. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @AssetID smallint = null
- @TransID numeric = null
- @RefTransID numeric = null
- @WithdrawalReason int =null
- @TransType smallint=null
- @TransDate smallDateTime = null
- @CustomerID bigint=null
- @ContractDate smalldatetime = null
- @ContractNO nvarchar(50)= null
- @UserID nvarchar(50) = null
- @Notes nvarchar(500) = null
- @Longitude nvarchar(50) = null
- @Latitude nvarchar(50) = null
- @OldCustomerID bigint=null
- @AssetAmount float = null
- @StoreNo int =null
- @ContactID int =null
- @OldContactID int =null
- @cmdType varchar(50)=null
## Tables Read
- [[Assets]]
- [[AssetsCustomerLink]]
- [[AssetsTransactions]]
- [[AssetsWarehouseTransactions]]
- [[Customers]]
- [[CustomersContactPersonsLink]]
- [[Locations]]
- [[SystemCodes]]
- [[Users]]
## Tables Written
- [[AssetsCustomerLink]]
- [[AssetsTransactions]]
- [[Customers]]
## Callers
_None (no known callers)_
## Callees
- [[Pro_AssetsWarehouseTransactionsCalc]]
## Impact / Dependencies

**Tables Read**
- [[Assets]]
- [[AssetsCustomerLink]]
- [[AssetsTransactions]]
- [[AssetsWarehouseTransactions]]
- [[Customers]]
- [[CustomersContactPersonsLink]]
- [[Locations]]
- [[SystemCodes]]
- [[Users]]

**Tables Written**
- [[AssetsCustomerLink]]
- [[AssetsTransactions]]
- [[Customers]]

**Callers**
- [[Pro_AssetsWarehouseTransactionsCalc]]

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
