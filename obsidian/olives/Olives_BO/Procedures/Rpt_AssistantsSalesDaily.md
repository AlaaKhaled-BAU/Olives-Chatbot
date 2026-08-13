---
type: procedure
database: Olives_BO
name: Rpt_AssistantsSalesDaily
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - [[Items]]
  - [[SalespersonsAssistants]]
  - [[SalespersonsAssistantsTransactions]]
  - [[TargetsReferences]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_AssistantsSalesDaily


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, SalespersonsAssistants, SalespersonsAssistantsTransactions, TargetsReferences, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID Smallint =1
- @FromDate SmallDateTime ='2021-05-01'
- @ToDate SmallDateTime ='2021-05-29'
- @FromAssist int =1
- @ToAssist int =9999
## Tables Read
- [[Items]]
- [[SalespersonsAssistants]]
- [[SalespersonsAssistantsTransactions]]
- [[TargetsReferences]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Items]]
- [[SalespersonsAssistants]]
- [[SalespersonsAssistantsTransactions]]
- [[TargetsReferences]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

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
