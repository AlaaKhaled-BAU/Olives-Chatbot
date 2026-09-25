---
type: table
database: Olives_BO
name: SalesPersonsDevicePermissions
schema: dbo
tags: [#backoffice, #sales, #permissions, #configuration]
foreign_keys:
  - [[Companies]]
  - [[Positions]]
support_relevance: high
last_verified: 2026-09-19
---
# SalesPersonsDevicePermissions

## Business Purpose

Core mobile and tablet capability configuration table in Olives_BO.
Defines the functional selling mode and operational permissions granted to field salespersons based on their organizational role (PositionsID).

### Master Capability Flags:
- **MakeSalesInvoice**: 1 = Authorized to issue direct tax/cash sales invoices in the field. **The primary discriminator of Cash Van (فانات البيع المباشر)**.
- **MakeOrderTaking**: 1 = Authorized to book pre-orders for later warehouse delivery. **The primary discriminator of Order Taking (Pre-Sales / حجز الطلبيات)**.
- **AllowVanTransfer**: 1 = Authorized to perform van-to-van inventory transfers in the field (VanTransferHeader).
- **AllowUnloadOrder**: 1 = Authorized to generate end-of-day van stock return documents (TransfersOrdersHeaders, VouType = 2).
- **MakeReturnSales**: 1 = Authorized to process direct return invoices in the field.
- **AllowReturnOrder**: 1 = Authorized to create pre-order return requests for warehouse retrieval.

## Relational Join Path:
Links to dbo.SalesPersons via composite key:
```sql
SalesPersons.CompanyID = SalesPersonsDevicePermissions.CompanyID
AND SalesPersons.PositionID = SalesPersonsDevicePermissions.PositionsID
```

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| PositionsID | int | NO | ✓ | ✓ | [[Positions]] |
| MakeSalesInvoice | bit | YES |  |  | Direct invoice capability (Cash Van) |
| MakeOrderTaking | bit | YES |  |  | Pre-order capability (Pre-Sales) |
| AllowVanTransfer | bit | YES |  |  | Van-to-van transfer capability |
| AllowUnloadOrder | bit | YES |  |  | Van unload order capability |
| MakeReturnSales | bit | YES |  |  | Direct sales return capability |
| AllowReturnOrder | bit | YES |  |  | Return order request capability |
| MaxDiscountPerc | float | YES |  |  | Maximum discount threshold |

## See Also
- [[SalesPersons]]
- [[TransfersOrdersHeaders]]
- [[SalesPersonItemsBalance]]
