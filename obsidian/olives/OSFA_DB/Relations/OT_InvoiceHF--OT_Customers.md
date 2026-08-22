---
type: relation
database: OSFA_DB
name: OT_InvoiceHF--OT_Customers
tags: [#convention, #mobile]
support_relevance: high
parent_table: [[OT_InvoiceHF]]
referenced_table: [[OT_Customers]]
columns: "OT_InvoiceHF.CompNo,CustomerNo → OT_Customers.CompNo,CustomerNo"
last_verified: 2026-08-22
verified_source: db/vault_graph.json
---

# OT_InvoiceHF → OT_Customers

**Convention join** (no DB-level FK): OT_InvoiceHF.CompNo+CustomerNo → [[OT_Customers]].CompNo+CustomerNo

**Business meaning**: Tablet invoice header points at the customer snapshot row synced to the device. Keyed by CompNo+CustomerNo — the earlier CustomerID claim referenced a column that does not exist on this table (verified against vault_graph.json).

## Tenancy

OSFA staging row keyed by CompNo (+SalesmanNo snapshot dimension where present). Informational only: chatbot never queries OSFA_DB.

## See also

- [[OT_InvoiceHF]]
- [[OT_Customers]]
- [[Sync-Architecture]]
