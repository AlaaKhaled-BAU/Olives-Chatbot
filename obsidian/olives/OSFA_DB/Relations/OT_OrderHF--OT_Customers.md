---
type: relation
database: OSFA_DB
name: OT_OrderHF--OT_Customers
tags: [#convention, #mobile]
support_relevance: high
parent_table: [[OT_OrderHF]]
referenced_table: [[OT_Customers]]
columns: "OT_OrderHF.CompNo,CustomerNo → OT_Customers.CompNo,CustomerNo"
last_verified: 2026-08-22
verified_source: db/vault_graph.json
---

# OT_OrderHF → OT_Customers

**Convention join** (no DB-level FK): OT_OrderHF.CompNo+CustomerNo → [[OT_Customers]].CompNo+CustomerNo

**Business meaning**: Tablet order header points at the customer snapshot row synced to the device. Keyed by CompNo+CustomerNo — the earlier CustomerID claim referenced a column that does not exist on this table (verified against vault_graph.json).

## Tenancy

OSFA staging row keyed by CompNo (+SalesmanNo snapshot dimension where present). Informational only: chatbot never queries OSFA_DB.

## See also

- [[OT_OrderHF]]
- [[OT_Customers]]
- [[Sync-Architecture]]
