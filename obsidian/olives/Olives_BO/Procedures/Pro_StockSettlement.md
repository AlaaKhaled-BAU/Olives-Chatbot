---
type: procedure
database: Olives_BO
name: Pro_StockSettlement
schema: dbo
tags: [#backoffice, #inventory]
reads_from:
  - [[Items]]
  - [[ItemsUnits]]
  - OPENJSON
  - [[SalesPersons]]
  - [[TransfersOrdersDetails]]
  - [[TransfersOrdersHeaders]]
  - `dbo`
writes_to:
  - [[OT_InvoiceDF]]
  - [[OT_InvoiceHF]]
  - [[TransactionsHeaders]]
  - [[TransfersOrdersHeaders]]
called_by:
  - Pro_StockSettlement_182
  - sp_OACreate
  - sp_OADestroy
  - sp_OAGetProperty
  - sp_OAMethod
support_relevance: high
last_verified: 2026-07-05
---
# Pro_StockSettlement


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, ItemsUnits, OPENJSON, SalesPersons, TransfersOrdersDetails, TransfersOrdersHeaders, dbo. Writes OT_InvoiceDF, OT_InvoiceHF, TransactionsHeaders, TransfersOrdersHeaders. Calls 5 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo SmallInt = 2
- @CompBranch Int = 1
- @SalesmanID Int = 116
- @TrDate date  = '2025-01-20'
- @UserID Nvarchar(50) = 'admin'
## Tables Read
- [[Items]]
- [[ItemsUnits]]
- OPENJSON
- [[SalesPersons]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
- `dbo`
## Tables Written
- [[OT_InvoiceDF]]
- [[OT_InvoiceHF]]
- [[TransactionsHeaders]]
- [[TransfersOrdersHeaders]]
## Callers
_None (no known callers)_
## Callees
- Pro_StockSettlement_182
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod
## Impact / Dependencies

**Tables Read**
- [[Items]]
- [[ItemsUnits]]
- OPENJSON
- [[SalesPersons]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
- dbo

**Tables Written**
- [[OT_InvoiceDF]]
- [[OT_InvoiceHF]]
- [[TransactionsHeaders]]
- [[TransfersOrdersHeaders]]

**Callers**
- Pro_StockSettlement_182
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
