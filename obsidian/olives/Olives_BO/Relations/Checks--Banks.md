---
type: relation
database: Olives_BO
name: Checks--Banks
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[Checks]]
referenced_table: [[Banks]]
columns: "Checks.BankID → Banks.ID"
---
tenant_scoping: "chatbot queries t.-views only; SESSION_CONTEXT('CompanyID')"
last_verified: 2026-08-22
---

# Checks → Banks

**FK**: Checks.BankID → [[Banks]].ID

**Business meaning**: Check records reference their issuing bank. Essential for check clearing workflows and bank reconciliation.

**Source table**: [[Checks]]
**Target table**: [[Banks]]
