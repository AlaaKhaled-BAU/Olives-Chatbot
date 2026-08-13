---
type: procedure
database: Olives_BO
name: Falcons_Integ_Send_StatmentOfAccount
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[CustomerStatmentOfAccount]]
  - [[Customers]]
  - Falcons_Integration
  - db_cursor
  - `dbo`
writes_to:
  - [[CustomerStatmentOfAccount]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Falcons_Integ_Send_StatmentOfAccount


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerStatmentOfAccount, Customers, Falcons_Integration, db_cursor, dbo. Writes CustomerStatmentOfAccount. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 290
## Tables Read
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- Falcons_Integration
- db_cursor
- `dbo`
## Tables Written
- [[CustomerStatmentOfAccount]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- Falcons_Integration
- db_cursor
- dbo

**Tables Written**
- [[CustomerStatmentOfAccount]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
