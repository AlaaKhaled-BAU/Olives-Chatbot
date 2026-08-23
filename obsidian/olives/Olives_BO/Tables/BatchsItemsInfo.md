---
type: table
database: Olives_BO
name: BatchsItemsInfo
schema: dbo
tags: [#backoffice, #inventory]
foreign_keys:
  - [[Companies]]
  - [[Items]]
referenced_by:
  - [[Awael_Integ_BatchesQty]]
  - [[Awael_Integ_HisInvoices]]
  - [[Awtar_Integration_WithLog]]
  - [[Niroukh_Integration_WithLog]]
  - [[Pro_OrdersHeaders]]
  - [[Pro_ReturnOrdersHeaders]]
  - [[RamPharm_SAP_Integ]]
  - [[X3_Integ_SOA_Batches]]
support_relevance: high
last_verified: 2026-07-05
---
# BatchsItemsInfo


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores batchsitemsinfo records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Items]] |
| ItemNo | nvarchar | YES | ✓ | ✓ | [[Items]] |
| BatchNo | varchar | YES | ✓ |  |  |
| ExpireDate | smalldatetime | YES |  |  |  |
| Qty | money | YES |  |  |  |
| Ref1 | varchar | YES |  |  |  |
| Ref2 | varchar | YES |  |  |  |
| BatchBarcode | varchar | YES |  |  |  |
## Primary Key
CompanyID
ItemNo
BatchNo
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemNo -> [[Items]](CompanyID, ItemCode)
## Impact / Procedures Using This Table

**Reads (8):**
- [[Awael_Integ_BatchesQty]]
- [[Awael_Integ_HisInvoices]]
- [[Awtar_Integration_WithLog]]
- [[Niroukh_Integration_WithLog]]
- [[Pro_OrdersHeaders]]
- [[Pro_ReturnOrdersHeaders]]
- [[RamPharm_SAP_Integ]]
- [[X3_Integ_SOA_Batches]]

**Writes (6):**
- [[Awael_Integ_BatchesQty]]
- [[Awael_Integ_HisInvoices]]
- [[Awtar_Integration_WithLog]]
- [[Niroukh_Integration_WithLog]]
- [[RamPharm_SAP_Integ]]
- [[X3_Integ_SOA_Batches]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Role**: batch-level stock balances (ExpireDate/Qty per batch) — contrast with TransactionsBatchsItemsInfo which links batches to specific transaction lines
- **Carrier naming**: ItemNo references Items.ItemCode (no CompanyID in column name; tenant via table scoping)
## Tenancy

Chatbot queries `t.BatchsItemsInfo` only — auto-scoped by `SESSION_CONTEXT(N'CompanyID')`. Raw dbo access is blocked for `chatbot_ro`.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
