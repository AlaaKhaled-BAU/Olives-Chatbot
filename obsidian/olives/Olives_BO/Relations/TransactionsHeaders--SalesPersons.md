---
type: relation
database: Olives_BO
name: TransactionsHeaders--SalesPersons
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[TransactionsHeaders]]
referenced_table: [[SalesPersons]]
columns: "TransactionsHeaders.CompanyID,SalesPersonID → SalesPersons.CompanyID,ID"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# TransactionsHeaders → SalesPersons

**FK**: TransactionsHeaders.CompanyID,SalesPersonID → [[SalesPersons]].CompanyID,ID

**Business meaning**: The salesman who executed an inventory movement (sales, issue, receipt of goods) - the actor dimension for movement reports.

## Tenancy

Chatbot queries `t.TransactionsHeaders` and `t.SalesPersons` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[TransactionsHeaders]]
- [[SalesPersons]]
- [[OrdersHeaders--SalesPersons]]
- [[Receipts--SalesPersons]]
