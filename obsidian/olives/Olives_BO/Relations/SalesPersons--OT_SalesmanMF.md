---
type: relation
database: Olives_BO
name: SalesPersons--OT_SalesmanMF
tags: [#sync, #cross-db, #backoffice]
support_relevance: high
parent_table: [[SalesPersons]]
referenced_table: [[OT_SalesmanMF]]
columns: "SalesPersons.CompanyID,ID ↔ OT_SalesmanMF.CompNo,SalesmanNo"
last_verified: 2026-08-22
verified_source: db/vault_graph.json
---

# SalesPersons → OT_SalesmanMF

**Sync mapping**: SalesPersons.CompanyID,ID ↔ OT_SalesmanMF.CompNo,SalesmanNo

**Business meaning**: **Sync mapping** (no literal FK): salesman master vs tablet login row (Password, NextSerial counters, StoreNo). Mapping `(inferred)` from column shapes. Serial counters (NextSerial/InvNextSerial/RecNextSerial) live per device; diverging serials are a classic duplicate-voucher cause.

## Tenancy

Informational sync mapping only. The chatbot NEVER queries OT_* / OSFA_DB staging tables; all answers come from t. views on Olives_BO. See [[Sync-Architecture]] (shard 8, pending).

## See also

- [[SalesPersons]]
- [[OT_SalesmanMF]]
- [[Sync-Architecture]]
