---
type: table
database: Olives_BO
name: RequestToChangeDeliveryPaymentType
schema: dbo
tags: [#backoffice, #billing, #order, #reference, #workflow]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OT_ImportRequestToChangeDeliveryPaymentType]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-07-05
---
# RequestToChangeDeliveryPaymentType


## Business Purpose

Workflow request records for special approvals (credit, discount, exceptions).

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  | ✓ | [[Companies]] |
| SalesPersonNo | int | YES |  |  |  |
| OriginalSalespersonNo | int | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| TrTypeID | smallint | YES |  |  |  |
| TrTypeYear | smallint | YES |  |  |  |
| TrTypeNo | int | YES |  |  |  |
| InvoiceAmount | float | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| OldPaymentType | int | YES |  |  |  |
| NewPaymentType | int | YES |  |  |  |
| IsAproved | bit | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| OSFA_AutoID | numeric | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OT_ImportRequestToChangeDeliveryPaymentType]]

**Writes (2):**
- [[OT_ImportRequestToChangeDeliveryPaymentType]]
- [[WF_AddWorkFlowLevels]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Partial payment not tracked**: Receipt amount less than invoice total — aging report shows incorrect balance
- **Check bounce**: CheckStatus not updated after bank return — customer credit not restored
- **Currency conversion error**: ExRate differs from daily rate — receipt in wrong amount
- **Duplicate receipts**: Same payment applied twice — customer credit balance wrong

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
