---
type: table
database: OSFA_DB
name: OT_OrderDeliveryInfo
schema: dbo
tags: [#mobile, #order]
foreign_keys:
  - [[OT_OrderHF]]
referenced_by:
  - [[InsertOT_OrderDeliveryInfo]]
  - [[OT_OrderDeliveryInfo_CheckAttach]]
  - [[OT_OrderDeliveryInfo_UpdateAttach]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_OrderDeliveryInfo



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ | ✓ | [[OT_OrderHF]] |
| OrderYear | smallint | NO | ✓ | ✓ | [[OT_OrderHF]] |
| OrderNo | int | NO | ✓ | ✓ | [[OT_OrderHF]] |
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
CompNo
OrderYear
OrderNo
## Foreign Keys
CompNo, OrderYear, OrderNo -> [[OT_OrderHF]](CompNo, OrderYear, OrderNo)
## Impact / Procedures Using This Table

**Reads (3):**
- [[InsertOT_OrderDeliveryInfo]]
- [[OT_OrderDeliveryInfo_CheckAttach]]
- [[OT_OrderDeliveryInfo_UpdateAttach]]

**Writes (2):**
- [[InsertOT_OrderDeliveryInfo]]
- [[OT_OrderDeliveryInfo_UpdateAttach]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
