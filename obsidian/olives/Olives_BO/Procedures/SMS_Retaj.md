---
type: procedure
database: Olives_BO
name: SMS_Retaj
schema: dbo
tags: [#integration]
reads_from:
  - Customers
  - OrdersDetails
  - OrdersHeaders
  - Receipts
  - TransactionsDetails
  - TransactionsHeaders
writes_to:
  - LogActionTransaction
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# SMS_Retaj

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 6 table(s); writes 1; calls 2 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
## Tables Read
- [[Customers]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
- [[LogActionTransaction]]
## Cross-DB Tables
References tables in **OSFA_DB** (qualified as `OSFA_DB.dbo.*`):
- [[OSFA_DB/Tables/OT_InvoiceHF|OT_InvoiceHF]]
- [[OSFA_DB/Tables/OT_Payments|OT_Payments]]
## Callers
_None_
## Callees
- `parseJSON`
- `trim`
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
