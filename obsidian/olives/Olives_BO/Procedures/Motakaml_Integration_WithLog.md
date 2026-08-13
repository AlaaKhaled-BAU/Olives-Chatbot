---
type: procedure
database: Olives_BO
name: Motakaml_Integration_WithLog
schema: dbo
tags: [#backoffice, #integration, #log]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[CompanyBranches]]
  - Cur_Banks
  - Cur_CompanyBranches
  - Cur_Locations_Level1
  - Cur_Locations_Level2
  - [[IntegrationErrorLog]]
  - [[Locations]]
  - OLIV
writes_to:
  - [[Customers]]
  - [[Items]]
  - [[ItemsUnitsDetails]]
  - OFIS_CL11MF_TAB
  - [[PriceListDetails]]
  - [[PriceLists]]
called_by:
  - [[SP_IntegrationErrorLog]]
support_relevance: high
last_verified: 2026-07-05
---
# Motakaml_Integration_WithLog


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, CompanyBranches, Cur_Banks, Cur_CompanyBranches, Cur_Locations_Level1, Cur_Locations_Level2, IntegrationErrorLog, Locations, OLIV. Writes Customers, Items, ItemsUnitsDetails, OFIS_CL11MF_TAB, PriceListDetails, PriceLists. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
## Tables Read
- [[Banks]]
- [[Branches]]
- [[CompanyBranches]]
- Cur_Banks
- Cur_CompanyBranches
- Cur_Locations_Level1
- Cur_Locations_Level2
- [[IntegrationErrorLog]]
- [[Locations]]
- OLIV
## Tables Written
- [[Customers]]
- [[Items]]
- [[ItemsUnitsDetails]]
- OFIS_CL11MF_TAB
- [[PriceListDetails]]
- [[PriceLists]]
## Callers
_None (no known callers)_
## Callees
- [[SP_IntegrationErrorLog]]
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- [[CompanyBranches]]
- Cur_Banks
- Cur_CompanyBranches
- Cur_Locations_Level1
- Cur_Locations_Level2
- [[IntegrationErrorLog]]
- [[Locations]]
- OLIV

**Tables Written**
- [[Customers]]
- [[Items]]
- [[ItemsUnitsDetails]]
- OFIS_CL11MF_TAB
- [[PriceListDetails]]
- [[PriceLists]]

**Callers**
- [[SP_IntegrationErrorLog]]

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
