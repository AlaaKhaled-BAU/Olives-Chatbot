---
type: procedure
database: Olives_BO
name: Pro_AssetsWarehouseTransactions
schema: dbo
tags: [#assets, #backoffice, #inventory]
reads_from:
  - [[Assets]]
  - [[AssetsWarehouseTransactions]]
  - [[ERPStores]]
writes_to:
  - [[Assets]]
  - [[AssetsWarehouseTransactions]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_AssetsWarehouseTransactions


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Assets, AssetsWarehouseTransactions, ERPStores. Writes Assets, AssetsWarehouseTransactions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @AssetID bigint = null
- @AssetName varchar(500) =null
- @AssetType int = null
- @CustomerID bigint = null
- @TransDate smalldatetime= null
- @AssetSerial nvarchar(50)=null
- @Status int = null
- @Notes nvarchar(500)= null
- @AssetValue float = null
- @AssetVolume float = null
- @TransType smallint = null
- @TransID numeric= null
- @RefTransID numeric = null
- @StoreNo int = null
- @ToStoreNo int = null
- @Qty float = null
- @cmdType varchar(50)=null
## Tables Read
- [[Assets]]
- [[AssetsWarehouseTransactions]]
- [[ERPStores]]
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
- [[AssetsWarehouseTransactions]]
- [[ERPStores]]

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
