---
type: procedure
database: Olives_BO
name: Pro_IssueAssets
schema: dbo
tags: [#assets, #backoffice]
reads_from:
  - [[Assets]]
  - [[AssetsCustomerLink]]
  - [[AssetsTransactions]]
  - [[AssetsWarehouseTransactions]]
  - [[ClientsActive]]
  - [[Customers]]
  - Fun_ConvArrayToTable
  - [[Locations]]
  - [[Users]]
  - cur_approve
writes_to:
  - [[Assets]]
  - [[AssetsTransactions]]
  - [[Customers]]
called_by:
  - [[Pro_AssetsWarehouseTransactionsCalc]]
support_relevance: high
last_verified: 2026-07-05
---
# Pro_IssueAssets


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Assets, AssetsCustomerLink, AssetsTransactions, AssetsWarehouseTransactions, ClientsActive, Customers, Fun_ConvArrayToTable, Locations, Users, cur_approve. Writes Assets, AssetsTransactions, Customers. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @AssetID smallint = null
- @SalesmanNo smallint = null
- @TransID numeric = null
- @FromDate smalldatetime = null
- @ToDate smalldatetime = null
- @approveLst nvarchar(500) = null
- @TransType smallint=null
- @TransDate smallDateTime = null
- @CustomerID bigint=null
- @ContactID bigint=null
- @ContractDate smalldatetime = null
- @ContractNO nvarchar(50)= null
- @UserID nvarchar(50) = null
- @Notes nvarchar(500) = null
- @Longitude nvarchar(50) = null
- @Latitude nvarchar(50) = null
- @cmdType varchar(50)='Select All'
- @Qty float = null
## Tables Read
- [[Assets]]
- [[AssetsCustomerLink]]
- [[AssetsTransactions]]
- [[AssetsWarehouseTransactions]]
- [[ClientsActive]]
- [[Customers]]
- Fun_ConvArrayToTable
- [[Locations]]
- [[Users]]
- cur_approve
## Tables Written
- [[Assets]]
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
- [[ClientsActive]]
- [[Customers]]
- Fun_ConvArrayToTable
- [[Locations]]
- [[Users]]
- cur_approve

**Tables Written**
- [[Assets]]
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
