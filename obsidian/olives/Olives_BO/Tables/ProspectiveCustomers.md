---
type: table
database: Olives_BO
name: ProspectiveCustomers
schema: dbo
tags: [#backoffice, #customer]
foreign_keys:
referenced_by:
  - [[AX_INTEG_SENDSALESQUOTATIONS]]
  - [[OT_ImportCompetitveItemsData]]
  - [[OT_ImportCustomerSurveyAnswers]]
  - [[OT_ImportNewCust_Prospective]]
  - [[OT_ImportSalesQuotations]]
  - [[Pro_ProspectiveCustomers]]
  - [[Pro_SalesQuotationHeaders]]
  - [[Rpt_Customers_NotesProcpective]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Customer-Setup
---
# ProspectiveCustomers


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores prospectivecustomers records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| ID | bigint | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ForeignName | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| TypeID | int | YES |  |  |  |
| LocationID | int | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| Account | nvarchar | YES |  |  |  |
| Barcode | nvarchar | YES |  |  |  |
| Contact | nvarchar | YES |  |  |  |
| TelephoneNo | nvarchar | YES |  |  |  |
| MobileNo | nvarchar | YES |  |  |  |
| FaxNo | nvarchar | YES |  |  |  |
| POBox | nvarchar | YES |  |  |  |
| Address | nvarchar | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| WebSite | nvarchar | YES |  |  |  |
| Email | nvarchar | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
| UserID | nvarchar | YES |  |  |  |
| Password | nvarchar | YES |  |  |  |
| CustomerImage | image | YES |  |  |  |
| PriceListID | int | YES |  |  |  |
| PositionsID | int | YES |  |  |  |
| TaxInclude | bit | YES |  |  |  |
| CreditCash | smallint | YES |  |  |  |
| CommercialRegistrationNo | nvarchar | YES |  |  |  |
| ProfessionlicenceNo | nvarchar | YES |  |  |  |
| NewCustRefNo | nvarchar | YES |  |  |  |
| TabSysID | varchar | YES |  |  |  |
| Class_ID | int | YES |  |  |  |
| PostedToERP | bit | YES |  |  |  |
| CompanyNationalID | varchar | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (8):**
- [[AX_INTEG_SENDSALESQUOTATIONS]]
- [[OT_ImportCompetitveItemsData]]
- [[OT_ImportCustomerSurveyAnswers]]
- [[OT_ImportNewCust_Prospective]]
- [[OT_ImportSalesQuotations]]
- [[Pro_ProspectiveCustomers]]
- [[Pro_SalesQuotationHeaders]]
- [[Rpt_Customers_NotesProcpective]]

**Writes (2):**
- [[OT_ImportNewCust_Prospective]]
- [[Pro_ProspectiveCustomers]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Duplicate customers**: Multiple records with same name/phone created during sync — support agent sees duplicate entries in dropdowns
- **Orphan references**: Customer records referenced by transactions that were soft-deleted — causes FK violation on cleanup
- **Balance mismatch**: CustomerBalance field diverges from actual calculated balance — run reconciliation proc
- **Suspend stuck**: IsSuspended flag not clearing after payment — check WF approval chain
- **GPS not collected**: IsCollectedGPS flag false — affects route optimization

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
