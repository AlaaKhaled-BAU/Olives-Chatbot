---
type: relation
database: Olives_BO
name: PriceListDetails--Items
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[PriceListDetails]]
referenced_table: [[Items]]
columns: "PriceListDetails.ItemCode → Items.ItemCode"
---
tenant_scoping: "chatbot queries t.-views only; SESSION_CONTEXT('CompanyID')"
last_verified: 2026-08-22
---

# PriceListDetails → Items

**FK**: PriceListDetails.ItemCode → [[Items]].ItemCode

**Business meaning**: Each price list entry defines the price for one specific item. Enables customer-tier and promotion pricing.

**Source table**: [[PriceListDetails]]
**Target table**: [[Items]]
