---
type: relation
database: Olives_BO
name: Receipts_PaidTrans--Receipts
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[Receipts_PaidTrans]]
referenced_table: [[Receipts]]
columns: "Receipts_PaidTrans.ReceiptID → Receipts.ID"
---

# Receipts_PaidTrans → Receipts

**FK**: Receipts_PaidTrans.ReceiptID → [[Receipts]].ID

**Business meaning**: Maps individual paid invoices to the receipt that covered them. Supports accurate invoice-level payment allocation.

**Source table**: [[Receipts_PaidTrans]]
**Target table**: [[Receipts]]
