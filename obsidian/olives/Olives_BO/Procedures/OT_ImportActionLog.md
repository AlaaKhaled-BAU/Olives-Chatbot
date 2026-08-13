---
type: procedure
database: Olives_BO
name: OT_ImportActionLog
schema: dbo
tags: [#backoffice, #log, #mobile]
reads_from:
  - [[ClientsActive]]
  - [[LogActionTransaction]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[CustomerStockTacking]]
  - [[LogActionTransaction]]
  - [[OrdersHeaders]]
  - [[OT_ActionLog]]
  - [[PendingInvoices]]
  - [[Receipts]]
  - [[ReturnOrdersHeaders]]
  - [[SalespersonsAssistantsTransactions]]
  - [[SalesQuotationHeaders]]
  - [[TransactionsHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportActionLog


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, LogActionTransaction, SalesPersons, dbo. Writes CustomerStockTacking, LogActionTransaction, OrdersHeaders, OT_ActionLog, PendingInvoices, Receipts, ReturnOrdersHeaders, SalespersonsAssistantsTransactions, SalesQuotationHeaders, TransactionsHeaders. Invoked by 3 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
## Tables Read
- [[ClientsActive]]
- [[LogActionTransaction]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[CustomerStockTacking]]
- [[LogActionTransaction]]
- [[OrdersHeaders]]
- [[OT_ActionLog]]
- [[PendingInvoices]]
- [[Receipts]]
- [[ReturnOrdersHeaders]]
- [[SalespersonsAssistantsTransactions]]
- [[SalesQuotationHeaders]]
- [[TransactionsHeaders]]
## Callers
- [[AbuOda_Comp2_Integ]]
- [[Qetaf_Integ]]
- [[RamPharm_SAP_Integ]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[LogActionTransaction]]
- [[SalesPersons]]
- dbo

**Tables Written**
- [[CustomerStockTacking]]
- [[LogActionTransaction]]
- [[OrdersHeaders]]
- [[OT_ActionLog]]
- [[PendingInvoices]]
- [[Receipts]]
- [[ReturnOrdersHeaders]]
- [[SalespersonsAssistantsTransactions]]
- [[SalesQuotationHeaders]]
- [[TransactionsHeaders]]

**Callers**
_None_

**Callees**
- [[AbuOda_Comp2_Integ]]
- [[Qetaf_Integ]]
- [[RamPharm_SAP_Integ]]


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
