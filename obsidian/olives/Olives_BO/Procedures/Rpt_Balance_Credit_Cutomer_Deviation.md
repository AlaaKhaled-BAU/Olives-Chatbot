---
type: procedure
database: Olives_BO
name: Rpt_Balance_Credit_Cutomer_Deviation
schema: dbo
tags: [#backoffice, #billing, #inventory, #reporting]
reads_from:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_Balance_Credit_Cutomer_Deviation


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersFinancialDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @compno int=1
- @FromCustomer nvarchar(15)=0
- @ToCustomer nvarchar(15)='zzzzzzz'
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersFinancialDetails]]

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
