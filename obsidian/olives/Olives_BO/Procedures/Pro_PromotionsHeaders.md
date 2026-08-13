---
type: procedure
database: Olives_BO
name: Pro_PromotionsHeaders
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[ClientsActive]]
  - [[CompanyBranches]]
  - [[CompanyParameters]]
  - [[CustomersPromotionsExceptions]]
  - Fun_GetPromotionsByCustomerGroupUser
  - [[PromotionClasses]]
  - [[PromotionsApprovalLog]]
  - [[PromotionsApprovalSetup]]
  - [[PromotionsCondUnCodInput]]
  - [[PromotionsCondUnCodOutput]]
  - [[PromotionsCustomersGroupsLink]]
  - [[PromotionsHeaders]]
  - [[PromotionsPrioritiesLink]]
  - [[PromotionsRangeInput]]
  - [[PromotionsSalesmanGroupsLink]]
writes_to:
  - [[PromotionsApprovalLog]]
  - PromotionsApproveLog
  - [[PromotionsCondUnCodInput]]
  - PromotionsCondUnCodInputLog
  - [[PromotionsCondUnCodOutput]]
  - PromotionsCondUnCodOutputLog
  - [[PromotionsCustomersGroupsLink]]
  - PromotionsCustomersGroupsLinkLog
  - [[PromotionsHeaders]]
  - PromotionsHeadersLog
  - PromotionsPrioritiesLinkLog
  - PromotionsRangeInputLog
  - [[PromotionsSalesmanGroupsLink]]
  - PromotionsSalesmanGroupsLinkLog
  - [[UserPromotionsLink]]
called_by:
support_relevance: high
last_verified: 2026-07-05
related_workflows: [[Promotion-Setup]]
---
# Pro_PromotionsHeaders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, CompanyBranches, CompanyParameters, CustomersPromotionsExceptions, Fun_GetPromotionsByCustomerGroupUser, PromotionClasses, PromotionsApprovalLog, PromotionsApprovalSetup, PromotionsCondUnCodInput, PromotionsCondUnCodOutput, PromotionsCustomersGroupsLink, PromotionsHeaders, PromotionsPrioritiesLink, PromotionsRangeInput, PromotionsSalesmanGroupsLink. Writes PromotionsApprovalLog, PromotionsApproveLog, PromotionsCondUnCodInput, PromotionsCondUnCodInputLog, PromotionsCondUnCodOutput, PromotionsCondUnCodOutputLog, PromotionsCustomersGroupsLink, PromotionsCustomersGroupsLinkLog, PromotionsHeaders, PromotionsHeadersLog, PromotionsPrioritiesLinkLog, PromotionsRangeInputLog, PromotionsSalesmanGroupsLink, PromotionsSalesmanGroupsLinkLog, UserPromotionsLink. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID int = null
- @Name nvarchar (200)=null
- @PromotionType int = -1
- @PromotionClass int = null
- @InputQtyAmount float = null
- @OutPutType int = null
- @OutQtyAmount float = null
- @MaxQty float = null
- @OutQtyAmount_2 float = null
- @UseInReturn bit = null
- @UseInSales bit = null
- @IsAmountWithoutTax bit = null
- @InputItemUnitID nvarchar(50) = null
- @ItemCode nvarchar(100) = null
- @OutItemUnitID nvarchar(50) = null
- @StartDate smalldatetime =null
- @EndDate smalldatetime =null
- @IsSuspended bit = null
- @Reference1 nvarchar (40)=null
- @Reference2 nvarchar (40)=null
- @PromotionDetails nvarchar (200) = null
- @Notes nvarchar (Max) = null
- @UseRateToCalcBonus bit = null
- @NotDouble bit = null
- @cmdType varchar(50)=null
- @ApplyForAllUnit bit = null
- @DiscountType	smallint	= 0
- @IncludeInTargetBonus	bit	 = null
- @RoundType smallint = null
- @InvoiceType  smallint=null
- @IsNeedCoupon bit = null
- @RunAfterAllPromos bit = null
- @BonusWithPrice bit = null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @CustomersGroup nvarchar(max)='1,2,3,'
- @SalesmanGroup nvarchar(max)='1,2,3,'
- @PCName varchar(100)=null
- @UserID nvarchar(100)=null
- @OpType smallint = null
- @LogID Numeric(30,0) = 0 output
- @NewID bigint = 0 output
- @OutPutSameInput bit = null
- @NeedWFApproval bit = null
- @SalesmanCanChangeOutPutQty bit = null
- @AssignPromotion AssignPromotion ReadOnly
- @ToCompNo int =null
- @PromotionCode int=null
- @CopyFrom int = null
- @AppUser varchar = null
- @SalesPersonType int =Null
- @IsRequiredInTrans bit=null
- @AccumulatedAmount float = null
## Tables Read
- [[ClientsActive]]
- [[CompanyBranches]]
- [[CompanyParameters]]
- [[CustomersPromotionsExceptions]]
- Fun_GetPromotionsByCustomerGroupUser
- [[PromotionClasses]]
- [[PromotionsApprovalLog]]
- [[PromotionsApprovalSetup]]
- [[PromotionsCondUnCodInput]]
- [[PromotionsCondUnCodOutput]]
- [[PromotionsCustomersGroupsLink]]
- [[PromotionsHeaders]]
- [[PromotionsPrioritiesLink]]
- [[PromotionsRangeInput]]
- [[PromotionsSalesmanGroupsLink]]
## Tables Written
- [[PromotionsApprovalLog]]
- PromotionsApproveLog
- [[PromotionsCondUnCodInput]]
- PromotionsCondUnCodInputLog
- [[PromotionsCondUnCodOutput]]
- PromotionsCondUnCodOutputLog
- [[PromotionsCustomersGroupsLink]]
- PromotionsCustomersGroupsLinkLog
- [[PromotionsHeaders]]
- PromotionsHeadersLog
- PromotionsPrioritiesLinkLog
- PromotionsRangeInputLog
- [[PromotionsSalesmanGroupsLink]]
- PromotionsSalesmanGroupsLinkLog
- [[UserPromotionsLink]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[CompanyBranches]]
- [[CompanyParameters]]
- [[CustomersPromotionsExceptions]]
- Fun_GetPromotionsByCustomerGroupUser
- [[PromotionClasses]]
- [[PromotionsApprovalLog]]
- [[PromotionsApprovalSetup]]
- [[PromotionsCondUnCodInput]]
- [[PromotionsCondUnCodOutput]]
- [[PromotionsCustomersGroupsLink]]
- [[PromotionsHeaders]]
- [[PromotionsPrioritiesLink]]
- [[PromotionsRangeInput]]
- [[PromotionsSalesmanGroupsLink]]

**Tables Written**
- [[PromotionsApprovalLog]]
- PromotionsApproveLog
- [[PromotionsCondUnCodInput]]
- PromotionsCondUnCodInputLog
- [[PromotionsCondUnCodOutput]]
- PromotionsCondUnCodOutputLog
- [[PromotionsCustomersGroupsLink]]
- PromotionsCustomersGroupsLinkLog
- [[PromotionsHeaders]]
- PromotionsHeadersLog
- PromotionsPrioritiesLinkLog
- PromotionsRangeInputLog
- [[PromotionsSalesmanGroupsLink]]
- PromotionsSalesmanGroupsLinkLog
- [[UserPromotionsLink]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
