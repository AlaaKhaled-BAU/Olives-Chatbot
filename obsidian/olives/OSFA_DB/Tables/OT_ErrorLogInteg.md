---
type: table
database: OSFA_DB
name: OT_ErrorLogInteg
schema: dbo
tags: [#auth, #integration, #log, #mobile]
foreign_keys:
referenced_by:
support_relevance: low
last_verified: 2026-07-05
---
# OT_ErrorLogInteg



## Business Purpose


Integration data store for syncing mobile transactions with external systems.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| ID | bigint | YES | ✓ |  |  |
| CompNo | smallint | YES |  |  |  |
| SalesmanNo | int | YES |  |  |  |
| ErrDesc | ntext | YES |  |  |  |
| SysDate | smalldatetime | YES |  |  |  |
## Primary Key
ID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Integration stuck**: IsPosted flag not clearing — check ERP connection and error log
- **Duplicate sent**: Same transaction sent multiple times — ERP shows duplicates
- **Mapping error**: Field mapping fails — check IntegrationPostedTransactions for error details
- **Timeout**: Large batch exceeds ERP timeout — split into smaller batches

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
- [[OT_RequestToLoginToCustomerWithoutVerficiation]]
- [[OT_RequestToLoginToCustomerWithoutVerficiation_Insert]]
- [[WF_Attachment_CheckExist]]
- [[OT_OnlineRpt_ReturnChecks]]
- [[OT_OnlineRpt_SalesmanSalesByItemOrCateg]]
- [[OT_OnlineRpt_SalesmanSalesByCustomer]]
- [[OT_OrderHistoryDF]]
- [[OT_JsonLog]]
- [[OT_ErrorLog]]

- [[OT_CustomersItemsAssigment]]
- [[OT_Banks]]
- [[OT_CompanyBranches]]
- [[Glossary]]
- [[Shared/Runbooks/Sync-Conflict]]
