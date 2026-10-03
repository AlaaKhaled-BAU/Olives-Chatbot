---
type: table
database: Olives_BO
name: CustomersGPSLocations
schema: dbo
tags: [#backoffice, #customer, #gps]
foreign_keys:
  - [[Companies]]
  - [[Customers]]
referenced_by:
  - [[OT_ImportCustomerGPS]]
  - [[Pro_Customers]]
  - [[Pro_CustomersFinancialDetails]]
  - [[Pro_CustomersGPS]]
  - [[Pro_LocationsAndSalespersonsLink]]
  - [[Pro_MerchandiseDashboard]]
  - [[Rpt_AssetsByLocation]]
  - [[Rpt_NotSoldPerCateg]]
  - [[Rpt_SalesAreaAndCategoryByCust]]
  - [[Rpt_SalesPerRoute]]
  - [[Rpt_SalesPerRouteWithSalesman]]
  - [[Rpt_SalesmanItemSalesPerRoute]]
  - [[Rpt_SoldUnsoldPerRoute]]
  - [[Rpt_UnloadCustomersPerRoute]]
support_relevance: high
last_verified: 2026-07-05
---
# CustomersGPSLocations


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customersgpslocations records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Customers]] |
| CustomerID | bigint | NO | ✓ | ✓ | [[Customers]] |
| LineID | int | NO | ✓ |  |  |
| GPSX | nvarchar | YES |  |  |  |
| GPSY | nvarchar | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| Loc_Address | nvarchar | YES |  |  |  |
| Posted | bit | YES |  |  |  |
| LocationID | int | YES |  |  |  |
## Primary Key
CompanyID
CustomerID
LineID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (24):**
- [[OT_ImportCustomerGPS]]
- [[Pro_Customers]]
- [[Pro_CustomersFinancialDetails]]
- [[Pro_CustomersGPS]]
- [[Pro_LocationsAndSalespersonsLink]]
- [[Pro_MerchandiseDashboard]]
- [[Rpt_AssetsByLocation]]
- [[Rpt_NotSoldPerCateg]]
- [[Rpt_SalesAreaAndCategoryByCust]]
- [[Rpt_SalesPerRoute]]
- [[Rpt_SalesPerRouteWithSalesman]]
- [[Rpt_SalesmanItemSalesPerRoute]]
- [[Rpt_SoldUnsoldPerRoute]]
- [[Rpt_UnloadCustomersPerRoute]]

**Writes (3):**
- [[OT_ImportCustomerGPS]]
- [[Pro_CustomersGPS]]

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
