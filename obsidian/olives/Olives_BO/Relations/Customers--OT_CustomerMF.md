---
type: relation
database: Olives_BO
name: Customers--OT_CustomerMF
tags: [#sync, #cross-db, #backoffice]
support_relevance: high
parent_table: [[Customers]]
referenced_table: [[OT_CustomerMF]]
columns: "Customers.CompanyID,ID ↔ OT_CustomerMF.CompNo,(SalesmanNo,)CustomerNo"
last_verified: 2026-08-22
verified_source: db/vault_graph.json
---

# Customers → OT_CustomerMF

**Sync mapping**: Customers.CompanyID,ID ↔ OT_CustomerMF.CompNo,(SalesmanNo,)CustomerNo

**Business meaning**: **Sync mapping** (no literal FK): back-office customer master vs tablet snapshot. CompanyID-CompNo and ID-CustomerNo mapping is `(inferred)`; OT_CustomerMF additionally carries SalesmanNo as the per-van snapshot dimension. A customer appears on a van only after the customers-info sync pushed it (`(inferred)` driver). Balance fields on the replica (CurrBalance/ChqsBalance) are stale snapshots - never answer balance questions from them.

## Tenancy

Informational sync mapping only. The chatbot NEVER queries OT_* / OSFA_DB staging tables; all answers come from t. views on Olives_BO. See [[Sync-Architecture]] (shard 8, pending).

## See also

- [[Customers]]
- [[OT_CustomerMF]]
- [[Sync-Architecture]]
