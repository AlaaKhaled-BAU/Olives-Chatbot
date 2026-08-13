---
type: table
database: Olives_BO
name: CatalogMedia
schema: dbo
tags: [#backoffice, #log]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[Pro_CatalogMedia]]
  - [[Pro_Items]]
support_relevance: low
last_verified: 2026-07-05
---
# CatalogMedia


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores catalogmedia records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | NO |  | ✓ | [[Companies]] |
| Name | nvarchar | YES |  |  |  |
| FilePath | nvarchar | YES |  |  |  |
| FileType | smallint | NO |  |  |  |
## Primary Key
AutoID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_CatalogMedia]]
- [[Pro_Items]]

**Writes (1):**
- [[Pro_CatalogMedia]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Rapid growth**: Table size growing fast — archive old records periodically
- **Orphan log entries**: No corresponding source transaction — investigate data source
- **No cleanup**: No purge job configured — disk space may fill up

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Olives_BO/Tables/Tech_CustomizationPerformedTasks]]
- [[Olives_BO/Tables/CustomersFinancialDetails2]]
- [[Olives_BO/Tables/forupdateonly]]
- [[Olives_BO/Tables/Clients]]
- [[Olives_BO/Tables/Customers2]]
- [[Olives_BO/Tables/EmpDetails]]
- [[Olives_BO/Tables/ClientsWFID]]
- [[Olives_BO/Tables/CustomersFinancialDetails_Old]]
- [[Olives_BO/Procedures/RunSQLWebAPI_Integ]]
- [[Olives_BO/Procedures/SMSSEND_ZUMOT]]
- [[Olives_BO/Procedures/Test_Banks]]
- [[Olives_BO/Procedures/Alpha_GetCurrRate]]
- [[Olives_BO/Procedures/Awtar_Integ_GetDataFromAPI]]
