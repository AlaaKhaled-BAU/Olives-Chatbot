---
type: relation
database: Olives_BO
name: SalespersonsGPSTracking--SalesPersons
tags: [#convention, #backoffice]
support_relevance: high
parent_table: [[SalespersonsGPSTracking]]
referenced_table: [[SalesPersons]]
columns: "SalespersonsGPSTracking.CompanyID,SalesPersonID → SalesPersons.CompanyID,ID"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# SalespersonsGPSTracking → SalesPersons

**Convention join** (no DB-level FK): SalespersonsGPSTracking.CompanyID,SalesPersonID → [[SalesPersons]].CompanyID,ID

**Business meaning**: GPS ping stream (GpsX/GpsY plus TrDateTime) per salesman; convention join - both columns exist but no DB constraint backs them. High-volume: always bound by date range.

## Tenancy

Chatbot queries `t.SalespersonsGPSTracking` and `t.SalesPersons` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[SalespersonsGPSTracking]]
- [[SalesPersons]]
- [[CustomersVisitActivity]]
- [[RoutesInformation]]
