---
type: relation
database: Olives_BO
name: StoresBalances--Items
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[StoresBalances]]
referenced_table: [[Items]]
columns: "StoresBalances.CompanyID,ItemCode → Items.CompanyID,ItemCode"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# StoresBalances → Items

**FK**: StoresBalances.CompanyID,ItemCode → [[Items]].CompanyID,ItemCode

**Business meaning**: Current stock snapshot per store (CompanyID+StoreNo+ItemCode gives Qty). StoreNo has NO FK target - no Stores dimension table exists; treat store numbers as bare codes. For movement history use TransactionsDetails instead.

## Tenancy

Chatbot queries `t.StoresBalances` and `t.Items` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[StoresBalances]]
- [[Items]]
- [[StoresBalances]]
- [[TransactionsDetails--Items]]
- [[_MOC-Olives_BO]]
