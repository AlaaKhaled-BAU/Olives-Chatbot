---
type: relation
database: Olives_BO
name: Checks--Receipts
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[Checks]]
referenced_table: [[Receipts]]
columns: "Checks.CompanyID,TransactionTypeID,TransactionYear,TransactionNo → Receipts.CompanyID,TransactionTypeID,TransactionYear,TransactionNo"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# Checks → Receipts

**FK**: Checks.CompanyID,TransactionTypeID,TransactionYear,TransactionNo → [[Receipts]].CompanyID,TransactionTypeID,TransactionYear,TransactionNo

**Business meaning**: Check instruments collected under a receipt session; the four-part key ties each check to the visit receipt that took it. Core for check aging and due-date follow-up.

## Tenancy

Chatbot queries `t.Checks` and `t.Receipts` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[Checks]]
- [[Receipts]]
- [[Checks--Customers]]
- [[Checks--Banks]]
- [[Receipts_PaidTrans--Receipts]]
