---
type: relation
database: Olives_BO
name: Customers--PriceLists
tags: [#convention, #backoffice]
support_relevance: high
parent_table: [[Customers]]
referenced_table: [[PriceLists]]
columns: "Customers.CompanyID,PriceListID → PriceLists.CompanyID,ID"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# Customers → PriceLists

**Convention join** (NO declared FK despite prior note): Customers.CompanyID+PriceListID → [[PriceLists]].CompanyID+ID

**Business meaning**: Assigns the default price tier used when pricing orders/invoices for a customer; overridable per customer-item via ItemsPriceExceptions.

## Tenancy

Chatbot queries `t.Customers` and `t.PriceLists` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[Customers]]
- [[PriceLists]]
- [[PriceListDetails--PriceLists]]
- [[_MOC-Olives_BO]]
