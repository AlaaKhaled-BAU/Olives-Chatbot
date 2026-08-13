---
type: relation
database: Olives_BO
name: BankDepositHF--Companies
tags: [#fk]
support_relevance: medium
parent_table: [[BankDepositHF]]
referenced_table: [[Companies]]
columns: "BankDepositHF.CompanyID → Companies.ID"
---

# BankDepositHF → Companies

**FK**: BankDepositHF.CompanyID → [[Companies]].ID

**Business meaning**: AUTO-GENERATED — verify before trusting.

**Source table**: [[BankDepositHF]]
**Target table**: [[Companies]]
