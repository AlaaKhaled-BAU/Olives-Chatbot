---
type: relation
database: Olives_BO
name: TransactionsDetails--Items
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[TransactionsDetails]]
referenced_table: [[Items]]
columns: "TransactionsDetails.ItemCode → Items.ItemCode"
---
tenant_scoping: "chatbot queries t.-views only; SESSION_CONTEXT('CompanyID')"
last_verified: 2026-08-22
---

# TransactionsDetails → Items

**FK**: TransactionsDetails.ItemCode → [[Items]].ItemCode

**Business meaning**: Each line item on a transaction references one product from the master Items catalog. Drives inventory valuation and COGS calculations.

**Source table**: [[TransactionsDetails]]
**Target table**: [[Items]]
