---
type: relation
database: Olives_BO
name: Receipts_PaidTrans--Receipts
tags: [#convention, #backoffice]
support_relevance: high
parent_table: [[Receipts_PaidTrans]]
referenced_table: [[Receipts]]
columns: "Receipts_PaidTrans.CompanyID,TransactionTypeID,TransactionYear,TransactionNo → Receipts.CompanyID,TransactionTypeID,TransactionYear,TransactionNo"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# Receipts_PaidTrans → Receipts

**Convention join** (no DB-level FK): Receipts_PaidTrans.CompanyID+TransactionTypeID+TransactionYear+TransactionNo → [[Receipts]].CompanyID+TransactionTypeID+TransactionYear+TransactionNo

**Business meaning**: Each paid-trans row records an amount settled against a receipt session (PaidAmount plus optional discount). Fixes the previous claim of a `ReceiptID → Receipts.ID` FK: no ReceiptID column exists on this table.

## Tenancy

Chatbot queries `t.Receipts_PaidTrans` and `t.Receipts` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[Receipts_PaidTrans]]
- [[Receipts]]
- [[Checks--Receipts]]
- [[_MOC-Olives_BO]]
