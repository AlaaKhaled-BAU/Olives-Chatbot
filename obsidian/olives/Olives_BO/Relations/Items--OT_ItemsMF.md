---
type: relation
database: Olives_BO
name: Items--OT_ItemsMF
tags: [#fk, #sync, #cross-db, #items]
support_relevance: high
parent_table: [[Items]]
referenced_table: [[OT_ItemsMF]]
columns: "Items.ID ↔ OT_ItemsMF.ItemID (tablet sync replica)"
---

# Items → OT_ItemsMF

**Sync mapping**: `Items` is the Back-Office item master; `OT_ItemsMF` is its replica on the OSFA tablet (OT_ = Olives Tablet prefix). The tablet reads `OT_ItemsMF` during van custody loading (Upload Order). There is no literal FK — the link is a one-way sync populated by `OT_SendItemsInfo` during "Send Data".

**Business meaning**: New or changed items in BO only appear on the tablet after a successful item sync. A missing item on the tablet almost always means the sync did not push it (see ticket pattern: new items missing in custody loading). Common breakage points in the push chain: `SalesPersonItemsAssignment` (item not assigned to the salesman), `ItemsCategories` / `ItemsUnits` INNER JOINs (missing category or default unit makes the item invisible), and `Items.IsSuspended = 1`.

**Source table**: [[Items]] (Olives_BO)
**Target table**: [[OT_ItemsMF]] (OSFA_DB)
**Sync driver**: [[OT_SendItemsInfo]] → called by [[OT_SendSalesmanData]]

## See also
- [[Items]]
- [[OT_ItemsMF]]
- [[OT_SendItemsInfo]]
- [[SalesPersonItemsAssignment]]
