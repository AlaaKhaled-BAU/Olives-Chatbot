---
type: procedure
database: Olives_BO
name: Pro_AssetsWarehouseTransactionsCalc
schema: dbo
tags: [#assets, #backoffice, #inventory]
reads_from:
  - [[AssetsCustomerLink]]
  - [[AssetsTransactions]]
  - [[AssetsWarehouseTransactions]]
  - [[SalesPersons]]
writes_to:
  - [[AssetsCustomerLink]]
  - [[AssetsWarehouseTransactions]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_AssetsWarehouseTransactionsCalc


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads AssetsCustomerLink, AssetsTransactions, AssetsWarehouseTransactions, SalesPersons. Writes AssetsCustomerLink, AssetsWarehouseTransactions. Invoked by 3 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint=1
- @AutoID numeric
## Tables Read
- [[AssetsCustomerLink]]
- [[AssetsTransactions]]
- [[AssetsWarehouseTransactions]]
- [[SalesPersons]]
## Tables Written
- [[AssetsCustomerLink]]
- [[AssetsWarehouseTransactions]]
## Callers
- [[Pro_AssetTransfer]]
- [[Pro_IssueAssets]]
- [[Pro_WithdrawAssets]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[AssetsCustomerLink]]
- [[AssetsTransactions]]
- [[AssetsWarehouseTransactions]]
- [[SalesPersons]]

**Tables Written**
- [[AssetsCustomerLink]]
- [[AssetsWarehouseTransactions]]

**Callers**
_None_

**Callees**
- [[Pro_AssetTransfer]]
- [[Pro_IssueAssets]]
- [[Pro_WithdrawAssets]]


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
