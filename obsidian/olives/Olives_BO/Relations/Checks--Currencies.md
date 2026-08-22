---
type: relation
database: Olives_BO
name: Checks--Currencies
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[Checks]]
referenced_table: [[Currencies]]
columns: "Checks.CurrencyID → Currencies.ID"
---
tenant_ref: "Currencies is a global reference table (unscoped in t.)"
tenant_scoping: "chatbot queries t.-views only; SESSION_CONTEXT('CompanyID')"
last_verified: 2026-08-22
---

# Checks → Currencies

**FK**: Checks.CurrencyID → [[Currencies]].ID

**Business meaning**: Each check is denominated in a specific currency. Enables multi-currency check reconciliation and FX reporting.

**Source table**: [[Checks]]
**Target table**: [[Currencies]]
