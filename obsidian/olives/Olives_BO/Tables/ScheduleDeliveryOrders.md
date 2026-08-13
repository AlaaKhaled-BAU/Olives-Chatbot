---
type: table
database: Olives_BO
name: ScheduleDeliveryOrders
schema: dbo
tags: [#backoffice, #order]
foreign_keys:
  - [[Companies]]
  - [[DeliveryCars]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# ScheduleDeliveryOrders


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores scheduledeliveryorders records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersons]] |
| OrderYear | int | NO | ✓ | ✓ | [[OrdersHeaders]] |
| OrderNo | int | NO | ✓ | ✓ | [[OrdersHeaders]] |
| ScheduleID | int | NO | ✓ |  |  |
| SalesPersonID | int | YES |  | ✓ | [[SalesPersons]] |
| CarID | int | YES |  | ✓ | [[DeliveryCars]] |
| ScheduleDateTime | smalldatetime | YES |  |  |  |
| AssigmentDateTime | smalldatetime | YES |  |  |  |
| Status | int | YES |  |  |  |
## Primary Key
CompanyID
OrderYear
OrderNo
ScheduleID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CarID -> [[DeliveryCars]](CompanyID, ID)
CompanyID, OrderYear, OrderNo -> [[OrdersHeaders]](CompanyID, OrderYear, OrderNo)
CompanyID, SalesPersonID -> [[SalesPersons]](CompanyID, ID)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
