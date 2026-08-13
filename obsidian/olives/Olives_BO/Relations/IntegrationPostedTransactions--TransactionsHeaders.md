---
type: relation
database: Olives_BO
name: IntegrationPostedTransactions--TransactionsHeaders
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[IntegrationPostedTransactions]]
referenced_table: [[TransactionsHeaders]]
columns: "IntegrationPostedTransactions.TransactionTypeID,TransactionYear,TransactionNo → TransactionsHeaders.TransactionTypeID,TransactionYear,TransactionNo"
---

# IntegrationPostedTransactions → TransactionsHeaders

**FK**: IntegrationPostedTransactions.TransactionTypeID,TransactionYear,TransactionNo → [[TransactionsHeaders]].TransactionTypeID,TransactionYear,TransactionNo

**Business meaning**: Tracks which BO transactions have been sent to the external ERP. Prevents duplicate posting and enables audit trail.

**Source table**: [[IntegrationPostedTransactions]]
**Target table**: [[TransactionsHeaders]]
