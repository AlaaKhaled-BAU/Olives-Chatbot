---
type: table
database: Olives_BO
name: SalespersonsMessages
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
  - [[Companies]]
  - [[SalesPersons]]
referenced_by:
  - [[OT_ImportInvoicesDelivery]]
  - [[OT_ImportReturnOrder]]
  - [[Pro_DeliveryCar]]
  - [[Pro_OrdersDetails]]
  - [[Pro_OrdersHeaders]]
  - [[Pro_ReceiptRequests]]
  - [[Pro_ReceiptRequestsSchedule]]
  - [[Pro_ReturnOrdersHeaders]]
  - [[Pro_SalesPersonsMessages]]
  - [[Pro_TransfersOrdersHeaders]]
  - [[Rpt_SalesmanMessages]]
  - [[WF_AddWorkFlowLevelOne]]
support_relevance: high
last_verified: 2026-07-05
---
# SalespersonsMessages


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersonsmessages records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersons]] |
| SalespersonID | int | NO | ✓ | ✓ | [[SalesPersons]] |
| MsgID | bigint | NO | ✓ |  |  |
| MsgDateTime | smalldatetime | YES |  |  |  |
| MessageText | nvarchar | YES |  |  |  |
| IsRead | bit | YES |  |  |  |
| ReadDateTime | smalldatetime | YES |  |  |  |
| UserID | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
SalespersonID
MsgID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, SalespersonID -> [[SalesPersons]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (9):**
- [[OT_ImportInvoicesDelivery]]
- [[OT_ImportReturnOrder]]
- [[Pro_DeliveryCar]]
- [[Pro_OrdersDetails]]
- [[Pro_ReceiptRequests]]
- [[Pro_ReceiptRequestsSchedule]]
- [[Pro_SalesPersonsMessages]]
- [[Pro_TransfersOrdersHeaders]]
- [[Rpt_SalesmanMessages]]

**Writes (11):**
- [[OT_ImportInvoicesDelivery]]
- [[OT_ImportReturnOrder]]
- [[Pro_DeliveryCar]]
- [[Pro_OrdersDetails]]
- [[Pro_OrdersHeaders]]
- [[Pro_ReceiptRequests]]
- [[Pro_ReceiptRequestsSchedule]]
- [[Pro_ReturnOrdersHeaders]]
- [[Pro_SalesPersonsMessages]]
- [[Pro_TransfersOrdersHeaders]]
- [[WF_AddWorkFlowLevelOne]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[OSFA_DB/Procedures/OT_UpdateSalesmanMsgs]]
