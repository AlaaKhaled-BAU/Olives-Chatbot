---
type: relation
database: Olives_BO
name: ReturnOrdersHeaders--Customers
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[ReturnOrdersHeaders]]
referenced_table: [[Customers]]
columns: "ReturnOrdersHeaders.CompanyID,CustomerID → Customers.CompanyID,ID"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# ReturnOrdersHeaders → Customers

**FK**: ReturnOrdersHeaders.CompanyID,CustomerID → [[Customers]].CompanyID,ID

**Business meaning**: Customer who returned goods; drives return-rate and reversal reporting.

## Tenancy

Chatbot queries `t.ReturnOrdersHeaders` and `t.Customers` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[ReturnOrdersHeaders]]
- [[Customers]]
- [[ReturnOrdersHeaders--SalesPersons]]
- [[InvoiceHistoryHF--Customers]]
