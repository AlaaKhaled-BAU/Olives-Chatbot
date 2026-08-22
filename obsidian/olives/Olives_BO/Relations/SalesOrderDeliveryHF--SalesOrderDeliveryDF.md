---
type: relation
database: Olives_BO
name: SalesOrderDeliveryHF--SalesOrderDeliveryDF
tags: [#convention, #backoffice]
support_relevance: high
parent_table: [[SalesOrderDeliveryHF]]
referenced_table: [[SalesOrderDeliveryDF]]
columns: "SalesOrderDeliveryHF.CompNo,OrderYear,OrderNo → SalesOrderDeliveryDF.CompNo,OrderYear,OrderNo"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# SalesOrderDeliveryHF → SalesOrderDeliveryDF

**Convention join** (no DB-level FK): SalesOrderDeliveryHF.CompNo,OrderYear,OrderNo → [[SalesOrderDeliveryDF]].CompNo,OrderYear,OrderNo

**Business meaning**: Delivered-order lines to header; DF carries OrderedQty/DeliveredQty/OutstandingQty so fill-rate questions resolve here. Convention join.

## Tenancy

Chatbot queries `t.SalesOrderDeliveryHF` and `t.SalesOrderDeliveryDF` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[SalesOrderDeliveryHF]]
- [[SalesOrderDeliveryDF]]
- [[SalesOrderDeliveryHF--Customers]]
