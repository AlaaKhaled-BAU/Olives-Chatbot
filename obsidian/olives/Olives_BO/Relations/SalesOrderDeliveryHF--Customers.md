---
type: relation
database: Olives_BO
name: SalesOrderDeliveryHF--Customers
tags: [#convention, #backoffice]
support_relevance: high
parent_table: [[SalesOrderDeliveryHF]]
referenced_table: [[Customers]]
columns: "SalesOrderDeliveryHF.CompNo,CustomerNo → Customers.CompanyID,ID"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# SalesOrderDeliveryHF → Customers

**Convention join** (no DB-level FK): SalesOrderDeliveryHF.CompNo,CustomerNo → [[Customers]].CompanyID,ID

**Business meaning**: Customer that placed the delivered sales order; CompNo maps to Customers.CompanyID.

## Tenancy

Chatbot queries `t.SalesOrderDeliveryHF` and `t.Customers` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[SalesOrderDeliveryHF]]
- [[Customers]]
- [[SalesOrderDeliveryHF--SalesOrderDeliveryDF]]
- [[OrdersHeaders--Customers]]
