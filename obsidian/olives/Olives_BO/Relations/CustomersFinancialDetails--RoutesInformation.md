---
type: relation
database: Olives_BO
name: CustomersFinancialDetails--RoutesInformation
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[CustomersFinancialDetails]]
referenced_table: [[RoutesInformation]]
columns: "CustomersFinancialDetails.CompanyID,RouteID → RoutesInformation.CompanyID,ID"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# CustomersFinancialDetails → RoutesInformation

**FK**: CustomersFinancialDetails.CompanyID,RouteID → [[RoutesInformation]].CompanyID,ID

**Business meaning**: THE customer-to-route membership path: a customer belongs to a route through this table, not through Customers itself. Every "customers on route X" query goes here.

## Tenancy

Chatbot queries `t.CustomersFinancialDetails` and `t.RoutesInformation` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[CustomersFinancialDetails]]
- [[RoutesInformation]]
- [[SalesPersonsRoutes]]
- [[CustomersVisitActivity]]
- [[_MOC-Olives_BO]]
