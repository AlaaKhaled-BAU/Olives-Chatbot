---
type: relation
database: OSFA_DB
name: OT_UnloadOrderHF--OT_SalesPersons
tags: [#fk, #mobile]
support_relevance: medium
parent_table: `"`OT_UnloadOrderHF`"`
referenced_table: `"`OT_SalesPersons`"`
columns: "OT_UnloadOrderHF.SalesmanNo → `OT_SalesPersons`.ID"
---

# OT_UnloadOrderHF → OT_SalesPersons

**FK**: OT_UnloadOrderHF.SalesmanNo → `OT_SalesPersons`.ID

**Business meaning**: Unload orders (returns from van to warehouse) are assigned to a specific salesperson.

**Source table**: `OT_UnloadOrderHF`
**Target table**: `OT_SalesPersons`
