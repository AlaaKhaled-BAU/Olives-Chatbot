---
type: relation
database: Olives_BO
name: ReturnOrdersHeaders--SalesPersons
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[ReturnOrdersHeaders]]
referenced_table: [[SalesPersons]]
columns: "ReturnOrdersHeaders.CompanyID,SalesPersonID → SalesPersons.CompanyID,ID"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# ReturnOrdersHeaders → SalesPersons

**FK**: ReturnOrdersHeaders.CompanyID,SalesPersonID → [[SalesPersons]].CompanyID,ID

**Business meaning**: Salesman who collected the return - nets against his sold quantities.

## Tenancy

Chatbot queries `t.ReturnOrdersHeaders` and `t.SalesPersons` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[ReturnOrdersHeaders]]
- [[SalesPersons]]
- [[ReturnOrdersHeaders--Customers]]
- [[TransactionsHeaders--SalesPersons]]
