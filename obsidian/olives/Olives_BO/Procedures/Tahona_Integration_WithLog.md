---
type: procedure
database: Olives_BO
name: Tahona_Integration_WithLog
schema: dbo
tags: [#backoffice, #integration, #log]
reads_from:
  - [[Banks]]
  - [[BusinessUnits]]
  - [[CompanyBranches]]
  - Cur_Banks
  - Cur_Branches
  - [[CustomersTypes]]
  - [[IntegrationErrorLog]]
  - [[PaymentsTypes]]
  - [[PriceLists]]
  - [[SalesPersonsGroups]]
  - TAHONA
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Tahona_Integration_WithLog


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, BusinessUnits, CompanyBranches, Cur_Banks, Cur_Branches, CustomersTypes, IntegrationErrorLog, PaymentsTypes, PriceLists, SalesPersonsGroups, TAHONA. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
## Tables Read
- [[Banks]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- Cur_Banks
- Cur_Branches
- [[CustomersTypes]]
- [[IntegrationErrorLog]]
- [[PaymentsTypes]]
- [[PriceLists]]
- [[SalesPersonsGroups]]
- TAHONA
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[BusinessUnits]]
- [[CompanyBranches]]
- Cur_Banks
- Cur_Branches
- [[CustomersTypes]]
- [[IntegrationErrorLog]]
- [[PaymentsTypes]]
- [[PriceLists]]
- [[SalesPersonsGroups]]
- TAHONA

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
