---
type: procedure
database: Olives_BO
name: Jazeera_Integ
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - CheckCustFinDet
  - [[CustomerChqList]]
  - [[CustomerStatmentOfAccount]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[CustomersPaidTransList]]
  - [[CustomersPromotionsGroups]]
  - [[CustomersPromotionsGroupsLink]]
  - [[CustomersTypes]]
  - [[Drawers]]
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
  - [[Items]]
writes_to:
  - [[Banks]]
  - [[Branches]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[Drawers]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[Positions]]
  - [[SalesPersons]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Jazeera_Integ


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, CheckCustFinDet, CustomerChqList, CustomerStatmentOfAccount, Customers, CustomersFinancialDetails, CustomersPaidTransList, CustomersPromotionsGroups, CustomersPromotionsGroupsLink, CustomersTypes, Drawers, InvoiceHistoryDF, InvoiceHistoryHF, Items. Writes Banks, Branches, Customers, CustomersFinancialDetails, Drawers, Items, ItemsCategories, Positions, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Banks]]
- [[Branches]]
- CheckCustFinDet
- [[CustomerChqList]]
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPaidTransList]]
- [[CustomersPromotionsGroups]]
- [[CustomersPromotionsGroupsLink]]
- [[CustomersTypes]]
- [[Drawers]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
## Tables Written
- [[Banks]]
- [[Branches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Drawers]]
- [[Items]]
- [[ItemsCategories]]
- [[Positions]]
- [[SalesPersons]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- CheckCustFinDet
- [[CustomerChqList]]
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[CustomersPaidTransList]]
- [[CustomersPromotionsGroups]]
- [[CustomersPromotionsGroupsLink]]
- [[CustomersTypes]]
- [[Drawers]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]

**Tables Written**
- [[Banks]]
- [[Branches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Drawers]]
- [[Items]]
- [[ItemsCategories]]
- [[Positions]]
- [[SalesPersons]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
