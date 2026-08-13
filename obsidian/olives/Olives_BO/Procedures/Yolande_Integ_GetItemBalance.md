---
type: procedure
database: Olives_BO
name: Yolande_Integ_GetItemBalance
schema: dbo
tags: [#backoffice, #integration, #inventory]
reads_from:
  - [[Customers]]
  - [[CustomersPaidTransList]]
  - [[SalesPersonItemsBalance]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[CustomersPaidTransList]]
  - [[SalesPersonItemsBalance]]
  - [[SalesPersons]]
called_by:
  - [[OT_SendSalesmanData]]
support_relevance: high
last_verified: 2026-07-05
---
# Yolande_Integ_GetItemBalance


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersPaidTransList, SalesPersonItemsBalance, SalesPersons, dbo. Writes CustomersPaidTransList, SalesPersonItemsBalance, SalesPersons. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @SalesmanNo int
- @SendDate smalldatetime = null
## Tables Read
- [[Customers]]
- [[CustomersPaidTransList]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[CustomersPaidTransList]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
## Callers
_None (no known callers)_
## Callees
- [[OT_SendSalesmanData]]
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersPaidTransList]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- dbo

**Tables Written**
- [[CustomersPaidTransList]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]

**Callers**
- [[OT_SendSalesmanData]]

**Callees**
_None_


## When to Run This

Run when pulling data from an external API/system. Called during sync cycles or on-demand data refresh.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
