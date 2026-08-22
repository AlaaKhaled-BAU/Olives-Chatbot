---
type: relation
database: Olives_BO
name: ReturnOrdersHeaders--RoutesInformation
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[ReturnOrdersHeaders]]
referenced_table: [[RoutesInformation]]
columns: "ReturnOrdersHeaders.CompanyID,RouteID → RoutesInformation.CompanyID,ID"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# ReturnOrdersHeaders → RoutesInformation

**FK**: ReturnOrdersHeaders.CompanyID,RouteID → [[RoutesInformation]].CompanyID,ID

**Business meaning**: Route where the return occurred; used in route-quality/coverage reports alongside TransactionsHeaders.RouteID.

## Tenancy

Chatbot queries `t.ReturnOrdersHeaders` and `t.RoutesInformation` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[ReturnOrdersHeaders]]
- [[RoutesInformation]]
- [[TransactionsHeaders--RoutesInformation]]
- [[CustomersFinancialDetails--RoutesInformation]]
