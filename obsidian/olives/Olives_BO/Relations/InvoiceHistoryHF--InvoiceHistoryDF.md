---
type: relation
database: Olives_BO
name: InvoiceHistoryHF--InvoiceHistoryDF
tags: [#convention, #backoffice]
support_relevance: high
parent_table: [[InvoiceHistoryHF]]
referenced_table: [[InvoiceHistoryDF]]
columns: "InvoiceHistoryHF.CompNo,VouYear,VouNo,VouType → InvoiceHistoryDF.CompNo,VouYear,VouNo,VouType"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# InvoiceHistoryHF → InvoiceHistoryDF

**Convention join** (no DB-level FK): InvoiceHistoryHF.CompNo,VouYear,VouNo,VouType → [[InvoiceHistoryDF]].CompNo,VouYear,VouNo,VouType

**Business meaning**: Posted invoice lines belong to their header voucher; together they are the authoritative sales history behind most sales/target reports. No DB constraint exists - the four-part key is by convention only.

## Tenancy

Chatbot queries `t.InvoiceHistoryHF` and `t.InvoiceHistoryDF` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[InvoiceHistoryHF]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF--Customers]]
