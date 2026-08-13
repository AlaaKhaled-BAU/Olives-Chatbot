---
type: procedure
database: Olives_BO
name: Tablet_AssetsTransactions_Insert
schema: dbo
tags: [#assets, #backoffice, #mobile]
reads_from:
  - [[AssetsCustomerLink]]
  - [[AssetsTransactions]]
  - [[AssetsWarehouseTransactions]]
  - [[Customers]]
  - [[SalesPersons]]
writes_to:
  - [[AssetsTransactions]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Tablet_AssetsTransactions_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads AssetsCustomerLink, AssetsTransactions, AssetsWarehouseTransactions, Customers, SalesPersons. Writes AssetsTransactions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint=1
- @AssetID	bigint	=1
- @TransType	smallint=1
- @TransDate	smalldatetime='2022-10-10'
- @CustomerID	bigint=314
- @ContractNo	nvarchar(50)='111111'
- @ContractDate	smalldatetime='2022-10-11'
- @SalesmanNo	int=3003
- @Notes	nvarchar(500)	='NNNNNNNNNNN'
- @Latitude	nvarchar(50)='0'
- @Longitude	nvarchar(50)='0'
- @TabletSysID	varchar(50)	='AAAA'
- @WithdrawalReason int=0
## Tables Read
- [[AssetsCustomerLink]]
- [[AssetsTransactions]]
- [[AssetsWarehouseTransactions]]
- [[Customers]]
- [[SalesPersons]]
## Tables Written
- [[AssetsTransactions]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[AssetsCustomerLink]]
- [[AssetsTransactions]]
- [[AssetsWarehouseTransactions]]
- [[Customers]]
- [[SalesPersons]]

**Tables Written**
- [[AssetsTransactions]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
