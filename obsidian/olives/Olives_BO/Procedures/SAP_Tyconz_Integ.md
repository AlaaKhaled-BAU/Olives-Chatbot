---
type: procedure
database: Olives_BO
name: SAP_Tyconz_Integ
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Banks]]
  - [[BusinessUnits]]
  - [[CompanyBranches]]
  - Cur_Banks
  - Cur_Branches
  - [[IntegrationErrorLog]]
  - `dbo`
writes_to:
  - [[Banks]]
  - [[BanksAccounts]]
  - [[Branches]]
  - [[BusinessUnits]]
  - [[CompanyBranches]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersPaidTransList]]
  - [[CustomersTypes]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - ManualReconciliation
  - [[PaymentsTypes]]
  - [[Positions]]
  - [[PriceListDetails]]
  - [[PriceLists]]
  - [[Receipts_PaidTrans]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
called_by:
  - [[SAP_Tyconz_Integ_ItemsUnitAD]]
  - [[SP_IntegrationErrorLog]]
support_relevance: high
last_verified: 2026-07-05
---
# SAP_Tyconz_Integ


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, BusinessUnits, CompanyBranches, Cur_Banks, Cur_Branches, IntegrationErrorLog, dbo. Writes Banks, BanksAccounts, Branches, BusinessUnits, CompanyBranches, Customers, CustomersFinancialDetails, CustomersPaidTransList, CustomersTypes, Items, ItemsCategories, ItemsUnits, ItemsUnitsDetails, ManualReconciliation, PaymentsTypes, Positions, PriceListDetails, PriceLists, Receipts_PaidTrans, SalesPersons, SalesPersonsGroups. Calls 2 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID nvarchar(50) = 7
## Tables Read
- [[Banks]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- Cur_Banks
- Cur_Branches
- [[IntegrationErrorLog]]
- `dbo`
## Tables Written
- [[Banks]]
- [[BanksAccounts]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPaidTransList]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- ManualReconciliation
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[Receipts_PaidTrans]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
## Callers
_None (no known callers)_
## Callees
- [[SAP_Tyconz_Integ_ItemsUnitAD]]
- [[SP_IntegrationErrorLog]]
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- Cur_Banks
- Cur_Branches
- [[IntegrationErrorLog]]
- dbo

**Tables Written**
- [[Banks]]
- [[BanksAccounts]]
- [[Branches]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPaidTransList]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- ManualReconciliation
- [[PaymentsTypes]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[Receipts_PaidTrans]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]

**Callers**
- [[SAP_Tyconz_Integ_ItemsUnitAD]]
- [[SP_IntegrationErrorLog]]

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
