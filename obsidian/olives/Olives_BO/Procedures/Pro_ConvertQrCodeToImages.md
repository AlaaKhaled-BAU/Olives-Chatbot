---
type: procedure
database: Olives_BO
name: Pro_ConvertQrCodeToImages
schema: dbo
tags: [#backoffice]
reads_from:
  - JoTaxResult
  - TransactionsHeaders
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Pro_ConvertQrCodeToImages

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 2 table(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromDate date
- @ToDate date
## Tables Read
- [[JoTaxResult]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
_None_
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
