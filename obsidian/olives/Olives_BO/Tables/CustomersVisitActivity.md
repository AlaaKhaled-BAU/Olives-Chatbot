---
type: table
database: Olives_BO
name: CustomersVisitActivity
schema: dbo
tags: [#backoffice, #customer, #sales]
foreign_keys:
  - [[Companies]]
  - [[Customers]]
  - [[Positions]]
referenced_by:
  - [[OT_ImportCustomerSurveyAnswers]]
  - [[Pro_CustomersVisitActivity]]
support_relevance: high
last_verified: 2026-10-03
---
# CustomersVisitActivity

## Business Purpose
The customer visit task configuration table — defines mandatory or ordered activities (`VisitActivityInOrder`) that a salesman occupying position `PositionsID` must perform when visiting a customer `CustomerID` (e.g. shelf survey before invoice, stock audit before orders). Queryable via `t.CustomersVisitActivity`.

## Chatbot semantics
(Query `t.CustomersVisitActivity` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| أنشطة الزيارة المطلوبة | `CustomerID`, `PositionsID`, `VisitActivityInOrder` | Direct filter | Task sequence configured for visit |
| ترتيب مهام الزيارة | `VisitActivityInOrder` | Comma-separated or ordered task codes | Enforcement string on mobile app |

## Grain & keys
- **Composite PK**: (`CompanyID`, `CustomerID`, `PositionsID`)
- **Tenant key**: `CompanyID`
- **FKs**: `CustomerID` → [[Customers]](ID), `PositionsID` → [[Positions]](ID)

## Pipeline
Configured in Back Office visit workflow screens (`Pro_CustomersVisitActivity`). Synchronized to mobile devices via `OT_SendCustomersInfo`.

## Related
- [[Customers]]
- [[Positions]]
- [[LogActionTransaction]]
- [[RequestToExceedFinishAllTasks]]


## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Positions]] |
| CustomerID | bigint | NO | ✓ | ✓ | [[Customers]] |
| PositionsID | int | NO | ✓ | ✓ | [[Positions]] |
| VisitActivityInOrder | varchar | YES |  |  |  |
## Primary Key
CompanyID
CustomerID
PositionsID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
CompanyID, PositionsID -> [[Positions]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (2):**
- [[OT_ImportCustomerSurveyAnswers]]
- [[Pro_CustomersVisitActivity]]

**Writes (1):**
- [[Pro_CustomersVisitActivity]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Format**: VisitActivityInOrder is a CSV of activity tokens (e.g. Agreements,Catalog,...,Order,) — parse by splitting on commas, trailing comma common
## Tenancy

Chatbot queries `t.CustomersVisitActivity` only — auto-scoped by `SESSION_CONTEXT(N'CompanyID')`. Raw dbo access is blocked for `chatbot_ro`.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
