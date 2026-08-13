---
type: procedure
database: Olives_BO
name: PlanogramMediabyAssets
schema: dbo
tags: [#assets, #backoffice]
reads_from:
  - [[Assets]]
  - [[AssetsCustomerLink]]
  - [[PlanogramMedia]]
  - [[PlanogramMediaCustomersLink]]
writes_to:
  - [[PlanogramMedia]]
  - [[PlanogramMediaCustomersLink]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# PlanogramMediabyAssets


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Assets, AssetsCustomerLink, PlanogramMedia, PlanogramMediaCustomersLink. Writes PlanogramMedia, PlanogramMediaCustomersLink. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=1
## Tables Read
- [[Assets]]
- [[AssetsCustomerLink]]
- [[PlanogramMedia]]
- [[PlanogramMediaCustomersLink]]
## Tables Written
- [[PlanogramMedia]]
- [[PlanogramMediaCustomersLink]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Assets]]
- [[AssetsCustomerLink]]
- [[PlanogramMedia]]
- [[PlanogramMediaCustomersLink]]

**Tables Written**
- [[PlanogramMedia]]
- [[PlanogramMediaCustomersLink]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
