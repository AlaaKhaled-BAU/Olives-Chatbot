---
type: relation
database: Olives_BO
name: Customers--SalesPersons
tags: [#convention, #backoffice]
support_relevance: high
parent_table: [[Customers]]
referenced_table: [[SalesPersons]]
columns: "Customers.CompanyID,SalesPersonID → SalesPersons.CompanyID,ID"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# Customers → SalesPersons

**Convention join** (NO declared FK despite prior note): Customers.CompanyID+SalesPersonID → [[SalesPersons]].CompanyID+ID

**Business meaning**: Assigns each customer to a primary salesperson; drives territory, visit planning and commission attribution. Verified 2026-08-22: no DB constraint backs this link — do not rely on FK metadata to discover it.

## Tenancy

Chatbot queries `t.Customers` and `t.SalesPersons` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[Customers]]
- [[SalesPersons]]
- [[CustomersFinancialDetails--RoutesInformation]]
- [[_MOC-Olives_BO]]
