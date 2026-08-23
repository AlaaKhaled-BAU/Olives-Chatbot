---
type: relation
database: Olives_BO
name: SalesPersons--SalesPersonsRoutes
tags: [#convention, #backoffice]
support_relevance: high
parent_table: [[SalesPersons]]
referenced_table: [[SalesPersonsRoutes]]
columns: "SalesPersons.CompanyID,PositionID ↔ SalesPersonsRoutes.CompanyID,PositionsID"
last_verified: 2026-08-22
verified_source: live SQL instance (INFORMATION_SCHEMA + sys.foreign_keys)
tenant_scoping: "chatbot queries t.-views only; SESSION_CONTEXT('CompanyID')"
---

# SalesPersons → SalesPersonsRoutes

**Convention join (no DB-level FK):** `SalesPersons.CompanyID+PositionID` ↔ `SalesPersonsRoutes.CompanyID+PositionsID` (also `SalesPersonsAdditionalRoutes.FromPositionID`). The weekly route plan is keyed by POSITION, never by salesman id directly — resolving "salesman X's route" always goes through his position row.

`WeekDay` is 1–7 = Saturday–Friday (verified against the `Day` column data). `Week1..Week4` hold alternative route ids per slot; which slot applies on a given date is decided application-side — do NOT assume week-of-month.

Customer membership of a route: see [[CustomersFinancialDetails--RoutesInformation]].

## Tenancy

Chatbot queries `t.SalesPersons`, `t.SalesPersonsRoutes` only — auto-scoped by `SESSION_CONTEXT(N'CompanyID')`.

## See also

- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- [[CustomersFinancialDetails--RoutesInformation]]
- [[_MOC-Olives_BO]]
