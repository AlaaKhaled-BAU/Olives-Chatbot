---
type: relation
database: Olives_BO
name: Items--ItemsGroups
tags: [#fk]
support_relevance: medium
parent_table: [[Items]]
referenced_table: [[ItemsGroups]]
columns: "Items.CompanyID, ItemGroupID → ItemsGroups.CompanyID, ID"
---

# Items → ItemsGroups

**FK**: Items.CompanyID, ItemGroupID → [[ItemsGroups]].CompanyID, ID

**Business meaning**: AUTO-GENERATED — verify before trusting.

**Source table**: [[Items]]
**Target table**: [[ItemsGroups]]
