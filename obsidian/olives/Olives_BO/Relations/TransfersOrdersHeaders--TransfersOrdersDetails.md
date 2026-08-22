---
type: relation
database: Olives_BO
name: TransfersOrdersHeaders--TransfersOrdersDetails
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[TransfersOrdersHeaders]]
referenced_table: [[TransfersOrdersDetails]]
columns: "TransfersOrdersDetails.CompanyID,OrderYear,OrderNo,VouType → TransfersOrdersHeaders.CompanyID,OrderYear,OrderNo,VouType"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# TransfersOrdersHeaders → TransfersOrdersDetails

**FK**: TransfersOrdersDetails.CompanyID,OrderYear,OrderNo,VouType → [[TransfersOrdersDetails]].CompanyID,OrderYear,OrderNo,VouType

**Business meaning**: Van-stock transfer lines under their voucher (FK declared on the details side); VouType separates request from issue vouchers.

## Tenancy

Chatbot queries `t.TransfersOrdersHeaders` and `t.TransfersOrdersDetails` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[TransfersOrdersHeaders]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersDetails--Items]]
- [[VanTransferHeader--VanTransferDetails]]
