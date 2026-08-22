---
type: relation
database: Olives_BO
name: Receipts_Currency--Receipts
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[Receipts_Currency]]
referenced_table: [[Receipts]]
columns: "Receipts_Currency.CompanyID,TransactionTypeID,TransactionYear,TransactionNo → Receipts.CompanyID,TransactionTypeID,TransactionYear,TransactionNo"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# Receipts_Currency → Receipts

**FK**: Receipts_Currency.CompanyID,TransactionTypeID,TransactionYear,TransactionNo → [[Receipts]].CompanyID,TransactionTypeID,TransactionYear,TransactionNo

**Business meaning**: Per-currency breakdown of each receipt amount; joins on the same four-part key as Checks.

## Tenancy

Chatbot queries `t.Receipts_Currency` and `t.Receipts` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[Receipts_Currency]]
- [[Receipts]]
- [[Receipts--Customers]]
- [[Receipts--Currencies]]
