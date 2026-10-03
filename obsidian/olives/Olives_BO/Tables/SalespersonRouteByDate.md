---
type: table
database: Olives_BO
name: SalespersonRouteByDate
schema: dbo
tags: [#backoffice, #gps, #sales]
foreign_keys:
referenced_by:
  - [[Pro_SalespersonRouteByDate]]
support_relevance: high
last_verified: 2026-10-03
---
# SalespersonRouteByDate

## Business Purpose
Sparse **date-specific route override** table — overrides the standard weekly route template ([[SalesPersonsRoutes]]) for specific calendar dates. Used by certain clients when salesmen are assigned temporary special routes on particular days. Queryable via `t.SalespersonRouteByDate`.

## Chatbot semantics
(Query `t.SalespersonRouteByDate` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| مسار مخصص لتاريخ معين | `PositionID`, `Date`, `RouteID` | Filter by date and position | Overrides default weekday route |
| اسم المسار البديل | Join `t.RoutesInformation` | `RoutesInformation.ID = r.RouteID` | Name of override route |

**Do not confuse with:**
- `SalesPersonsRoutes`: The primary weekly recurring route calendar.
- `LogActionTransaction`: Actual visit logs.

## Grain & keys
- **Composite PK**: (`CompanyID`, `PositionID`, `RouteID`, `Date`)
- **Tenant key**: `CompanyID`

## Pipeline
Maintained via Back Office calendar route screens (`Pro_SalespersonRouteByDate`). Checked by `OT_SendSalesmanData` during mobile sync.

## Related
- [[SalesPersonsRoutes]]
- [[RoutesInformation]]
- [[CustomersFinancialDetails]]
- [[Positions]]


## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| PositionID | int | NO | ✓ |  |  |
| RouteID | int | NO | ✓ |  |  |
| Date | date | NO | ✓ |  |  |
| Notes | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
PositionID
RouteID
Date
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_SalespersonRouteByDate]]

**Writes (1):**
- [[Pro_SalespersonRouteByDate]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
