---
type: procedure
database: Olives_BO
name: Alpha_GetItemBalance
schema: dbo
tags: [#backoffice, #inventory]
reads_from:
  - [[Items]]
  - [[SalesPersonItemsAssignment]]
  - [[SalesPersonItemsBalance]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[OT_BatchsInfo]]
  - [[SalesPersonItemsBalance]]
  - [[SalesPersons]]
called_by:
  - [[OT_SendSalesmanData]]
support_relevance: high
last_verified: 2026-07-05
---
# Alpha_GetItemBalance


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, SalesPersonItemsAssignment, SalesPersonItemsBalance, SalesPersons, dbo. Writes OT_BatchsInfo, SalesPersonItemsBalance, SalesPersons. Invoked by 1 procedure(s). Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
- @SalesmanNo int
- @SendDate smalldatetime = null
- @SendCompanyData bit = 1
## Tables Read
- [[Items]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[OT_BatchsInfo]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
## Callers
- [[OT_SendSalesmanData]]
## Callees
- [[OT_SendSalesmanData]]
## Impact / Dependencies

**Tables Read**
- [[Items]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- dbo

**Tables Written**
- [[OT_BatchsInfo]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]

**Callers**
- [[OT_SendSalesmanData]]

**Callees**
- [[OT_SendSalesmanData]]


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
