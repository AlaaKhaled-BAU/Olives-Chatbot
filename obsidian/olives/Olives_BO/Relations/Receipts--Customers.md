---
type: relation
database: Olives_BO
name: Receipts--Customers
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[Receipts]]
referenced_table: [[Customers]]
columns: "Receipts.CustomerID → Customers.ID"
---
tenant_scoping: "chatbot queries t.-views only; SESSION_CONTEXT('CompanyID')"
last_verified: 2026-08-22
---

# Receipts → Customers

**FK**: Receipts.CustomerID → [[Customers]].ID

**Business meaning**: Each payment receipt is linked to a customer. Enables customer balance reconciliation and receipt aging.

**Source table**: [[Receipts]]
**Target table**: [[Customers]]
