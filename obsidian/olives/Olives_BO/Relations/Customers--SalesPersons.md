---
type: relation
database: Olives_BO
name: Customers--SalesPersons
tags: [#convention, #backoffice]
support_relevance: high
parent_table: [[Customers]]
referenced_table: [[SalesPersons]]
columns: "CustomersFinancialDetails.PositionsID ↔ Positions ← SalesPersons.PositionID"
last_verified: 2026-08-22
verified_source: live SQL instance (INFORMATION_SCHEMA + sys.foreign_keys)
tenant_scoping: "chatbot queries t.-views only; SESSION_CONTEXT('CompanyID')"
---

# Customers → SalesPersons

**There is NO direct customer-to-salesman link.** `Customers` has no SalesPersonId column (live-verified). Two real paths:

**Assignment (who owns the customer):**
`t.CustomersFinancialDetails.PositionsID` → `Positions (CompanyID, ID)` ← `SalesPersons.PositionID` — both hops are declared FKs. A customer can hold several CFD rows (one per position/business unit).

**Acting salesman (who transacted):** `OrdersHeaders`, `Receipts`, `TransactionsHeaders`, `ReturnOrdersHeaders`, `TransfersOrdersHeaders` each carry `CompanyID+SalesPersonID -> SalesPersons.CompanyID+ID` (declared).

## Tenancy

Chatbot queries `t.CustomersFinancialDetails`, `t.SalesPersons`, `t.Positions` only — auto-scoped by `SESSION_CONTEXT(N'CompanyID')`.

## See also

- [[Customers]]
- [[SalesPersons]]
- [[CustomersFinancialDetails--Customers]]
- [[CustomersFinancialDetails--RoutesInformation]]
