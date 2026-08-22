---
type: relation
database: Olives_BO
name: OrdersDetails--Items
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[OrdersDetails]]
referenced_table: [[Items]]
columns: "OrdersDetails.CompanyID,ItemCode → Items.CompanyID,ItemCode"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# OrdersDetails → Items

**FK**: OrdersDetails.CompanyID,ItemCode → [[Items]].CompanyID,ItemCode

**Business meaning**: Which product each order line buys; unit conversion resolves through UnitID to ItemsUnits.ID. Composite with CompanyID - item codes repeat across companies.

## Tenancy

Chatbot queries `t.OrdersDetails` and `t.Items` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[OrdersDetails]]
- [[Items]]
- [[OrdersHeaders--OrdersDetails]]
- [[Items--OT_ItemsMF]]
