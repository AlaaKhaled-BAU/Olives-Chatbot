---
type: procedure
database: Olives_BO
name: OT_Online_RptSalesAndReturnPercByCustomer_Supervisor
schema: dbo
tags: [#backoffice, #customer, #mobile, #order, #sales]
reads_from:
  - [[Customers]]
  - [[Items]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_Online_RptSalesAndReturnPercByCustomer_Supervisor


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Items, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int
- @FromDate datetime
- @ToDate datetime
- @CustomerNo bigint
## Tables Read
- [[Customers]]
- [[Items]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[Items]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
