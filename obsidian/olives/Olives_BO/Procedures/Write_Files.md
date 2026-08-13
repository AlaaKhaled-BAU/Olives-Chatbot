---
type: procedure
database: Olives_BO
name: Write_Files
schema: dbo
tags: [#maintenance]
reads_from:
writes_to:
called_by:
  - Pro_Customers
  - Thuraya_SendIncomingPayment_API
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Write_Files

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — called by 2 proc(s); calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @doc_name varchar(MAX)
- @Document varbinary(MAX)
- @Doc_Path varchar(MAX)
- @output tinyint OUTPUT
## Tables Read
_None_
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
- [[Pro_Customers]]
- [[Thuraya_SendIncomingPayment_API]]
## Callees
- [[Create_Directory]]
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
