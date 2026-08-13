---
type: table
database: Olives_BO
name: MaintinanceOrders
schema: dbo
tags: [#backoffice, #order]
foreign_keys:
referenced_by:
  - [[MaintinanceOrdersImages_Insert]]
  - [[MaintinanceOrders_Insert]]
  - [[Pro_MaintinanceOrders]]
support_relevance: high
last_verified: 2026-07-05
---
# MaintinanceOrders


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores maintinanceorders records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  |  |  |
| SalesmanNo | int | YES |  |  |  |
| CustomerID | bigint | YES |  |  |  |
| CustTel | varchar | YES |  |  |  |
| ContactPerson | varchar | YES |  |  |  |
| LicencePersonName | varchar | YES |  |  |  |
| CommercialCustName | varchar | YES |  |  |  |
| MaintenanceOrderType | int | YES |  |  |  |
| FavouriteVisitTime | varchar | YES |  |  |  |
| CustRefrigerator | varchar | YES |  |  |  |
| NewCustName | varchar | YES |  |  |  |
| NewLicenceCustName | varchar | YES |  |  |  |
| NewContactPerson | varchar | YES |  |  |  |
| NewCommercialCustName | varchar | YES |  |  |  |
| NewCustTel | varchar | YES |  |  |  |
| CustRefrigeratorNo | varchar | YES |  |  |  |
| ContractNo | varchar | YES |  |  |  |
| Diagnostic | varchar | YES |  |  |  |
| MaintenanceNotes | varchar | YES |  |  |  |
| RefrigeratorSerialNo | varchar | YES |  |  |  |
| RefrigeratorModel | varchar | YES |  |  |  |
| RefrigeratorDrawReasonID | int | YES |  |  |  |
| RefrigeratorDrawReasonNotes | varchar | YES |  |  |  |
| DeviceSysID | varchar | YES |  |  |  |
| CustomerHasBeenVisited | bit | YES |  |  |  |
| SupervisorNotes | nvarchar | YES |  |  |  |
| EvaluatingCustomerSite | nvarchar | YES |  |  |  |
| EvaluatingCustomerFinancialPosition | nvarchar | YES |  |  |  |
| CustomerAgreement | nvarchar | YES |  |  |  |
| FirstApproval | bit | YES |  |  |  |
| FirstApprovalDescription | nvarchar | YES |  |  |  |
| FirstApprovalUserID | varchar | YES |  |  |  |
| SecondApproval | bit | YES |  |  |  |
| SecondApprovalDescription | nvarchar | YES |  |  |  |
| SecondApprovalUserID | varchar | YES |  |  |  |
| SendToUserID | nvarchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (3):**
- [[MaintinanceOrdersImages_Insert]]
- [[MaintinanceOrders_Insert]]
- [[Pro_MaintinanceOrders]]

**Writes (2):**
- [[MaintinanceOrders_Insert]]
- [[Pro_MaintinanceOrders]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
