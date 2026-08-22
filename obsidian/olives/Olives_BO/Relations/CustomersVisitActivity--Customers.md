---
type: relation
database: Olives_BO
name: CustomersVisitActivity--Customers
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[CustomersVisitActivity]]
referenced_table: [[Customers]]
columns: "CustomersVisitActivity.CompanyID,CustomerID → Customers.CompanyID,ID"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# CustomersVisitActivity → Customers

**FK**: CustomersVisitActivity.CompanyID,CustomerID → [[Customers]].CompanyID,ID

**Business meaning**: Visit activity requirement/log per customer (keyed also by PositionsID) controlling activity capture during order flow.

## Tenancy

Chatbot queries `t.CustomersVisitActivity` and `t.Customers` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[CustomersVisitActivity]]
- [[Customers]]
- [[CustomersFinancialDetails--RoutesInformation]]
- [[SalespersonsGPSTracking--SalesPersons]]
