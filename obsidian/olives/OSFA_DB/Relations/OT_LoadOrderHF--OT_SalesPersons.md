---
type: relation
database: OSFA_DB
name: OT_LoadOrderHF--OT_SalesPersons
tags: [#fk, #mobile]
support_relevance: medium
parent_table: `"`OT_LoadOrderHF`"`
referenced_table: `"`OT_SalesPersons`"`
columns: "OT_LoadOrderHF.SalesmanNo → `OT_SalesPersons`.ID"
---

# OT_LoadOrderHF → OT_SalesPersons

**FK**: OT_LoadOrderHF.SalesmanNo → `OT_SalesPersons`.ID

**Business meaning**: Load orders (inventory from warehouse to van) are assigned to a specific salesperson.

**Source table**: `OT_LoadOrderHF`
**Target table**: `OT_SalesPersons`
