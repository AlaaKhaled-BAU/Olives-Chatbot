---
type: procedure
database: Olives_BO
name: Pro_CustomersFinancialDetails
schema: dbo
tags: [#backoffice, #customer]
reads_from:
  - [[BusinessUnits]]
  - [[ClientsActive]]
  - [[CompanyBranches]]
  - Cust_cursor
  - [[Customers]]
  - [[CustomersClasses]]
  - [[CustomersFinancialDetails]]
  - [[CustomersGPSLocations]]
  - [[CustomersGroups]]
  - [[CustomersPromotionsGroups]]
  - [[CustomersTypes]]
  - EarlyPayment
  - Fun_ConvArrayToTable
  - GetSalesmanParentTreeByID
  - [[Locations]]
writes_to:
  - AutoChangeCustomerClassLog
  - [[BusinessUnits]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - Order
  - Route
  - top
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_CustomersFinancialDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads BusinessUnits, ClientsActive, CompanyBranches, Cust_cursor, Customers, CustomersClasses, CustomersFinancialDetails, CustomersGPSLocations, CustomersGroups, CustomersPromotionsGroups, CustomersTypes, EarlyPayment, Fun_ConvArrayToTable, GetSalesmanParentTreeByID, Locations. Writes AutoChangeCustomerClassLog, BusinessUnits, Customers, CustomersFinancialDetails, Order, Route, top. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @CustomerID bigint =318
- @PositionsID int = 1
- @CustomerClassID int = null
- @OldCustomerClassID int = null
- @BusinessUnitID int = 0
- @PaymentTypeID int = null
- @PriceListID int = null
- @RouteID int = 1
- @Discount float = null
- @CustomersPromotionsGroupsID int = null
- @DeliveryDays int = null
- @CreditLimit float = null
- @DueDays smallint = null
- @ChqsDueDays smallint = null
- @AllowChqs bit = null
- @IsSuspended bit = null
- @FavouriteVisitTime smalldatetime = null
- @Reference1 nvarchar(20) = null
- @Reference2 nvarchar(20) = null
- @TaxInclude bit = null
- @CustIDs nvarchar(MAX) = null
- @FromRouteArray nvarchar(MAX) = null
- @cmdType varchar(50)='Select Assign Class By Location'
- @CreditCash int =null
- @VisitOrder varchar(50)=null
- @MaxInvoiceValue float = null
- @MaxInvoiceCount int = null
- @EarlyRepaymentDiscountPerc float = null
- @OrderCashDiscount float = null
- @DiscountEarlyPayDays int = null
- @ChqLimit float = null
- @FromSalesmanID int = null
- @ToSalesmanID int = null
- @Result int = 0 output
- @FromLocation int = null
- @ToLocation int = null
- @FromRoute int = null
- @ToRoute int = 0
- @IsAssigned bit =0
- @AssignCustomersToSalesman AssignCustomersToSalesman ReadOnly
- @AssignClassIDToLocation AssignCustomersToSalesman ReadOnly
- @MoveOnly bit =null
- @CopyBy bit =null, -- 0 Location 1 Route
- @AllowManualDiscount bit =null
- @CompanyBranchID int=null
- @LocLineID int = null
- @LocationID int = null
- @ClassID int = null
## Tables Read
- [[BusinessUnits]]
- [[ClientsActive]]
- [[CompanyBranches]]
- Cust_cursor
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- [[CustomersGPSLocations]]
- [[CustomersGroups]]
- [[CustomersPromotionsGroups]]
- [[CustomersTypes]]
- EarlyPayment
- Fun_ConvArrayToTable
- GetSalesmanParentTreeByID
- [[Locations]]
## Tables Written
- AutoChangeCustomerClassLog
- [[BusinessUnits]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Order
- Route
- top
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[BusinessUnits]]
- [[ClientsActive]]
- [[CompanyBranches]]
- Cust_cursor
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- [[CustomersGPSLocations]]
- [[CustomersGroups]]
- [[CustomersPromotionsGroups]]
- [[CustomersTypes]]
- EarlyPayment
- Fun_ConvArrayToTable
- GetSalesmanParentTreeByID
- [[Locations]]

**Tables Written**
- AutoChangeCustomerClassLog
- [[BusinessUnits]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Order
- Route
- top

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
