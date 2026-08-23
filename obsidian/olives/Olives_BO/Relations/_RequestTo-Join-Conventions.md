---
type: relation
database: Olives_BO
name: _RequestTo-Join-Conventions
tags: [#convention, #workflow]
support_relevance: high
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# RequestTo* family - join conventions

Applies to every `RequestTo*` table (34 live tables): device-raised approval requests (credit limit,
discount, price change, void, visit exceptions...). They share one shape:

- PK `AutoID`; most (not all — e.g. RequestToVoidTransaction lacks them) carry `OSFA_AutoID` / `TabletSysID` provenance columns from the device round-trip
- `CompanyID` -> Companies.ID is usually the ONLY declared FK
- `SalesPersonNo` / `CustomerNo` reference [[SalesPersons]].ID / [[Customers]].ID
  by CONVENTION - no DB constraints exist for them
- approval state lives in `IsAproved`; approval levels resolve via
  WF_SetupDetails -> WF_SetupHeader plus WF_Functions

## Tenancy

Chatbot queries `t.RequestTo*` only - auto-scoped by SESSION_CONTEXT(N'CompanyID').

## See also

- [[RequestToExceedCustomerCreditLimit--Customers]]
- [[WF_Functions]] (approval-function ID catalog)
- [[WF_SetupDetails--WF_SetupHeader]]
- [[WF_SetupDetails--WF_SetupHeader]]
- [[_MOC-Olives_BO]]
