---
type: procedure
database: Olives_BO
name: Rpt_Niroukh_SalesPerTeamQ
schema: dbo
tags: [#backoffice, #reporting, #sales]
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
# Rpt_Niroukh_SalesPerTeamQ


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerTargets, CustomerTargetsDetails, Customers, InvoiceHistoryDF, InvoiceHistoryHF, Items, TargetsReferences. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 2
- @FromCustomer bigint = 1
- @ToCustomer bigint = 999999999
- @Year smallint = 2024
- @UserID nvarchar(50)='admin'
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

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
