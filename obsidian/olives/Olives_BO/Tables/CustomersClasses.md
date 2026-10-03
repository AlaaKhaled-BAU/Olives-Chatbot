---
type: table
database: Olives_BO
name: CustomersClasses
schema: dbo
tags: [#backoffice, #customer, #reference]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OT_SendCustomersInfo]]
  - [[POAOnlineReport]]
  - [[Pro_CustomerReceivablesInfo]]
  - [[Pro_Customers]]
  - [[Pro_CustomersClass]]
  - [[Pro_CustomersFinancialDetails]]
  - [[Pro_CustomersPromotionsGroupsLink]]
  - [[Pro_ImportData]]
  - [[Pro_Locations]]
  - [[Pro_SalesPersons]]
  - [[Pro_SalesmanClassTarget]]
  - [[RPT_NIROUKHCUSTOMERCLASSTARGET]]
  - [[RPT_ZalloumReportTWO]]
  - [[Rpt_CheckAging]]
  - [[Rpt_ChecksByStatus]]
  - [[Rpt_ChequeStatusWithSettelment]]
  - [[Rpt_Coverage]]
  - [[Rpt_CustomerClassChange]]
  - [[Rpt_CustomerClassesByRoute]]
  - [[Rpt_CustomersVisitsCountByClass]]
  - [[Rpt_NewCustomer]]
  - [[Rpt_ProspectiveCustomer]]
  - [[Rpt_ReceiptsByCustomersClass]]
  - [[Rpt_ReceiptsBySalesman]]
  - [[Rpt_RouteSummaryByDelivery]]
  - [[Rpt_RouteSummaryBySalesman]]
  - [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
  - [[Rpt_RouteSummaryBySalesmanByCustomerClass]]
  - [[Rpt_RouteSummaryBySalesman_Delivery]]
  - [[Rpt_RouteSummaryBySalesman_Sukhtian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
  - [[Rpt_SalesmanRouteAssignment]]
  - [[Rpt_UnvisitedCustomersByDate]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Customer-Setup
---
# CustomersClasses


## Business Purpose

Customer classification segments used for targeting, pricing, and reporting.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (39):**
- [[OT_SendCustomersInfo]]
- [[POAOnlineReport]]
- [[Pro_CustomerReceivablesInfo]]
- [[Pro_Customers]]
- [[Pro_CustomersClass]]
- [[Pro_CustomersFinancialDetails]]
- [[Pro_CustomersPromotionsGroupsLink]]
- [[Pro_ImportData]]
- [[Pro_Locations]]
- [[Pro_SalesPersons]]
- [[Pro_SalesmanClassTarget]]
- [[RPT_NIROUKHCUSTOMERCLASSTARGET]]
- [[RPT_ZalloumReportTWO]]
- [[Rpt_CheckAging]]
- [[Rpt_ChecksByStatus]]
- [[Rpt_ChequeStatusWithSettelment]]
- [[Rpt_Coverage]]
- [[Rpt_CustomerClassChange]]
- [[Rpt_CustomerClassesByRoute]]
- [[Rpt_CustomersVisitsCountByClass]]
- [[Rpt_NewCustomer]]
- [[Rpt_ProspectiveCustomer]]
- [[Rpt_ReceiptsByCustomersClass]]
- [[Rpt_ReceiptsBySalesman]]
- [[Rpt_RouteSummaryByDelivery]]
- [[Rpt_RouteSummaryBySalesman]]
- [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
- [[Rpt_RouteSummaryBySalesmanByCustomerClass]]
- [[Rpt_RouteSummaryBySalesman_Delivery]]
- [[Rpt_RouteSummaryBySalesman_Sukhtian]]
- [[Rpt_RouteSummaryBySalesman_Suktian]]
- [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
- [[Rpt_SalesmanRouteAssignment]]
- [[Rpt_UnvisitedCustomersByDate]]

**Writes (2):**
- [[Pro_CustomersClass]]
- [[Pro_ImportData]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing reference values**: Required dropdown items not present — selection fails on tablet
- **Duplicate codes**: Same code used for different descriptions — mapping ambiguity
- **Orphan references**: Referenced by deleted records — FK violation on delete attempt

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- See also (OSFA counterpart): [[OSFA_DB/Tables/OT_CustomersClasses]]
