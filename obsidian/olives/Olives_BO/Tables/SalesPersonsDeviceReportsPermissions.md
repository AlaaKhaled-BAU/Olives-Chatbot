---
type: table
database: Olives_BO
name: SalesPersonsDeviceReportsPermissions
schema: dbo
tags: [#auth, #backoffice, #reporting, #sales]
foreign_keys:
referenced_by:
  - [[Fill_Sales_Device_Reports]]
  - [[Pro_SalesPersonsDevicePermissions]]
  - [[TechnicalSupportTools_CopyReportsfornewSalesman]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesPersonsDeviceReportsPermissions


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersonsdevicereportspermissions records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| PositionsID | int | NO | ✓ |  |  |
| ReportID | int | NO | ✓ |  |  |
## Primary Key
CompanyID
PositionsID
ReportID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (4):**
- [[Fill_Sales_Device_Reports]]
- [[Pro_SalesPersonsDevicePermissions]]
- [[TechnicalSupportTools_CopyReportsfornewSalesman]]

**Writes (3):**
- [[Fill_Sales_Device_Reports]]
- [[Pro_SalesPersonsDevicePermissions]]
- [[TechnicalSupportTools_CopyReportsfornewSalesman]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
