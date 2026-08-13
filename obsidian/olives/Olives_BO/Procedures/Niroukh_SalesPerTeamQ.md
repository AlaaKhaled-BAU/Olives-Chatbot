---
type: procedure
database: Olives_BO
name: Niroukh_SalesPerTeamQ
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[CustomerTargets]]
  - [[CustomerTargetsDetails]]
  - [[Customers]]
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
  - [[Items]]
  - [[TargetsReferences]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Niroukh_SalesPerTeamQ


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerTargets, CustomerTargetsDetails, Customers, InvoiceHistoryDF, InvoiceHistoryHF, Items, TargetsReferences. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 2
- @FromCustomer bigint = 112110161
- @ToCustomer bigint = 112110623
- @Year smallint = 2024
- @UserID nvarchar(50)='admin'
- @byAmount bit=1
- @FromSalesmanID int =1
- @ToSalesmanID int=9999
- @AchievementType int=1
## Tables Read
- [[CustomerTargets]]
- [[CustomerTargetsDetails]]
- [[Customers]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[TargetsReferences]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomerTargets]]
- [[CustomerTargetsDetails]]
- [[Customers]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[TargetsReferences]]

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
