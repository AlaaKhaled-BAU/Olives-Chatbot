---
type: procedure
database: Olives_BO
name: SMS_ZumotPromoCodes
schema: dbo
tags: [#backoffice, #reference]
reads_from:
  - [[CouponsBooksDetails]]
  - [[CouponsBooksHeaders]]
  - Cur_SendSMS
  - [[Customers]]
  - [[PromotionsHeaders]]
  - `dbo`
writes_to:
  - [[CouponsBooksDetails]]
called_by:
  - sp_OACreate
  - sp_OADestroy
  - sp_OAGetProperty
  - sp_OAMethod
  - sp_OASetProperty
support_relevance: high
last_verified: 2026-07-05
---
# SMS_ZumotPromoCodes


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CouponsBooksDetails, CouponsBooksHeaders, Cur_SendSMS, Customers, PromotionsHeaders, dbo. Writes CouponsBooksDetails. Calls 5 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
## Tables Read
- [[CouponsBooksDetails]]
- [[CouponsBooksHeaders]]
- Cur_SendSMS
- [[Customers]]
- [[PromotionsHeaders]]
- `dbo`
## Tables Written
- [[CouponsBooksDetails]]
## Callers
_None (no known callers)_
## Callees
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod
- sp_OASetProperty
## Impact / Dependencies

**Tables Read**
- [[CouponsBooksDetails]]
- [[CouponsBooksHeaders]]
- Cur_SendSMS
- [[Customers]]
- [[PromotionsHeaders]]
- dbo

**Tables Written**
- [[CouponsBooksDetails]]

**Callers**
- sp_OACreate
- sp_OADestroy
- sp_OAGetProperty
- sp_OAMethod
- sp_OASetProperty

**Callees**
_None_


## When to Run This

SMS notification procedure. Called when the system needs to send SMS alerts. Check SMS configuration if messages aren't being delivered.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
