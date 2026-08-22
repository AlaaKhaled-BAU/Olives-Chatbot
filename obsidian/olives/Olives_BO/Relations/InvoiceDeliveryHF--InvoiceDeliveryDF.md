---
type: relation
database: Olives_BO
name: InvoiceDeliveryHF--InvoiceDeliveryDF
tags: [#convention, #backoffice]
support_relevance: high
parent_table: [[InvoiceDeliveryHF]]
referenced_table: [[InvoiceDeliveryDF]]
columns: "InvoiceDeliveryHF.CompNo,VouYear,VouNo,VouType → InvoiceDeliveryDF.CompNo,VouYear,VouNo,VouType"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# InvoiceDeliveryHF → InvoiceDeliveryDF

**Convention join** (no DB-level FK): InvoiceDeliveryHF.CompNo,VouYear,VouNo,VouType → [[InvoiceDeliveryDF]].CompNo,VouYear,VouNo,VouType

**Business meaning**: Delivery-stage invoice lines to header (IsDelivered / DeliveredSalesmanNo live on the header). Convention join - no DB constraint.

## Tenancy

Chatbot queries `t.InvoiceDeliveryHF` and `t.InvoiceDeliveryDF` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[InvoiceDeliveryHF]]
- [[InvoiceDeliveryDF]]
- [[InvoiceHistoryHF--InvoiceHistoryDF]]
- [[InvoiceDeliveryHF--Customers]]
