---
type: table
database: Olives_BO
name: RequestToApprovePromotion
schema: dbo
tags: [#backoffice, #sales, #workflow]
foreign_keys:

referenced_by:
  - [[OT_ImportRequestToApprovePromotion]]
  - [[Rpt_WorkFlowFunctions]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevelOne_Promotions]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-10-03
---
# RequestToApprovePromotion

## Business Purpose
Stores promotion approval requests submitted from mobile devices when applying special promotion campaigns or deals to a customer transaction. Corresponds to workflow `FunctionID = 28` ("Promo"). Key fields include `PromotionID`, `PromotionInfo` (serialized promo description, class, and notes), customer, salesman, date, and `IsAproved`. Queryable via `t.RequestToApprovePromotion`.

## Chatbot semantics
(Query `t.RequestToApprovePromotion` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| طلبات الموافقة على العروض / الحملات | `CustomerNo`, `SalesPersonNo`, `PromotionID` | Direct filters | Lists promo approval requests |
| تفاصيل العرض | `PromotionInfo` | Text description | Contains promo name, class, notes |
| حالة الموافقة | `IsAproved` | `IsAproved = 1` (approved), `0` or `NULL` (pending) | Direct approval flag |
| طلب ملغي | `IsCanceled` | `IsCanceled = 1` | Cancelled requests |
| الربط مع سجل الموافقات العام | Join `t.WF_MasterLog` | `m.FunctionID = 28 AND TRY_CAST(m.Ref1 AS numeric) = req.AutoID AND m.CompanyID = req.CompanyID` | View supervisor decision levels & notes |

**Do not confuse with:**
- `PromotionsHeaders`: Promotion definitions and rules master table.
- `RequestToApprovePromotionDetails`: Sub-detail items requested under the promotion.

## Grain & keys
- **PK**: `AutoID` (numeric identity, 1 row = 1 promo approval request)
- **Tenant key**: `CompanyID`
- **Conventions**: `CustomerNo` → [[Customers]](ID), `SalesPersonNo` → [[SalesPersons]](ID), `PromotionID` → [[PromotionsHeaders]](ID)

## Pipeline (how rows get here)
Raised on tablet when applying campaign → `OT_ImportRequestToApprovePromotion` inserts row into this table (`IsAproved = 0`) → calls `WF_AddWorkFlowLevelOne_Promotions @CompNo, 28, @NewAutoID` → inserts `WF_MasterLog` (`Ref1 = AutoID`). When supervisor approves, `WF_AddWorkFlowLevels` sets `IsAproved = 1`.

## Related
- [[WF_MasterLog]]
- [[WF_SubLog]]
- [[WF_Functions]]
- [[PromotionsHeaders]]
- [[RequestToApprovePromotionDetails]]
- [[_RequestTo-Join-Conventions]]


## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | NO | ✓ |  |  |
| CompanyID | smallint | YES |  |  |  |
| SalesPersonNo | int | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| PromotionInfo | nvarchar | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| IsAproved | bit | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| OSFA_AutoID | numeric | YES |  |  |  |
| PromotionID | int | YES |  |  |  |
| IsCanceled | bit | YES |  |  |  |

## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (3):**
- [[OT_ImportRequestToApprovePromotion]]
- [[Rpt_WorkFlowFunctions]]
- [[WF_AddWorkFlowLevelOne_Promotions]]

**Writes (4):**
- [[OT_ImportRequestToApprovePromotion]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevelOne_Promotions]]
- [[WF_AddWorkFlowLevels]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Stuck in workflow**: WF level not advancing — check WF_SETUPHD and approver chain
- **Missing approver**: No user assigned at workflow level — request never processed
- **Duplicate requests**: Same request submitted multiple times — approve/reject duplicates

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
