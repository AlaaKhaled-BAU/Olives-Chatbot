---
type: relation
database: Olives_BO
name: ItemsGroups--Companies
tags: [#fk]
support_relevance: medium
parent_table: [[ItemsGroups]]
referenced_table: [[Companies]]
columns: "ItemsGroups.CompanyID → Companies.ID"
---

# ItemsGroups → Companies

**FK**: ItemsGroups.CompanyID → [[Companies]].ID

**Business meaning**: AUTO-GENERATED — verify before trusting.

**Source table**: [[ItemsGroups]]
**Target table**: [[Companies]]
