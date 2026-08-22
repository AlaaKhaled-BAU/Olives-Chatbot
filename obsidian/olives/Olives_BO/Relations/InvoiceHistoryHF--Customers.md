---
type: relation
database: Olives_BO
name: InvoiceHistoryHF--Customers
tags: [#convention, #backoffice]
support_relevance: high
parent_table: [[InvoiceHistoryHF]]
referenced_table: [[Customers]]
columns: "InvoiceHistoryHF.CompNo,CustomerNo → Customers.CompanyID,ID"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# InvoiceHistoryHF → Customers

**Convention join** (no DB-level FK): InvoiceHistoryHF.CompNo,CustomerNo → [[Customers]].CompanyID,ID

**Business meaning**: Attributes every historical invoice to its customer for AR and sales-per-customer reporting. CompNo carries the company id matching Customers.CompanyID; no DB constraint.

## Tenancy

Chatbot queries `t.InvoiceHistoryHF` and `t.Customers` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[InvoiceHistoryHF]]
- [[Customers]]
- [[InvoiceHistoryHF--InvoiceHistoryDF]]
- [[Checks--Customers]]
- [[Receipts--Customers]]
