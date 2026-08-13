---
type: procedure
database: Olives_BO
name: Pro_AssetTransactionsList
schema: dbo
tags: [#assets, #backoffice]
reads_from:
  - [[Assets]]
  - [[AssetsTransactions]]
  - [[AssetsWarehouseTransactions]]
  - [[Customers]]
  - [[CustomersContactPersons]]
  - [[ERPStores]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_AssetTransactionsList


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Assets, AssetsTransactions, AssetsWarehouseTransactions, Customers, CustomersContactPersons, ERPStores. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @AssetID smallint = null
- @TransID numeric = null
- @FromDate smalldatetime = null
- @ToDate smalldatetime = null
- @approveLst nvarchar(500) = null
- @TransType smallint=null
- @TransDate smallDateTime = null
- @CustomerID bigint=null
- @ContractDate smalldatetime = null
- @ContractNO nvarchar(50)= null
- @UserID nvarchar(50) = null
- @Notes nvarchar(500) = null
- @Longitude nvarchar(50) = null
- @Latitude nvarchar(50) = null
- @cmdType varchar(50)=null
## Tables Read
- [[Assets]]
- [[AssetsTransactions]]
- [[AssetsWarehouseTransactions]]
- [[Customers]]
- [[CustomersContactPersons]]
- [[ERPStores]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Assets]]
- [[AssetsTransactions]]
- [[AssetsWarehouseTransactions]]
- [[Customers]]
- [[CustomersContactPersons]]
- [[ERPStores]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
