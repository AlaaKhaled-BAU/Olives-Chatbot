---
type: table
database: Olives_BO
name: CompanyBranches
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OT_SendCompData]]
  - [[OT_SendSalesmanData]]
  - [[Pro_CompanyBranches]]
  - [[Pro_CustomersFinancialDetails]]
  - [[Pro_CustomersPromotionsGroups]]
  - [[Pro_DeliveryCar]]
  - [[Pro_LastSalesmenTransactionsDateTime]]
  - [[Pro_PromotionsHeaders]]
  - [[Pro_SalesPersons]]
  - [[Pro_TransLock]]
  - [[Pro_UserCompanyBranchesLink]]
  - [[Rpt_CollectedReceiptsByCompany]]
  - [[Rpt_CustomerInfoAndRouteDetails]]
  - [[Rpt_CustomersSalesDetails]]
  - [[Rpt_IncreaseCreditLimit]]
  - [[Rpt_IncreaseCreditLimit_forALPHA]]
  - [[Rpt_LinkedCallCenter]]
  - [[Rpt_ReceivablesSalesInvoice]]
  - [[Rpt_ReportHeader]]
  - [[Rpt_SalesPersonsName]]
  - [[Rpt_SalesTransactionByDocumentsTypes]]
  - [[Rpt_SalesmanSalesByCategory2]]
  - [[Rpt_SalesmanSalesDetails]]
  - [[Rpt_SalesmanTimeSpentPerCustomer6_QimaH]]
  - [[Rpt_SalesmanTimeSpentPerCustomerQima7]]
  - [[Rpt_WFCustomersVisits]]
  - [[WF_GetPositionWFData]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Company-Setup
  - Users-and-Permissions
---
# CompanyBranches


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores companybranches records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| Address | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (73):**
- [[OT_SendCompData]]
- [[OT_SendSalesmanData]]
- [[Pro_CompanyBranches]]
- [[Pro_CustomersFinancialDetails]]
- [[Pro_CustomersPromotionsGroups]]
- [[Pro_DeliveryCar]]
- [[Pro_LastSalesmenTransactionsDateTime]]
- [[Pro_PromotionsHeaders]]
- [[Pro_SalesPersons]]
- [[Pro_TransLock]]
- [[Pro_UserCompanyBranchesLink]]
- [[Rpt_CollectedReceiptsByCompany]]
- [[Rpt_CustomerInfoAndRouteDetails]]
- [[Rpt_CustomersSalesDetails]]
- [[Rpt_IncreaseCreditLimit]]
- [[Rpt_IncreaseCreditLimit_forALPHA]]
- [[Rpt_LinkedCallCenter]]
- [[Rpt_ReceivablesSalesInvoice]]
- [[Rpt_ReportHeader]]
- [[Rpt_SalesPersonsName]]
- [[Rpt_SalesTransactionByDocumentsTypes]]
- [[Rpt_SalesmanSalesByCategory2]]
- [[Rpt_SalesmanSalesDetails]]
- [[Rpt_SalesmanTimeSpentPerCustomer6_QimaH]]
- [[Rpt_SalesmanTimeSpentPerCustomerQima7]]
- [[Rpt_WFCustomersVisits]]
- [[WF_GetPositionWFData]]

**Writes (28):**
- [[Pro_CompanyBranches]]

## Estimated Size / Volatility
Typical business table
## Common Issues
> [!warning] AUTO-GENERATED — verify before trusting

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
