---
type: procedure
database: Olives_BO
name: Niroukh_Integration_GetPromotion
schema: dbo
tags: [#backoffice, #integration, #sales]
reads_from:
  - [[CustomersPromotionsGroups]]
  - [[IntegrationErrorLog]]
  - [[Items]]
  - OPENJSON
  - [[PromotionsCondUnCodInput]]
  - [[PromotionsCondUnCodOutput]]
  - [[PromotionsCustomersGroupsLink]]
  - [[PromotionsHeaders]]
  - [[PromotionsRangeInput]]
  - [[PromotionsSalesmanGroupsLink]]
  - [[SalesPersonsGroups]]
writes_to:
  - [[CustomersPromotionsGroups]]
  - [[PromotionsCondUnCodInput]]
  - [[PromotionsCondUnCodOutput]]
  - [[PromotionsCustomersGroupsLink]]
  - [[PromotionsHeaders]]
  - [[PromotionsRangeInput]]
  - [[PromotionsSalesmanGroupsLink]]
called_by:
  - [[Niroukh_Integ_GetDataFromAPI]]
support_relevance: high
last_verified: 2026-07-05
---
# Niroukh_Integration_GetPromotion


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersPromotionsGroups, IntegrationErrorLog, Items, OPENJSON, PromotionsCondUnCodInput, PromotionsCondUnCodOutput, PromotionsCustomersGroupsLink, PromotionsHeaders, PromotionsRangeInput, PromotionsSalesmanGroupsLink, SalesPersonsGroups. Writes CustomersPromotionsGroups, PromotionsCondUnCodInput, PromotionsCondUnCodOutput, PromotionsCustomersGroupsLink, PromotionsHeaders, PromotionsRangeInput, PromotionsSalesmanGroupsLink. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID nvarchar(50) = 1
## Tables Read
- [[CustomersPromotionsGroups]]
- [[IntegrationErrorLog]]
- [[Items]]
- OPENJSON
- [[PromotionsCondUnCodInput]]
- [[PromotionsCondUnCodOutput]]
- [[PromotionsCustomersGroupsLink]]
- [[PromotionsHeaders]]
- [[PromotionsRangeInput]]
- [[PromotionsSalesmanGroupsLink]]
- [[SalesPersonsGroups]]
## Tables Written
- [[CustomersPromotionsGroups]]
- [[PromotionsCondUnCodInput]]
- [[PromotionsCondUnCodOutput]]
- [[PromotionsCustomersGroupsLink]]
- [[PromotionsHeaders]]
- [[PromotionsRangeInput]]
- [[PromotionsSalesmanGroupsLink]]
## Callers
_None (no known callers)_
## Callees
- [[Niroukh_Integ_GetDataFromAPI]]
## Impact / Dependencies

**Tables Read**
- [[CustomersPromotionsGroups]]
- [[IntegrationErrorLog]]
- [[Items]]
- OPENJSON
- [[PromotionsCondUnCodInput]]
- [[PromotionsCondUnCodOutput]]
- [[PromotionsCustomersGroupsLink]]
- [[PromotionsHeaders]]
- [[PromotionsRangeInput]]
- [[PromotionsSalesmanGroupsLink]]
- [[SalesPersonsGroups]]

**Tables Written**
- [[CustomersPromotionsGroups]]
- [[PromotionsCondUnCodInput]]
- [[PromotionsCondUnCodOutput]]
- [[PromotionsCustomersGroupsLink]]
- [[PromotionsHeaders]]
- [[PromotionsRangeInput]]
- [[PromotionsSalesmanGroupsLink]]

**Callers**
- [[Niroukh_Integ_GetDataFromAPI]]

**Callees**
_None_


## When to Run This

Run when pulling data from an external API/system. Called during sync cycles or on-demand data refresh.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
