---
type: procedure
database: Olives_BO
name: Alpha_Integ_SendItemsReplacement
schema: dbo
tags: [#backoffice, #integration, #inventory]
reads_from:
  - 168
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[ItemsReplacementHeaders]]
  - OT_ItemsReplacmentHF_1
  - [[SalesPersons]]
writes_to:
  - 110
  - [[ItemsReplacementHeaders]]
  - [[OT_ItemsReplacmentDF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Alpha_Integ_SendItemsReplacement


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads 168, Customers, CustomersFinancialDetails, ItemsReplacementHeaders, OT_ItemsReplacmentHF_1, SalesPersons. Writes 110, ItemsReplacementHeaders, OT_ItemsReplacmentDF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- 168
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[ItemsReplacementHeaders]]
- OT_ItemsReplacmentHF_1
- [[SalesPersons]]
## Tables Written
- 110
- [[ItemsReplacementHeaders]]
- [[OT_ItemsReplacmentDF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- 168
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[ItemsReplacementHeaders]]
- OT_ItemsReplacmentHF_1
- [[SalesPersons]]

**Tables Written**
- 110
- [[ItemsReplacementHeaders]]
- [[OT_ItemsReplacmentDF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
