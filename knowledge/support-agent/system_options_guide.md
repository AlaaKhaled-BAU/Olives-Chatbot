# System Options Troubleshooting Guide

This guide groups the 754 options of the Olives Field Automation platform into operational categories. Support agents must use this to check parameter mismatches when diagnosing configuration errors.

> [!WARNING]
> ### 🔄 Options Sync & Salesman Customization
> * **Salesman Context**: Options are loaded *per salesman* inside the OSFA replica database (`OT_SystemOptions` table). A value can be `1` for salesman A and `0` for salesman B.
> * **Sync Transient Warning**: **Never run direct UPDATE queries on `OT_SystemOptions`.** BO synchronization scripts will wipe these values and overwrite them with values computed from BO settings.
> * **Correct Resolution Rule**: To adjust option behaviors permanently, edit the configuration columns in BO (`CompanyParameters` or `SalesPersonsDevicePermissions`).
> * **System Criticality**: Careless query modifications on options tables will cause synchronization locks or lock salespersons out of the system.

## Categories Summary

- [GPS / Geofencing / Map](#gps--geofencing--map) (27 options)
- [Pricing & Discounts](#pricing-and-discounts) (114 options)
- [Invoicing & Sales Orders](#invoicing-and-sales-orders) (285 options)
- [Returns & Expiries](#returns-and-expiries) (13 options)
- [Promotions & Coupons](#promotions-and-coupons) (19 options)
- [Payments & Collections](#payments-and-collections) (62 options)
- [Stock & Van Inventory](#stock-and-van-inventory) (36 options)
- [Printer & Printing](#printer-and-printing) (15 options)
- [Security & Authentication](#security-and-authentication) (21 options)
- [General & Sync / Miscellaneous](#general-and-sync--miscellaneous) (159 options)

---

## GPS / Geofencing / Map

| Option ID | Description | Options & Default Meanings |
|---|---|---|
| `3` | **Login To Cust GPS Check** | 0=Off |
| `6` | **Login To Cust GPS Delay** | Distance In Meters |
| `157` | **Cust LogOut GPS Check** | 0=Off |
| `184` | **Use Map In Set Customer Location** | 0=Off |
| `211` | **No GPS Check For Non Route Customers** | 0=Off |
| `216` | **Check Customer GPS On Customer Trans** | 0=Off |
| `218` | **Sort Route By GPS Distance** | 0=Off |
| `224` | **Use Both GPS And Barcode For Cust Login ( Must Enable GPS And Barcode )** | 0=Off |
| `236` | **New Customer GPS Not Required** | 0=Off |
| `245` | **Check GPS Avi Before Make Transaction** | 0=Off |
| `254` | **Get Accured GPS After Trans** | 0=Off |
| `256` | **Customer Is Near Salesman Distance** | # Meter |
| `257` | **Check Customer Is Near Timer Interval** | 0=Off |
| `289` | **Get Accured GPS After Survey** | 0=Off |
| `344` | **Get My Location By Map** | 0=Off |
| `389` | **Dont Get GPS When Take Photo** | 0=Off |
| `409` | **Take Photo When Get Customer GPS** | 0=Off |
| `417` | **Dont Allow to Use Fake GPS** | 0=Off |
| `418` | **Fake GPS Apps Exceptions** | 0=Off |
| `422` | **Allow Salesman Select Cust Location In Login** | 0=Off |
| `434` | **Use Get Customer GPS Per Location** | 0=Off |
| `544` | **Check Load Unload Store GPS Location** | 0=Off |
| `562` | **Login To Customer Must Have Collected GPS** | 0=Off |
| `591` | **Collect Cust GPS Affect To Local Customer** | 0=Off |
| `616` | **Allow changing the marker for the customer location** | 0=Off |
| `718` | **Collect Customers GPS Locations Prospective Customer** | 0=Off |
| `752` | **Collect Cust GPS Affect To Local Customer Only If Not Collected Before** | 0=Off |

## Pricing & Discounts

| Option ID | Description | Options & Default Meanings |
|---|---|---|
| `4` | **Link DocType With TaxPerc In Invoice** | 0=Off |
| `12` | **Price Tax** | 0=Off |
| `15` | **Allow Sale With Price Zero** | 0=Off |
| `19` | **Use Price Level** | 0=Off |
| `26` | **Use Payment Discount** | 0=Off |
| `35` | **Discount % In Cash Invoice** | 0 : Not Active |
| `90` | **Discount % In Check Invoice** | 0 : Not Active |
| `100` | **Use Range Price** | 0=Off |
| `109` | **Hide Price In External Catalog** | 0=Off |
| `122` | **Enable Accumulation Item Discount** | 0=Off |
| `132` | **Discount % In Cash Return Invoice** | 0 : Not Active |
| `143` | **Use Multi Currency** | 0=Off |
| `149` | **Request To Add Discount** | 0=Off |
| `150` | **Waiting Time for Request To Add Discount** | Time in Seconds |
| `151` | **Checking Time for Request To Add Discount** | Time in Seconds |
| `183` | **Calculate Tax 1 To Sales Tax** | First Char 0 = Accumulated, 1 = Not Accumulated |
| `188` | **Request To Add Discount In Order** | 0=Off |
| `189` | **Waiting Time for Request To Add Discount In Order** | Time in Seconds |
| `190` | **Checking Time for Request To Add Discount In Order** | Time in Seconds |
| `191` | **Use Customer Discount In Unit Price With Item Exception** | 0=Off |
| `195` | **Request To AddExtraBonus In Order** | 0=Off |
| `196` | **Waiting Time for Request To AddExtraBonus In Order** | Time in Seconds |
| `197` | **Checking Time for Request To AddExtraBonus In Order** | Time in Seconds |
| `198` | **Request To AddExtraBonus In Invoice** | 0=Off |
| `201` | **Request To Change Price In Order** | 0=Off |
| `202` | **Waiting Time for Request To Change Price In Order** | Time in Seconds |
| `203` | **Checking Time for Request To Change Price In Order** | Time in Seconds |
| `204` | **Request To Change Price In Invoice** | 0=Off |
| `209` | **Default Price List No For Prospective Customers** | No Of Price list |
| `214` | **Convert Bonus To Discount** | 0=Off |
| `223` | **Apply Discount In Promotion 13 on Voucher** | 0=Off |
| `227` | **Total Max Discount Percent In Invoice** | -1 : Not Active, # AS Percent |
| `232` | **Generate Auto Payment For Cash Invoices** | 0=Off |
| `246` | **Use Last Sell Price in Return Not Linked With Invoice** | 0=Off |
| `247` | **Use Calculated Unit Price In Return With Link Invoice (Luxary)** | 0=Off |
| `248` | **Use Sell Price2 From PriceList In Returns** | 0=Off |
| `249` | **Use Sales Return Without Default Discount** | 0=Off |
| `250` | **Allow Sale With Zero Price By Some Doc Types** | 0=Off |
| `252` | **Use Multi Currency In Same Payment** | 0=Off |
| `259` | **Choice Convert Bonus To Discount In Return With Link Invoice** | 0=Off |
| `277` | **Use Only Default Currency In Payment Per Customer** | 0=Off |
| `280` | **Request To AddExtraBonusAndDiscount In Order** | 0=Off |
| `281` | **Waiting Time for Request To AddExtraBonusAndDiscount In Order** | Time in Seconds |
| `282` | **Checking Time for Request To AddExtraBonusAndDiscount In Order** | Time in Seconds |
| `283` | **Request To AddExtraBonusAndDiscount In Invoice** | 0=Off |
| `290` | **Enter Payment for Cash Invoice In Two Currency** | 0=Off |
| `294` | **Default Price** | 0: Not Active, 1 OR 2 OR 3 |
| `298` | **Update Customer Price List After Cust Login** | 0=Off |
| `300` | **Request To AddExtraBonusAndDiscount In Order** | Perc |
| `305` | **Allow Manual Discount By Customers** | 0=Off |
| `309` | **Check Total Before Tax Dic Must Greater Than Disc Vou** | 0=Off |
| `316` | **Enable Calc Discount With Tax** | 0=Off |
| `318` | **Use Avg Sell Price in Return Not Linked With Invoice** | 0=Off |
| `333` | **Allow Bonus In Sales Return** | 0=Off |
| `347` | **Validate Target Bonus** | 0=Off |
| `349` | **Include Input Qty In Target Bonus** | 0=Off |
| `362` | **Make Cust Discount Zero If have Promotion** | 0=Off |
| `363` | **Validate Items Conv Rate** | 0=Off |
| `386` | **Use Division Golden Arrow Items Filter** | 0=Off |
| `388` | **Validate Target Bonus By Item Ref** | 0=Off |
| `398` | **Dont Include Bonus In Batch Entry** | 0=Off |
| `410` | **Enable WF For Range Price** | 0=Off |
| `416` | **Dont Allow Make Return With Invoice Have Bonus or Disc** | 0=Off |
| `421` | **Allow Salesman Select Pricelist** | -1 Off |
| `426` | **Request To AddExtraBonusAndDiscount In SalesQuotation** | 0=Off |
| `427` | **Use Salesman Item Bonus Target By Salesman Group** | 0=Off |
| `431` | **Document Types Without Customer Discount** | 0=Off |
| `437` | **Calc Bonus Tax** | 0=Off |
| `447` | **Use Last Sell Price in SalesOrder** | 0=Off |
| `455` | **Print Auto Generated Cash Payment** | 0=Off |
| `459` | **Use Sales Order Cash Discount** | 0=Off |
| `462` | **Show Shelf Price (Price3) And Tax Percent In Item Dialog** | 0=Off |
| `475` | **Check Promotion 12,13,14 Calc Amount After Discount** | 0=Off |
| `499` | **Use Optional Item Price With Tax Or Not** | 0=Off |
| `502` | **Validate Not Taxable Customer Alert** | 0=Off |
| `511` | **Exception Permission To Change Price in Sales Order** | 0=Off |
| `531` | **Customer SalesTax No Required To Make Trans** | 0=Off |
| `532` | **Use Multi Currency** | 0=Off |
| `533` | **Use Calc Prices From Lower Unit Price** | 0=Off |
| `537` | **Show Currency Exchange Rate In Payment Like ERP** | 0=Off |
| `539` | **Allow Sales In Zero Price Customer Exception** | 0=Off |
| `568` | **Select Manual Bonus Type** | 0=Off |
| `584` | **Calc Bonus In Return Link With Invoice** | 0=Off |
| `601` | **Only Make Payment with Customer Currency** | 0=Off |
| `604` | **Refresh Item Discount With CalcAccumulation** | 0=Off |
| `609` | **Catalog Price List** | PriceListNo |
| `618` | **Allow Edit Discount Perc In Pay Invoice** | 0=Off |
| `622` | **Al Hayat Show Price Info In SalesOrder Item Dialog** | 0=Off |
| `623` | **Waiting Time for Request To Exceed Pay Invoice Discount** | Time in Seconds |
| `624` | **Checking Time for Request To Exceed Pay Invoice Discount** | Time in Seconds |
| `625` | **Use Salesman Item Bonus Target By Customer** | 0=Off |
| `626` | **Request To Exceed Pay Invoice Discount** | 0=Off |
| `627` | **Disable Exchange Rate in payment** | 0=Off |
| `628` | **Use Sales persons Daily Currency Totals** | 0=Off |
| `635` | **Hide Shelf Price** | 0=Off |
| `647` | **WF_AddExtraBonus Include Item Discount** | 0=Off |
| `654` | **SalesOrder Price Level** | 0=Off |
| `664` | **Calc Pay Discount Base On Net InvoiceAmt In Pay Invoice** | 0=Off |
| `675` | **Allow Edit Pay Amount In Pay Invoice With Discount** | 0=Off |
| `678` | **Use Customer Item Sales Bonus Limit** | 0=Off |
| `682` | **Only Show Items Have Price In Transactions** | 0=Off |
| `684` | **Disable Promotions Related To Item Have Price Less Than Max Range** | 0=Off |
| `688` | **Use Last Sell Price in SalesInvoice** | 0=Off |
| `690` | **Zero Prices And No ItemStatus In SalesReturn** | 0=Off |
| `701` | **Don't Allow change spin Price List** | 0=Off |
| `703` | **Add Discount To Customer Orders** | 0=Off |
| `707` | **Use One Item Discount Promotion** | 0=Off |
| `708` | **LoadOrders Price List** | PriceListNo |
| `710` | **JOTax ServerIP** | 0=Off |
| `712` | **Use JoTax** | 0=Off |
| `720` | **Allow Bonus By DocumentType In SalesOdrer** | 0=Off |
| `723` | **Use Max Items Discount** | 0=Off |
| `724` | **Salesmn Stock Pricelist** | 0=Off |
| `729` | **Use One Price In Catalog** | 0=Off |

## Invoicing & Sales Orders

| Option ID | Description | Options & Default Meanings |
|---|---|---|
| `2` | **Show Item QOH/Weight In Order** | 0=None |
| `8` | **Max Row Count In Invoice** | 0=NoCheck |
| `10` | **Invoice Report Class Name** | 787 |
| `13` | **PaymentType RequiredInSalesOrder** | 0=Off |
| `14` | **Same Item Status In Sales Return** | 0=Off |
| `16` | **Return Invoice Report Class Name** | 2 |
| `23` | **Sales Return Password** | N/A To Void This Feature |
| `24` | **Get Default Upload Order Qty** | 0=Off |
| `29` | **Mark Zero Qty In Order As Red** | 0=Off |
| `30` | **Mark Zero Net Sales In Order As Red** | 0=Off |
| `31` | **Amend Change Cash Credit In Invoice** | 0=Off |
| `32` | **Amend Change Cash Credit In Return Invoice** | 0=Off |
| `33` | **Cash Only In Invoice** | 0=Off |
| `34` | **Credit Only Return Invoice** | 0=Off |
| `36` | **Request To Exceed Customer Credit Limit** | 0=Off |
| `37` | **Waiting Time for Request To Exceed Customer Credit Limit** | Time in Seconds |
| `38` | **Checking Time for Request To Exceed Customer Credit Limit** | Time in Seconds |
| `41` | **Load Order Report Class Name** | 882 |
| `43` | **Max Row Count In Order** | 0=NoCheck |
| `44` | **Sales Order Report Class Name** | 3 |
| `45` | **Note must enter in invoice** | 0=Off |
| `46` | **Note must enter in return invoice** | 0=Off |
| `47` | **Request To Return Invoice** | 0=Off |
| `48` | **Waiting Time for Request To Return invoice** | Time in Seconds |
| `49` | **Checking Time for Request To Return invoice** | Time in Seconds |
| `50` | **Invoice Cash Credit By Customer Payment Type** | 0=Off |
| `51` | **Check Credit Limit In Invoice** | 0=Off |
| `52` | **Requested by must enter in invoice** | 0=Off |
| `53` | **Requested by must enter in return invoice** | 0=Off |
| `57` | **Check Invoice Exceed Due Date** | 0=Off |
| `58` | **Check Salesman Credit Limit In Invoice** | 0=Off |
| `59` | **Request To Exceed Salesman Credit Limit** | 0=Off |
| `60` | **Waiting Time for Request To Exceed Salesman Credit Limit** | Time in Seconds |
| `61` | **Checking Time for Request To Exceed Salesman Credit Limit** | Time in Seconds |
| `63` | **Amend Change Payment Type In Order** | 0=Off |
| `64` | **Amend Change Payment Type In Invoice** | 0=Off |
| `65` | **Amend Change Payment Type In Return Invoice** | 0=Off |
| `71` | **Show Qty In Sales Order** | 0=Off |
| `72` | **Auto Refresh Qty In Sales Order** | 0=Off |
| `73` | **Check Qty In Sales Order** | 0=Off |
| `76` | **Amend Change No. Of Copies In Invoice** | 0=Off |
| `78` | **Enable Proforma Invoice** | 0=Off |
| `79` | **Get Default Upload Order Qty BySales** | 0=Off |
| `80` | **Request To Change Invoice Payment Type** | 0=Off |
| `81` | **Waiting Time for Request To Change Invoice Payment Type** | Time in Seconds |
| `82` | **Checking Time for Request To Change Invoice Payment Type** | Time in Seconds |
| `83` | **Request To Exceed Checks Due Date** | 0=Off |
| `84` | **Waiting Time for Request To Exceed Checks Due Date** | Time in Seconds |
| `85` | **Checking Time for Request To Exceed Checks Due Date** | Time in Seconds |
| `86` | **Disable Print Proforma Invoice** | 0=Off |
| `88` | **Enable Check Payment In Invoice** | 0=Off |
| `89` | **Number Of Check Days In Invoice** | Number Of Days |
| `92` | **Empty Unload Order** | 0=Off |
| `93` | **Disable Credit Invoice For Suspended Customer** | 0=Off |
| `94` | **Enable No Sales Reason** | 0=Off |
| `101` | **Enable Salesman Stock** | 0=Off |
| `106` | **Default Invoice Type** | -1 Not Active ,0: Credit, 1: Cash, 2:Check |
| `111` | **Enable Proforma Order** | 0=Off |
| `112` | **Disable Print Proforma Order** | 0=Off |
| `114` | **Enable Reprint Reason On Invoice** | 0=Off |
| `115` | **Enable Reprint Reason On Return Invoice** | 0=Off |
| `117` | **Enable Reprint Reason On Sales Order** | 0=Off |
| `118` | **Enable Reprint Reason On Load Order** | 0=Off |
| `119` | **Enable Reprint Reason On Unload Order** | 0=Off |
| `121` | **Enable Reprint Reason On Salesman Stock** | 0=Off |
| `123` | **Request To Exceed Customer Invoice Due** | 0=Off |
| `124` | **Waiting Time for Request To Exceed Customer Invoice Due** | Time in Seconds |
| `125` | **Checking Time for Request To Exceed Customer Invoice Due** | Time in Seconds |
| `128` | **Exceed Due Invoice Amount** | Remaining Amount |
| `130` | **Allow Free Invoice** | 0=Off |
| `131` | **Enable Return Invoice By Select Invoice** | 0=Off |
| `133` | **Enable Select Invoice in Return Invoice** | 0=Off |
| `137` | **Check Invoice Exceed Due Date In Orders** | 0=Off |
| `145` | **Disable Zero Qty In Sales** | 0=Off |
| `148` | **Disable Payment Without Settlement Invoice If Exist** | 0=Off |
| `152` | **Default Return Invoice Type** | -1 Not Active , 0: Credit, 1: Cash |
| `154` | **Enable Fill Customer Stock From Invoice History** | 0=Off |
| `167` | **Must Visit Customer Route in Order** | 0=Off |
| `169` | **Auto Open Activities By Order** | 0= Not Active |
| `170` | **Request To Exceed CustomerInvoiceDueInOrder** | 0=Off |
| `171` | **Waiting Time for Request To Exceed CustomerInvoiceDueInOrder** | Time in Seconds |
| `172` | **Checking Time for Request To Exceed CustomerInvoiceDueInOrder** | Time in Seconds |
| `173` | **Check Exceed CustomerInvoiceDueInOrder** | 0=Off |
| `176` | **Group Cust  By Related Salespersons** | 0=Off |
| `179` | **Credit Invoice Before Due Day** | Num Of Days |
| `180` | **Enable Salesman Procedures** | 0=Off |
| `185` | **Request To Exceed Customer Credit Limit In Order** | 0=Off |
| `186` | **Waiting Time for Request To Exceed Customer Credit Limit In Order** | Time in Seconds |
| `187` | **Checking Time for Request To Exceed Customer Credit Limit In Order** | Time in Seconds |
| `194` | **Merge  Collection Target With Sales Target** | 0=Off |
| `213` | **Class RPT Item Sales** | 0 |
| `215` | **User Expire date in Customer Stock & Retrun Order** | 0=Off |
| `225` | **Validate Sales Voucher Promotion Log** | 0=Off |
| `228` | **Disable Promotion With Return By Invoice** | 0=Off |
| `233` | **Make Default Upload Order By Van Custody** | 0=Off |
| `239` | **Rpt_Print_Proforma_Reciepts** | 1 |
| `240` | **Return Order Qty Only** | 0=Off |
| `251` | **Stop Make Stock Transactions After Unload Order** | 0=Off |
| `253` | **Default Upload Order By Van Custody Qty Unit Serial** | #=Unit Serial |
| `255` | **Use Multi Store And Multi Salesman** | 0=Off |
| `261` | **Salesman Must Enter Order Or Invoice From Catalog** | 0=Off |
| `262` | **Dont Allow Make Payment With Invoice have Credit Limit** | 0=Off |
| `263` | **Must Make Payment With Invoice have Or Not have Credit Limit** | 0=Off |
| `264` | **Allow Payment Only For Credit Customers** | 0=Off |
| `271` | **Add Prospective Customer before save Sales Quotation** | 0=Off |
| `278` | **Open Payment After Cust Login if have peinding invoices** | 0=Off |
| `279` | **Filter Items Units in Upload Order** | 0=Off |
| `284` | **Check Exceed CustomerInvoiceDueInOrderAndInvoice With Cust Balance** | 0=Off |
| `287` | **Class InvReturn And Invoice Print Online Report** | 1 |
| `288` | **Calc Customer Balance Without Current Orders** | 0=Off |
| `292` | **Use Salesman Msg Timer Interval** | 0=Off |
| `296` | **Show Item Batchs In Order** | 0=Off |
| `299` | **Ask Salesman to add All Current Items in UnLoad Order** | 0=Off |
| `301` | **Auto Refresh Qty In Load Order** | 0=Off |
| `302` | **Disabel Printer Icon From Salesman Option Activity** | 0=Off |
| `303` | **Use Order Delivery Info** | 0=Off |
| `306` | **Allow Salesman To Change Company Settings** | 0=Off |
| `307` | **Allow Salesman Issue Money To Cust** | 0=Off |
| `308` | **Allow Salesman Approve His Stock** | 0=Off |
| `312` | **Pay Invoices Round** | 0=Off |
| `313` | **additional Salesman KPIS** | 0=Off |
| `317` | **Enable Salbeshian Hospital Invoice** | 0=Off |
| `319` | **No WorkFlow in Return Linked With Invoice In Same Day** | 0=Off |
| `320` | **Request To Return Invoice** | 0=Off |
| `323` | **Print Invoice and Return in same file - Class Name** | 1 |
| `337` | **Salesman Routes Report Class Name** | 0 |
| `340` | **Dont Validate Min Qty In Upload Order Custudy** | 0=Off |
| `341` | **Sales Order Main Store With 999999** | 0=Off |
| `345` | **Use Direct online invoice to ERP** | 0=Off |
| `346` | **Use Order Delivery System** | 0=Off |
| `352` | **Request To Exceed Invoice Amount Approve** | 0=Off |
| `353` | **Waiting Time for RequestToExceedInvoiceAmount Approve** | Time in Seconds |
| `354` | **Checking Time for RequestToExceedInvoiceAmount Approve** | Time in Seconds |
| `355` | **Request To Exceed Invoice Count Approve** | 0=Off |
| `356` | **Waiting Time for Request To Exceed Invoice Count Approve** | Time in Seconds |
| `357` | **Checking Time for Request To Exceed Invoice Count Approve** | Time in Seconds |
| `358` | **Use Invoices Due Days From Pay Types** | 0=Off |
| `359` | **Allow Skip Credit Limit Validation In Order** | 0=Off |
| `360` | **Use Items Sales Units Filter** | 0=Off |
| `364` | **Sales Quotation Report Class Name** | 99 |
| `365` | **Use Invoice Delivery System** | 0=Off |
| `370` | **Allow Edit Sales Order** | 0=Off |
| `371` | **Edit Sales Order Source** | 0=Off |
| `374` | **Add Days To Sales Order Delivery Date** | 0=Off |
| `375` | **Ask Salesman For Customer Visit** | 0=Off |
| `379` | **Make Unload Order For Damaged Returns Items** | 0=Off |
| `380` | **Use Aske For Suggested Items In Invoice** | 0=Off |
| `381` | **Use Salesman Car Counter** | 0=Off |
| `384` | **Use Expected Invoice Amount As Info** | 0=Off |
| `385` | **Use Salesman Seals No.** | 0=Off |
| `387` | **Use Pay Invoice Early By InvDate** | 0=Off |
| `390` | **Use Auto Transaction For Salesman Stock** | 0=Off |
| `391` | **Enter Password When Make Salesman Stock** | 0=Off |
| `397` | **Must Use Suggest Order Or Invoice** | 0=Off |
| `399` | **Use Invoice Delivery Transfer** | 0=Off |
| `403` | **Payment Without Pay Invoices Not Allow** | 0=Off |
| `405` | **Salesman Can Change Server IP From Login Screen** | 0=Off |
| `406` | **Salesman Can Edit Customer Mobile No** | 0=Off |
| `407` | **Link Batches In Return With Invoice** | 0=Off |
| `408` | **Salesman Must Approve SalesOrder To Send To Server** | 0=Off |
| `411` | **Request To Exceed Customer Visit Order** | 0=Off |
| `412` | **Waiting Time for Request To Exceed Customer Visit Order Approve** | Time in Seconds |
| `413` | **Checking Time for Request To Exceed Customer Visit Order Approve** | Time in Seconds |
| `419` | **Use Opened SalesOrders And Quotation** | 0=Off |
| `420` | **Use Auto Upload Order From SalesOrder** | 0=Off |
| `430` | **Link Return with Today Invoice Only** | 0=Off |
| `432` | **Dont Show Items Zero Qty Main Store In Load Order** | 0=Off |
| `433` | **Must Return All Invoice Item In Linked Return** | 0=Off |
| `436` | **Use Store Items Filter In Orders** | 0=Off |
| `438` | **Allow Salesman to Edit Customer Info** | 0=Off |
| `445` | **Use Pay Invoice Early By InvDate Partially** | 0=Off |
| `446` | **Auto Customer Logout If Salesman Is Distant** | 0=Off |
| `453` | **Use Survey For Salesman** | 0=Off |
| `454` | **Aske Supervisor For Visit Cust Type With Salesman Or Not** | 0=Off |
| `458` | **Use Auto Salesman Stock** | 0=Off |
| `460` | **Calc Check Due Days From Manual Paid Invoice** | 0=Off |
| `463` | **Filter Items In Return Order** | 0=Off |
| `466` | **Use Show Invoice Details From Account Statement** | 0=Off |
| `468` | **Auto Open Load Order After Update Data** | 0=Off |
| `469` | **Use POS Invoice** | 0=Off |
| `470` | **Use Cash Credit Invoice Serials** | 0=Off |
| `472` | **Use Update Order History Status From Online** | 0=Off |
| `474` | **Use SalesOrder Based On Quotation** | 0=Off |
| `476` | **Invoice Delivery Report Class Name** | 0 |
| `477` | **Add Payment Invoice Data** | 0=Off |
| `480` | **Use Salesman Stock Settlement With Auto Invoice And Return** | 0=Off |
| `481` | **Dont Ask Salesman For Route Customer Visit** | 0=Off |
| `482` | **Total Payment Must Equal Total Paid Invoice** | 0=Off |
| `483` | **SalesOrder Requierd Note** | 0=Off |
| `484` | **Checks Due Dates From Last Day of Previous Month** | 0=Off |
| `486` | **Use Salesman Assistants** | 0=Off |
| `488` | **Limit Items Amount In Load Order** | 0=Off |
| `489` | **Use Salesman Stock Items Details** | 0=Off |
| `490` | **Add Zero Qty Auto In Salesman Stock For Avi Items** | 0=Off |
| `492` | **Use Postpone SalesOrder WorkFlow** | 0=Off |
| `495` | **Use Replacement Sales Return** | 0=Off |
| `496` | **Request To Make Zero Amount Invoice** | 0=Off |
| `497` | **Waiting Time for Request To Make Zero Amount Invoice** | Time in Seconds |
| `498` | **Checking Time for Request To Make Zero Amount Invoice** | Time in Seconds |
| `503` | **Filter Items From Linked Invoice In Return** | 0=Off |
| `504` | **Pay Invoices By Customer Group Reference** | 0=Off |
| `505` | **Use Promo 14 Input By Invoice Amount_Zumot** | 0=Off |
| `510` | **Disable Promotions In Sales Order** | 0=Off |
| `512` | **Show Main Qty In Load Order** | 0=Off |
| `513` | **Check Qty In Load Order** | 0=Off |
| `514` | **Required Store No In Load Order** | 0=Off |
| `515` | **Use Salesman Sales Target Login Alarm** | 0=Off |
| `516` | **Required Store No In Salesman Stock** | 0=Off |
| `519` | **Select Salesman In Return Order** | 0=Off |
| `521` | **DueDay Invoice** | 0=Off |
| `522` | **Use SalesPersonGroup Item Sales Qty Limit** | 0=Off |
| `523` | **Use Customer Item Sales Qty Limit** | 0=Off |
| `528` | **Report Item Avg Sales By Customer** | 0=Off |
| `536` | **Customer Statement Of Account With Local Salesman Trans** | 0=Off |
| `540` | **Dont Check CreditLimit In SalesOrder IF Balance And CreditLimit Zero** | 0=Off |
| `543` | **Show Categ For Available Items Only In Invoice** | 0=Off |
| `549` | **Salesman Operations Time Off** | 0 Not Active, Hours between 0-23 |
| `550` | **Return Invoice Link Search With BatchNo** | 0=Off |
| `551` | **Require Item Image In Return Order** | 0=Off |
| `552` | **Dont Add Pay Invoice For Credit Invoices** | 0=Off |
| `553` | **Validate Delivery Date Day In SalesOrder** | 0=Off |
| `554` | **Invoice Amount Only Is Default For CreditLimit Payment** | 0=Off |
| `555` | **Order Item Use Note** |  |
| `556` | **Class RPT Customers Invoices Pay** | 0 |
| `558` | **Invoice History  Class Name** | 0 |
| `561` | **URL request salesman dashboard** | URL |
| `564` | **Prevent Make Payment For Customer Who Had Undelivered Invoice** | 0=Off |
| `565` | **Return Invoice Must Linked To Invoice** | 0=Off |
| `570` | **Show Ref4 InsteadOf DueDate In Pay Invoice** | 0=Off |
| `571` | **Show Icon pay invoice in payment** | 0=Off |
| `574` | **Use Return Credit Limit** | 0=Off |
| `576` | **Disable Auto Settlement Invoice Button In Payment** | 0=Off |
| `577` | **Max DueDay Invoice In SysOp 521** | 0=Off |
| `578` | **Show Invoice Detail Invoice in Payment** | 0=Off |
| `579` | **Show Ref1 In InvNo In InvoiceHistory** | 0=Off |
| `585` | **Show Ref1 In Return Invoice Link Dialog** | 0=Off |
| `586` | **Must Update Data After Make Upload Order** | 0=Off |
| `588` | **Update CreditInvoiceList Online When Make Payment** | 0=Off |
| `593` | **Use Shipping Orders (القمة الماسية)** | 0=Off |
| `596` | **Must Enter Retrun Reason In Return Order** | 0=Off |
| `597` | **Must Enter Expiry Date In Return Order** | 0=Off |
| `603` | **Use Sales Order Trans Fees** | 0=Off |
| `607` | **Amount  pay invoice canot zero** | 0=Off |
| `608` | **Free Cust Invoice Link With Inv His** | 0=Off |
| `612` | **Can Edit Order Delivery Invoice** | 0=Off |
| `619` | **Allow Make Normal Invoice Within SalesOrder Delivery** | 0=Off |
| `621` | **AlWafi_ Get Settlement Invoice Info** | 0=Off |
| `633` | **Use Invoice From Return** | 0=Off |
| `634` | **Use Issue Items Based On SalesOrder** | 0=Off |
| `642` | **Dont Request To Return Invoice In Replacement** | 0 |
| `643` | **Salesman Balance Report Class Name** | 11111111 |
| `644` | **Free Cust Invoice Link With Inv His With Barcode** | 0=Off |
| `650` | **validate item invoice type** | 0=Off |
| `658` | **Amend Change No. Of Copies In Load order** | 0=Off |
| `660` | **Ask Salesman For Customer Visit By Tow Screen** | 0=Off |
| `662` | **Use Store Items Filter In Orders Multi Level** | 0=Off |
| `666` | **Use IsForSales for items** | 0=Off |
| `671` | **Invoice Items Must WithIn Promotion Input** | 0=Off |
| `674` | **Update Store Qty Every Open SalesOrder By Cust** | 0=Off |
| `687` | **Can Not Sale Customer Have One Credit Invoice** | 0=Off |
| `694` | **Class RPT Sales Orders History** | 0 |
| `695` | **Telegraph  Items sold  In Orders and inv** | 0=Off |
| `697` | **Use Online Stop Salesman** | 0=Off |
| `702` | **Use Return From Invoice In Unit4** | 0=Off |
| `706` | **Request To Change Invoice Payment Type Not Equal Customer PayType** | 0=Off |
| `713` | **Use years before Invoice VouNo** | 0=Off |
| `714` | **select Salesman from Dialog in action_settings_login** | 0=Off |
| `715` | **use copy sales order** | 0=Off |
| `717` | **Validate Delivery Date not same today In SalesOrder** | 0=Off |
| `719` | **Update Salesman Balance Before Add Invoice** | 0=Off |
| `721` | **Allow CustIssue Amount Only For Credit Customers** | 0=Off |
| `722` | **Credit Sales Not Allow For Customers Not Have CreditLimit** | 0=Off |
| `725` | **Add Minimum Sales Invoice \ Order Value Option By Item Category** | 0=Off |
| `727` | **Use Online Stop Salesman without login system settings** | 0=Off |
| `728` | **Use SalesOrder Based On Customer Stock** | 0=Off |
| `734` | **Allow Salesman Request to cancel payment** | 0=Off |
| `737` | **Allow Salesman to make Bank Deposit** | 0=Off |
| `739` | **Use Minimum Sales Invoice \ Order Value Option By Customer Group Only** | 0=Off |
| `747` | **Hide Salesman Balance** | 0=Off |
| `748` | **Use Budget Limt For Sales Items** | 0=Off |
| `749` | **use wf for reutrn if the salesman dosenot make invoice for the same customer** | 0=Off |
| `750` | **select  Salesman  when Aske Supervisor For Visit Cust Type With Salesman** | 0=Off |
| `753` | **Use Order From Excel File** | 0=Off |
| `756` | **Default DocType Type** | 0=Off |
| `763` | **Return Invoice As Original Linked Invoice Units** | No Of Price list |

## Returns & Expiries

| Option ID | Description | Options & Default Meanings |
|---|---|---|
| `42` | **Default Return Status** | 1=Valid |
| `62` | **Print Damaged Return Items Summary** | 199 |
| `77` | **Amend Change No. Of Copies In Return** | 0=Off |
| `168` | **Must Take Picture in Return By Status** | 0=Off |
| `242` | **Print Damaged Return ItemsStatus Summary** | 2 |
| `267` | **Disable Change Item Status In Return** | 0=Off |
| `311` | **Use Return Checks** | 0=Off |
| `382` | **Use Return Reason** | 0=Off |
| `441` | **Use Return Delivery System** | 0=Off |
| `449` | **Allow Add Item Batch In Return Trans** | 0=Off |
| `526` | **Use Manufacturers Defect Jibreni** | 0=Off |
| `573` | **Use Items Stock Online For Damaged** | 0=Off |
| `575` | **Use Return Qty Limit** | 0=Off |

## Promotions & Coupons

| Option ID | Description | Options & Default Meanings |
|---|---|---|
| `99` | **Zalloum Promotion** | 0=Off |
| `129` | **Enable Promotion Output Item From Input Item** | 0=Off |
| `159` | **Use Promotions Priorities** | 0=Off |
| `164` | **Use Promotions Coupons** | 0=Off |
| `199` | **Enable Promotions Checking Sorting** | 0=Off |
| `241` | **Show Promotion Details List** | 0=Off |
| `273` | **Allow Insert Promotion Input Items In Voucher** | 0=Off |
| `314` | **Use Update Promotion Online** | 0=Off |
| `328` | **Request To Promotion Approve** | 0=Off |
| `329` | **Waiting Time for Request To Promotion Approve** | Time in Seconds |
| `330` | **Checking Time for Request To Promotion Approve** | Time in Seconds |
| `348` | **No Partial Input Promotions** | 0=Off |
| `478` | **Use Promotion Group Selection** | 0=Off |
| `518` | **SpeedUp Load Promotions** | 0=Off |
| `527` | **Use Coupons With Customer Filter** | 0=Off |
| `617` | **Use Promotions Dont Apply** | 0=Off |
| `670` | **Show Coupon No. In List** | 0=Off |
| `698` | **Use  Customer Promotions Link** | 0=Off |
| `700` | **Add New Customer To Customer List In Device And Link With Promotion Group** | 0=Off |

## Payments & Collections

| Option ID | Description | Options & Default Meanings |
|---|---|---|
| `11` | **Payment Report Class Name** | 0 |
| `69` | **Check Suspended Customers** | 0=Off |
| `102` | **Cash Only Customer List** | 0: Not Active    list: 1,15,20...etc |
| `103` | **Use Check Due Days Avarage** | 0=Off |
| `116` | **Enable Reprint Reason On Payment** | 0=Off |
| `126` | **Check Due Days Avarage - Addition Days** | Number Of Days |
| `136` | **Checking Time for Request To Visit Customer Not In Route** | Time in Seconds |
| `138` | **Disable Complex Payment (Cash Only Or Check Only)** | 0=Off |
| `147` | **Enable Payment Activity** | 0: All, 1:Without Settlement, 2:Settlement |
| `153` | **Check Tablet Date** | -1 Not Active , # Of Days |
| `160` | **Request To Exceed Chq Limit** | 0=Off |
| `161` | **Waiting Time for Request To Exceed Chq Limit** | Time in Seconds |
| `162` | **Checking Time for Request To Exceed Chq Limit** | Time in Seconds |
| `163` | **Check Exceed Chq Limit** | 0=Off |
| `175` | **Chq Count in Payments** | 0 : Not Active, # |
| `181` | **Validate Check DueDate With Last InvDueDate** | 0=Off |
| `193` | **Customer Balance Without Chq Balance** | 0=Off |
| `222` | **Checking Time for RequestForCustomerLoginWithoutVerficiation** | Time in Seconds |
| `231` | **Checking Time for Request To AddNewCustomer** | Time in Seconds |
| `291` | **Must Select Document Type in Receipt** | 0=Off |
| `321` | **Waiting Time for Request To Add Drawer** | Time in Seconds |
| `322` | **Checking Time for Request To Add Drawer** | Time in Seconds |
| `324` | **Request To Add Check** | 0=Off |
| `325` | **Waiting Time for Request To Add Check** | Time in Seconds |
| `326` | **Checking Time for Request To Add Check** | Time in Seconds |
| `331` | **Check Drawer Is Required** | 0=Off |
| `336` | **Checking Time for Request To Make Transaction for Suspend Customer Approve** | Time in Seconds |
| `338` | **Use Receipt Requests** | 0=Off |
| `343` | **Filter Banks By Company Ref** | 0=Off |
| `351` | **Use Bank Transfer In Payment** | 0=Off |
| `367` | **Paid As FIFO Validation In Payment** | 0=Off |
| `368` | **Amend Make Payment More Than Default Amount** | 0=Off |
| `378` | **Required Cheque Bank Account No** | 0=Off |
| `395` | **Select Department In Payment (For Hakkak)** | 0=Off |
| `444` | **Checking Time for Request To Link Customer  Approve** | Time in Seconds |
| `464` | **Auto Fill Checks Total In Payment Amount** | 0=Off |
| `529` | **Confirm Payment Amount Msg** | 0=Off |
| `547` | **require check image** | 0=Off |
| `559` | **checks date less than today's date** | 0=Offline |
| `580` | **Check TelNo In Edit Customer** | 0=Off |
| `581` | **Request To Change Delivery PaymentType** | 0=Off |
| `582` | **Waiting Time for Request To Change Delivery PaymentType** | Time in Seconds |
| `583` | **Checking Time for Request To Change Delivery PaymentType** | Time in Seconds |
| `590` | **Get chq due days after end of month by days (telegraph)** | 0=Off |
| `614` | **Payment_Branches** | 0=Off |
| `620` | **Auto Fill Pay Inv Total In Payment Amount** | 0=Off |
| `631` | **number check digits  must be entered** | number check digits |
| `638` | **Checking Time for Request To Finish All Tasks** | Time in Seconds |
| `661` | **Login To Cust NFC Check** | 0=Off |
| `663` | **Check Automatic date&time** | 0=Off |
| `665` | **Skip Login To Cust Barcode Check If The Barcode Empty** | 0=Off |
| `668` | **Use Open Close Cash** | 0=Off |
| `669` | **Payment_Denominations** | 0=Off |
| `680` | **Check cusomer name and phone is exist new customer** | 0=Off |
| `686` | **Checking Time for Request To Exceed Pay Over Balance.** | Time in Seconds |
| `689` | **Request To Exceed Checks Pay Over Balance** | 0=Off |
| `691` | **Enter Foreign Pay Amount Only In Payment** | 0=Off |
| `735` | **Waiting Time for Request to cancel payment** | Time in Seconds |
| `736` | **Checking Time for Request to cancel payment** | Time in Seconds |
| `742` | **Show Check box for reutrn checks** | 0=Off |
| `746` | **Hide the Add Check button when the payment  Cash Only** | 0=Off |
| `760` | **payment all customer without login customer** | 0=Off |

## Stock & Van Inventory

| Option ID | Description | Options & Default Meanings |
|---|---|---|
| `9` | **Open Cust Stock Tacking After Login** | 0=Off |
| `25` | **Only Integer Qty** | 0=Off |
| `87` | **Disable Print Item Stock** | 0=Off |
| `91` | **Hide Item Stock** | 0=Off |
| `97` | **Hide Stock Qty** | 0=Off |
| `105` | **Show Store Qty Report** | 0=Off |
| `110` | **Hide Qty Availability in Catalog** | 0=Off |
| `120` | **Enable Reprint Reason On Customer Stock** | 0=Off |
| `158` | **Van Transfare Report Class Name** | 1 |
| `219` | **Upload Data After Cust Logout** | 0=Off |
| `266` | **Use Items Batches In Vouchers** | 0=Off |
| `274` | **Use Special Qty** | 0=Off |
| `276` | **Select Items Batches From List** | 0=Off |
| `304` | **Show Muilty Store Qty Report** | 0=Off |
| `392` | **Use Daily Transfered Qty Report** | 0=Off |
| `393` | **Use Items Qty Status Report** | 0=Off |
| `394` | **Dont Validate Qty In Unload Voucher** | 0=Off |
| `404` | **Use Items Qty Details From Batch Info** | 0=Off |
| `461` | **Use Items Qty Details From Batch Info-Required** | 0=Off |
| `491` | **Use One Item In Customer Stock Per Category** | 0=Off |
| `500` | **Hide Zero Unit Qty In Item Stock Description** | 0=Off |
| `517` | **Show Zero Qty in Item Stock** | 0=Off |
| `520` | **Calc In And Out Qty In Item Replacement** | 0=Off |
| `525` | **SpeedUp Items Stock List** | 0=Off |
| `535` | **Use One Valid Unload Only** | 0=Off |
| `566` | **Search Items Barcode in ItemsBatches** | 0=Off |
| `592` | **Use Special Qty Per Customer** | 0: Not Active, # Customer Number 1235,5646,568 ...etc |
| `595` | **Must Update Data Before Print Item Stock** | 0=Off |
| `599` | **Show Cust History Batch Expire** | 0=Off |
| `645` | **Dont Modify Auto Unload Items** | 0=Off |
| `649` | **Must Import Export before Unload** | 0=Off |
| `655` | **Calc Unload Qty With Items Balance** | 0=Off |
| `672` | **Show total qty. In item stock** | 0=Off |
| `704` | **Show total qty. In item stock in unit one** | 0=Off |
| `726` | **Items Categ Stock By Items Class** | 0=Off |
| `733` | **Select Item Class In Customer Stock** | 0=Off |

## Printer & Printing

| Option ID | Description | Options & Default Meanings |
|---|---|---|
| `75` | **Disable Re-Print Icons** | 0=Off |
| `95` | **Print Customer Statment of Account** | 0=Off |
| `104` | **Print Image factor** | 1: Default Count, Count * n, n=value 1,1.25,1.5 ...etc |
| `139` | **Disable Cancel Print Dialog** | 0=Off |
| `141` | **Amend Change No. Of Copies In Paymnet** | 0=Off |
| `155` | **Print Pause Time Between Images** | Time in Second 1000 = 1 Second |
| `156` | **Print Spacing** | Sewoo 3 inch (line count 1,2,3 ...etc) Sewoo 4 inch (form Heigth 90,100,110 ...etc) |
| `178` | **Hide Change  Printer  Address** | 0=Off |
| `234` | **Sewoo Spliting Image Height** | #=Height |
| `297` | **Copy Count RePrint** | 0=Off |
| `342` | **Printing Image Quality** | # 0-100 |
| `350` | **Max Print Count** | 0=Off |
| `594` | **Print As One Shot** | 0=Off |
| `605` | **Sujab Item Grouping In Printing** | 0=Off |
| `745` | **Granting permission to print at a size of 4 inches on Chinese printers** | 0=Off |

## Security & Authentication

| Option ID | Description | Options & Default Meanings |
|---|---|---|
| `1` | **Login To Cust Method** | 0=Direct Login |
| `7` | **Enable PassKey Cust Login** | 0=Off |
| `40` | **Pass Code** | -1 : Random Key |
| `200` | **Enable Password Security** | 0=Off |
| `207` | **Use Session Management In Tablet** | 0=Off |
| `208` | **Session Expire TimeOut** | Time in Minutes |
| `220` | **RequestForCustomerLoginWithoutVerficiation** | 0=Off |
| `221` | **Waiting Time for RequestForCustomerLoginWithoutVerficiation** | Time in Seconds |
| `226` | **Customers Login Without Verification** | 0: Not Active, # Customer Number 1235,5646,568 ...etc |
| `377` | **Skip Permissions In Tablets** | 0=Off |
| `451` | **Enable PassKey Per Time** | 0=Off |
| `501` | **Use Special Password to Hide History** | 0=Off |
| `508` | **Enable PassKey By Key Generation** | 0=Off |
| `542` | **Edit Customer With Verification Code** | 0=Off |
| `560` | **Survey Only Allowed In Login To Customer As Visit** | 0=Off |
| `602` | **Use End Journy Password** | 0=Off |
| `611` | **Update Settings on login** | 0=Off |
| `632` | **Allow Screens In Cust Login Not As Visit** |  |
| `659` | **Hide Customer Info If The Login Not As Visit** | 0=Off |
| `693` | **Activity Password** | 0=Off |
| `759` | **Show Customer Target Dialog After Login In Customer** | 0=Off |

## General & Sync / Miscellaneous

| Option ID | Description | Options & Default Meanings |
|---|---|---|
| `5` | **Cust Selection Type** | 0 None |
| `17` | **Barcode Type** | 1=Camera |
| `18` | **Online Status** | 0=Offline |
| `22` | **Def Copy Count** |  |
| `27` | **Cust Photo Quality** | 0-100 |
| `28` | **Only Customers On Routes** | 0=Off |
| `39` | **Allow Competitive Items** | 0=Off |
| `54` | **Use Bus Unit ID** | 0=Off |
| `55` | **Auto Export Data** | 0=Off |
| `56` | **Auto Export Data Time** | Time in Minutes |
| `66` | **Customers Operations Time Off** | 0 Not Active, Hours between 0-23 |
| `68` | **Serial Type** | 0: Stander Serials, 1: Serials By Notebook, 2: Serial By Customers Notebook |
| `70` | **Auto Refresh Customer Information** | 0=Off |
| `74` | **Hide Operation Lists** | 0=Off |
| `96` | **Statment Balace Report Class Name** | 1 |
| `98` | **Auto Refresh Time out In seconds** | From 1 To 20 |
| `127` | **Lock All Operation To Import Data** | 0=Off |
| `134` | **Request To Visit Customer Not In Route** | 0=Off |
| `135` | **Waiting Time for Request To Visit Customer Not In Route** | Time in Seconds |
| `140` | **Enable Contracts** | 0=Off |
| `142` | **Must Update Data Every Day** | 0=Off |
| `144` | **Must Visit Customer Route First** | 0=Off |
| `146` | **Import Images On Wifi Only** | 0=Off |
| `165` | **Categories Report Class Name** | 1 |
| `166` | **Show Clear Db Button** | 0=Off |
| `174` | **Enable Prospective Customers** | 0=Off |
| `177` | **Default Cust Info Tab Index** | 0 : Not Active, # |
| `182` | **Use Data From Multi Company** | 0=Off |
| `192` | **Customer Logout Notes** | 0=Off |
| `205` | **Enable Item Replacement** | 0=Off |
| `206` | **Show Info Dialog First** | 0=Off |
| `210` | **Class RPT Item Replacment** | 1 |
| `212` | **Online KPI** | 0=Off |
| `217` | **Enable Accumilative Accont Statment** | 0=Off |
| `229` | **Request To AddNewCustomer** | 0=Off |
| `230` | **Waiting Time for Request To AddNewCustomer** | Time in Seconds |
| `235` | **New Customer Must Take All Photos** | 0=Off |
| `237` | **New Customer Required Fields** | # Field Order In Screen With ; Separated |
| `238` | **Chart Type** | 1=Gauge |
| `243` | **Customer Logout Notes Length** | 0=Off |
| `244` | **Use Items Barcode Scanning Entry** | 0=Off |
| `258` | **NoTransaction Timer Notification** | 0=Off |
| `265` | **Dont Allow Make Multiple Survey For Same Customer** | 0=Off |
| `268` | **Disable Change DashBoard Type** | 0=Off |
| `269` | **Notes Is Required In Voucher** | 0=Off |
| `270` | **Notes Is Required In Voucher Length** | 0=Off |
| `272` | **Virtual Prospective Customer ID** | #= Cust ID |
| `275` | **Lock All Operation After Open Report** | 0=Off |
| `285` | **Get Last Text Answer In Survey** | 0=Off |
| `286` | **Dont Calc Local Collection Amount For Target** | 0=Off |
| `293` | **Use Extra Notes** | 0=Off |
| `295` | **Use All Items Search List** | 0=Off |
| `310` | **POS Service URL** | 0=Off |
| `315` | **Enable Supervisor Reports** | 0=Off |
| `327` | **Hide Financial Info In Customer Info** | 0=Off |
| `332` | **Customer Visit Must Take All Photos** | 0=Off |
| `334` | **Request To Make Transaction for Suspend Customer Approve** | 0=Off |
| `335` | **Waiting Time for Request To Make Transaction for Suspend Customer Approve** | Time in Seconds |
| `339` | **Visit Customer one time per day** | 0=Off |
| `361` | **Route Cust View Type** | 0=By Route |
| `366` | **Use Signs In Transactions** | 0=Off |
| `369` | **Route List Coloring By Cust Class** | 0=Off |
| `372` | **Multi Level Catalog Filter** | 0=Off |
| `373` | **Measure Spec Type** | 1=AT_MOST |
| `376` | **Dont Show All Items if customer not have assigment** | 0=Off |
| `383` | **Use Survey With Customers Link** | 0=Off |
| `396` | **Required Activities In Visit** | 0= Not Active |
| `400` | **Use Internet Status In Action Log** | 0=Off |
| `401` | **Use OneSignal Notifications** | 0=Off |
| `402` | **Use Special Note For Customer In Visit** | 0=Off |
| `414` | **Enable Customer Visit Postpone** | 0=Off |
| `415` | **Use Maintenance Request** | 0=Off |
| `423` | **Use Internal Memo** | 0=Off |
| `424` | **Pass Key Allow Period** | Time in Miniutes |
| `425` | **Use Item Suggest Group Items Type** | 0=Off |
| `428` | **Handel Camera Back Issue Waiting Seconds** | 0=Off |
| `429` | **Handel Symbol In URL** | 0=Off |
| `435` | **Use Planogram** | 0=Off |
| `439` | **Use Wieghted Items Barcode** | 0=Off |
| `440` | **Start Wieghted Items Barcode** | 0=Off |
| `442` | **Request To Link Customer** | 0=Off |
| `443` | **Waiting Time for Request To Link Customer  Approve** | Time in Seconds |
| `448` | **Auto Logout Customer After Finish All Activities** | 0=Off |
| `450` | **Use Online Customer Balance Validation** | 0=Off |
| `452` | **Minimum Vists Duration In Minute** | 0=Off |
| `456` | **Use Colors For Items And Categs Have Target** | 0=Off |
| `457` | **Use Basket Items** | 0=Off |
| `465` | **Use Minimum Collection Target** | 0=Off |
| `467` | **Use Attachment In Transactions** | 0=Off |
| `471` | **Hide Catalog** | 0=Off |
| `473` | **Use Multi Image Type** | 0=Off |
| `479` | **Use Unvisited Route Reason** | 0=Off |
| `485` | **Limitation of Take Photo Count for Customer Galary** | 0=Off |
| `487` | **Update Customer Info with system setting** | 0=Off |
| `493` | **Survey Report Class Name** | 0 |
| `506` | **Use Customers Balance Aging** | 0=Off |
| `509` | **Items Catalog For Available Items Only** | 0=Off |
| `524` | **Use Gap Delivery** | 0=Off |
| `530` | **Edit Customer Required Fields** | # Field Order In Screen With ; Separated |
| `534` | **Use WF Shortcut In OSFA** | 0=Off |
| `538` | **Use Jebrini Round** | 0=Off |
| `541` | **Edit Customer Hide Fields** | # Field Order In Screen With ; Separated |
| `545` | **Scan Cust Barcode Before Save Trans** | 0=Off |
| `546` | **Format Amount With Comma** | 0=Off |
| `548` | **No Full Update In 3G** | 0=Off |
| `557` | **search item multiple textbox** | 0=Offline |
| `563` | **Hide Take Photo** | 0=Off |
| `567` | **Sort Item Categ In Voucher** | 0=Off |
| `569` | **Search Items By Categ dialog** | 0=Off |
| `572` | **Use Multi Customer Type Early Pay Days** | 0=Off |
| `587` | **Only Customers Notes Is Required In Voucher** | 0: Not Active, # Customer Number 1235,5646,568 ...etc |
| `589` | **Olives Server Connection Validate** | 0=Off |
| `600` | **Use Assets Transactions** | 0=Off |
| `606` | **Use Stop Transation** | 0=Off |
| `610` | **Use Items Related To Items** | 0=Off |
| `613` | **Refresh Cust Visit Duration UI** | 0=Off |
| `615` | **Hide Customers List** | 0=Off |
| `629` | **Use Receive Items** | 0=Off |
| `630` | **Customer Issue Amount Report Class Name** | 0 |
| `636` | **Request To Finish All Tasks** | 0=Off |
| `637` | **Waiting Time for Request To Finish All Tasks** | Time in Seconds |
| `639` | **Receive Items  Report Class Name** | 11111111 |
| `640` | **Cust Issue Amount  Report Class Name** | 11111111 |
| `641` | **Journy Summary Report Class Name** | 0 |
| `646` | **Issue Items Report Class Name** | 0 |
| `648` | **Use WIFI Auto Manager** | 0=Off |
| `651` | **Use Concret Delivery** | 0=Off |
| `652` | **Add New Customer To Customer List In Device** | 0=Off |
| `653` | **Disable Start End Journy** | 0=Off |
| `656` | **Use Call Center Report** | 0=Off |
| `657` | **Use Customer Assets** | 0=Off |
| `667` | **WF Exceed Cheuqe DueDate Days Aftrer Deduct Customer Cheuqe Due Day** | 0=Off |
| `673` | **Can't select multiples VisitDays** | 0=Off |
| `676` | **Ge Data Statment of Account Online** | 0=Off |
| `679` | **Disable Catalog Shop Cart** | 0=Off |
| `681` | **Use Item Note In Transaction** | 0=Off |
| `683` | **Default Customer** | Customer No, 0: off |
| `685` | **Waiting Time for Request To Exceed Pay Over Balance** | Time in Seconds |
| `692` | **Use Medical REP** | 0=Off |
| `696` | **Show Stander New Customer Info** | 0=Off |
| `699` | **Enhance Layout For Mobile** | 0=Off |
| `705` | **Sold QuantitiesReport Class Name** | 15 |
| `709` | **Use Data From Multi Company Without Filter Items** | 0=Off |
| `711` | **Validate JSON Object Before Send To Server** | 0=Off |
| `716` | **Use Image List** | 0=Off |
| `730` | **New Prospictive Customer Required Fields** | # Field Order In Screen With ; Separated |
| `731` | **New Prospictive Customer Must Take All Photos** | 0=Off |
| `732` | **Allow edit customer one time only** | 0=Off |
| `738` | **Use Items Group Selection In Trans** | 0=Off |
| `740` | **Hide Select file from Attachment Dialog** | 0=Off |
| `741` | **Enter Notes for no action on auto open activity** | 0=Off |
| `743` | **Enable Calender in POA** | 0=Off |
| `744` | **Show statement of account** | 0=Off |
| `751` | **Customer Visit Must Take All Photos Regardless Time Visit** | 0=Off |
| `754` | **must logout from customer before update data** | 0=Off |
| `757` | **Enable Coaching Report** | 0=Off |
| `758` | **Use Update Customer Data From List** | 0=Off |
| `762` | **Default CustType For  Customers** | No Of Price list |
| `764` | **Hide POA** | No Of Price list |

