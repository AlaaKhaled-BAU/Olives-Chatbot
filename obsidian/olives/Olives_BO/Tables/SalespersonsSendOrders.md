---
type: table
database: Olives_BO
name: SalespersonsSendOrders
schema: dbo
tags: [#backoffice, #order, #sales]
foreign_keys:
referenced_by:
  - [[OT_SENDSALESMANDATAFROMORDERS]]
  - [[PRO_MANAGESENDDATA]]
  - [[Pro_SalespersonsSendOrders]]
support_relevance: high
last_verified: 2026-07-05
---
# SalespersonsSendOrders


## Business Purpose

Integration data store for syncing sales transactions with external systems.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| SendID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  |  |  |
| SalespersonID | int | YES |  |  |  |
| RequestDateTime | datetime | YES |  |  |  |
| Status | nvarchar | YES |  |  |  |
| IsSent | bit | YES |  |  |  |
| Result | nvarchar | YES |  |  |  |
| StartDateTime | datetime | YES |  |  |  |
| FinishDateTime | datetime | YES |  |  |  |
| ErrorCount | int | YES |  |  |  |
## Primary Key
SendID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (3):**
- [[OT_SENDSALESMANDATAFROMORDERS]]
- [[PRO_MANAGESENDDATA]]
- [[Pro_SalespersonsSendOrders]]

**Writes (1):**
- [[Pro_SalespersonsSendOrders]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
