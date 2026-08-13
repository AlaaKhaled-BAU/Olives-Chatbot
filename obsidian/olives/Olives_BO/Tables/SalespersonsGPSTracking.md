---
type: table
database: Olives_BO
name: SalespersonsGPSTracking
schema: dbo
tags: [#backoffice, #gps, #sales]
foreign_keys:
referenced_by:
  - [[Pro_DeliveryDashboard]]
  - [[Pro_SalespersonsGPSTracking]]
  - [[Rpt_WFGPSTracking]]
support_relevance: high
last_verified: 2026-07-05
---
# SalespersonsGPSTracking


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersonsgpstracking records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| SalesPersonID | int | NO | ✓ |  |  |
| TrDateTime | datetime | NO | ✓ |  |  |
| TabletSysID | varchar | YES | ✓ |  |  |
| GpsX | varchar | YES |  |  |  |
| GpsY | varchar | YES |  |  |  |
| Notes | varchar | YES |  |  |  |
## Primary Key
CompanyID
SalesPersonID
TrDateTime
TabletSysID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (3):**
- [[Pro_DeliveryDashboard]]
- [[Pro_SalespersonsGPSTracking]]
- [[Rpt_WFGPSTracking]]

**Writes (1):**
- [[Pro_SalespersonsGPSTracking]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
