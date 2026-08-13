---
type: relation
database: Olives_BO
name: Items--ItemsCategories
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[Items]]
referenced_table: [[ItemsCategories]]
columns: "Items.CategCode → ItemsCategories.CategCode"
---

# Items → ItemsCategories

**FK**: Items.CategCode → [[ItemsCategories]].CategCode

**Business meaning**: Every item belongs to a category. Drives category-level reporting, promotions targeting, and catalog navigation.

**Source table**: [[Items]]
**Target table**: [[ItemsCategories]]
