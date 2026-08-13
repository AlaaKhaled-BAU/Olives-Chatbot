---
type: procedure
database: Olives_BO
name: AX_INTEG_SENDSALESQUOTATIONS
schema: dbo
tags: [#backoffice, #integration, #order, #sales]
reads_from:
  - [[Companies]]
  - [[ProspectiveCustomers]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# AX_INTEG_SENDSALESQUOTATIONS


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Companies, ProspectiveCustomers, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
_None_
## Tables Read
- [[Companies]]
- [[ProspectiveCustomers]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Companies]]
- [[ProspectiveCustomers]]
- dbo

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
