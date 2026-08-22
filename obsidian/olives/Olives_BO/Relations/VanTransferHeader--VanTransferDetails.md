---
type: relation
database: Olives_BO
name: VanTransferHeader--VanTransferDetails
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[VanTransferHeader]]
referenced_table: [[VanTransferDetails]]
columns: "VanTransferDetails.CompanyID,OrderYear,OrderNo → VanTransferHeader.CompanyID,OrderYear,OrderNo"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# VanTransferHeader → VanTransferDetails

**FK**: VanTransferDetails.CompanyID,OrderYear,OrderNo → [[VanTransferDetails]].CompanyID,OrderYear,OrderNo

**Business meaning**: Van-to-van transfer lines under their header; FromSalespersonID/ToSalespersonID on the header say which vans exchanged stock.

## Tenancy

Chatbot queries `t.VanTransferHeader` and `t.VanTransferDetails` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[VanTransferHeader]]
- [[VanTransferDetails]]
- [[TransfersOrdersHeaders--TransfersOrdersDetails]]
