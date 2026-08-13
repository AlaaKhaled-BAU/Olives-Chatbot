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

# Receipts → Currencies

**FK**: Receipts.CurrencyID → [[Currencies]].ID

**Business meaning**: Denotes the currency in which a receipt was collected. Essential for multi-currency reconciliation and FX gain/loss reporting.

**Source table**: [[Receipts]]
**Target table**: [[Currencies]]
