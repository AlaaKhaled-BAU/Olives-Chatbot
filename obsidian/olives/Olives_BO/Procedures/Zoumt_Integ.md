---
type: procedure
database: Olives_BO
name: Zoumt_Integ
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - 168
  - [[TransfersOrdersDetails]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Zoumt_Integ


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads 168, TransfersOrdersDetails. Invoked by 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint
- @OrderYear	smallint
- @OrderNo	int
## Tables Read
- 168
- [[TransfersOrdersDetails]]
## Tables Written
_None_
## Callers
- [[Pro_TransfersOrdersHeaders]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- 168
- [[TransfersOrdersDetails]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
- [[Pro_TransfersOrdersHeaders]]


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
