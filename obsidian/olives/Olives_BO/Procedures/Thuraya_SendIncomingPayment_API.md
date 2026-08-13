---
type: procedure
database: Olives_BO
name: Thuraya_SendIncomingPayment_API
schema: dbo
tags: [#backoffice]
reads_from:
  - Customers
  - CustomersPaidTransList
  - Receipts_PaidTrans
  - SalesPersons
writes_to:
  - IntegrationErrorLog
  - Receipts
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Thuraya_SendIncomingPayment_API

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 4 table(s); writes 2; calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompNo int
- @Output int OUTPUT
## Tables Read
- [[Customers]]
- [[CustomersPaidTransList]]
- [[Receipts_PaidTrans]]
- [[SalesPersons]]
## Tables Written
- [[IntegrationErrorLog]]
- [[Receipts]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- [[Write_Files]]
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
