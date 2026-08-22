---
type: relation
database: Olives_BO
name: TransactionsHeaders--RoutesInformation
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[TransactionsHeaders]]
referenced_table: [[RoutesInformation]]
columns: "TransactionsHeaders.CompanyID,RouteID → RoutesInformation.CompanyID,ID"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# TransactionsHeaders → RoutesInformation

**FK**: TransactionsHeaders.CompanyID,RouteID → [[RoutesInformation]].CompanyID,ID

**Business meaning**: Route where the transaction happened; pairs with CustomersFinancialDetails.RouteID to answer coverage and sold-vs-route questions.

## Tenancy

Chatbot queries `t.TransactionsHeaders` and `t.RoutesInformation` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[TransactionsHeaders]]
- [[RoutesInformation]]
- [[CustomersFinancialDetails--RoutesInformation]]
- [[ReturnOrdersHeaders--RoutesInformation]]
