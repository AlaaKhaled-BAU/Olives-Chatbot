---
type: table
database: Olives_BO
name: OrdersDeliveryInfo
schema: dbo
tags: [#backoffice, #order]
foreign_keys:
  - [[OrdersHeaders]]
referenced_by:
  - [[OT_ImportSalesOrders]]
support_relevance: high
last_verified: 2026-07-05
---
# OrdersDeliveryInfo


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores ordersdeliveryinfo records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[OrdersHeaders]] |
| OrderYear | int | NO | ✓ | ✓ | [[OrdersHeaders]] |
| OrderNo | int | NO | ✓ | ✓ | [[OrdersHeaders]] |
| PoNo | nvarchar | YES |  |  |  |
| CustName | nvarchar | YES |  |  |  |
| CustAddress | nvarchar | YES |  |  |  |
| MobNo | nvarchar | YES |  |  |  |
| TelNo | nvarchar | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| Ref1 | nvarchar | YES |  |  |  |
| Ref2 | nvarchar | YES |  |  |  |
| AttachmentPath | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
OrderYear
OrderNo
## Foreign Keys
CompanyID, OrderYear, OrderNo -> [[OrdersHeaders]](CompanyID, OrderYear, OrderNo)
## Impact / Procedures Using This Table

**Reads (0):**
_None_

**Writes (1):**
- [[OT_ImportSalesOrders]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
