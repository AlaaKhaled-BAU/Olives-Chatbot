---
type: relation
database: Olives_BO
name: BankDepositHF--SalesPersons
tags: [#fk]
support_relevance: medium
parent_table: [[BankDepositHF]]
referenced_table: [[SalesPersons]]
columns: "BankDepositHF.CompanyID, SalespersonID → SalesPersons.CompanyID, ID"
---

# BankDepositHF → SalesPersons

**FK**: BankDepositHF.CompanyID, SalespersonID → [[SalesPersons]].CompanyID, ID

**Business meaning**: AUTO-GENERATED — verify before trusting.

**Source table**: [[BankDepositHF]]
**Target table**: [[SalesPersons]]
