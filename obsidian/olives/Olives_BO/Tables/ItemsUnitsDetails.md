---
type: table
database: Olives_BO
name: ItemsUnitsDetails
schema: dbo
tags: [#backoffice, #inventory]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[ItemsUnits]]
referenced_by:
  - [[OSFA_SP_Api]]
  - [[OSFA_SP_Api_Jawad]]
  - [[OT_SendItemsInfo]]
  - [[Pro_Items]]
  - [[Pro_ItemsUnits]]
  - [[Pro_ItemsUnitsDetails]]
  - [[Pro_PriceListDetails]]
  - [[Pro_TransfersOrders_Auto]]
  - [[Rpt_CustomerSalesByUnit]]
  - [[Rpt_LoadOrderFirstApproval]]
  - [[Rpt_ReceivablesSalesInvoice]]
  - [[Rpt_SalesPersonItemBalance]]
  - [[Rpt_SalesmanSalesByCategory2]]
support_relevance: high
last_verified: 2026-07-05
---
# ItemsUnitsDetails


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores itemsunitsdetails records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[ItemsUnits]] |
| ItemCode | nvarchar | NO | ✓ | ✓ | [[Items]] |
| UnitID | nvarchar | NO | ✓ | ✓ | [[ItemsUnits]] |
| ConvertRate | float | YES |  |  |  |
| UnitSerial | int | YES |  |  |  |
| Barcode | nvarchar | YES |  |  |  |
| Volume | float | YES |  |  |  |
| Weight | float | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
| UsedInUploadOrder | bit | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |

## Primary Key
CompanyID
ItemCode
UnitID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, UnitID -> [[ItemsUnits]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (53):**
- [[OT_SendItemsInfo]]
- [[Pro_Items]]
- [[Pro_ItemsUnits]]
- [[Pro_ItemsUnitsDetails]]
- [[Pro_PriceListDetails]]
- [[Pro_TransfersOrders_Auto]]
- [[Rpt_CustomerSalesByUnit]]
- [[Rpt_LoadOrderFirstApproval]]
- [[Rpt_ReceivablesSalesInvoice]]
- [[Rpt_SalesPersonItemBalance]]
- [[Rpt_SalesmanSalesByCategory2]]

**Writes (45):**
- [[OSFA_SP_Api]]
- [[OSFA_SP_Api_Jawad]]
- [[Pro_ItemsUnitsDetails]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Conversion**: ConvertRate expresses this unit against the item default unit (Items.UnitID) — multiply when normalizing quantities
## Tenancy

Chatbot queries `t.ItemsUnitsDetails` only — auto-scoped by `SESSION_CONTEXT(N'CompanyID')`. Raw dbo access is blocked for `chatbot_ro`.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
