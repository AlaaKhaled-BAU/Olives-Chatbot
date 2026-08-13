---
type: table
database: OSFA_DB
name: OT_NewCustomers
schema: dbo
tags: [#customer, #mobile]
foreign_keys:
referenced_by:
  - [[OT_NewCustomersSpecialFieldsInsert]]
  - [[OT_NewCustomers_CheckExist]]
  - [[OT_NewCustomers_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_NewCustomers



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| ID | bigint | YES | ✓ |  |  |
| SalesmanNo | smallint | YES |  |  |  |
| CustName | varchar | YES |  |  |  |
| Address | varchar | YES |  |  |  |
| Tel | varchar | YES |  |  |  |
| Mobile | varchar | YES |  |  |  |
| Contact | varchar | YES |  |  |  |
| Email | varchar | YES |  |  |  |
| GPSX | varchar | YES |  |  |  |
| GPSY | varchar | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| Posted | bit | YES |  |  |  |
| CustType | int | YES |  |  |  |
| MainType | int | YES |  |  |  |
| TaxInclude | int | YES |  |  |  |
| SysID | varchar | YES |  |  |  |
| PrNo | int | YES |  |  |  |
| CommercialRegistrationNo | nvarchar | YES |  |  |  |
| ProfessionlicenceNo | nvarchar | YES |  |  |  |
| RefNo | nvarchar | YES |  |  |  |
| ServerDate | smalldatetime | YES |  |  |  |
| PostedToERP | bit | YES |  |  |  |
| ERP_CustNo | varchar | YES |  |  |  |
| Class_ID | int | YES |  |  |  |
| CompanyNationalID | varchar | YES |  |  |  |
| ShipAddress | varchar | YES |  |  |  |
| PayType | int | YES |  |  |  |
| CreditLimit | float | YES |  |  |  |
| ExpectedAnnualSales | float | YES |  |  |  |
| MoreInfo1 | varchar | YES |  |  |  |
| MoreInfo2 | varchar | YES |  |  |  |
| Approved | bit | YES |  |  |  |
| ChecksLimit | float | YES |  |  |  |
| CollectionDue | varchar | YES |  |  |  |
| CommercialName | varchar | YES |  |  |  |
| RegistrationDate | smalldatetime | YES |  |  |  |
| PostedToERPDateTime | smalldatetime | YES |  |  |  |
| FinalApproval | bit | YES |  |  |  |
| InvoiceDueDays | int | YES |  |  |  |
| ChequeDueDays | int | YES |  |  |  |
| LocationID | int | YES |  |  |  |
| GroupID | int | YES |  |  |  |
| ContactPersonID | int | YES |  |  |  |
| VisitDays | varchar | YES |  |  |  |
| IsStartWork | bit | YES |  |  |  |
| AssetDate | smalldatetime | YES |  |  |  |
| Channel | varchar | YES |  |  |  |
| Division | varchar | YES |  |  |  |
| Segment | varchar | YES |  |  |  |
| Sub_channel | varchar | YES |  |  |  |
| Block | varchar | YES |  |  |  |
| City | varchar | YES |  |  |  |
| Street | varchar | YES |  |  |  |
## Primary Key
CompNo
ID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (3):**
- [[OT_NewCustomersSpecialFieldsInsert]]
- [[OT_NewCustomers_CheckExist]]
- [[OT_NewCustomers_Insert]]

**Writes (1):**
- [[OT_NewCustomers_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Duplicate customers**: Multiple records with same name/phone created during sync — support agent sees duplicate entries in dropdowns
- **Orphan references**: Customer records referenced by transactions that were soft-deleted — causes FK violation on cleanup
- **Balance mismatch**: CustomerBalance field diverges from actual calculated balance — run reconciliation proc
- **Suspend stuck**: IsSuspended flag not clearing after payment — check WF approval chain
- **GPS not collected**: IsCollectedGPS flag false — affects route optimization

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
- [[Shared/Runbooks/Orphan-Records]]
