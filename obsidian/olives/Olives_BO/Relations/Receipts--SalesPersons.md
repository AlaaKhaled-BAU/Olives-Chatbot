---
type: relation
database: Olives_BO
name: Receipts--SalesPersons
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[Receipts]]
referenced_table: [[SalesPersons]]
columns: "Receipts.SalesPersonID → SalesPersons.ID"
---
tenant_scoping: "chatbot queries t.-views only; SESSION_CONTEXT('CompanyID')"
last_verified: 2026-08-22
---

# Receipts → SalesPersons

**FK**: Receipts.SalesPersonID → [[SalesPersons]].ID

**Business meaning**: Identifies the salesperson who processed or is credited for the receipt. Used for commission calculation and sales performance analytics.

**Source table**: [[Receipts]]
**Target table**: [[SalesPersons]]
