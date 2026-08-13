---
type: procedure
database: Olives_BO
name: Rpt_first_last_visit_Invoice_TowerExcel
schema: dbo
tags: [#backoffice, #billing, #reporting, #sales]
reads_from:
  - [[LogActionTransaction]]
  - [[SalesPersonsDevicePermissions]]
  - [[TransactionsHeaders]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_first_last_visit_Invoice_TowerExcel


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads LogActionTransaction, SalesPersonsDevicePermissions, TransactionsHeaders, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNO int
- @Date smalldatetime
## Tables Read
- [[LogActionTransaction]]
- [[SalesPersonsDevicePermissions]]
- [[TransactionsHeaders]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[LogActionTransaction]]
- [[SalesPersonsDevicePermissions]]
- [[TransactionsHeaders]]
- [[salespersons]]

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
