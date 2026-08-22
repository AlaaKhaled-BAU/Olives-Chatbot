---
type: relation
database: Olives_BO
name: Items--OT_ItemsMF
tags: [#sync, #cross-db, #items]
support_relevance: high
parent_table: [[Items]]
referenced_table: [[OT_ItemsMF]]
columns: "Items.CompanyID,ItemCode ↔ OT_ItemsMF.CompNo(+SalesmanNo),ItemNo"
sync_driver: "[[OT_SendItemsInfo]] <- [[OT_SendSalesmanData]] (inferred)"
last_verified: 2026-08-22
verified_source: db/vault_graph.json
---

# Items → OT_ItemsMF

**Sync mapping** (no literal FK): Olives_BO item master ↔ OSFA tablet replica. BO key = CompanyID+ItemCode; tablet PK = CompNo+SalesmanNo+ItemNo. Value equivalence ItemCode↔ItemNo is `(inferred)` from naming and the OT_InvoiceDF--OT_Items note; column existence verified both sides.

**Business meaning**: New or changed items reach a van only after a successful item sync pushed by [[OT_SendItemsInfo]] under [[OT_SendSalesmanData]] (driver attribution `(inferred)` from shard-8 map). A missing item in custody loading almost always means sync skipped it: item not in [[SalesPersonItemsAssignment]], missing category/default-unit INNER JOIN, or Items suspended flag set. Corrects the previous Items.ID ↔ ItemID line — Items has no ID column.

## Tenancy

Informational sync mapping only. The chatbot NEVER queries OT_* / OSFA_DB staging tables; all answers come from t. views on Olives_BO. See [[Sync-Architecture]] (shard 8, pending).

## See also

- [[Items]]
- [[OT_ItemsMF]]
- [[OT_SendItemsInfo]]
- [[SalesPersonItemsAssignment]]
- [[Sync-Architecture]]
