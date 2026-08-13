---
type: procedure
database: Olives_BO
name: Rpt_ChecksTest
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[Checks]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_ChecksTest


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Checks. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint =1
- @FromDate nvarchar(50)='2020-1-1'
- @ToDate nvarchar(50)='2025-1-1'
- @BankID int = -1
## Tables Read
- [[Checks]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Checks]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
