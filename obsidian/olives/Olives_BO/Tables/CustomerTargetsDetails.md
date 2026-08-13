---
type: table
database: Olives_BO
name: CustomerTargetsDetails
schema: dbo
tags: [#backoffice, #customer, #sales]
foreign_keys:
  - [[Companies]]
  - [[Customers]]
  - [[CustomerTargets]]
  - [[TargetsReferences]]
referenced_by:
  - [[BO_Online_RptCustomerSalesTargetDetails]]
  - [[Niroukh_SalesPerTeamQ]]
  - [[Pro_CustomerTargets]]
  - [[Pro_CustomerTargetsDetails]]
  - [[RPT_CUSTOMERSMAIN_SUBTARGETREPORT_COLLECTIONS]]
  - [[RPT_CUSTOMERSMAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
  - [[RPT_NIROUKHCUSTOMERSMAIN_SUBTARGETREPORT]]
  - [[Rpt_CompareCustSalesByCategAndTargetRef]]
  - [[Rpt_MonthlyCompareSalesTargetWithCustomer]]
  - [[Rpt_Niroukh_SalesPerTeamQ]]
support_relevance: high
last_verified: 2026-07-05
---
# CustomerTargetsDetails


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customertargetsdetails records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[TargetsReferences]] |
| CustomerID | bigint | NO | ✓ | ✓ | [[CustomerTargets]] |
| TargetYear | smallint | NO | ✓ | ✓ | [[CustomerTargets]] |
| TargetMonth | int | NO | ✓ | ✓ | [[CustomerTargets]] |
| TargetReferenceID | int | NO | ✓ | ✓ | [[TargetsReferences]] |
| Quantity | float | YES |  |  |  |
| Amount | float | YES |  |  |  |
## Primary Key
CompanyID
CustomerID
TargetYear
TargetMonth
TargetReferenceID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
CompanyID, CustomerID, TargetYear, TargetMonth -> [[CustomerTargets]](CompanyID, CustomerID, TargetYear, TargetMonth)
CompanyID, TargetReferenceID -> [[TargetsReferences]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (10):**
- [[BO_Online_RptCustomerSalesTargetDetails]]
- [[Niroukh_SalesPerTeamQ]]
- [[Pro_CustomerTargets]]
- [[Pro_CustomerTargetsDetails]]
- [[RPT_CUSTOMERSMAIN_SUBTARGETREPORT_COLLECTIONS]]
- [[RPT_CUSTOMERSMAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
- [[RPT_NIROUKHCUSTOMERSMAIN_SUBTARGETREPORT]]
- [[Rpt_CompareCustSalesByCategAndTargetRef]]
- [[Rpt_MonthlyCompareSalesTargetWithCustomer]]
- [[Rpt_Niroukh_SalesPerTeamQ]]

**Writes (2):**
- [[Pro_CustomerTargets]]
- [[Pro_CustomerTargetsDetails]]

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
- [[Olives_BO/Tables/CustomersFinancialDetails2]]
- [[Olives_BO/Tables/MultiTargets]]
- [[Olives_BO/Tables/Clients]]
- [[Olives_BO/Tables/Customers2]]
- [[Olives_BO/Tables/ClientsWFID]]
- [[Olives_BO/Tables/WieghtTargets]]
- [[Olives_BO/Tables/CustomersFinancialDetails_Old]]
- [[Olives_BO/Tables/PromotionTypes]]
