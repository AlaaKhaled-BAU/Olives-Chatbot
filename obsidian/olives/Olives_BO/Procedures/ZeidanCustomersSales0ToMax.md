---
type: procedure
database: Olives_BO
name: ZeidanCustomersSales0ToMax
schema: dbo
tags: [#backoffice, #customer, #sales]
reads_from:
  - [[Customers]]
  - [[CustomersSalesFrom0toMax]]
  - [[TransactionsHeaders]]
  - sysobjects
writes_to:
  - [[CustomersSalesFrom0toMax]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# ZeidanCustomersSales0ToMax


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersSalesFrom0toMax, TransactionsHeaders, sysobjects. Writes CustomersSalesFrom0toMax. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @companyid int
- @FromDate smalldatetime
- @ToDate smalldatetime
## Tables Read
- [[Customers]]
- [[CustomersSalesFrom0toMax]]
- [[TransactionsHeaders]]
- sysobjects
## Tables Written
- [[CustomersSalesFrom0toMax]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersSalesFrom0toMax]]
- [[TransactionsHeaders]]
- sysobjects

**Tables Written**
- [[CustomersSalesFrom0toMax]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
