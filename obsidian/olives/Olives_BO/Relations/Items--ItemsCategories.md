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
tenant_scoping: "chatbot queries t.-views only; SESSION_CONTEXT('CompanyID')"
last_verified: 2026-08-22
---

# Items → ItemsCategories

**FK**: Items.CategCode → [[ItemsCategories]].CategCode

**Business meaning**: Every item belongs to a category. Drives category-level reporting, promotions targeting, and catalog navigation.

**Source table**: [[Items]]
**Target table**: [[ItemsCategories]]
