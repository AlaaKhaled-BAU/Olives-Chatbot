---
type: relation
database: Olives_BO
name: Customers--PriceLists
tags: [#convention, #backoffice]
support_relevance: high
parent_table: [[Customers]]
referenced_table: [[SalesPersons]]
columns: "CustomersFinancialDetails.PositionsID ↔ Positions ← SalesPersons.PositionID"
last_verified: 2026-08-22
verified_source: live SQL instance (INFORMATION_SCHEMA + sys.foreign_keys)
tenant_scoping: "chatbot queries t.-views only; SESSION_CONTEXT('CompanyID')"
---

# Customers → PriceLists

**The customer's default price list lives on CustomersFinancialDetails, not Customers.** `Customers` has no PriceListId column (only a legacy `PriceListID_Tmp`; live-verified).

**Declared FK:** `t.CustomersFinancialDetails.CompanyID+PriceListID` → `[[PriceLists]].CompanyID+ID` (one row per position/business unit — different positions may price the same customer differently).
**Transactional:** `OrdersHeaders.CompanyID+PriceListID` → `[[PriceLists]]` (declared) snapshots the list used per order.

## Tenancy

Chatbot queries `t.CustomersFinancialDetails`, `t.SalesPersons`, `t.Positions` only — auto-scoped by `SESSION_CONTEXT(N'CompanyID')`.

## See also

- [[Customers]]
- [[SalesPersons]]
- [[CustomersFinancialDetails--Customers]]
- [[PriceListDetails--PriceLists]]
- [[CustomersFinancialDetails--RoutesInformation]]
