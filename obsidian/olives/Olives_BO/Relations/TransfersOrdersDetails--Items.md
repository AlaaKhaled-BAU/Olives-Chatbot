---
type: relation
database: Olives_BO
name: TransfersOrdersDetails--Items
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[TransfersOrdersDetails]]
referenced_table: [[Items]]
columns: "TransfersOrdersDetails.CompanyID,ItemCode → Items.CompanyID,ItemCode"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# TransfersOrdersDetails → Items

**FK**: TransfersOrdersDetails.CompanyID,ItemCode → [[Items]].CompanyID,ItemCode

**Business meaning**: Product moved by a transfer line; unit resolution through UnitID to ItemsUnits.ID.

## Tenancy

Chatbot queries `t.TransfersOrdersDetails` and `t.Items` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[TransfersOrdersDetails]]
- [[Items]]
- [[TransfersOrdersHeaders--TransfersOrdersDetails]]
- [[StoresBalances--Items]]
