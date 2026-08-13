---
type: table
database: Olives_BO
name: CompetitveItemsDataHF
schema: dbo
tags: [#backoffice, #inventory]
foreign_keys:
  - [[Companies]]
  - [[Customers]]
  - [[ProspectiveCustomers]]
  - [[SalesPersons]]
referenced_by:
  - [[OT_ImportCompetitveItemsData]]
  - [[Pro_CompanyParameters]]
  - [[Pro_CompetitveItemsDataHF]]
  - [[Rpt_CustomerStockandCompetitveItems]]
  - [[SalesmanInfo]]
support_relevance: high
last_verified: 2026-07-05
---
# CompetitveItemsDataHF


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores competitveitemsdatahf records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersons]] |
| TrYear | smallint | NO | ✓ |  |  |
| TrNo | int | NO | ✓ |  |  |
| SalesPersons | int | YES |  | ✓ | [[SalesPersons]] |
| CustomerID | bigint | YES |  | ✓ | [[Customers]] |
| TrDate | smalldatetime | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| ServerDate | smalldatetime | YES |  |  |  |
| IsProspectiveCustomer | bit | YES |  |  |  |
| ProspectiveCustomerID | bigint | YES |  | ✓ | [[ProspectiveCustomers]] |
## Primary Key
CompanyID
TrYear
TrNo
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
CompanyID, ProspectiveCustomerID -> [[ProspectiveCustomers]](CompanyID, ID)
CompanyID, SalesPersons -> [[SalesPersons]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (4):**
- [[Pro_CompanyParameters]]
- [[Pro_CompetitveItemsDataHF]]
- [[Rpt_CustomerStockandCompetitveItems]]
- [[SalesmanInfo]]

**Writes (1):**
- [[OT_ImportCompetitveItemsData]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Duplicate barcodes**: Multiple items sharing same barcode — POS picks wrong item
- **Price mismatch**: Sell price in Items differs from PriceListDetails — customer charged wrong amount
- **Stock discrepancy**: QtyInAllStores differs from sum of StoreBalances — run CALCITEMBALANCE
- **Missing units**: Item has no valid ItemUnits — cannot be sold
- **Tax config wrong**: IsTaxExempt flag incorrect — ZATCA/legal reporting mismatch

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
