---
type: relation
database: Olives_BO
name: TransactionsDetails--TransactionsHeaders
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[TransactionsDetails]]
referenced_table: [[TransactionsHeaders]]
columns: "TransactionsDetails.TransactionTypeID,TransactionYear,TransactionNo → TransactionsHeaders.TransactionTypeID,TransactionYear,TransactionNo"
---

# TransactionsDetails → TransactionsHeaders

**FK**: TransactionsDetails.TransactionTypeID,TransactionYear,TransactionNo → [[TransactionsHeaders]].TransactionTypeID,TransactionYear,TransactionNo

**Business meaning**: Line-item detail to header relationship. Every line belongs to exactly one transaction. The composite FK on TypeID+Year+No matches the header PK.

**Source table**: [[TransactionsDetails]]
**Target table**: [[TransactionsHeaders]]
