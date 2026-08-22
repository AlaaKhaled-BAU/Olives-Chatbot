---
type: relation
database: Olives_BO
name: InvoiceDeliveryHF--Customers
tags: [#convention, #backoffice]
support_relevance: high
parent_table: [[InvoiceDeliveryHF]]
referenced_table: [[Customers]]
columns: "InvoiceDeliveryHF.CompNo,CustomerNo → Customers.CompanyID,ID"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# InvoiceDeliveryHF → Customers

**Convention join** (no DB-level FK): InvoiceDeliveryHF.CompNo,CustomerNo → [[Customers]].CompanyID,ID

**Business meaning**: Recipient customer of a delivery-stage invoice; reconciles what left the van versus what was invoiced.

## Tenancy

Chatbot queries `t.InvoiceDeliveryHF` and `t.Customers` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[InvoiceDeliveryHF]]
- [[Customers]]
- [[InvoiceDeliveryHF--InvoiceDeliveryDF]]
- [[InvoiceHistoryHF--Customers]]
