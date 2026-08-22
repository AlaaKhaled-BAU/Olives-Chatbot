---
type: relation
database: Olives_BO
name: OrdersHeaders--OrdersDetails
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[OrdersHeaders]]
referenced_table: [[OrdersDetails]]
columns: "OrdersHeaders.CompanyID,OrderYear,OrderNo → OrdersDetails.CompanyID,OrderYear,OrderNo"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# OrdersHeaders → OrdersDetails

**FK**: OrdersHeaders.CompanyID,OrderYear,OrderNo → [[OrdersDetails]].CompanyID,OrderYear,OrderNo

**Business meaning**: Order line items belong to their header voucher via the full three-part key (FK declared on the details side). Never join on OrderNo alone - order numbers repeat across years.

## Tenancy

Chatbot queries `t.OrdersHeaders` and `t.OrdersDetails` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[OrdersHeaders]]
- [[OrdersDetails]]
- [[OrdersHeaders--Customers]]
- [[OrdersDetails--Items]]
