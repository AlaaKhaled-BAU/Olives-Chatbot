---
type: procedure
database: Olives_BO
name: Pro_JoTaxResend
schema: dbo
tags: [#backoffice, #billing, #legal]
reads_from:
  - Headers
  - [[JoTaxResult]]
  - OSFA_DB
  - [[TransactionsHeaders]]
  - cursor
writes_to:
  - [[OT_InvoiceHF]]
  - [[TransactionsHeaders]]
called_by:
  - [[JoTax_Integ_SendTransaction]]
support_relevance: high
last_verified: 2026-07-05
---
# Pro_JoTaxResend


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Headers, JoTaxResult, OSFA_DB, TransactionsHeaders, cursor. Writes OT_InvoiceHF, TransactionsHeaders. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int =1
## Tables Read
- Headers
- [[JoTaxResult]]
- OSFA_DB
- [[TransactionsHeaders]]
- cursor
## Tables Written
- [[OT_InvoiceHF]]
- [[TransactionsHeaders]]
## Callers
_None (no known callers)_
## Callees
- [[JoTax_Integ_SendTransaction]]
## Impact / Dependencies

**Tables Read**
- Headers
- [[JoTaxResult]]
- OSFA_DB
- [[TransactionsHeaders]]
- cursor

**Tables Written**
- [[OT_InvoiceHF]]
- [[TransactionsHeaders]]

**Callers**
- [[JoTax_Integ_SendTransaction]]

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
