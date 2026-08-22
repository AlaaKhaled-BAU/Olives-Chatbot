---
type: relation
database: Olives_BO
name: Receipts--Currencies
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[Receipts]]
referenced_table: [[Currencies]]
columns: "Receipts.CurrencyID → Currencies.ID"
---
tenant_ref: "Currencies is a global reference table (unscoped in t.)"
tenant_scoping: "chatbot queries t.-views only; SESSION_CONTEXT('CompanyID')"
last_verified: 2026-08-22
---

# Receipts → Currencies

**FK**: Receipts.CurrencyID → [[Currencies]].ID

**Business meaning**: Denotes the currency in which a receipt was collected. Essential for multi-currency reconciliation and FX gain/loss reporting.

**Source table**: [[Receipts]]
**Target table**: [[Currencies]]
