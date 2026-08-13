---
type: procedure
database: OSFA_DB
name: Pro_SendOrderSMS
schema: dbo
tags: [#integration]
reads_from:
  - OT_CustomerMF
  - OT_InvoiceHF
writes_to:
  - OrdersSMSSebd
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Pro_SendOrderSMS

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in OSFA_DB — reads 2 table(s); writes 1. See sections below for the full dependency map.
## Parameters
_None_
## Tables Read
- [[OT_CustomerMF]]
- [[OT_InvoiceHF]]
## Tables Written
- [[OrdersSMSSebd]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
_None_
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-OSFA_DB|OSFA_DB MOC]]
