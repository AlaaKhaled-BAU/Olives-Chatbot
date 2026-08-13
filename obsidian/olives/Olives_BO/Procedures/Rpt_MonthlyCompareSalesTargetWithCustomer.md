---
type: procedure
database: Olives_BO
name: Rpt_MonthlyCompareSalesTargetWithCustomer
schema: dbo
tags: [#backoffice, #customer, #reporting, #sales]
reads_from:
  - [[ClientsActive]]
  - [[CustomerTargets]]
  - [[CustomerTargetsDetails]]
  - [[Customers]]
  - [[Items]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[TargetsReferences]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_MonthlyCompareSalesTargetWithCustomer


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, CustomerTargets, CustomerTargetsDetails, Customers, Items, OrdersDetails, OrdersHeaders, TargetsReferences, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @FromCustomer bigint=314
- @ToCustomer bigint=314
- @Year smallint=2023
- @FromMonth smallint=1
- @ToMonth smallint=1
- @UserID nvarchar(50)=null
- @IsMainTarget smallint = 1
## Tables Read
- [[ClientsActive]]
- [[CustomerTargets]]
- [[CustomerTargetsDetails]]
- [[Customers]]
- [[Items]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[TargetsReferences]]
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
- [[ClientsActive]]
- [[CustomerTargets]]
- [[CustomerTargetsDetails]]
- [[Customers]]
- [[Items]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[TargetsReferences]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
