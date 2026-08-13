---
type: relation
database: OSFA_DB
name: OT_InvoiceDF--OT_Items
tags: [#fk, #mobile]
support_relevance: high
parent_table: [[OT_InvoiceDF]]
referenced_table: `"`OT_Items`"`
columns: "OT_InvoiceDF.ItemNo → `OT_Items`.ItemNo"
---

# OT_InvoiceDF → OT_Items

**FK**: OT_InvoiceDF.ItemNo → `OT_Items`.ItemNo

**Business meaning**: Mobile invoice lines reference the item catalog synced from BO to the tablet.

**Source table**: [[OT_InvoiceDF]]
**Target table**: `OT_Items`
