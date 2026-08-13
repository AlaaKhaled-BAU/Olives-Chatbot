---
type: procedure
database: Olives_BO
name: Rpt_Assistants
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[SalesPersons]]
  - [[SalespersonsAssistants]]
  - [[SalespersonsAssistantsTransactions]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_Assistants


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalesPersons, SalespersonsAssistants, SalespersonsAssistantsTransactions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID SmallInt = 1
- @SalesmanID Int = -1
- @AssistantID Int = -1
- @FromDate SmallDateTime = '2021-05-09'
- @ToDate SmallDateTime = '2021-06-09'
## Tables Read
- [[SalesPersons]]
- [[SalespersonsAssistants]]
- [[SalespersonsAssistantsTransactions]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalesPersons]]
- [[SalespersonsAssistants]]
- [[SalespersonsAssistantsTransactions]]

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
