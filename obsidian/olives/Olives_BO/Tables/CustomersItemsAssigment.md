---
type: table
database: Olives_BO
name: CustomersItemsAssigment
schema: dbo
tags: [#backoffice, #customer, #inventory]
foreign_keys:
  - [[Companies]]
  - [[Customers]]
  - [[Items]]
  - [[Positions]]
referenced_by:
  - [[Pro_CustomersItemsAssigment]]
support_relevance: high
last_verified: 2026-07-05
---
# CustomersItemsAssigment


## Business Purpose
Customer product assortment and authorization table in Olives_BO. Enforces customer-specific item restrictions, specifying exactly which products (`ItemCode`) are allowed (or prohibited) to be sold to a specific customer account (`CustomerID`) under a designated sales position (`PositionsID`).
- **Targeted Merchandising**: Used for contract compliance (e.g. key account agreements where a hypermarket or retail chain only accepts authorized SKUs) or regulatory restrictions (e.g. licensed items, tobacco/pharma).
- **Mobile Validation**: When salesmen enter orders or invoices on the tablet, the system checks whether the selected customer is permitted to purchase the selected item.

## Chatbot semantics
(Query `t.CustomersItemsAssigment` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule |
|----------------------|-----------|---------------|
| الأصناف المصرح ببيعها للعميل | `CustomerID`, `ItemCode`, `PositionsID` | `CustomerID = @CustomerID` |
| هل الصنف مسموح بيعه لهذا العميل | `CustomerID`, `ItemCode` | `CustomerID = @CustomerID AND ItemCode = @ItemCode` |
| اسم العميل واسم الصنف | Join `t.Customers`, `t.Items` | `ca.CustomerID = c.ID AND ca.ItemCode = i.ItemCode` |

**Do not confuse with:**
- `t.SalesPersonItemsAssignment` (restriction of items permitted for a salesman / position).
- `t.CustomersFinancialDetails` (customer payment terms, credit limits, price lists, and assigned route).

## Grain & keys
- **Grain**: One row per position, customer, and assigned item (`PositionsID`, `CustomerID`, `ItemCode`).
- **Composite PK**: `CompanyID`, `PositionsID`, `CustomerID`, `ItemCode`.
- **Tenant Key**: `CompanyID`.

## Pipeline
Back Office Trade Marketing / Key Account Setup (`Pro_CustomersItemsAssigment`) → `CustomersItemsAssigment` → Synced to mobile handheld devices via `OT_SendSalesmanData`.

## Related
- [[Customers]]
- [[Items]]
- [[SalesPersonItemsAssignment]]
- [[Positions]]

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Positions]] |
| PositionsID | int | NO | ✓ | ✓ | [[Positions]] |
| CustomerID | bigint | NO | ✓ | ✓ | [[Customers]] |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
## Primary Key
CompanyID
PositionsID
CustomerID
ItemCode
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, PositionsID -> [[Positions]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (5):**
- [[Pro_CustomersItemsAssigment]]

**Writes (4):**
- [[Pro_CustomersItemsAssigment]]

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
