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

Tablet→BO sync for the field action log (called during OSFA import, not by the chatbot).

Reads unposted `OSFA_DB.dbo.OT_ActionLog` (`Posted = 0`) for `@CompNo`, inserts matching rows into BO `LogActionTransaction` (including `OSFA_AutoID`, GPS, `RouteID`, `AssistantsIDs`, `CustLocLineID`, device flags), then sets `OT_ActionLog.Posted = 1`.

After the copy it repairs/enriches BO documents from the log (metadata only — no EXEC from chatbot):
- Dedupes some log rows (`Data5 = '1'`) for visit vs document action groups
- `ActionID` 32: marks `OrdersHeaders.UsedInAutoUploadOrder` using Data1=year, Data2=order no
- Stamps `LocationLineID` onto orders (5), sales invoices (4), return invoices (9), receipts (12), return orders (13), quotations (16), customer stock-taking (26) using Data1=year, Data2=doc no
- Splits `AssistantsIDs` into `SalespersonsAssistantsTransactions`
- `ActionID` 49: last pending-invoice JSON in Data1 → `PendingInvoices`

If this proc fails, tablet rows stay unposted in OSFA and BO visit/document GPS is stale. Chatbot reads the resulting `t.LogActionTransaction` only.
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
