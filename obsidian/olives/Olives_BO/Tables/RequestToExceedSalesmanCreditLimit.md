---
type: table
database: Olives_BO
name: RequestToExceedSalesmanCreditLimit
schema: dbo
tags: [#backoffice, #billing, #sales, #workflow]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OT_ImportRequestToExceedSalesmanCreditLimit]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-07-05
---
# RequestToExceedSalesmanCreditLimit


## Business Purpose

Workflow request records for special approvals (credit, discount, exceptions).

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  | ✓ | [[Companies]] |
| SalesPersonNo | int | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| InvoiceAmount | float | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| IsAproved | bit | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| SalesmanCreditLimit | float | YES |  |  |  |
| SalesmanBanalce | float | YES |  |  |  |
| ExceedAmount | float | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OT_ImportRequestToExceedSalesmanCreditLimit]]

**Writes (3):**
- [[OT_ImportRequestToExceedSalesmanCreditLimit]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
