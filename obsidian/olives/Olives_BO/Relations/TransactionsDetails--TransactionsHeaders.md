---
type: relation
database: Olives_BO
name: TransactionsDetails--TransactionsHeaders
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[TransactionsDetails]]
referenced_table: [[TransactionsHeaders]]
columns: "TransactionsDetails.CompanyID,TransactionTypeID,TransactionYear,TransactionNo → TransactionsHeaders.CompanyID,TransactionTypeID,TransactionYear,TransactionNo"
---
tenant_scoping: "chatbot queries t.-views only; SESSION_CONTEXT('CompanyID')"
last_verified: 2026-08-22
---

# TransactionsDetails → TransactionsHeaders

**FK**: TransactionsDetails.CompanyID,TransactionTypeID,TransactionYear,TransactionNo → [[TransactionsHeaders]].CompanyID,TransactionTypeID,TransactionYear,TransactionNo

**Business meaning**: Line-item detail to header relationship. Every line belongs to exactly one transaction. The composite FK on TypeID+Year+No matches the header PK.

**Source table**: [[TransactionsDetails]]
**Target table**: [[TransactionsHeaders]]
