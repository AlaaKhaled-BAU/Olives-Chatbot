---
type: procedure
database: Olives_BO
name: X3_INTEGRATIONPROMOTION_WITHLOG
schema: dbo
tags: [#backoffice, #integration, #log, #sales]
reads_from:
  - [[Companies]]
  - [[Customers]]
  - [[CustomersPromotionsGroups]]
  - [[CustomersPromotionsGroupsLink]]
  - [[Items]]
  - [[PromotionsCondUnCodInput]]
  - [[PromotionsCondUnCodOutput]]
  - [[PromotionsCustomersGroupsLink]]
  - [[PromotionsHeaders]]
  - [[PromotionsRangeInput]]
  - [[PromotionsSalesmanGroupsLink]]
  - [[SalesPersonItemsAssignment]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# X3_INTEGRATIONPROMOTION_WITHLOG


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Companies, Customers, CustomersPromotionsGroups, CustomersPromotionsGroupsLink, Items, PromotionsCondUnCodInput, PromotionsCondUnCodOutput, PromotionsCustomersGroupsLink, PromotionsHeaders, PromotionsRangeInput, PromotionsSalesmanGroupsLink, SalesPersonItemsAssignment, SalesPersons, SalesPersonsGroups, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
_None_
## Tables Read
- [[Companies]]
- [[Customers]]
- [[CustomersPromotionsGroups]]
- [[CustomersPromotionsGroupsLink]]
- [[Items]]
- [[PromotionsCondUnCodInput]]
- [[PromotionsCondUnCodOutput]]
- [[PromotionsCustomersGroupsLink]]
- [[PromotionsHeaders]]
- [[PromotionsRangeInput]]
- [[PromotionsSalesmanGroupsLink]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Companies]]
- [[Customers]]
- [[CustomersPromotionsGroups]]
- [[CustomersPromotionsGroupsLink]]
- [[Items]]
- [[PromotionsCondUnCodInput]]
- [[PromotionsCondUnCodOutput]]
- [[PromotionsCustomersGroupsLink]]
- [[PromotionsHeaders]]
- [[PromotionsRangeInput]]
- [[PromotionsSalesmanGroupsLink]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- dbo

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
