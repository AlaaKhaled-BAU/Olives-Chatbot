SQL Documentation

Olives\_BO

|  |  |
| --- | --- |
| Server | 10.0.10.105 |
| Author | OthmanAbuArab |
| Created | Saturday, January 10, 2026 10:29:01 PM |
|  |  |

# Table of Contents

[Table of Contents 2](#_Toc256000000)

[![](data:image/png;base64...) 10.0.10.105 13](#_Toc256000001)

[![](data:image/png;base64...) User databases 15](#_Toc256000002)

[![](data:image/png;base64...) Olives\_­BO Database 16](#_Toc256000003)

[![](data:image/png;base64...) Tables 17](#_Toc256000004)

[![](data:image/png;base64...) [dbo].[Activity­List] 33](#_Toc256000005)

[![](data:image/png;base64...) [dbo].[Add\_­Customer] 34](#_Toc256000006)

[![](data:image/png;base64...) [dbo].[Add­Discount­To­Customer­Orders] 35](#_Toc256000007)

[![](data:image/png;base64...) [dbo].[Assets] 36](#_Toc256000008)

[![](data:image/png;base64...) [dbo].[Assets­Customer­Link] 37](#_Toc256000009)

[![](data:image/png;base64...) [dbo].[Assets­Transactions] 38](#_Toc256000010)

[![](data:image/png;base64...) [dbo].[Assets­Warehouse­Transactions] 40](#_Toc256000011)

[![](data:image/png;base64...) [dbo].[Balad\_­Add\_­Customer\_­Table] 41](#_Toc256000012)

[![](data:image/png;base64...) [dbo].[Bank­Deposit­DF] 42](#_Toc256000013)

[![](data:image/png;base64...) [dbo].[Bank­Deposit­HF] 43](#_Toc256000014)

[![](data:image/png;base64...) [dbo].[Banks] 44](#_Toc256000015)

[![](data:image/png;base64...) [dbo].[Banks­Accounts] 45](#_Toc256000016)

[![](data:image/png;base64...) [dbo].[Batchs­Items­Info] 46](#_Toc256000017)

[![](data:image/png;base64...) [dbo].[Branches] 47](#_Toc256000018)

[![](data:image/png;base64...) [dbo].[Business­Units] 48](#_Toc256000019)

[![](data:image/png;base64...) [dbo].[Car­And­Salesperson­Link] 49](#_Toc256000020)

[![](data:image/png;base64...) [dbo].[Catalog­Media] 50](#_Toc256000021)

[![](data:image/png;base64...) [dbo].[Checks] 51](#_Toc256000022)

[![](data:image/png;base64...) [dbo].[Class­Target­Rate] 53](#_Toc256000023)

[![](data:image/png;base64...) [dbo].[Clients] 54](#_Toc256000024)

[![](data:image/png;base64...) [dbo].[Clients­Active] 55](#_Toc256000025)

[![](data:image/png;base64...) [dbo].[Clients­WFID] 56](#_Toc256000026)

[![](data:image/png;base64...) [dbo].[Companies] 57](#_Toc256000027)

[![](data:image/png;base64...) [dbo].[Company­Branches] 59](#_Toc256000028)

[![](data:image/png;base64...) [dbo].[Company­Parameters] 60](#_Toc256000029)

[![](data:image/png;base64...) [dbo].[Competitive­Items] 64](#_Toc256000030)

[![](data:image/png;base64...) [dbo].[Competitve­Items­Data­DF] 65](#_Toc256000031)

[![](data:image/png;base64...) [dbo].[Competitve­Items­Data­HF] 66](#_Toc256000032)

[![](data:image/png;base64...) [dbo].[Contract­Items] 67](#_Toc256000033)

[![](data:image/png;base64...) [dbo].[Contracts] 68](#_Toc256000034)

[![](data:image/png;base64...) [dbo].[Coupons­Books­Details] 69](#_Toc256000035)

[![](data:image/png;base64...) [dbo].[Coupons­Books­Headers] 70](#_Toc256000036)

[![](data:image/png;base64...) [dbo].[Currencies] 71](#_Toc256000037)

[![](data:image/png;base64...) [dbo].[Currencies­Denominations] 72](#_Toc256000038)

[![](data:image/png;base64...) [dbo].[Currencies­Rate] 73](#_Toc256000039)

[![](data:image/png;base64...) [dbo].[Customer­Chq­List] 74](#_Toc256000040)

[![](data:image/png;base64...) [dbo].[Customer­Class­Targets] 75](#_Toc256000041)

[![](data:image/png;base64...) [dbo].[Customer­Class­Targets­Details] 76](#_Toc256000042)

[![](data:image/png;base64...) [dbo].[Customer­Data\_­Sample] 77](#_Toc256000043)

[![](data:image/png;base64...) [dbo].[Customer­Login­Actions] 78](#_Toc256000044)

[![](data:image/png;base64...) [dbo].[Customer­Paid­Trans\_­Form­ERP] 79](#_Toc256000045)

[![](data:image/png;base64...) [dbo].[Customer­Phone] 80](#_Toc256000046)

[![](data:image/png;base64...) [dbo].[Customer­Receivables­Info] 81](#_Toc256000047)

[![](data:image/png;base64...) [dbo].[Customers] 82](#_Toc256000048)

[![](data:image/png;base64...) [dbo].[Customers2] 85](#_Toc256000049)

[![](data:image/png;base64...) [dbo].[Customer­Sales­By­Category] 86](#_Toc256000050)

[![](data:image/png;base64...) [dbo].[Customers­Balance­Aging] 87](#_Toc256000051)

[![](data:image/png;base64...) [dbo].[Customers­Balance­Aging\_­Inmaa] 88](#_Toc256000052)

[![](data:image/png;base64...) [dbo].[Customers­Bonus­Types­Link] 89](#_Toc256000053)

[![](data:image/png;base64...) [dbo].[Customers­Classes] 90](#_Toc256000054)

[![](data:image/png;base64...) [dbo].[Customers­Contact­Persons] 91](#_Toc256000055)

[![](data:image/png;base64...) [dbo].[Customers­Contact­Persons­Link] 92](#_Toc256000056)

[![](data:image/png;base64...) [dbo].[Customers­Financial­Details] 93](#_Toc256000057)

[![](data:image/png;base64...) [dbo].[Customers­Financial­Details\_­Old] 96](#_Toc256000058)

[![](data:image/png;base64...) [dbo].[Customers­Financial­Details2] 98](#_Toc256000059)

[![](data:image/png;base64...) [dbo].[Customers­GPSLocations] 100](#_Toc256000060)

[![](data:image/png;base64...) [dbo].[Customers­Groups] 101](#_Toc256000061)

[![](data:image/png;base64...) [dbo].[Customers­Item­Qty­Limit] 102](#_Toc256000062)

[![](data:image/png;base64...) [dbo].[Customers­Items­Assigment] 103](#_Toc256000063)

[![](data:image/png;base64...) [dbo].[Customers­Items­Log] 104](#_Toc256000064)

[![](data:image/png;base64...) [dbo].[Customers­Log] 105](#_Toc256000065)

[![](data:image/png;base64...) [dbo].[Customers­Monthly­Collection­Target] 106](#_Toc256000066)

[![](data:image/png;base64...) [dbo].[Customers­Paid­Trans­List] 107](#_Toc256000067)

[![](data:image/png;base64...) [dbo].[Customers­Payment­Types­Link] 108](#_Toc256000068)

[![](data:image/png;base64...) [dbo].[Customers­Promotions­Exceptions] 109](#_Toc256000069)

[![](data:image/png;base64...) [dbo].[Customers­Promotions­Groups] 110](#_Toc256000070)

[![](data:image/png;base64...) [dbo].[Customers­Promotions­Groups­Link] 111](#_Toc256000071)

[![](data:image/png;base64...) [dbo].[Customers­Return­Item­Qty­Limit] 112](#_Toc256000072)

[![](data:image/png;base64...) [dbo].[Customers­Sales­From0to­Max] 113](#_Toc256000073)

[![](data:image/png;base64...) [dbo].[Customer­Statment­Of­Account] 114](#_Toc256000074)

[![](data:image/png;base64...) [dbo].[Customer­Stock­Tacking] 115](#_Toc256000075)

[![](data:image/png;base64...) [dbo].[Customer­Stock­Tacking­Details] 117](#_Toc256000076)

[![](data:image/png;base64...) [dbo].[Customers­Types] 118](#_Toc256000077)

[![](data:image/png;base64...) [dbo].[Customers­Visit­Activity] 119](#_Toc256000078)

[![](data:image/png;base64...) [dbo].[Customers­WFFunctions­Auto­Approve] 120](#_Toc256000079)

[![](data:image/png;base64...) [dbo].[Customer­Targets] 121](#_Toc256000080)

[![](data:image/png;base64...) [dbo].[Customer­Targets­Details] 122](#_Toc256000081)

[![](data:image/png;base64...) [dbo].[Customer­Type­Early­Pay­Days] 123](#_Toc256000082)

[![](data:image/png;base64...) [dbo].[Customer­Type­Targets] 124](#_Toc256000083)

[![](data:image/png;base64...) [dbo].[Customer­Type­Targets­Details] 125](#_Toc256000084)

[![](data:image/png;base64...) [dbo].[Daily­Procedures] 126](#_Toc256000085)

[![](data:image/png;base64...) [dbo].[Debit­Credit­Note­Trans] 127](#_Toc256000086)

[![](data:image/png;base64...) [dbo].[Delivery­Cars] 128](#_Toc256000087)

[![](data:image/png;base64...) [dbo].[Delivery­Manifest] 129](#_Toc256000088)

[![](data:image/png;base64...) [dbo].[Delivery­Prova­D] 130](#_Toc256000089)

[![](data:image/png;base64...) [dbo].[Delivery­Prova­H] 131](#_Toc256000090)

[![](data:image/png;base64...) [dbo].[Delivery­Route] 132](#_Toc256000091)

[![](data:image/png;base64...) [dbo].[Device­Reports­List] 133](#_Toc256000092)

[![](data:image/png;base64...) [dbo].[Devices­Info] 134](#_Toc256000093)

[![](data:image/png;base64...) [dbo].[Discount­Early­Pay­By­Invoice­Ref] 135](#_Toc256000094)

[![](data:image/png;base64...) [dbo].[Documents­Types] 136](#_Toc256000095)

[![](data:image/png;base64...) [dbo].[DR\_­Dynamic­Reports] 137](#_Toc256000096)

[![](data:image/png;base64...) [dbo].[DR\_­Dynamic­Reports­Dictionary] 138](#_Toc256000097)

[![](data:image/png;base64...) [dbo].[DR\_­Dynamic­Reports­Parameters] 139](#_Toc256000098)

[![](data:image/png;base64...) [dbo].[Drawers] 140](#_Toc256000099)

[![](data:image/png;base64...) [dbo].[Efawateercom­Payment] 141](#_Toc256000100)

[![](data:image/png;base64...) [dbo].[Emp­Details] 142](#_Toc256000101)

[![](data:image/png;base64...) [dbo].[ERPStores] 143](#_Toc256000102)

[![](data:image/png;base64...) [dbo].[ERPStores­Items­Link] 144](#_Toc256000103)

[![](data:image/png;base64...) [dbo].[Error­Log] 145](#_Toc256000104)

[![](data:image/png;base64...) [dbo].[Excel] 146](#_Toc256000105)

[![](data:image/png;base64...) [dbo].[Excel2] 147](#_Toc256000106)

[![](data:image/png;base64...) [dbo].[Excel­Reports] 148](#_Toc256000107)

[![](data:image/png;base64...) [dbo].[forupdateonly] 149](#_Toc256000108)

[![](data:image/png;base64...) [dbo].[Gap­Tags] 150](#_Toc256000109)

[![](data:image/png;base64...) [dbo].[Gap­Trans­Headers] 151](#_Toc256000110)

[![](data:image/png;base64...) [dbo].[Gap­Trans­Tags] 152](#_Toc256000111)

[![](data:image/png;base64...) [dbo].[Gap­Trans­Time­Line] 153](#_Toc256000112)

[![](data:image/png;base64...) [dbo].[Groups­Menu] 154](#_Toc256000113)

[![](data:image/png;base64...) [dbo].[Image­Types] 155](#_Toc256000114)

[![](data:image/png;base64...) [dbo].[Integration­Error­Log] 156](#_Toc256000115)

[![](data:image/png;base64...) [dbo].[Integration­Posted­Transactions] 157](#_Toc256000116)

[![](data:image/png;base64...) [dbo].[Intenal­Memo­Approve] 158](#_Toc256000117)

[![](data:image/png;base64...) [dbo].[Internal­Memo] 159](#_Toc256000118)

[![](data:image/png;base64...) [dbo].[Invoice­Delivery­DF] 160](#_Toc256000119)

[![](data:image/png;base64...) [dbo].[Invoice­Delivery­HF] 161](#_Toc256000120)

[![](data:image/png;base64...) [dbo].[Invoice­History­DF] 163](#_Toc256000121)

[![](data:image/png;base64...) [dbo].[Invoice­History­HF] 164](#_Toc256000122)

[![](data:image/png;base64...) [dbo].[Invoice­Return­Link] 165](#_Toc256000123)

[![](data:image/png;base64...) [dbo].[Issue­Items­Details] 166](#_Toc256000124)

[![](data:image/png;base64...) [dbo].[Issue­Items­Headers] 168](#_Toc256000125)

[![](data:image/png;base64...) [dbo].[Items] 171](#_Toc256000126)

[![](data:image/png;base64...) [dbo].[Items­Barcodes] 174](#_Toc256000127)

[![](data:image/png;base64...) [dbo].[Items­Categories] 175](#_Toc256000128)

[![](data:image/png;base64...) [dbo].[Items­Categ­Stock­Details] 176](#_Toc256000129)

[![](data:image/png;base64...) [dbo].[Items­Categ­Stock­Header] 177](#_Toc256000130)

[![](data:image/png;base64...) [dbo].[Items­Classes] 178](#_Toc256000131)

[![](data:image/png;base64...) [dbo].[Items­Group­Bonus­Target] 179](#_Toc256000132)

[![](data:image/png;base64...) [dbo].[Items­Groups] 180](#_Toc256000133)

[![](data:image/png;base64...) [dbo].[Items­Inventory] 181](#_Toc256000134)

[![](data:image/png;base64...) [dbo].[Items­Minimum­Sales] 182](#_Toc256000135)

[![](data:image/png;base64...) [dbo].[Items­Price­Exceptions] 183](#_Toc256000136)

[![](data:image/png;base64...) [dbo].[Items­Priority] 185](#_Toc256000137)

[![](data:image/png;base64...) [dbo].[Items­Related­To­Items] 186](#_Toc256000138)

[![](data:image/png;base64...) [dbo].[Items­Replacement­Details] 187](#_Toc256000139)

[![](data:image/png;base64...) [dbo].[Items­Replacement­Groups] 188](#_Toc256000140)

[![](data:image/png;base64...) [dbo].[Items­Replacement­Headers] 189](#_Toc256000141)

[![](data:image/png;base64...) [dbo].[Items­Suggest­Group] 191](#_Toc256000142)

[![](data:image/png;base64...) [dbo].[Items­Suggest­Group­Link] 192](#_Toc256000143)

[![](data:image/png;base64...) [dbo].[Items­Suggest­Group­Link­With­Items] 193](#_Toc256000144)

[![](data:image/png;base64...) [dbo].[Items­Units] 194](#_Toc256000145)

[![](data:image/png;base64...) [dbo].[Items­Units­Details] 195](#_Toc256000146)

[![](data:image/png;base64...) [dbo].[Items­Units­Details\_1] 196](#_Toc256000147)

[![](data:image/png;base64...) [dbo].[Jo­Tax­Result] 197](#_Toc256000148)

[![](data:image/png;base64...) [dbo].[JOTax­Settings] 198](#_Toc256000149)

[![](data:image/png;base64...) [dbo].[JSONData­Log] 199](#_Toc256000150)

[![](data:image/png;base64...) [dbo].[Kasih­Survey] 200](#_Toc256000151)

[![](data:image/png;base64...) [dbo].[Language] 202](#_Toc256000152)

[![](data:image/png;base64...) [dbo].[Language­Dictionary] 203](#_Toc256000153)

[![](data:image/png;base64...) [dbo].[Locations] 204](#_Toc256000154)

[![](data:image/png;base64...) [dbo].[Location­Targets] 205](#_Toc256000155)

[![](data:image/png;base64...) [dbo].[Location­Targets­Details] 206](#_Toc256000156)

[![](data:image/png;base64...) [dbo].[Log­Actions] 207](#_Toc256000157)

[![](data:image/png;base64...) [dbo].[Log­Action­Transaction] 208](#_Toc256000158)

[![](data:image/png;base64...) [dbo].[Log­Action­Transaction\_] 210](#_Toc256000159)

[![](data:image/png;base64...) [dbo].[Maintinance­Orders] 212](#_Toc256000160)

[![](data:image/png;base64...) [dbo].[Maintinance­Orders­Approve] 214](#_Toc256000161)

[![](data:image/png;base64...) [dbo].[MAZ\_­Route\_­EMAIL\_­Final] 215](#_Toc256000162)

[![](data:image/png;base64...) [dbo].[Menu] 216](#_Toc256000163)

[![](data:image/png;base64...) [dbo].[MIMETypes] 217](#_Toc256000164)

[![](data:image/png;base64...) [dbo].[MMS\_­Assistants] 218](#_Toc256000165)

[![](data:image/png;base64...) [dbo].[MMS\_­Close­Order­Reasons] 219](#_Toc256000166)

[![](data:image/png;base64...) [dbo].[MMS\_­Devices­Info] 220](#_Toc256000167)

[![](data:image/png;base64...) [dbo].[MMS\_­Diagnostic] 221](#_Toc256000168)

[![](data:image/png;base64...) [dbo].[MMS\_­DV\_­Error­Log] 222](#_Toc256000169)

[![](data:image/png;base64...) [dbo].[MMS\_­Invoice­Details] 223](#_Toc256000170)

[![](data:image/png;base64...) [dbo].[MMS\_­Invoices­Headers] 224](#_Toc256000171)

[![](data:image/png;base64...) [dbo].[MMS\_­Items] 225](#_Toc256000172)

[![](data:image/png;base64...) [dbo].[MMS\_­Items­Categories] 226](#_Toc256000173)

[![](data:image/png;base64...) [dbo].[MMS\_­Link\_­Device\_­Diagnostic] 227](#_Toc256000174)

[![](data:image/png;base64...) [dbo].[MMS\_­Link\_­Device\_­Items] 228](#_Toc256000175)

[![](data:image/png;base64...) [dbo].[MMS\_­Link\_­Supervisor\_­Maintenance­Unit] 229](#_Toc256000176)

[![](data:image/png;base64...) [dbo].[MMS\_­Link\_­Supervisor\_­Technician] 230](#_Toc256000177)

[![](data:image/png;base64...) [dbo].[MMS\_­Link\_­Technician\_­Assistant] 231](#_Toc256000178)

[![](data:image/png;base64...) [dbo].[MMS\_­Maintenance­Technician] 232](#_Toc256000179)

[![](data:image/png;base64...) [dbo].[MMS\_­Maintenance­Technician\_­Items­Balance] 233](#_Toc256000180)

[![](data:image/png;base64...) [dbo].[MMS\_­Maintenance­Technician­Permissions] 234](#_Toc256000181)

[![](data:image/png;base64...) [dbo].[MMS\_­Maintenance­Technician­Permissions\_­Def] 235](#_Toc256000182)

[![](data:image/png;base64...) [dbo].[MMS\_­Maintenance­Technician­Trans­Serials] 236](#_Toc256000183)

[![](data:image/png;base64...) [dbo].[MMS\_­Maintenance­Unit] 237](#_Toc256000184)

[![](data:image/png;base64...) [dbo].[MMS\_­Order­Details] 238](#_Toc256000185)

[![](data:image/png;base64...) [dbo].[MMS\_­Orders­Header] 239](#_Toc256000186)

[![](data:image/png;base64...) [dbo].[MMS\_­Order­Status] 240](#_Toc256000187)

[![](data:image/png;base64...) [dbo].[MMS\_­Order­Types] 241](#_Toc256000188)

[![](data:image/png;base64...) [dbo].[MMS\_­Order­Visit­Details] 242](#_Toc256000189)

[![](data:image/png;base64...) [dbo].[MMS\_­Order­Visit­Images] 243](#_Toc256000190)

[![](data:image/png;base64...) [dbo].[MMS\_­Order­Visits] 244](#_Toc256000191)

[![](data:image/png;base64...) [dbo].[MMS\_­Payments­Checks­Details] 247](#_Toc256000192)

[![](data:image/png;base64...) [dbo].[MMS\_­Payments­Header] 248](#_Toc256000193)

[![](data:image/png;base64...) [dbo].[MMS\_­Reporters] 249](#_Toc256000194)

[![](data:image/png;base64...) [dbo].[MMS\_­Schedule­Support­Visits] 250](#_Toc256000195)

[![](data:image/png;base64...) [dbo].[MMS\_­Schedule­Support­Visits\_­Log] 251](#_Toc256000196)

[![](data:image/png;base64...) [dbo].[MMS\_­Show­Rooms] 252](#_Toc256000197)

[![](data:image/png;base64...) [dbo].[MMS\_­Supervisors] 253](#_Toc256000198)

[![](data:image/png;base64...) [dbo].[MMS\_­System­Codes] 254](#_Toc256000199)

[![](data:image/png;base64...) [dbo].[MMS\_­System­Settings] 255](#_Toc256000200)

[![](data:image/png;base64...) [dbo].[MMS\_­Tax­Type] 256](#_Toc256000201)

[![](data:image/png;base64...) [dbo].[Mobile­Version­Salesmen] 257](#_Toc256000202)

[![](data:image/png;base64...) [dbo].[Multi­Targets] 258](#_Toc256000203)

[![](data:image/png;base64...) [dbo].[Nairoukh\_­Awtar\_­Salespersons­Exemptions] 259](#_Toc256000204)

[![](data:image/png;base64...) [dbo].[Nairoukh­Route­Customers­Position­Change] 260](#_Toc256000205)

[![](data:image/png;base64...) [dbo].[New­Competitive­Items] 261](#_Toc256000206)

[![](data:image/png;base64...) [dbo].[New­Customer­Default­Value] 262](#_Toc256000207)

[![](data:image/png;base64...) [dbo].[New­Customer­Special­Fields\_­Def] 263](#_Toc256000208)

[![](data:image/png;base64...) [dbo].[Notifications] 264](#_Toc256000209)

[![](data:image/png;base64...) [dbo].[No­Transactions­Log] 265](#_Toc256000210)

[![](data:image/png;base64...) [dbo].[No­Transactions­Reasons] 266](#_Toc256000211)

[![](data:image/png;base64...) [dbo].[Olives­Menu] 267](#_Toc256000212)

[![](data:image/png;base64...) [dbo].[Olives­Pages] 268](#_Toc256000213)

[![](data:image/png;base64...) [dbo].[Olives­User­Permissions] 269](#_Toc256000214)

[![](data:image/png;base64...) [dbo].[OLV\_­PDC] 270](#_Toc256000215)

[![](data:image/png;base64...) [dbo].[Orders­Delivery­Details] 271](#_Toc256000216)

[![](data:image/png;base64...) [dbo].[Orders­Delivery­Info] 273](#_Toc256000217)

[![](data:image/png;base64...) [dbo].[Orders­Details] 274](#_Toc256000218)

[![](data:image/png;base64...) [dbo].[Orders­Details\_­Log] 277](#_Toc256000219)

[![](data:image/png;base64...) [dbo].[Orders­Headers] 278](#_Toc256000220)

[![](data:image/png;base64...) [dbo].[OT\_­Send­Log] 281](#_Toc256000221)

[![](data:image/png;base64...) [dbo].[OWGM\_­Gates] 282](#_Toc256000222)

[![](data:image/png;base64...) [dbo].[OWGM\_­Gates­Users] 283](#_Toc256000223)

[![](data:image/png;base64...) [dbo].[OWGM\_­Lock­Log] 284](#_Toc256000224)

[![](data:image/png;base64...) [dbo].[OWGM\_­Transactions] 285](#_Toc256000225)

[![](data:image/png;base64...) [dbo].[Payments­Orders] 286](#_Toc256000226)

[![](data:image/png;base64...) [dbo].[Payments­Types] 288](#_Toc256000227)

[![](data:image/png;base64...) [dbo].[Pending­Invoices] 289](#_Toc256000228)

[![](data:image/png;base64...) [dbo].[Pending­Orders­Details] 290](#_Toc256000229)

[![](data:image/png;base64...) [dbo].[Pending­Orders­Headers] 291](#_Toc256000230)

[![](data:image/png;base64...) [dbo].[Planogram­Media] 292](#_Toc256000231)

[![](data:image/png;base64...) [dbo].[Planogram­Media­Customers­Link] 293](#_Toc256000232)

[![](data:image/png;base64...) [dbo].[POADetails] 294](#_Toc256000233)

[![](data:image/png;base64...) [dbo].[POAHeader] 295](#_Toc256000234)

[![](data:image/png;base64...) [dbo].[Pos\_­Invoice­Order­HF] 296](#_Toc256000235)

[![](data:image/png;base64...) [dbo].[Positions] 298](#_Toc256000236)

[![](data:image/png;base64...) [dbo].[Price­List­Details] 299](#_Toc256000237)

[![](data:image/png;base64...) [dbo].[Price­List­Details­From­GCI] 301](#_Toc256000238)

[![](data:image/png;base64...) [dbo].[Price­List­Qty­Ranges] 302](#_Toc256000239)

[![](data:image/png;base64...) [dbo].[Price­Lists] 303](#_Toc256000240)

[![](data:image/png;base64...) [dbo].[Procedure­Change­Log] 304](#_Toc256000241)

[![](data:image/png;base64...) [dbo].[Promotion­Budget] 305](#_Toc256000242)

[![](data:image/png;base64...) [dbo].[Promotion­Classes] 306](#_Toc256000243)

[![](data:image/png;base64...) [dbo].[Promotion­Item­Groups] 307](#_Toc256000244)

[![](data:image/png;base64...) [dbo].[Promotions­Approval­Log] 308](#_Toc256000245)

[![](data:image/png;base64...) [dbo].[Promotions­Approval­Setup] 309](#_Toc256000246)

[![](data:image/png;base64...) [dbo].[Promotions­Cond­Un­Cod­Input] 310](#_Toc256000247)

[![](data:image/png;base64...) [dbo].[Promotions­Cond­Un­Cod­Output] 311](#_Toc256000248)

[![](data:image/png;base64...) [dbo].[Promotions­Customers­Groups­Link] 312](#_Toc256000249)

[![](data:image/png;base64...) [dbo].[Promotions­Dont­Apply] 313](#_Toc256000250)

[![](data:image/png;base64...) [dbo].[Promotion­Selection­Groups] 314](#_Toc256000251)

[![](data:image/png;base64...) [dbo].[Promotion­Selection­Groups­Link] 315](#_Toc256000252)

[![](data:image/png;base64...) [dbo].[Promotions­Headers] 316](#_Toc256000253)

[![](data:image/png;base64...) [dbo].[Promotions­Priorities] 318](#_Toc256000254)

[![](data:image/png;base64...) [dbo].[Promotions­Priorities­Link] 319](#_Toc256000255)

[![](data:image/png;base64...) [dbo].[Promotions­Range­Input] 320](#_Toc256000256)

[![](data:image/png;base64...) [dbo].[Promotions­Salesman­Groups­Link] 321](#_Toc256000257)

[![](data:image/png;base64...) [dbo].[Promotion­Types] 322](#_Toc256000258)

[![](data:image/png;base64...) [dbo].[Prompt­Embeddings] 323](#_Toc256000259)

[![](data:image/png;base64...) [dbo].[Prospective­Customers] 324](#_Toc256000260)

[![](data:image/png;base64...) [dbo].[Prosto­Soft­Accounts] 326](#_Toc256000261)

[![](data:image/png;base64...) [dbo].[Receipt­Requests] 327](#_Toc256000262)

[![](data:image/png;base64...) [dbo].[Receipt­Requests­Invoices­Link] 328](#_Toc256000263)

[![](data:image/png;base64...) [dbo].[Receipt­Requests­Schedule] 329](#_Toc256000264)

[![](data:image/png;base64...) [dbo].[Receipts] 330](#_Toc256000265)

[![](data:image/png;base64...) [dbo].[Receipts\_­Branches] 333](#_Toc256000266)

[![](data:image/png;base64...) [dbo].[Receipts\_­Currency] 334](#_Toc256000267)

[![](data:image/png;base64...) [dbo].[Receipts\_­Paid­Trans] 335](#_Toc256000268)

[![](data:image/png;base64...) [dbo].[Receipts\_­Paid­Trans­Checks] 336](#_Toc256000269)

[![](data:image/png;base64...) [dbo].[Rec­Link­Inv] 337](#_Toc256000270)

[![](data:image/png;base64...) [dbo].[Report5Customers­Excemptions] 338](#_Toc256000271)

[![](data:image/png;base64...) [dbo].[Reprinted­Transactions] 339](#_Toc256000272)

[![](data:image/png;base64...) [dbo].[Reprint­Reasons] 340](#_Toc256000273)

[![](data:image/png;base64...) [dbo].[Request­Salesman­No­Transaction] 341](#_Toc256000274)

[![](data:image/png;base64...) [dbo].[Request­Salesman­Will­Not­Visit] 342](#_Toc256000275)

[![](data:image/png;base64...) [dbo].[Request­To­Add­Discount] 343](#_Toc256000276)

[![](data:image/png;base64...) [dbo].[Request­To­Add­Discount­In­Order] 344](#_Toc256000277)

[![](data:image/png;base64...) [dbo].[Request­To­Add­Drawer] 345](#_Toc256000278)

[![](data:image/png;base64...) [dbo].[Request­To­Add­Extra­Bonus] 346](#_Toc256000279)

[![](data:image/png;base64...) [dbo].[Request­To­Add­Extra­Bonus­And­Discount] 347](#_Toc256000280)

[![](data:image/png;base64...) [dbo].[Request­To­Add­New­Customer] 348](#_Toc256000281)

[![](data:image/png;base64...) [dbo].[Request­To­Allow­Take­Checks­From­Customer] 349](#_Toc256000282)

[![](data:image/png;base64...) [dbo].[Request­To­Approve­Promotion] 350](#_Toc256000283)

[![](data:image/png;base64...) [dbo].[Request­To­Approve­Promotion­Details] 351](#_Toc256000284)

[![](data:image/png;base64...) [dbo].[Request­To­Cancel­Payment] 352](#_Toc256000285)

[![](data:image/png;base64...) [dbo].[Request­To­Change­Delivery­Payment­Type] 353](#_Toc256000286)

[![](data:image/png;base64...) [dbo].[Request­To­Change­Invoice­Payment­Type] 354](#_Toc256000287)

[![](data:image/png;base64...) [dbo].[Request­To­Change­Item­Sell­Price] 355](#_Toc256000288)

[![](data:image/png;base64...) [dbo].[Request­To­Exceed­Check­Due­Date] 356](#_Toc256000289)

[![](data:image/png;base64...) [dbo].[Request­To­Exceed­Chq­Limit] 357](#_Toc256000290)

[![](data:image/png;base64...) [dbo].[Request­To­Exceed­Customer­Credit­Limit] 358](#_Toc256000291)

[![](data:image/png;base64...) [dbo].[Request­To­Exceed­Customer­Credit­Limit­In­Order] 359](#_Toc256000292)

[![](data:image/png;base64...) [dbo].[Request­To­Exceed­Customer­Invoice­Due­Days] 360](#_Toc256000293)

[![](data:image/png;base64...) [dbo].[Request­To­Exceed­Customer­Invoice­Due­Days­In­Order] 361](#_Toc256000294)

[![](data:image/png;base64...) [dbo].[Request­To­Exceed­Customer­Visit­Order] 362](#_Toc256000295)

[![](data:image/png;base64...) [dbo].[Request­To­Exceed­Finish­All­Tasks] 363](#_Toc256000296)

[![](data:image/png;base64...) [dbo].[Request­To­Exceed­Invoice­Amount] 364](#_Toc256000297)

[![](data:image/png;base64...) [dbo].[Request­To­Exceed­Invoice­Count] 365](#_Toc256000298)

[![](data:image/png;base64...) [dbo].[Request­To­Exceed­Pay­Invoice­Discount] 366](#_Toc256000299)

[![](data:image/png;base64...) [dbo].[Request­To­Exceed­Pay­Over­Balance] 367](#_Toc256000300)

[![](data:image/png;base64...) [dbo].[Request­To­Exceed­Salesman­Credit­Limit] 368](#_Toc256000301)

[![](data:image/png;base64...) [dbo].[Request­To­Increase­Customer­Creditlimit] 369](#_Toc256000302)

[![](data:image/png;base64...) [dbo].[Request­To­Link­Customer­To­Salesman] 370](#_Toc256000303)

[![](data:image/png;base64...) [dbo].[Request­To­Login­To­Customer­Without­Verficiation] 371](#_Toc256000304)

[![](data:image/png;base64...) [dbo].[Request­To­Make­Transaction­To­Suspended­Customer] 372](#_Toc256000305)

[![](data:image/png;base64...) [dbo].[Request­To­Make­Zero­Amount­Invoice] 373](#_Toc256000306)

[![](data:image/png;base64...) [dbo].[Request­To­Return­Invoice] 374](#_Toc256000307)

[![](data:image/png;base64...) [dbo].[Request­To­Visit­Customer­Not­In­Route] 375](#_Toc256000308)

[![](data:image/png;base64...) [dbo].[Request­To­Void­Transaction] 376](#_Toc256000309)

[![](data:image/png;base64...) [dbo].[Return­Orders­Details] 377](#_Toc256000310)

[![](data:image/png;base64...) [dbo].[Return­Orders­Headers] 379](#_Toc256000311)

[![](data:image/png;base64...) [dbo].[Routes­Information] 382](#_Toc256000312)

[![](data:image/png;base64...) [dbo].[Sales­Acheivment­Grades] 383](#_Toc256000313)

[![](data:image/png;base64...) [dbo].[Salesman­Cash­Settlement] 384](#_Toc256000314)

[![](data:image/png;base64...) [dbo].[Sales­Order­Delivery­DF] 385](#_Toc256000315)

[![](data:image/png;base64...) [dbo].[Sales­Order­Delivery­HF] 387](#_Toc256000316)

[![](data:image/png;base64...) [dbo].[Sales­Order­History­DF] 388](#_Toc256000317)

[![](data:image/png;base64...) [dbo].[Sales­Order­History­HF] 390](#_Toc256000318)

[![](data:image/png;base64...) [dbo].[Sales­Person­Bonus­Limit] 391](#_Toc256000319)

[![](data:image/png;base64...) [dbo].[Salesperson­Class­Target] 392](#_Toc256000320)

[![](data:image/png;base64...) [dbo].[Sales­Person­Collections­Targets] 393](#_Toc256000321)

[![](data:image/png;base64...) [dbo].[Sales­Person­Contracts­Assignment] 394](#_Toc256000322)

[![](data:image/png;base64...) [dbo].[Sales­Person­Customer­Count­Targets­DF] 395](#_Toc256000323)

[![](data:image/png;base64...) [dbo].[Sales­Person­Customer­Count­Targets­HF] 396](#_Toc256000324)

[![](data:image/png;base64...) [dbo].[Salesperson­Customers­Visits­By­Date] 397](#_Toc256000325)

[![](data:image/png;base64...) [dbo].[Salesperson­Cust­Stock­Items­Assignment] 398](#_Toc256000326)

[![](data:image/png;base64...) [dbo].[Salesperson­Cust­Stock­Items­Target­Link] 399](#_Toc256000327)

[![](data:image/png;base64...) [dbo].[Sales­Person­Group­Item­Bonus­Target] 400](#_Toc256000328)

[![](data:image/png;base64...) [dbo].[Sales­Person­Group­Item­Qty­Limit] 402](#_Toc256000329)

[![](data:image/png;base64...) [dbo].[Sales­Person­Item­Bonus­Target] 403](#_Toc256000330)

[![](data:image/png;base64...) [dbo].[Sales­Person­Item­Bonus­Target­By­Customer] 405](#_Toc256000331)

[![](data:image/png;base64...) [dbo].[Sales­Person­Items­Assignment] 406](#_Toc256000332)

[![](data:image/png;base64...) [dbo].[Sales­Person­Items­Balance] 407](#_Toc256000333)

[![](data:image/png;base64...) [dbo].[Sales­Person­Items­Balance­Batches] 408](#_Toc256000334)

[![](data:image/png;base64...) [dbo].[Sales­Person­Items­Sales­Units] 409](#_Toc256000335)

[![](data:image/png;base64...) [dbo].[Sales­Person­Items­Use­In­Load­Order] 410](#_Toc256000336)

[![](data:image/png;base64...) [dbo].[Sales­Person­New­Customers­Targets] 411](#_Toc256000337)

[![](data:image/png;base64...) [dbo].[Sales­Person­Notbook­Transactions­Serials] 412](#_Toc256000338)

[![](data:image/png;base64...) [dbo].[Salesperson­Route­By­Date] 413](#_Toc256000339)

[![](data:image/png;base64...) [dbo].[Sales­Persons] 414](#_Toc256000340)

[![](data:image/png;base64...) [dbo].[Sales­Persons­Additional­Routes] 417](#_Toc256000341)

[![](data:image/png;base64...) [dbo].[Salespersons­Assistants] 418](#_Toc256000342)

[![](data:image/png;base64...) [dbo].[Salespersons­Assistants­Transactions] 419](#_Toc256000343)

[![](data:image/png;base64...) [dbo].[Salespersons­Daily­Currency­Totals] 420](#_Toc256000344)

[![](data:image/png;base64...) [dbo].[Sales­Persons­Device­Permissions] 421](#_Toc256000345)

[![](data:image/png;base64...) [dbo].[Sales­Persons­Device­Reports­Permissions] 424](#_Toc256000346)

[![](data:image/png;base64...) [dbo].[Sales­Persons­Discount­Early­Pay­Discount] 425](#_Toc256000347)

[![](data:image/png;base64...) [dbo].[Salespersons­GPSTracking] 426](#_Toc256000348)

[![](data:image/png;base64...) [dbo].[Sales­Persons­Groups] 427](#_Toc256000349)

[![](data:image/png;base64...) [dbo].[Sales­Persons­Items­Groups] 428](#_Toc256000350)

[![](data:image/png;base64...) [dbo].[Salespersons­Messages] 429](#_Toc256000351)

[![](data:image/png;base64...) [dbo].[Salespersons­Messages­Definition] 430](#_Toc256000352)

[![](data:image/png;base64...) [dbo].[Sales­Person­Special­Targets] 431](#_Toc256000353)

[![](data:image/png;base64...) [dbo].[Salespersons­Procedures] 432](#_Toc256000354)

[![](data:image/png;base64...) [dbo].[Sales­Persons­Routes] 433](#_Toc256000355)

[![](data:image/png;base64...) [dbo].[Salespersons­Security] 434](#_Toc256000356)

[![](data:image/png;base64...) [dbo].[Salespersons­Send­Orders] 435](#_Toc256000357)

[![](data:image/png;base64...) [dbo].[Sales­Person­Stock­Tacking] 436](#_Toc256000358)

[![](data:image/png;base64...) [dbo].[Sales­Person­Stock­Tacking­Details] 438](#_Toc256000359)

[![](data:image/png;base64...) [dbo].[Salesperson­Target­Reference­Focus­Item] 439](#_Toc256000360)

[![](data:image/png;base64...) [dbo].[Sales­Person­Targets] 440](#_Toc256000361)

[![](data:image/png;base64...) [dbo].[Sales­Person­Targets­Details] 442](#_Toc256000362)

[![](data:image/png;base64...) [dbo].[Sales­Person­Targets­Off­Days] 444](#_Toc256000363)

[![](data:image/png;base64...) [dbo].[Sales­Person­Transactions­Serials] 445](#_Toc256000364)

[![](data:image/png;base64...) [dbo].[Sales­Person­Transactions­Serials­Multi] 447](#_Toc256000365)

[![](data:image/png;base64...) [dbo].[Sales­Quotation­Details] 449](#_Toc256000366)

[![](data:image/png;base64...) [dbo].[Sales­Quotation­Headers] 451](#_Toc256000367)

[![](data:image/png;base64...) [dbo].[Sales­Trans­Details] 453](#_Toc256000368)

[![](data:image/png;base64...) [dbo].[Sales­Trans­Header] 454](#_Toc256000369)

[![](data:image/png;base64...) [dbo].[Schedule­Delivery­Orders] 455](#_Toc256000370)

[![](data:image/png;base64...) [dbo].[Seals­Transactions] 456](#_Toc256000371)

[![](data:image/png;base64...) [dbo].[SMTPEmail­Settings] 457](#_Toc256000372)

[![](data:image/png;base64...) [dbo].[Special­Customer­Target] 458](#_Toc256000373)

[![](data:image/png;base64...) [dbo].[Stock­Settelment­Collection] 459](#_Toc256000374)

[![](data:image/png;base64...) [dbo].[Stores­Balances] 460](#_Toc256000375)

[![](data:image/png;base64...) [dbo].[Survey­Customers] 461](#_Toc256000376)

[![](data:image/png;base64...) [dbo].[Survey­Customers­Answers] 462](#_Toc256000377)

[![](data:image/png;base64...) [dbo].[Survey­Customers­Link] 463](#_Toc256000378)

[![](data:image/png;base64...) [dbo].[Survey­Prospective­Customers] 464](#_Toc256000379)

[![](data:image/png;base64...) [dbo].[Survey­Prospective­Customers­Answers] 465](#_Toc256000380)

[![](data:image/png;base64...) [dbo].[Surveys] 466](#_Toc256000381)

[![](data:image/png;base64...) [dbo].[Surveys\_­Questions] 467](#_Toc256000382)

[![](data:image/png;base64...) [dbo].[Surveys\_­Questions\_­Options] 468](#_Toc256000383)

[![](data:image/png;base64...) [dbo].[Survey­Salesmans] 469](#_Toc256000384)

[![](data:image/png;base64...) [dbo].[Survey­Salesmans­Answers] 470](#_Toc256000385)

[![](data:image/png;base64...) [dbo].[Survey­Sales­Persons­Assignment] 471](#_Toc256000386)

[![](data:image/png;base64...) [dbo].[System­Codes] 472](#_Toc256000387)

[![](data:image/png;base64...) [dbo].[Table\_1] 473](#_Toc256000388)

[![](data:image/png;base64...) [dbo].[Tag­Codes] 474](#_Toc256000389)

[![](data:image/png;base64...) [dbo].[Targets­References] 475](#_Toc256000390)

[![](data:image/png;base64...) [dbo].[Targets­Types] 476](#_Toc256000391)

[![](data:image/png;base64...) [dbo].[Tax­Codes] 477](#_Toc256000392)

[![](data:image/png;base64...) [dbo].[Tech\_­Customization­Performed­Tasks] 478](#_Toc256000393)

[![](data:image/png;base64...) [dbo].[Technical\_­CFD\_temp] 479](#_Toc256000394)

[![](data:image/png;base64...) [dbo].[Technical­Financial­Insert­Table\_­Temp] 481](#_Toc256000395)

[![](data:image/png;base64...) [dbo].[Territories] 482](#_Toc256000396)

[![](data:image/png;base64...) [dbo].[Transactions­Batchs­Items­Info] 483](#_Toc256000397)

[![](data:image/png;base64...) [dbo].[Transactions­Batchs­Items­Invoice­Link] 484](#_Toc256000398)

[![](data:image/png;base64...) [dbo].[Transactions­Details] 485](#_Toc256000399)

[![](data:image/png;base64...) [dbo].[Transactions­Headers] 488](#_Toc256000400)

[![](data:image/png;base64...) [dbo].[Transactions­Images] 492](#_Toc256000401)

[![](data:image/png;base64...) [dbo].[Transactions­Promotions] 493](#_Toc256000402)

[![](data:image/png;base64...) [dbo].[Transactions­Serials] 495](#_Toc256000403)

[![](data:image/png;base64...) [dbo].[Transactions­Suggested­Items] 496](#_Toc256000404)

[![](data:image/png;base64...) [dbo].[Transactions­Types] 497](#_Toc256000405)

[![](data:image/png;base64...) [dbo].[Transfers­Order\_­Auto] 498](#_Toc256000406)

[![](data:image/png;base64...) [dbo].[Transfers­Orders­Details] 499](#_Toc256000407)

[![](data:image/png;base64...) [dbo].[Transfers­Orders­Details\_­Error­Qty] 500](#_Toc256000408)

[![](data:image/png;base64...) [dbo].[Transfers­Orders­Headers] 501](#_Toc256000409)

[![](data:image/png;base64...) [dbo].[User­Activity] 503](#_Toc256000410)

[![](data:image/png;base64...) [dbo].[User­Company­Branches­Link] 504](#_Toc256000411)

[![](data:image/png;base64...) [dbo].[User­Customers­Promotions­Group­Link] 505](#_Toc256000412)

[![](data:image/png;base64...) [dbo].[User­Promotions­Link] 506](#_Toc256000413)

[![](data:image/png;base64...) [dbo].[Users] 507](#_Toc256000414)

[![](data:image/png;base64...) [dbo].[Users­Close­Date] 508](#_Toc256000415)

[![](data:image/png;base64...) [dbo].[Users­Favorite­Menu] 509](#_Toc256000416)

[![](data:image/png;base64...) [dbo].[Users­Groups] 510](#_Toc256000417)

[![](data:image/png;base64...) [dbo].[Users­Groups­Link] 511](#_Toc256000418)

[![](data:image/png;base64...) [dbo].[Vacations] 512](#_Toc256000419)

[![](data:image/png;base64...) [dbo].[Van­Transfer­Details] 513](#_Toc256000420)

[![](data:image/png;base64...) [dbo].[Van­Transfer­Header] 514](#_Toc256000421)

[![](data:image/png;base64...) [dbo].[Verification­Codes] 515](#_Toc256000422)

[![](data:image/png;base64...) [dbo].[WF\_­Functions] 516](#_Toc256000423)

[![](data:image/png;base64...) [dbo].[WF\_­Master­Log] 517](#_Toc256000424)

[![](data:image/png;base64...) [dbo].[WF\_­Positions­Ver] 518](#_Toc256000425)

[![](data:image/png;base64...) [dbo].[WF\_­Sales­Person­Items­Category­Values] 519](#_Toc256000426)

[![](data:image/png;base64...) [dbo].[WF\_­Setup­Details] 520](#_Toc256000427)

[![](data:image/png;base64...) [dbo].[WF\_­Setup­Header] 521](#_Toc256000428)

[![](data:image/png;base64...) [dbo].[WF\_­Sub­Log] 522](#_Toc256000429)

[![](data:image/png;base64...) [dbo].[WFMobile­Permission­Definition] 524](#_Toc256000430)

[![](data:image/png;base64...) [dbo].[WFMobile­Permission­Link] 525](#_Toc256000431)

[![](data:image/png;base64...) [dbo].[Widget\_­Functions] 526](#_Toc256000432)

[![](data:image/png;base64...) [dbo].[Widget\_­User\_­Log­Action] 527](#_Toc256000433)

[![](data:image/png;base64...) [dbo].[Wieght­Targets] 528](#_Toc256000434)

[![](data:image/png;base64...) [dbo].[Zatca­Company] 529](#_Toc256000435)

[![](data:image/png;base64...) [dbo].[Zatca­Customer] 530](#_Toc256000436)

[![](data:image/png;base64...) [dbo].[Zatca­Mode] 531](#_Toc256000437)

[![](data:image/png;base64...) [dbo].[Zatca­Result­Generate­Xml] 532](#_Toc256000438)

[![](data:image/png;base64...) [dbo].[Zatca­Sales­Persons] 534](#_Toc256000439)

|  |
| --- |
| ![](data:image/png;base64...) 10.0.10.105 |

Databases (1)

* ![](data:image/png;base64...) [Olives\_­BO](#AWOg+1CtxQL788xK118YzJkrSKc=)

Server Properties

|  |  |
| --- | --- |
| Property | Value |
| Product | Microsoft SQL Server |
| Version | 15.0.2130.3 |
| Language | English (United States) |
| Platform | NT x64 |
| Edition | Enterprise Edition (64-bit) |
| Engine Edition | 3 (Enterprise) |
| Processors | 32 |
| OS Version | 6.3 (17763) |
| Physical Memory | 32767 |
| Is Clustered | False |
| Root Directory | C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL |
| Collation | SQL\_­Latin1\_­General\_­CP1256\_­CI\_­AS |

Server Settings

|  |  |
| --- | --- |
| Property | Value |
| Default data file path | C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\ |
| Default backup file path | C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\Backup |
| Default log file path | C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\ |
| Recovery Interval (minutes) | 0 |
| Default index fill factor | 0 |
| Default backup media retention | 0 |
| Compress Backup | False |

Advanced Server Settings

|  |  |
| --- | --- |
| Property | Value |
| Full text upgrade option | 2 |
| Locks | 0 |
| Nested triggers enabled | True |
| Allow triggers to fire others | True |
| Default language | English |
| Network packet size | 4096 |
| Default fulltext language LCID | 1033 |
| Two-digit year cutoff | 2049 |
| Remote login timeout | 10 |
| Cursor threshold | -1 |
| Max text replication size | 65536 |
| Parallelism cost threshold | 5 |
| Max degree of parallelism | 4 |
| Min server memory | 4096 |
| Max server memory | 2147483647 |
| Scan for startup procs | False |
| Transform noise words | False |
| CLR enabled | False |
| Blocked process threshold | 0 |
| Filestream access level | False |
| Optimize for ad hoc workloads | False |
| CLR strict security | True |

|  |
| --- |
| ![](data:image/png;base64...) User databases |

Databases (1)

* ![](data:image/png;base64...) [Olives\_­BO](#AWOg+1CtxQL788xK118YzJkrSKc=)

|  |
| --- |
| ![](data:image/png;base64...) Olives\_­BO Database |

MS\_­Description

Sales Field Automation and Distribution Management database that stores master data, transactions, workflow approvals, asset tracking, merchandising activities, financial operations, and ERP integration data for the Olives platform.

|  |
| --- |
| ![](data:image/png;base64...) Tables |

Objects

|  |
| --- |
| Name |
| [dbo.Activity­List](#2V49Cud9CVvOcM5jCeJG5AVgE84=) Stores activity list data |
| [dbo.Add\_­Customer](#fzny8URgQhp1EMDKKbEB3AKAWUQ=) Stores add customer data |
| [dbo.Add­Discount­To­Customer­Orders](#ugVvYAW4Z5SiatPC1jKJaaT+EUw=) Stores add discount to customer orders data |
| [dbo.Assets](#K6CNYc8TwLULZY65085UG364+KY=) Assets |
| [dbo.Assets­Customer­Link](#YX60+7Aay0I8IF9BytIKWlPb2Y0=) Stores assets customer link data |
| [dbo.Assets­Transactions](#ypSuwnmZTPmFpW0FmvPUQvRaHHw=) Stores assets transactions data |
| [dbo.Assets­Warehouse­Transactions](#94PF9TUQLLtMObXiPDy+aQSD/yc=) Stores assets warehouse transactions data |
| [dbo.Balad\_­Add\_­Customer\_­Table](#jVcSofkdHohtKwEdlM202WLO+JQ=) Stores balad add customer table data |
| [dbo.Bank­Deposit­DF](#1QqL1BVU5LTvt/V3Rm6J7yF76k0=) Stores Bank Deposit detail line records |
| [dbo.Bank­Deposit­HF](#9e35+0qiczLeVUBKOOfACcL6BU4=) Stores Bank Deposit header records |
| [dbo.Banks](#PYH+j4Qz5uStxKmaxbJgMvXBdEw=) Stores banks data |
| [dbo.Banks­Accounts](#/SuG11/TD3WWNcFlPs6TT8Z/iYQ=) Stores banks accounts data |
| [dbo.Batchs­Items­Info](#iJbGE+tMq/S4GftIcrqHKfj34BY=) Stores batchs items info data |
| [dbo.Branches](#BMb4NUvwYVL/5aaAQB++QZZcgeI=) Stores branches data |
| [dbo.Business­Units](#nfNLb+EhlWiX9kN6JEFSAV6syXI=) Stores business units data |
| [dbo.Car­And­Salesperson­Link](#NsLVM1ScQgmKvOLu+rhJEAyMoio=) Stores car and salesperson link data |
| [dbo.Catalog­Media](#hFEl/nHVvLcmmyHQf4vw02IgZRQ=) Stores catalog media data |
| [dbo.Checks](#t5rkylWPznrB3Az5Kc95YjOlRjk=) Stores checks data |
| [dbo.Class­Target­Rate](#sh2DBHHr2W7b8bwsiq27A6p6qaA=) Stores class target rate data |
| [dbo.Clients](#OjBNqqbWWpKklbNKr1W6Ang9c5g=) Stores clients data |
| [dbo.Clients­Active](#bgt8UttY3cFCswtAdwX7szsBqIo=) Stores clients active data |
| [dbo.Clients­WFID](#bFHffhnOKtr9s7XDWnqM8lDcBYs=) Stores clients wfid data |
| [dbo.Companies](#xWl68O1P/ZZ1akX31muCMm2xzR0=) Stores companies data |
| [dbo.Company­Branches](#QtIx7cCe02/M8Iq2UstqD1tTYh4=) Stores company branches data |
| [dbo.Company­Parameters](#dCTLECNSLtbhprq/uSnHVJPZN6k=) Stores company parameters data |
| [dbo.Competitive­Items](#b4nxWXHiDzbVHPf7DkV5+Hz/mmk=) Stores competitive items data |
| [dbo.Competitve­Items­Data­DF](#+eS5Tt99durvtflfLWXYsgHHFOo=) Stores Competitve Items Data detail line records |
| [dbo.Competitve­Items­Data­HF](#xwPjLYIo+jJaGV7rij2frhvGio4=) Stores Competitve Items Data header records |
| [dbo.Contract­Items](#NgyLZ3sXlHRDppPNRH3LAjgNV+k=) Stores contract items data |
| [dbo.Contracts](#zSXpPHadqD7+V+akfh1GN7CwldI=) Stores contracts data |
| [dbo.Coupons­Books­Details](#FYByLXsEjK7VM+/rtAOy29dBUs0=) Stores Coupons Books detail line records |
| [dbo.Coupons­Books­Headers](#0ON2VfRM0v9FQb1E8yKRDkUcwjA=) Stores Coupons Books header records |
| [dbo.Currencies](#k0NURIzYF8aeO/uxKYIEdxSccAg=) Stores currencies data |
| [dbo.Currencies­Denominations](#19c12sWpRzkI2L0QAxbqNJQq5fk=) Stores currencies denominations data |
| [dbo.Currencies­Rate](#5qiA8sbOaOuUOrsgPFuT2AMP03g=) Stores currencies rate data |
| [dbo.Customer­Chq­List](#0tUTSUyQWLdN4AiytOT+R7lowTM=) Stores customer chq list data |
| [dbo.Customer­Class­Targets](#IT4JhR/yxVJEqAmwFRM4MjjAGnw=) Stores customer class targets data |
| [dbo.Customer­Class­Targets­Details](#TDYPZASIzsg83EqyQ1rHD7mKh3A=) Stores Customer Class Targets detail line records |
| [dbo.Customer­Data\_­Sample](#W1nYVZGyycJKlXvRqCcQNdnD5J0=) Stores customer data sample data |
| [dbo.Customer­Login­Actions](#KwnUhE/QtDI4VJSfDA92WxChl/Y=) Stores customer login actions data |
| [dbo.Customer­Paid­Trans\_­Form­ERP](#WNyEQJb4WqrWl+r2/Lu8vSIqjjk=) Stores customer paid trans form erp data |
| [dbo.Customer­Phone](#df/5rzAkCPUpie88IT+ieljqXfY=) Stores customer phone data |
| [dbo.Customer­Receivables­Info](#5Qi2Xr1O9UAJVMOkUiBYAmMXEvQ=) Stores customer receivables info data |
| [dbo.Customers](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) Stores customers data |
| [dbo.Customers2](#/zJRfBhcb574hZpQQqkbIdAGAqk=) Stores customers 2 data |
| [dbo.Customer­Sales­By­Category](#YMvYnDOwLduu/j0n5V/qfwOqCsU=) Stores customer sales by category data |
| [dbo.Customers­Balance­Aging](#46dLEZZCjXb90vsyBdxaaejh2HE=) Stores customers balance aging data |
| [dbo.Customers­Balance­Aging\_­Inmaa](#UD3jNkrGg3msenGTEsp/SnzA+aU=) Stores customers balance aging inmaa data |
| [dbo.Customers­Bonus­Types­Link](#tQLjXWyGaTH8sqeuN1CLTHYgpZc=) Stores customers bonus types link data |
| [dbo.Customers­Classes](#KrR7yySr/q1jKoCUyhbUJhKzp6M=) Stores customers classes data |
| [dbo.Customers­Contact­Persons](#nzjAQPUSe157+buvdP8f6QX01Ic=) Stores customers contact persons data |
| [dbo.Customers­Contact­Persons­Link](#lB5tFL8hha+RynrmCtDRpL/CAtk=) Stores customers contact persons link data |
| [dbo.Customers­Financial­Details](#SssAJ9yyQQ5egR1dKJIkDPb22AQ=) Stores Customers Financial detail line records |
| [dbo.Customers­Financial­Details\_­Old](#+4NqXlAVDWGJbEPyHOEYtLW9pIY=) Stores customers financial details old data |
| [dbo.Customers­Financial­Details2](#4uyyQgRLwseQiC8VhQoj3yztVL8=) Stores customers financial details 2 data |
| [dbo.Customers­GPSLocations](#E86/jK+058KHrwyG6QFDpivczQE=) Stores customers gps locations data |
| [dbo.Customers­Groups](#okyn1+fvA5B2jRl9YiDWFhbVXIg=) Stores customers groups data |
| [dbo.Customers­Item­Qty­Limit](#fmw+Ce5gyDVENS7rlH1JpIIxsCE=) Stores customers item qty limit data |
| [dbo.Customers­Items­Assigment](#NkSr5rcw2YKwRmgfcwtH3CFVXI8=) Stores customers items assigment data |
| [dbo.Customers­Items­Log](#xV3WwaY6eA+Ux48qijLBL/SGgjo=) Stores customers items log data |
| [dbo.Customers­Log](#72aAoDqx5efbgBT9nJB4ovDyRRA=) Stores customers log data |
| [dbo.Customers­Monthly­Collection­Target](#MFmnT+Qyp99oPEgMUregv4sSM6w=) Stores customers monthly collection target data |
| [dbo.Customers­Paid­Trans­List](#BDstIVXJslvt8hAzkCTFzj+ZH28=) Stores customers paid trans list data |
| [dbo.Customers­Payment­Types­Link](#lQ5NFYOEDz1hVDlbp34p8FXIv84=) Stores customers payment types link data |
| [dbo.Customers­Promotions­Exceptions](#GNxLxufY/FcmvXyzC4TgrS4idT8=) Stores customers promotions exceptions data |
| [dbo.Customers­Promotions­Groups](#CFvv0vB6qnd5JDiJpBfVpPfz9FY=) Stores customers promotions groups data |
| [dbo.Customers­Promotions­Groups­Link](#zf4YJlbQBDsDGs+UNyaSiXQBSu4=) Stores customers promotions groups link data |
| [dbo.Customers­Return­Item­Qty­Limit](#ro89ZM2XEydtfCLy9dsbAfcWWgg=) Stores customers return item qty limit data |
| [dbo.Customers­Sales­From0to­Max](#bPYdrclQbc0Y222//HJzwwu4bCA=) Stores customers sales from 0 to max data |
| [dbo.Customer­Statment­Of­Account](#+otUat1NsRqQf1UBal9cknv23bY=) Stores customer statment of account data |
| [dbo.Customer­Stock­Tacking](#UqtoPsN1f++adGXeDAi3Yi79T8I=) Stores customer stock tacking data |
| [dbo.Customer­Stock­Tacking­Details](#q3QOWoR0M1+mcdbwDn17Cd2Jlak=) Stores Customer Stock Tacking detail line records |
| [dbo.Customers­Types](#mUOPMl0ZzNBySPnrrjXsxaUEKvo=) Stores customers types data |
| [dbo.Customers­Visit­Activity](#WsgTX6imtrKGLK4kA6fkCTVaNAU=) Stores customers visit activity data |
| [dbo.Customers­WFFunctions­Auto­Approve](#kwSvCSxtGa7GmZ5kP0srlRoDIII=) Stores customers wf functions auto approve data |
| [dbo.Customer­Targets](#xFtDW8F50DUM+y3PCtJ+lSb9kJ0=) Stores customer targets data |
| [dbo.Customer­Targets­Details](#2tfexLjBhrXYvSwxj6r+j1iNRc0=) Stores Customer Targets detail line records |
| [dbo.Customer­Type­Early­Pay­Days](#t25OOhKCzuX4xRbPIoph1ROia2o=) Stores customer type early pay days data |
| [dbo.Customer­Type­Targets](#bBVLP3r/2IH82Om8eX+mV9+gJ3E=) Stores customer type targets data |
| [dbo.Customer­Type­Targets­Details](#kw2vg+ZWPjzgS3xgA4qcYdc268Y=) Stores Customer Type Targets detail line records |
| [dbo.Daily­Procedures](#poiMEFqRis/kSReUWjfL/6Ng9ck=) Stores daily procedures data |
| [dbo.Debit­Credit­Note­Trans](#jRBNpytc3Sw/sn1fqtlF6JzlLzg=) Stores debit credit note trans data |
| [dbo.Delivery­Cars](#TNGzSieGVszmfgt8DhcppCKtHI8=) Stores delivery cars data |
| [dbo.Delivery­Manifest](#2haYGHeEDzvS76pCUhoxCWh058g=) Stores delivery manifest data |
| [dbo.Delivery­Prova­D](#f2mSGwvhzkEoRgmouH1BcJz5GNs=) Stores delivery prova d data |
| [dbo.Delivery­Prova­H](#F3RNdI+akyEzuRmHMQJX9KEEPUE=) Stores delivery prova h data |
| [dbo.Delivery­Route](#zjX8Nbky0Gchw123Z7qgaxs7gQk=) Stores delivery route data |
| [dbo.Device­Reports­List](#lmEdaH69fK3Xzs0Err9JNBLV1Qg=) Stores device reports list data |
| [dbo.Devices­Info](#x3PV5yt656aq0BJSKfBmbooAD6s=) Stores devices info data |
| [dbo.Discount­Early­Pay­By­Invoice­Ref](#3do+8UC9Z4yGT9HYB+Ev3HSvf6I=) Stores discount early pay by invoice ref data |
| [dbo.Documents­Types](#gdlNDWGb4JDf/mDxiA3zOJvy/5o=) Stores documents types data |
| [dbo.DR\_­Dynamic­Reports](#E9davTFvz3Pi77oGLS5goXmPn2g=) Stores dr dynamic reports data |
| [dbo.DR\_­Dynamic­Reports­Dictionary](#y+apneRfYb0VxwHGXCP0plQhE3Y=) Stores dr dynamic reports dictionary data |
| [dbo.DR\_­Dynamic­Reports­Parameters](#nfhxhgQRCK/T+l5E98mm/4Ye01M=) Stores dr dynamic reports parameters data |
| [dbo.Drawers](#wNA1/7+fkspPVPr8ZtNm55GqVVs=) Stores drawers data |
| [dbo.Efawateercom­Payment](#AIgceuZuxRF4Gkz8xrSjhQAVAqI=) Stores efawateercom payment data |
| [dbo.Emp­Details](#TeD12fAH3CHZb1ht5twsP89XucA=) Stores Emp detail line records |
| [dbo.ERPStores](#hezrK488EdTfM5BK0auaFr51hsc=) Stores erp stores data |
| [dbo.ERPStores­Items­Link](#HMnVJmD5WTo6pC86t33lpC94Ctk=) Stores erp stores items link data |
| [dbo.Error­Log](#XqyclA0On6aR9YwtO4vPZZ74Rcw=) Stores Error­Log log records |
| [dbo.Excel](#MRGx0THfLL4pwbuDfEGPvdU3knE=) Stores excel data |
| [dbo.Excel2](#KoJyI2n090ziatNqJKHOW6Wm0uY=) Stores excel 2 data |
| [dbo.Excel­Reports](#VUmyjSHFllJhT3Pq4FDyXEBjvD4=) Stores excel reports data |
| [dbo.forupdateonly](#zM42+zhb7kanwDPMXUJ9r/Oxo64=) Stores forupdateonly data |
| [dbo.Gap­Tags](#1q6t5Dg0+l9Wli03ZQsG6olmZHc=) Stores gap tags data |
| [dbo.Gap­Trans­Headers](#7L1Vnj/F52SPk0WJ/YHwE9ChrQc=) Stores Gap Trans header records |
| [dbo.Gap­Trans­Tags](#nonRW8aPWeoEdWBjrRZo80/QXIA=) Stores gap trans tags data |
| [dbo.Gap­Trans­Time­Line](#rzYwBUucCXtC42eVDFDAx01PLTU=) Stores gap trans time line data |
| [dbo.Groups­Menu](#oIQVaAvucMdy9PDcerPJaBSRjuw=) Stores groups menu data |
| [dbo.Image­Types](#EGWMnYEjQh0yKe7JowKQk+sTLh4=) Stores image types data |
| [dbo.Integration­Error­Log](#yV5u/ByM3O5nY6O8xvBksaamExs=) Stores integration error log data |
| [dbo.Integration­Posted­Transactions](#UD0PrvjxUfAnUgLlw99hPVfClCw=) Stores integration posted transactions data |
| [dbo.Intenal­Memo­Approve](#Tjh2RLcpyf6GU0YgMoQxYIZQrVE=) Stores intenal memo approve data |
| [dbo.Internal­Memo](#5eiFVsAmVCTRrnKEWOt0O9Jqirs=) Stores internal memo data |
| [dbo.Invoice­Delivery­DF](#Py2eKCRYacexi4tn+f3cKi6vFdk=) Stores Invoice Delivery detail line records |
| [dbo.Invoice­Delivery­HF](#HzP++kNRo1VcdFnqIgGXEjqkCt0=) Stores Invoice Delivery header records |
| [dbo.Invoice­History­DF](#dm1+qqd/WQ+2204jTfjrT20H8w0=) Stores Invoice History detail line records |
| [dbo.Invoice­History­HF](#e/+K8dFskubwqsqkHy0EmM8IYQA=) Stores Invoice History header records |
| [dbo.Invoice­Return­Link](#EkEwAxi+kQXCpD4zKDQK3RBeFLw=) Stores invoice return link data |
| [dbo.Issue­Items­Details](#T8i2+xPFb2qcjncAwv+wmRm1fjQ=) Stores Issue Items detail line records |
| [dbo.Issue­Items­Headers](#n0zsYIhgt3HFGDQDkIZ/hWP6jnM=) Stores Issue Items header records |
| [dbo.Items](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) Stores items data |
| [dbo.Items­Barcodes](#lh/aVCPrdyow4uE2L4vg+KznBro=) Stores items barcodes data |
| [dbo.Items­Categories](#VLpTtrh4X181/GF+u73WO6VXNcU=) Stores items categories data |
| [dbo.Items­Categ­Stock­Details](#q4sGBVhsRY6N6zrJCbKsmaMHopg=) Stores Items Categ Stock detail line records |
| [dbo.Items­Categ­Stock­Header](#C9Ur/TZTJ7b47/VOVTUkoXn3r7c=) Stores Items Categ Stock header records |
| [dbo.Items­Classes](#tMGSpWb23eyxaVb5HBx7c2TARBU=) Stores items classes data |
| [dbo.Items­Group­Bonus­Target](#ONm27MxHeslaWEqWFYpIrpkGBVM=) Stores items group bonus target data |
| [dbo.Items­Groups](#MZfHge8v9E75q53qtli4sSu4w7Y=) Stores items groups data |
| [dbo.Items­Inventory](#eyGcp1WJ/s0eINTlHkm/LsZgVyc=) Stores items inventory data |
| [dbo.Items­Minimum­Sales](#KY7JbST2T6ArNInizXh10W+n9UQ=) Stores items minimum sales data |
| [dbo.Items­Price­Exceptions](#LxY7v0KdExYdgJsX40koAmehH78=) Stores items price exceptions data |
| [dbo.Items­Priority](#2gOUw9Lv5OfqQ+qOkmSEJkyxfWQ=) Stores items priority data |
| [dbo.Items­Related­To­Items](#9+ru9vrioD2aqzEOb1ZOOkcNueQ=) Stores items related to items data |
| [dbo.Items­Replacement­Details](#OnTMRN04ypzcN9KDKqSpDgTLy3Y=) Stores Items Replacement detail line records |
| [dbo.Items­Replacement­Groups](#6L20ljAajJs4sSuJI+icC2Hnigs=) Stores items replacement groups data |
| [dbo.Items­Replacement­Headers](#y11F0kJ6sM3TTvveJX8WrHifX1U=) Stores Items Replacement header records |
| [dbo.Items­Suggest­Group](#eFOPzB4o/FP/xq7NcBASDPwgaEw=) Stores items suggest group data |
| [dbo.Items­Suggest­Group­Link](#HtEWMeFYPChxddtF2k5Awq2V2A8=) Stores items suggest group link data |
| [dbo.Items­Suggest­Group­Link­With­Items](#wBMwJdPCjBszNH+xV3SXzujI0j8=) Stores items suggest group link with items data |
| [dbo.Items­Units](#FMCFC97OKTqtLQAZvqd9162BcGI=) Stores items units data |
| [dbo.Items­Units­Details](#e3n0Ugo25Gd9eHvYSfU7C/vdQA8=) Stores Items Units detail line records |
| [dbo.Items­Units­Details\_1](#mNFAy1OabpXv2XVya/w/lcInZyM=) Stores items units details 1 data |
| [dbo.Jo­Tax­Result](#tqiuQswXsaSG7JL/C2u9ZQsUldk=) Stores jo tax result data |
| [dbo.JOTax­Settings](#+lKQxHcMoE6c7M6+S6pBO8m28Pk=) Stores jo tax settings data |
| [dbo.JSONData­Log](#KrJgRCHFTePKUsgdpB07NK9OdpQ=) Stores json data log data |
| [dbo.Kasih­Survey](#Id3xCbU6xio1aKjJBUV0uUyal+Q=) Stores kasih survey data |
| [dbo.Language](#LmkrE7SDdGqWOHOQfXxYa9UElkw=) Stores language data |
| [dbo.Language­Dictionary](#s/xrje6hdwrVp+BJrgipp/90acg=) Stores language dictionary data |
| [dbo.Locations](#eNuBnAAgcTN3Hu1UlDB+jaS/yKQ=) Stores locations data |
| [dbo.Location­Targets](#xv9Dx8qyzuMEHBOqJJxT0nswzg0=) Stores location targets data |
| [dbo.Location­Targets­Details](#bdx4klaQNttPlu0b3vbtpjqsT4E=) Stores Location Targets detail line records |
| [dbo.Log­Actions](#ERgtdohr3Uv8bpbGBpFZyZ4UDSw=) Stores Log­Actions log records |
| [dbo.Log­Action­Transaction](#Z4IwlGoUGypyZ6ryEMzZLK6iZ8M=) Stores Log­Action­Transaction log records |
| [dbo.Log­Action­Transaction\_](#VOvmBChUaQOZIDkiMSpBHIfCoK8=) Stores Log­Action­Transaction\_ log records |
| [dbo.Maintinance­Orders](#iwjzdi4dB5Bhbwvbipp5Z02DM8I=) Stores maintinance orders data |
| [dbo.Maintinance­Orders­Approve](#jtkvridWwt0YYBYlhOkrviSsP9M=) Stores maintinance orders approve data |
| [dbo.MAZ\_­Route\_­EMAIL\_­Final](#yKieOM7rPTe1bIn1BAF/7ez/Fcg=) Stores maz route email final data |
| [dbo.Menu](#FnUAPCqnhxlqyV+PeKDOeSNn8tM=) Stores menu data |
| [dbo.MIMETypes](#IjT72UKcoTkDxD1ezS7I3nKdklo=) Stores mime types data |
| [dbo.MMS\_­Assistants](#wka74H7OQit6VidMTYAe4NPl3U4=) Stores mms assistants data |
| [dbo.MMS\_­Close­Order­Reasons](#RMWFEKQIT5i1l0aj1kacM4DpG6A=) Stores mms close order reasons data |
| [dbo.MMS\_­Devices­Info](#m/05OIuhh6hPEQWFRqh5cBmFu+o=) Stores mms devices info data |
| [dbo.MMS\_­Diagnostic](#me6Q1dPOrKAfJ7RLUkH8Dm3Ypi0=) Stores mms diagnostic data |
| [dbo.MMS\_­DV\_­Error­Log](#3d/LN6PM9e9xTLpLXkDgRSZmPgo=) Stores mms dv error log data |
| [dbo.MMS\_­Invoice­Details](#yIfrj3WetUv9AoTljws0uUj7MZI=) Stores MMS Invoice detail line records |
| [dbo.MMS\_­Invoices­Headers](#aZ3dNAjvSVkXd8F3rYCFvJzcPJM=) Stores MMS Invoices header records |
| [dbo.MMS\_­Items](#jCiOonp1M2lfwrXRd4H/FaFKyao=) Stores mms items data |
| [dbo.MMS\_­Items­Categories](#EEBAR2UgrZCXmCghLEErcVpadTc=) Stores mms items categories data |
| [dbo.MMS\_­Link\_­Device\_­Diagnostic](#j7iPzusoCSZ2sfR80NZ2ObJowsI=) Stores mms link device diagnostic data |
| [dbo.MMS\_­Link\_­Device\_­Items](#bg2rAbCuRA+Qj5QvFTUBWcwUs/A=) Stores mms link device items data |
| [dbo.MMS\_­Link\_­Supervisor\_­Maintenance­Unit](#1ujJf5UHrrN7RWhUU2vQPLzNhGA=) Stores mms link supervisor maintenance unit data |
| [dbo.MMS\_­Link\_­Supervisor\_­Technician](#wugnqBmqIAf+sMuyVKahDOzj248=) Stores mms link supervisor technician data |
| [dbo.MMS\_­Link\_­Technician\_­Assistant](#p7YLlvB+Nj2StlVW6RBB9ajoJrE=) Stores mms link technician assistant data |
| [dbo.MMS\_­Maintenance­Technician](#o3dWGb3gVpr27C3o3f/cCZVkw+c=) Stores mms maintenance technician data |
| [dbo.MMS\_­Maintenance­Technician\_­Items­Balance](#hKqeHj8GpYn4sF1rzjqr7PCbzfQ=) Stores mms maintenance technician items balance data |
| [dbo.MMS\_­Maintenance­Technician­Permissions](#xjgKNW3hIyhA5Z04XvvpX8Pem+g=) Stores mms maintenance technician permissions data |
| [dbo.MMS\_­Maintenance­Technician­Permissions\_­Def](#wEZu/0IqR112+qL3W5XRjzx75t0=) Stores mms maintenance technician permissions def data |
| [dbo.MMS\_­Maintenance­Technician­Trans­Serials](#sp3VpK7hrIwRRhskHcbNLwx+HHs=) Stores mms maintenance technician trans serials data |
| [dbo.MMS\_­Maintenance­Unit](#k4iU+6c8t0NVTZxaks2qs3rv42c=) Stores mms maintenance unit data |
| [dbo.MMS\_­Order­Details](#wKdIgvTtFIrkojnRS/bQHg7+2nM=) Stores MMS Order detail line records |
| [dbo.MMS\_­Orders­Header](#2AZEsoxptSLNCgkvwys3GkaCD5s=) Stores MMS Orders header records |
| [dbo.MMS\_­Order­Status](#sIe+XrbobQh+yOlqaSWoA+/XyJM=) Stores mms order status data |
| [dbo.MMS\_­Order­Types](#aadN/tqwT4UctfE7xCWB7wh5kfk=) Stores mms order types data |
| [dbo.MMS\_­Order­Visit­Details](#ENYSFs4qiwZNDJJzyaqzp6xNumI=) Stores MMS Order Visit detail line records |
| [dbo.MMS\_­Order­Visit­Images](#njY4WUXiEs1MEMwJTQhnfjQkTn4=) Stores mms order visit images data |
| [dbo.MMS\_­Order­Visits](#E7Rp8+V0ilc7yr3P/SCvr8qXGx0=) Stores mms order visits data |
| [dbo.MMS\_­Payments­Checks­Details](#56+iaEEDXxRRYKCt8hNEzuSLIUw=) Stores MMS Payments Checks detail line records |
| [dbo.MMS\_­Payments­Header](#uWIkqpE3FT8rx+zChseoBW8g1V4=) Stores MMS Payments header records |
| [dbo.MMS\_­Reporters](#6d1qdEkmZYW3suwakH3nz5gBkSw=) Stores mms reporters data |
| [dbo.MMS\_­Schedule­Support­Visits](#yJp+00SYMsWMW+e3m6meGzIqyHQ=) Stores mms schedule support visits data |
| [dbo.MMS\_­Schedule­Support­Visits\_­Log](#2mqo6GyrdnTmm0uwAnzSgBvbw6A=) Stores mms schedule support visits log data |
| [dbo.MMS\_­Show­Rooms](#rBnY5gTm+uVk4xvCpQdELjYL1lo=) Stores mms show rooms data |
| [dbo.MMS\_­Supervisors](#gJ4TlQFuKzjGSgrYV9AGeSuDO+g=) Stores mms supervisors data |
| [dbo.MMS\_­System­Codes](#Tl6htrK7qAsC2O0Y7ZpexCdURyQ=) Stores mms system codes data |
| [dbo.MMS\_­System­Settings](#SaxlTC9Yie/qVUsBP5SekfpkLgc=) Stores mms system settings data |
| [dbo.MMS\_­Tax­Type](#48pylN1cQ9NhBDKlliEv0wkeAW0=) Stores mms tax type data |
| [dbo.Mobile­Version­Salesmen](#Kc4WQtcz9MKNW53nRpcVcfGE0AA=) Stores mobile version salesmen data |
| [dbo.Multi­Targets](#xLEbPhPlQEILTGn8jvPYiIbE2n8=) Stores multi targets data |
| [dbo.Nairoukh\_­Awtar\_­Salespersons­Exemptions](#ME4qzA3gQKD6e0Yq1m6CS3Mj6Mo=) Stores nairoukh awtar salespersons exemptions data |
| [dbo.Nairoukh­Route­Customers­Position­Change](#7ookG/+rEG/wDGBPQs/g2Ts2HvY=) Stores nairoukh route customers position change data |
| [dbo.New­Competitive­Items](#NymHIIyB75lSWmNENvuNbD9gPxE=) Stores new competitive items data |
| [dbo.New­Customer­Default­Value](#I5VQ8XAjG/KEZwjVYDGr4j4f9XM=) Stores new customer default value data |
| [dbo.New­Customer­Special­Fields\_­Def](#EuwbQE9wQYW96RY+KZweJVZH9SU=) Stores new customer special fields def data |
| [dbo.Notifications](#hEqUhi5l/V9spNjyTkpNf4ZdNRE=) Stores notifications data |
| [dbo.No­Transactions­Log](#uHrRmKtFNwlHhUaaQVOEg0AY9qY=) Stores no transactions log data |
| [dbo.No­Transactions­Reasons](#toLtTFY6Ob5u1aklBdmXETlRiNc=) Stores no transactions reasons data |
| [dbo.Olives­Menu](#nxsAcgtZzWG8rKXJeTsQQeeQgBc=) Stores olives menu data |
| [dbo.Olives­Pages](#umDYyQd/6G5m1+B9mm2585SO9Co=) Stores olives pages data |
| [dbo.Olives­User­Permissions](#4pF6aMfUN1KclSAGCNtyrqm3rn4=) Stores olives user permissions data |
| [dbo.OLV\_­PDC](#EqwKx2X0JzzFowNfxZNRow/jpTU=) Stores olv pdc data |
| [dbo.Orders­Delivery­Details](#3/Wz3bVjOB8vILRnYslrV+gitvQ=) Stores Orders Delivery detail line records |
| [dbo.Orders­Delivery­Info](#NpJFYaa4cp7IBheaKvmB4vEv5gM=) Stores orders delivery info data |
| [dbo.Orders­Details](#ac0JxNTydSTnAtNRvzK3jD4cJoI=) Stores Orders detail line records |
| [dbo.Orders­Details\_­Log](#zKHoMqqT+3vASEmlCccbN9PvtM4=) Stores orders details log data |
| [dbo.Orders­Headers](#DayzTm2CXWhInZ/pRQJ0Z15TOuE=) Stores Orders header records |
| [dbo.OT\_­Send­Log](#Gn3WUYdvVnUIoSwEifb8Fb1pEs0=) Stores ot send log data |
| [dbo.OWGM\_­Gates](#rHzx/v5OVFhsXO2i7zO1AMykThc=) Stores owgm gates data |
| [dbo.OWGM\_­Gates­Users](#ZS4W/usNaQLqodsUPntjShh7RXQ=) Stores owgm gates users data |
| [dbo.OWGM\_­Lock­Log](#BSSnj4KWjxIya4ImQ5WK6fVW5EM=) Stores owgm lock log data |
| [dbo.OWGM\_­Transactions](#Lm8wK7rvdD9O408kQgMRxJBKB/s=) Stores owgm transactions data |
| [dbo.Payments­Orders](#uycbIqEGYNC5O2uqNdFuBuu7/lw=) Stores payments orders data |
| [dbo.Payments­Types](#lO8zg+RAFUjBCTc7z+Mf67JVfuQ=) Stores payments types data |
| [dbo.Pending­Invoices](#hEiTSdMr8sxidLWB0VzjG3Q0TKU=) Stores pending invoices data |
| [dbo.Pending­Orders­Details](#92ljx36/llQ1mXhUG2QO9IWRDv0=) Stores Pending Orders detail line records |
| [dbo.Pending­Orders­Headers](#8qVmiQDTr9AnSh1ifTlh8nH166k=) Stores Pending Orders header records |
| [dbo.Planogram­Media](#31gsgcnVnTI5wSuYYv6G7WjmztA=) Stores planogram media data |
| [dbo.Planogram­Media­Customers­Link](#uKpXbTbXg74d1JRp53uQZK0mNkc=) Stores planogram media customers link data |
| [dbo.POADetails](#kfaMng0jW7A34t78Ps+ZtneL8g4=) Stores POA detail line records |
| [dbo.POAHeader](#EQvzXZD0CVNFuEaOPo45dJGp1v0=) Stores POA header records |
| [dbo.Pos\_­Invoice­Order­HF](#0A8R2puKnZsM5bX4SGjqcO2VnYY=) Stores Pos Invoice Order header records |
| [dbo.Positions](#0hezp3sBJ5vepFnPict7YRgZ7Gg=) Stores positions data |
| [dbo.Price­List­Details](#v7NaJKoQygMRE4YO5PaFOmuqaKg=) Stores Price List detail line records |
| [dbo.Price­List­Details­From­GCI](#hAJpQVQysavM23YKYvRt0yzO+/U=) Stores price list details from gci data |
| [dbo.Price­List­Qty­Ranges](#tgoTL4pjp6d5NO4DidpGJsGPX4A=) Stores price list qty ranges data |
| [dbo.Price­Lists](#UTuGUXmxHIFiIaREw25LxgcqPnU=) Stores price lists data |
| [dbo.Procedure­Change­Log](#Fz3OCmZF3kJs+YXg4z+YDTJuFTI=) Stores procedure change log data |
| [dbo.Promotion­Budget](#EBSbEEBsBE4QluH3N8dh1+OvLio=) Stores promotion budget data |
| [dbo.Promotion­Classes](#2hsG62388LC8A5b97+xZe9r4UMo=) Stores promotion classes data |
| [dbo.Promotion­Item­Groups](#c0MmZtsKwdrDgwPAo2ndXfOrz0Y=) Stores promotion item groups data |
| [dbo.Promotions­Approval­Log](#SGy7TYMOP/NBnL81y3jn1NxK7EQ=) Stores promotions approval log data |
| [dbo.Promotions­Approval­Setup](#90+q/v7bszARyHriSDoXZKwlMwo=) Stores promotions approval setup data |
| [dbo.Promotions­Cond­Un­Cod­Input](#moRfKWKKxvqNE2Doi2ji/8xPwHc=) Stores promotions cond un cod input data |
| [dbo.Promotions­Cond­Un­Cod­Output](#dU4i91hdnmipHSuJlIi31l0hOSM=) Stores promotions cond un cod output data |
| [dbo.Promotions­Customers­Groups­Link](#PfgcKuzix1YvrAoDK7vyTzqI3sA=) Stores promotions customers groups link data |
| [dbo.Promotions­Dont­Apply](#BKU6ZWcSVcnSxZKZfU6Gr3e9XlQ=) Stores promotions dont apply data |
| [dbo.Promotion­Selection­Groups](#YeVoFXZwuRdsrP712Ey9+k2+A1Q=) Stores promotion selection groups data |
| [dbo.Promotion­Selection­Groups­Link](#USeZXO58g/4Zm3Og8YxYnaxQwZE=) Stores promotion selection groups link data |
| [dbo.Promotions­Headers](#ahTdfFcl5CBnl0mrOXzm3bmregU=) Stores Promotions header records |
| [dbo.Promotions­Priorities](#vW9ydMaj0P2bPNmRT1PpK/4eQLU=) Stores promotions priorities data |
| [dbo.Promotions­Priorities­Link](#Np0/ZqZrivV6IB8LjYQMF2iM4qc=) Stores promotions priorities link data |
| [dbo.Promotions­Range­Input](#o/2bus5UXETkiOnP2HaUI1MvD7g=) Stores promotions range input data |
| [dbo.Promotions­Salesman­Groups­Link](#zCBQdTgqUpkOg50esUjauHPHRbA=) Stores promotions salesman groups link data |
| [dbo.Promotion­Types](#thgdRbS7z02VuhEURESkGGfvNfM=) Stores promotion types data |
| [dbo.Prompt­Embeddings](#wNbOmlP3RuSxgFaXcREtV7sZUnY=) Stores prompt embeddings data |
| [dbo.Prospective­Customers](#QwqkjSfpb3x+znCX5SBEksY/jeE=) Stores prospective customers data |
| [dbo.Prosto­Soft­Accounts](#3RKCCQAk3VgvESOHcKk0o9+kjFg=) Stores prosto soft accounts data |
| [dbo.Receipt­Requests](#xrtsEQ83UqlUIsYbDFnXZaEJ7XA=) Stores receipt requests data |
| [dbo.Receipt­Requests­Invoices­Link](#nQFsdCt8LJX8uqxEhG0eEtDkK1w=) Stores receipt requests invoices link data |
| [dbo.Receipt­Requests­Schedule](#B7XJUWf4UTvzmgiMyupMtdy8Ztk=) Stores receipt requests schedule data |
| [dbo.Receipts](#HG1TRL9sPjSgLFh35//BPsYmHtk=) Stores receipts data |
| [dbo.Receipts\_­Branches](#OIufxbGwtMvdriQ59bgFiQx3zUQ=) Stores receipts branches data |
| [dbo.Receipts\_­Currency](#TqehSG1LdOqUVFEfZwHVHowXUNg=) Stores receipts currency data |
| [dbo.Receipts\_­Paid­Trans](#YZyADzOSNwQ9jkByvLCyZzZS9XI=) Stores receipts paid trans data |
| [dbo.Receipts\_­Paid­Trans­Checks](#bHToTMwalykbikVR5EwFO94Anm0=) Stores receipts paid trans checks data |
| [dbo.Rec­Link­Inv](#qiqamgSu+oyk6+DDOURyxKXvmrs=) Stores rec link inv data |
| [dbo.Report5Customers­Excemptions](#dpGHdKSJXnVvtjB+8f8bRa8A8b8=) Stores report 5 customers excemptions data |
| [dbo.Reprinted­Transactions](#dPbV670c8Cw59t1RL9HSsw3lvlM=) Stores reprinted transactions data |
| [dbo.Reprint­Reasons](#BmIpENCX8UPPP42kgYWU2hnd3ns=) Stores reprint reasons data |
| [dbo.Request­Salesman­No­Transaction](#x0dXHi3aPR3tbKQRnHNzpIz+khE=) Stores request salesman no transaction data |
| [dbo.Request­Salesman­Will­Not­Visit](#yf/DJApG5OxZOEQzjm47GGaLFDs=) Stores request salesman will not visit data |
| [dbo.Request­To­Add­Discount](#c7fjcyg7CPYs6vT87GgzAI/zC/Y=) Stores request to add discount data |
| [dbo.Request­To­Add­Discount­In­Order](#2wvTqlLgW9Zz1ov5nriRnCTaVlc=) Stores request to add discount in order data |
| [dbo.Request­To­Add­Drawer](#B4mQ9vHH0dlWVg2wZblspnsGKbw=) Stores request to add drawer data |
| [dbo.Request­To­Add­Extra­Bonus](#HwoB6Hf8FhZ6EpGEjnitrljTWm8=) Stores request to add extra bonus data |
| [dbo.Request­To­Add­Extra­Bonus­And­Discount](#2DNt79S0zsUJbZ0JpiH7+KPRfPQ=) Stores request to add extra bonus and discount data |
| [dbo.Request­To­Add­New­Customer](#kK9CjmAiL4bGrLq5lA4EF3SpM2U=) Stores request to add new customer data |
| [dbo.Request­To­Allow­Take­Checks­From­Customer](#EhZxSr2sNDSxpVES1KtJIy3qoQU=) Stores request to allow take checks from customer data |
| [dbo.Request­To­Approve­Promotion](#pQ6HwEn2SmwM1uYR5CoBxuewGVk=) Stores request to approve promotion data |
| [dbo.Request­To­Approve­Promotion­Details](#MJwSqSw6b4wqKAsCh0Gl0vxz7JM=) Stores Request To Approve Promotion detail line records |
| [dbo.Request­To­Cancel­Payment](#t6ros/89r3YsW14Uljyh5Qpa6JE=) Stores request to cancel payment data |
| [dbo.Request­To­Change­Delivery­Payment­Type](#x/xDAbXoDyU9RQK12zeTqVUsZS0=) Stores request to change delivery payment type data |
| [dbo.Request­To­Change­Invoice­Payment­Type](#0XwtlNT/Ckm4h/0PEsyIn7uukq0=) Stores request to change invoice payment type data |
| [dbo.Request­To­Change­Item­Sell­Price](#vBzpo6b8qr6UyNJD9mPUDANQ/ds=) Stores request to change item sell price data |
| [dbo.Request­To­Exceed­Check­Due­Date](#Q4oDP+TS7YSdmpl7YykbSpixfDY=) Stores request to exceed check due date data |
| [dbo.Request­To­Exceed­Chq­Limit](#IbmIH5b8Fyg1nSgWenoSMQ0zZxk=) Stores request to exceed chq limit data |
| [dbo.Request­To­Exceed­Customer­Credit­Limit](#y00gq/Op1M/p3d3xft8MLh/pitI=) Stores request to exceed customer credit limit data |
| [dbo.Request­To­Exceed­Customer­Credit­Limit­In­Order](#IfleRHbzb+Guajs2gVXZY7iTjPA=) Stores request to exceed customer credit limit in order data |
| [dbo.Request­To­Exceed­Customer­Invoice­Due­Days](#JSBHUGAPkCSLqoAx3K9oJ1b+DqA=) Stores request to exceed customer invoice due days data |
| [dbo.Request­To­Exceed­Customer­Invoice­Due­Days­In­Order](#gGY9uFtDYk+fQtmwuA7uEOcAoDA=) Stores request to exceed customer invoice due days in order data |
| [dbo.Request­To­Exceed­Customer­Visit­Order](#pT7Uvu8A9xZVKtb/IQmtA7yNEY4=) Stores request to exceed customer visit order data |
| [dbo.Request­To­Exceed­Finish­All­Tasks](#FLj6EKzFFOnU/pCgRzmYNgl28Qg=) Stores request to exceed finish all tasks data |
| [dbo.Request­To­Exceed­Invoice­Amount](#y5u1tuMak14qvZwgtloka/XaA8U=) Stores request to exceed invoice amount data |
| [dbo.Request­To­Exceed­Invoice­Count](#LEHX9odsujuhFtL+Dx3+pX2V5BU=) Stores request to exceed invoice count data |
| [dbo.Request­To­Exceed­Pay­Invoice­Discount](#l/4pYdYwVtwwfBnLLpLD6mhJkio=) Stores request to exceed pay invoice discount data |
| [dbo.Request­To­Exceed­Pay­Over­Balance](#wY7U232y32maUymHRYyho4NyVN0=) Stores request to exceed pay over balance data |
| [dbo.Request­To­Exceed­Salesman­Credit­Limit](#UyhnrT7eTYvd28FGfUiFW7Y/ViY=) Stores request to exceed salesman credit limit data |
| [dbo.Request­To­Increase­Customer­Creditlimit](#IGnM5CFGpIe5zoBfkQLWJm5Wjeo=) Stores request to increase customer creditlimit data |
| [dbo.Request­To­Link­Customer­To­Salesman](#ED6bsVkYov7GnbUA+yS9oaU5Nxs=) Stores request to link customer to salesman data |
| [dbo.Request­To­Login­To­Customer­Without­Verficiation](#yVGIquflnrJEVbzdnFPlRIdguu4=) Stores request to login to customer without verficiation data |
| [dbo.Request­To­Make­Transaction­To­Suspended­Customer](#LJdKF5gpHZ3kawJ2a+f0DfIIklA=) Stores request to make transaction to suspended customer data |
| [dbo.Request­To­Make­Zero­Amount­Invoice](#ANPt2sOQR+io3/w6vVxrBDQ3n+A=) Stores request to make zero amount invoice data |
| [dbo.Request­To­Return­Invoice](#UcHM7GZoCvgSTGtzdOUFzC8h7Ek=) Stores request to return invoice data |
| [dbo.Request­To­Visit­Customer­Not­In­Route](#NhMPLUk/wajOlIn2EYygDV9Vk7A=) Stores request to visit customer not in route data |
| [dbo.Request­To­Void­Transaction](#QNHZsHqjpoU7xXvEkRyJ/MhI2Vo=) Stores request to void transaction data |
| [dbo.Return­Orders­Details](#tGWQYCGhh1nRhQULT5vFZjdxxWE=) Stores Return Orders detail line records |
| [dbo.Return­Orders­Headers](#437+uqToRlwutPBVm9jW7LjF9Zw=) Stores Return Orders header records |
| [dbo.Routes­Information](#/xmJfUelVYBo8GKROYRcdBbYMXI=) Stores routes information data |
| [dbo.Sales­Acheivment­Grades](#9peuhZIhmfCSSb669jdu8nYT27E=) Stores sales acheivment grades data |
| [dbo.Salesman­Cash­Settlement](#A3Ze00S/MkJFI1vQ80E29PNEDxs=) Stores salesman cash settlement data |
| [dbo.Sales­Order­Delivery­DF](#VuY/d3vkxQq/0JH26G0rgxxFPyk=) Stores Sales Order Delivery detail line records |
| [dbo.Sales­Order­Delivery­HF](#qRLoKEH9diIGs2TNgiZZ7vtSjFI=) Stores Sales Order Delivery header records |
| [dbo.Sales­Order­History­DF](#qBw3AmOajuI4ZtTfIaeni/zc3wY=) Stores Sales Order History detail line records |
| [dbo.Sales­Order­History­HF](#11q66Ezr043bQzejB8gB49aKpFU=) Stores Sales Order History header records |
| [dbo.Sales­Person­Bonus­Limit](#C1uYOB84PFrspXSy5qKoxaKXPCI=) Stores sales person bonus limit data |
| [dbo.Salesperson­Class­Target](#TDaq2ODZxtZyYKdrvK32Q575+w0=) Stores salesperson class target data |
| [dbo.Sales­Person­Collections­Targets](#JTP7PMMGIAievJdaPLdev78LTd8=) Stores sales person collections targets data |
| [dbo.Sales­Person­Contracts­Assignment](#7IiGbcYKdVhPBZDU9h/hcmK+4UA=) Stores sales person contracts assignment data |
| [dbo.Sales­Person­Customer­Count­Targets­DF](#zQRC4m+pYMMqqHc3hKVGJAkNmNE=) Stores Sales Person Customer Count Targets detail line records |
| [dbo.Sales­Person­Customer­Count­Targets­HF](#744T5frnf46PgKvJ53r2PGxkXr0=) Stores Sales Person Customer Count Targets header records |
| [dbo.Salesperson­Customers­Visits­By­Date](#ryrW/R3zwQkZTt7Dq5OH7Gj29po=) Stores salesperson customers visits by date data |
| [dbo.Salesperson­Cust­Stock­Items­Assignment](#yRWQ/eGFZmSAxfgPzjyl0OHpXR8=) Stores salesperson cust stock items assignment data |
| [dbo.Salesperson­Cust­Stock­Items­Target­Link](#b43MQqzsQIjSEmPV4dGhxixPE80=) Stores salesperson cust stock items target link data |
| [dbo.Sales­Person­Group­Item­Bonus­Target](#HcQUHiJK27JxFeM1oZj8WD1Pd3s=) Stores sales person group item bonus target data |
| [dbo.Sales­Person­Group­Item­Qty­Limit](#eh0Sl1f8NzUsfZjaWwSJQxbiJw0=) Stores sales person group item qty limit data |
| [dbo.Sales­Person­Item­Bonus­Target](#jsqAVxC1rsxcfcgDv637S/bwxdE=) Stores sales person item bonus target data |
| [dbo.Sales­Person­Item­Bonus­Target­By­Customer](#YkdsttOxMcCRXWqEf5foOS0P2ZM=) Stores sales person item bonus target by customer data |
| [dbo.Sales­Person­Items­Assignment](#VuwAQqeQzVBaSiq8r6LvTWcyVK8=) Stores sales person items assignment data |
| [dbo.Sales­Person­Items­Balance](#9T4oIcwDSV9sblyeLCTJZLIovIw=) Stores sales person items balance data |
| [dbo.Sales­Person­Items­Balance­Batches](#MlyAb4F34gN1Blh3UWgdprc+vXM=) Stores sales person items balance batches data |
| [dbo.Sales­Person­Items­Sales­Units](#3MzdVrdzX61bodHXeIRVWWzhWK8=) Stores sales person items sales units data |
| [dbo.Sales­Person­Items­Use­In­Load­Order](#/QDiwv9QBQ4qeEE8yhe1yXblFrE=) Stores sales person items use in load order data |
| [dbo.Sales­Person­New­Customers­Targets](#p3JmCTvKj/vJ5EmW1eh2IOXJRxg=) Stores sales person new customers targets data |
| [dbo.Sales­Person­Notbook­Transactions­Serials](#e+PRii5n0NT+pWS852gO1uslxGE=) Stores sales person notbook transactions serials data |
| [dbo.Salesperson­Route­By­Date](#VVnqHqNCaDrgk1GD2DTAKh5jLeY=) Stores salesperson route by date data |
| [dbo.Sales­Persons](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) Stores sales persons data |
| [dbo.Sales­Persons­Additional­Routes](#9OcbZHe+sazSxVSzNHJR8XL4TOg=) Stores sales persons additional routes data |
| [dbo.Salespersons­Assistants](#0ccl2xEd8tya0kAz75PQRq0zNqs=) Stores salespersons assistants data |
| [dbo.Salespersons­Assistants­Transactions](#ZSVvmI9fqC/7OkEWS30QMh03its=) Stores salespersons assistants transactions data |
| [dbo.Salespersons­Daily­Currency­Totals](#/21iAMcdTThzgAYslIPf4msHv5s=) Stores salespersons daily currency totals data |
| [dbo.Sales­Persons­Device­Permissions](#HDNMxAbdbkV5fpjAqyo4w24NU/c=) Stores sales persons device permissions data |
| [dbo.Sales­Persons­Device­Reports­Permissions](#Vf8dhaEnUP3t5uK3DQLd/jYkWP0=) Stores sales persons device reports permissions data |
| [dbo.Sales­Persons­Discount­Early­Pay­Discount](#icILIOKf+poDmeDAulaQ4YiXznc=) Stores sales persons discount early pay discount data |
| [dbo.Salespersons­GPSTracking](#QxA0F85wkH9kLPC2YzJ4uhdflRY=) Stores salespersons gps tracking data |
| [dbo.Sales­Persons­Groups](#IJwFVeRoDj2cXKxVh0vr44Q0tYU=) Stores sales persons groups data |
| [dbo.Sales­Persons­Items­Groups](#T4bMH2XeiwZJ/HIYyvDM6ayjsI4=) Stores sales persons items groups data |
| [dbo.Salespersons­Messages](#BKy01fmBbj+QmGl0mkTlqzmT7wg=) Stores salespersons messages data |
| [dbo.Salespersons­Messages­Definition](#+jCuqD2Q4eGxFj57Vt8E/n1PBPw=) Stores salespersons messages definition data |
| [dbo.Sales­Person­Special­Targets](#tcpPVe+Vk1cMiSFngwYNzHbDI+s=) Stores sales person special targets data |
| [dbo.Salespersons­Procedures](#e3p1nLtjefdXbT8DiPHRcXjAhcI=) Stores salespersons procedures data |
| [dbo.Sales­Persons­Routes](#Vq4gNzt6u4MhYlXtbECPakGf1nE=) Stores sales persons routes data |
| [dbo.Salespersons­Security](#clLJ4yNXkQcHDjFKfGb5wTU3e+E=) Stores salespersons security data |
| [dbo.Salespersons­Send­Orders](#bq6yGRtjSg99m2OVUstLe+Lqq5Y=) Stores salespersons send orders data |
| [dbo.Sales­Person­Stock­Tacking](#OHlpZ7FSFtTE/XSxq3pv60j7SGg=) Stores sales person stock tacking data |
| [dbo.Sales­Person­Stock­Tacking­Details](#H/UlDqkOS9KOJUff9IUMgIsbEkQ=) Stores Sales Person Stock Tacking detail line records |
| [dbo.Salesperson­Target­Reference­Focus­Item](#WYbKrlC7+RwN9xA9ny4ZaeX+JUA=) Stores salesperson target reference focus item data |
| [dbo.Sales­Person­Targets](#jtTF4ZU/xg5jXQSLOvkiNqRWA2g=) Stores sales person targets data |
| [dbo.Sales­Person­Targets­Details](#+EBPf8dlg9429d47IgRNffnwI/8=) Stores Sales Person Targets detail line records |
| [dbo.Sales­Person­Targets­Off­Days](#oxsA99hb/pND29TlXTgQleCKXDc=) Stores sales person targets off days data |
| [dbo.Sales­Person­Transactions­Serials](#ROvwmUyKjfiWvnr8Bll8Oco+wTg=) Stores sales person transactions serials data |
| [dbo.Sales­Person­Transactions­Serials­Multi](#9G5nT8f9gX73t2TrnXm7luwi4s8=) Stores sales person transactions serials multi data |
| [dbo.Sales­Quotation­Details](#FqWGoGRiZatYMw+CyaI12AGNSvA=) Stores Sales Quotation detail line records |
| [dbo.Sales­Quotation­Headers](#vsiuN2f/+QOPd7ByOOecNSo/qlU=) Stores Sales Quotation header records |
| [dbo.Sales­Trans­Details](#Wo/QVdwjtHARrpuINGzfOyhSOoQ=) Stores Sales Trans detail line records |
| [dbo.Sales­Trans­Header](#3p+bEPlkIn0MCQiOwvpTiOLoKFg=) Stores Sales Trans header records |
| [dbo.Schedule­Delivery­Orders](#1xfUMAumu1dlMX51KnGp5Zb9uqI=) Stores schedule delivery orders data |
| [dbo.Seals­Transactions](#hwtpgkwEarqJAm1mKaNMIcOyPRo=) Stores seals transactions data |
| [dbo.SMTPEmail­Settings](#TYHXZ6JVNzeEsSQ1pyrzRC6HsIQ=) Stores smtp email settings data |
| [dbo.Special­Customer­Target](#u2a8B/4FOEUyFf//2NvGUOf+GHA=) Stores special customer target data |
| [dbo.Stock­Settelment­Collection](#ctn2Ecb88N86WnyJgpNIX6XqE4I=) Stores stock settelment collection data |
| [dbo.Stores­Balances](#iLOZQTKGDEk8/LjG4KA874MOQP8=) Stores stores balances data |
| [dbo.Survey­Customers](#t4jdXBCQM1hjU6qJkXaOQkRot9w=) Stores survey customers data |
| [dbo.Survey­Customers­Answers](#8Tmnx2axLQnbMD/nrrUAF70x4rA=) Stores survey customers answers data |
| [dbo.Survey­Customers­Link](#S5kPkbtMwOF21UU1T3TnphDNZME=) Stores survey customers link data |
| [dbo.Survey­Prospective­Customers](#VLbcdMdPKaxw25aZFRzeQGU2Suw=) Stores survey prospective customers data |
| [dbo.Survey­Prospective­Customers­Answers](#qTyZ8cyyBecKWjdTMqT8D2g2aYE=) Stores survey prospective customers answers data |
| [dbo.Surveys](#fNvXDUwEI42reNhV6GJ0DrgY+lY=) Stores surveys data |
| [dbo.Surveys\_­Questions](#bmgbYLzTtKX7dmB5qYiAKdJ8ilU=) Stores surveys questions data |
| [dbo.Surveys\_­Questions\_­Options](#3TaP0DMAUwTCOmz2Y/sjVOSyKO4=) Stores surveys questions options data |
| [dbo.Survey­Salesmans](#SKLEPzkj1BkgGhexsc6Oh8iz9KU=) Stores survey salesmans data |
| [dbo.Survey­Salesmans­Answers](#UDFYkFKW4zLWQwltf7Iw79Jccfg=) Stores survey salesmans answers data |
| [dbo.Survey­Sales­Persons­Assignment](#ugeuIznwGf6h0SfRTsFc1eo43Ho=) Stores survey sales persons assignment data |
| [dbo.System­Codes](#fmbVLwBOxzM8JMKPcjrkVPCOulo=) Stores system codes data |
| [dbo.Table\_1](#d5FXp3k+/xKQ/LE1wZmBAMxIG8E=) Stores table 1 data |
| [dbo.Tag­Codes](#2vhrsfu/gyaXaTOKzZIfgaVkEPE=) Stores tag codes data |
| [dbo.Targets­References](#pTJEdyfW1its0oUM5wpR5Npe6Js=) Stores targets references data |
| [dbo.Targets­Types](#0/4snZsACLzbPDsnGKCgpJuaMnM=) Stores targets types data |
| [dbo.Tax­Codes](#2aMH2GTeQ0/nMkE2YLc55f3SnEE=) Stores tax codes data |
| [dbo.Tech\_­Customization­Performed­Tasks](#g7Oh16vjCIqeQ5hvg9ozNeFeeYs=) Stores tech customization performed tasks data |
| [dbo.Technical\_­CFD\_temp](#L482cRnBkiyO555PVo3ptZrWkEQ=) Stores technical cfd temp data |
| [dbo.Technical­Financial­Insert­Table\_­Temp](#9aRzF17ExuPNtqYR9ZEA9vLMF+o=) Stores technical financial insert table temp data |
| [dbo.Territories](#f/nEqxjjd80P8fRBayc6oACm5sQ=) Stores territories data |
| [dbo.Transactions­Batchs­Items­Info](#rNcxMl40YV3QTtQxGvLUSrGGmxA=) Stores transactions batchs items info data |
| [dbo.Transactions­Batchs­Items­Invoice­Link](#ZBHzaGwbXViQluujceOjrJ29rkQ=) Stores transactions batchs items invoice link data |
| [dbo.Transactions­Details](#QJXPDZNOgNNitwQP2NnfyCdC89c=) Stores Transactions detail line records |
| [dbo.Transactions­Headers](#GZhiGjtXLJ5ft4FPZAin/6qox5k=) Stores Transactions header records |
| [dbo.Transactions­Images](#y2TZ3xwBzPdOu0tR8OJadba5/cA=) Stores transactions images data |
| [dbo.Transactions­Promotions](#QlfQHR4HRki/ih0Fcr4QZbBuU2E=) Stores transactions promotions data |
| [dbo.Transactions­Serials](#u7uWokIxaXe84YeHIDtOVbwwWXU=) Stores transactions serials data |
| [dbo.Transactions­Suggested­Items](#Nrpi5A2Ng1vPyD/RTPvDgbpPwiE=) Stores transactions suggested items data |
| [dbo.Transactions­Types](#5KHGGmOv19tzIe7dNJ3JOc6tR1w=) Stores transactions types data |
| [dbo.Transfers­Order\_­Auto](#lGv9mdFzZxjFVCVRHII8LfLmlHM=) Stores transfers order auto data |
| [dbo.Transfers­Orders­Details](#RTZqtyr0VqJMPJNIDu5SdEzL3+M=) Stores Transfers Orders detail line records |
| [dbo.Transfers­Orders­Details\_­Error­Qty](#JmwxZz1WnK16Gg4Bqa4KOUN/v4Q=) Stores transfers orders details error qty data |
| [dbo.Transfers­Orders­Headers](#HROFEZUB00Khi58CJy9R53BF/wI=) Stores Transfers Orders header records |
| [dbo.User­Activity](#ZXiT3qlYL1AF7hBWNWe5AqQ2220=) Stores user-related data for User­Activity |
| [dbo.User­Company­Branches­Link](#QaI/ZAvryikiKsaJnD6GXz+HMWg=) Stores user-related data for User­Company­Branches­Link |
| [dbo.User­Customers­Promotions­Group­Link](#WU1Xx3D2xgps3oHKR8vFzNrZyg8=) Stores user-related data for User­Customers­Promotions­Group­Link |
| [dbo.User­Promotions­Link](#srTVT5mhbZp3cnVpZAFhKER2cMM=) Stores user-related data for User­Promotions­Link |
| [dbo.Users](#xK94j3lvTOeFWmPRc97loDl7d/s=) Stores user-related data for Users |
| [dbo.Users­Close­Date](#9Ug1O3PLnPQmQYl2YwMynS6Mp/w=) Stores user-related data for Users­Close­Date |
| [dbo.Users­Favorite­Menu](#LcTj+69+3JVSwHqeu6IhuNPGq4o=) Stores user-related data for Users­Favorite­Menu |
| [dbo.Users­Groups](#KDsSfvwpkrBNASfe9IQSaouPrJw=) Stores user-related data for Users­Groups |
| [dbo.Users­Groups­Link](#kZJ1TXzn7dTa0q4T3wVq0826Ezc=) Stores user-related data for Users­Groups­Link |
| [dbo.Vacations](#g1ad77UHw5EPOZgX6Aybk8YFQI8=) Stores vacations data |
| [dbo.Van­Transfer­Details](#nR0XPybxuWIChYMtokbRWVHNUTI=) Stores Van Transfer detail line records |
| [dbo.Van­Transfer­Header](#p4970K6/GvlyIDOTHceKMW96gPw=) Stores Van Transfer header records |
| [dbo.Verification­Codes](#ieASLQHM6pxc+AX3zPyz69td5Hc=) Stores verification codes data |
| [dbo.WF\_­Functions](#R6akNrGibdwM/6sX4OhptH8w0Bc=) Stores wf functions data |
| [dbo.WF\_­Master­Log](#R2S9JBN1K6Z+s503zfGMaQDR7eI=) Stores wf master log data |
| [dbo.WF\_­Positions­Ver](#URBjOJnKzhdDUh62DxOuxQ7B05U=) Stores wf positions ver data |
| [dbo.WF\_­Sales­Person­Items­Category­Values](#z+ZSL3nZi05xvU21Si3TOQZ2BwE=) Stores wf sales person items category values data |
| [dbo.WF\_­Setup­Details](#IrdvlRjLLZ8r8Kz4M64qRls3ihw=) Stores WF Setup detail line records |
| [dbo.WF\_­Setup­Header](#jTJzILI7QzyFMo/CaFcnOUl5LFo=) Stores WF Setup header records |
| [dbo.WF\_­Sub­Log](#KAMPrc9v+fSg4qOhDW6lcJz0ovk=) Stores wf sub log data |
| [dbo.WFMobile­Permission­Definition](#GIy1Yc7+JJ3KWSLtXubpwoDobNM=) Stores wf mobile permission definition data |
| [dbo.WFMobile­Permission­Link](#tlN7PcuxEJsWyMwFgD8bM3SxXRM=) Stores wf mobile permission link data |
| [dbo.Widget\_­Functions](#TZyP/g7gTX3UZgcjQiBHriQuFQg=) Stores widget functions data |
| [dbo.Widget\_­User\_­Log­Action](#OsIyNY2lcWgiY8r8Wg7R9sfJiN0=) Stores widget user log action data |
| [dbo.Wieght­Targets](#F61qYo+qw8TSN9BSAtlV5sCQLuQ=) Stores wieght targets data |
| [dbo.Zatca­Company](#TOto/3x8E1kJErtya6KtmSb4OeI=) Stores zatca company data |
| [dbo.Zatca­Customer](#y401Xrdzpy+fpzriuOOheecyDGU=) Stores zatca customer data |
| [dbo.Zatca­Mode](#43xAqIvixFpvcOWecM3g8ZXHZbg=) Stores zatca mode data |
| [dbo.Zatca­Result­Generate­Xml](#m03CiJX+rnllmOVL6GIZfaYQz98=) Stores zatca result generate xml data |
| [dbo.Zatca­Sales­Persons](#xi8A0aZN83ZU9/OBci5GKdjfCog=) Stores zatca sales persons data |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Activity­List] |

MS\_­Description

This table contains predefined activities that sales representatives can perform during customer visits such as merchandising, surveys, stock checks, and promotional tasks.

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| Activity­Desc Activity description | nvarchar(100) | 200 | NULL allowed |
| Activity­No Activity number | smallint | 2 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Add\_­Customer] |

MS\_­Description

Sales representatives can register new customers from the field.
These records are stored here until they are reviewed and officially added to the Customers master table.

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| Company­ID Company identifier | smallint | 2 | NOT NULL |
| Name Name | nvarchar(200) | 400 | NULL allowed |
| Type­ID Type identifier | int | 4 | NULL allowed |
| Location­ID Location identifier | int | 4 | NULL allowed |
| Salesmanno Salesmanno | int | 4 | NULL allowed |
| Payment­Type Payment type | int | 4 | NULL allowed |
| Pricelist Pricelist | int | 4 | NULL allowed |
| Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |
| Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |
| ISAdded Flag indicating added | bit | 1 | NULL allowed |
| Number Number | int | 4 | NULL allowed |
| Customer­Promotiongroup­ID Customer promotiongroup identifier | int | 4 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Add­Discount­To­Customer­Orders] |

MS\_­Description

This table maintains the master records of company-owned assets used to support sales and merchandising activities in the market. Assets may be assigned to customers, tracked by serial numbers, and monitored through transactions such as delivery, transfer, or withdrawal.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Trans­ID Trans identifier | bigint | 8 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NOT NULL |  |
|  | Customer­ID Customer identifier | bigint | 8 | NULL allowed |  |
|  | Sales­Person­ID Sales identifier | int | 4 | NULL allowed |  |
|  | Categ­Code Categ code | nvarchar(50) | 100 | NULL allowed |  |
|  | Discount­Amount Discount amount | float | 8 | NULL allowed |  |
|  | Notes Notes | nvarchar(max) | max | NULL allowed |  |
|  | Tr­Date­Time Tr date time | smalldatetime | 4 | NULL allowed |  |
|  | WFApproved Wf approved | bit | 1 | NULL allowed |  |
|  | Posted­To­ERP Posted to erp | bit | 1 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Assets] |

MS\_­Description

This table maintains the master records of company-owned assets used to support sales and merchandising activities in the market. Assets may be assigned to customers, tracked by serial numbers, and monitored through transactions such as delivery, transfer, or withdrawal.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company ID | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Asset­ID Asset ID | bigint | 8 | NOT NULL |
|  | Asset­Name Asset name | varchar(500) | 500 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(50) | 100 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(50) | 100 | NULL allowed |
|  | Asset­Type Asset type | int | 4 | NULL allowed |
| ![](data:image/png;base64...) | Asset­Serial Asset serial | nvarchar(50) | 100 | NULL allowed |
|  | Status Status | int | 4 | NULL allowed |
|  | Notes Notes | nvarchar(500) | 1000 | NULL allowed |
|  | Asset­Value Asset value | float | 8 | NULL allowed |
|  | Asset­Volume Asset volume | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Assets\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Assets­Customer­Link] |

MS\_­Description

This table is used to identify which customer is currently linked to or holding a specific asset. It helps the system know where the asset is deployed and who is responsible for it.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Asset­ID Asset identifier | bigint | 8 | NOT NULL |
|  | Customer­ID Customer identifier | bigint | 8 | NULL allowed |
|  | Contact­ID Contact identifier | bigint | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Assets­Transactions] |

MS\_­Description

This table records all movements and operational events related to assets, such as delivery, withdrawal, transfer, and assignment. It provides the transactional history of each asset.Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |  |
| ![](data:image/png;base64...) | Trans­ID Trans identifier | numeric(18,0) | 9 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...) | Asset­ID Asset identifier | bigint | 8 | NOT NULL |  |
|  | Trans­Type Trans type | smallint | 2 | NULL allowed |  |
|  | Trans­Date Trans date | smalldatetime | 4 | NULL allowed |  |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NULL allowed |  |
|  | Contract­No Contract number | nvarchar(50) | 100 | NULL allowed |  |
|  | Contract­Date Contract date | smalldatetime | 4 | NULL allowed |  |
| ![](data:image/png;base64...) | User­ID User identifier | nvarchar(50) | 100 | NULL allowed |  |
| ![](data:image/png;base64...) | Salesman­No Salesman number | int | 4 | NULL allowed |  |
|  | Withdrawal­Reason Withdrawal reason | int | 4 | NULL allowed |  |
|  | Notes Notes | nvarchar(500) | 1000 | NULL allowed |  |
|  | Customer­Location­ID Customer location identifier | int | 4 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Asset­Amount Asset amount | float | 8 | NULL allowed |  |
|  | Ref­Trans­ID Ref trans identifier | numeric(18,0) | 9 | NULL allowed |  |
|  | Store­No Store number | int | 4 | NULL allowed |  |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |  |
|  | Approved Flag indicating approved | bit | 1 | NULL allowed |  |
|  | Is­Transfer Flag indicating transfer | bit | 1 | NULL allowed |  |
|  | Contact­ID Contact identifier | bigint | 8 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Assets­Transactions\_­Assets | Company­ID->[[dbo].[Assets].[Company­ID]](#K6CNYc8TwLULZY65085UG364+KY=), Asset­ID->[[dbo].[Assets].[Asset­ID]](#K6CNYc8TwLULZY65085UG364+KY=) |
| FK\_­Assets­Transactions\_­Assets­Transactions | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |
| FK\_­Assets­Transactions\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Assets­Transactions\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Salesman­No->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |
| FK\_­Assets­Transactions\_­Users | User­ID->[[dbo].[Users].[User­ID]](#xK94j3lvTOeFWmPRc97loDl7d/s=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Assets­Warehouse­Transactions] |

MS\_­Description

This table records warehouse-level movements of company assets, such as issuing assets from stores, receiving them back, and transferring them between inventory locations.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |  |
| ![](data:image/png;base64...) | Trans­ID Trans identifier | numeric(18,0) | 9 | NOT NULL | 1 - 1 |
|  | Trans­Type Trans type | smallint | 2 | NULL allowed |  |
|  | Asset­ID Asset identifier | bigint | 8 | NULL allowed |  |
|  | Trans­Date Trans date | smalldatetime | 4 | NULL allowed |  |
|  | Assets­Trans­Ref Assets trans reference | numeric(18,0) | 9 | NULL allowed |  |
|  | Is­Transfer Flag indicating transfer | bit | 1 | NULL allowed |  |
|  | Ref­Trans­ID Ref trans identifier | numeric(18,0) | 9 | NULL allowed |  |
|  | Store­No Store number | int | 4 | NULL allowed |  |
|  | Qty Quantity | float | 8 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Balad\_­Add\_­Customer\_­Table] |

MS\_­Description

This table stores customer records entered through the Balad add-customer process, typically before being validated or synchronized with the main customer master.

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| Company­ID Company identifier | smallint | 2 | NOT NULL |
| Customer­ID Customer identifier | bigint | 8 | NULL allowed |
| Name Name | nvarchar(200) | 400 | NULL allowed |
| Type­ID Type identifier | int | 4 | NULL allowed |
| Location­ID Location identifier | int | 4 | NULL allowed |
| Salesmanno Salesmanno | int | 4 | NULL allowed |
| Payment­Type Payment type | int | 4 | NULL allowed |
| Pricelist Pricelist | int | 4 | NULL allowed |
| Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |
| Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |
| Address Address | nvarchar(max) | max | NULL allowed |
| ISAdded Flag indicating added | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Bank­Deposit­DF] |

MS\_­Description

This table stores the detail lines of bank deposit transactions, where each record represents a deposited receipt or payment linked to a deposit header

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Vou­Year Vou year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Vou­No Vou number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Rec­Year Rec year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Rec­Type Rec type | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Rec­No Rec number | int | 4 | NOT NULL |
|  | Rec­Amount Rec amount | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Bank­Deposit­DF\_­Bank­Deposit­HF | Company­ID->[[dbo].[Bank­Deposit­HF].[Company­ID]](#9e35+0qiczLeVUBKOOfACcL6BU4=), Vou­Year->[[dbo].[Bank­Deposit­HF].[Vou­Year]](#9e35+0qiczLeVUBKOOfACcL6BU4=), Vou­No->[[dbo].[Bank­Deposit­HF].[Vou­No]](#9e35+0qiczLeVUBKOOfACcL6BU4=) |
| FK\_­Bank­Deposit­DF\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Bank­Deposit­HF] |

MS\_­Description

This table stores the header information of bank deposit transactions, including the bank, branch, salesperson, deposit date, and approval or posting status.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Vou­Year Vou year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Vou­No Vou number | int | 4 | NOT NULL |
|  | Vou­Date Vou date | smalldatetime | 4 | NULL allowed |
| ![](data:image/png;base64...) | Salesperson­ID Salesperson identifier | int | 4 | NULL allowed |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Bank­No Bank number | int | 4 | NULL allowed |
| ![](data:image/png;base64...) | Branch­No Branch number | int | 4 | NULL allowed |
|  | Notes Notes | nvarchar(500) | 1000 | NULL allowed |
|  | Tr­Date­Time Tr date time | smalldatetime | 4 | NULL allowed |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |
|  | Is­Posted­To­ERP Flag indicating posted to erp | bit | 1 | NULL allowed |
|  | Tab­Sys­ID Tab sys identifier | nvarchar(50) | 100 | NULL allowed |
|  | Approve Flag indicating approve | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Bank­Deposit­HF\_­Banks | Company­ID->[[dbo].[Banks].[Company­ID]](#PYH+j4Qz5uStxKmaxbJgMvXBdEw=), Bank­No->[[dbo].[Banks].[ID]](#PYH+j4Qz5uStxKmaxbJgMvXBdEw=) |
| FK\_­Bank­Deposit­HF\_­Branches | Company­ID->[[dbo].[Branches].[Company­ID]](#BMb4NUvwYVL/5aaAQB++QZZcgeI=), Bank­No->[[dbo].[Branches].[Bank­ID]](#BMb4NUvwYVL/5aaAQB++QZZcgeI=), Branch­No->[[dbo].[Branches].[ID]](#BMb4NUvwYVL/5aaAQB++QZZcgeI=) |
| FK\_­Bank­Deposit­HF\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Bank­Deposit­HF\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Salesperson­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Banks] |

MS\_­Description

This table stores the master list of banks used in the system for financial transactions such as deposits, collections, and settlements.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Short­Name Short name | nvarchar(100) | 200 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Banks\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Banks­Accounts] |

MS\_­Description

This table stores the bank accounts associated with each bank and is used to identify the valid accounts used in deposit and financial operations.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Bank­ID Bank identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Account­Number Account number | nvarchar(100) | 200 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Banks­Accounts\_­Banks | Company­ID->[[dbo].[Banks].[Company­ID]](#PYH+j4Qz5uStxKmaxbJgMvXBdEw=), Bank­ID->[[dbo].[Banks].[ID]](#PYH+j4Qz5uStxKmaxbJgMvXBdEw=) |
| FK\_­Banks­Accounts\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Batchs­Items­Info] |

MS\_­Description

This table stores batch-level item information such as batch number, expiry date, quantity, and barcode for inventory tracking and expiry control.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­No Item number | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...) | Batch­No Batch number | varchar(100) | 100 | NOT NULL |
|  | Expire­Date Expire date | smalldatetime | 4 | NULL allowed |
|  | Qty Quantity | money | 8 | NULL allowed |
|  | Ref1 Ref 1 | varchar(100) | 100 | NULL allowed |
|  | Ref2 Ref 2 | varchar(100) | 100 | NULL allowed |
|  | Batch­Barcode Batch barcode | varchar(100) | 100 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Batchs­Items­Info\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Batchs­Items­Info\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­No->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Branches] |

MS\_­Description

This table stores bank branch information used in financial transactions and deposit processing.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Bank­ID Bank identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Short­Name Short name | nvarchar(10) | 20 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |
|  | Account­Number Account number | nvarchar(50) | 100 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Branches\_­Banks | Company­ID->[[dbo].[Banks].[Company­ID]](#PYH+j4Qz5uStxKmaxbJgMvXBdEw=), Bank­ID->[[dbo].[Banks].[ID]](#PYH+j4Qz5uStxKmaxbJgMvXBdEw=) |
| FK\_­Branches\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Business­Units] |

MS\_­Description

This table stores the company’s organizational business units, supporting hierarchical operational structures such as divisions, departments, or branches.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Parent Parent | int | 4 | NULL allowed |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Short­Name Short name | nvarchar(50) | 100 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |
|  | Level Level | int | 4 | NULL allowed |
| ![](data:image/png;base64...) | Company­Branche­ID Company branche identifier | int | 4 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Business­Units\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Business­Units\_­Company­Branches | Company­ID->[[dbo].[Company­Branches].[Company­ID]](#QtIx7cCe02/M8Iq2UstqD1tTYh4=), Company­Branche­ID->[[dbo].[Company­Branches].[ID]](#QtIx7cCe02/M8Iq2UstqD1tTYh4=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Car­And­Salesperson­Link] |

MS\_­Description

This table links vehicles with salespersons, drivers, and assistants for specific working dates to track field team transportation assignments.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(18,0) | 9 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Car­ID Car identifier | int | 4 | NULL allowed |  |
|  | Working­Date Working date | smalldatetime | 4 | NULL allowed |  |
|  | Driver­ID Driver identifier | int | 4 | NULL allowed |  |
|  | Salesperson­ID Salesperson identifier | int | 4 | NULL allowed |  |
|  | Assistant­ID Assistant identifier | int | 4 | NULL allowed |  |
|  | Location­ID Location identifier | int | 4 | NULL allowed |  |
|  | Barcode Barcode | nchar(10) | 20 | NULL allowed |  |
|  | Finish­Working­Date Finish working date | smalldatetime | 4 | NULL allowed |  |
|  | Note Note | nvarchar(max) | max | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Catalog­Media] |

MS\_­Description

This table stores media files used in catalogs, such as images, documents, or other resources displayed within the system.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |  |
|  | Name Name | nvarchar(max) | max | NULL allowed |  |
|  | File­Path File path | nvarchar(max) | max | NULL allowed |  |
|  | File­Type File type | smallint | 2 | NOT NULL |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Catalog­Media\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Checks] |

MS\_­Description

This table stores check records used in customer collections, payment processing, and financial settlement operations.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Bank­ID Bank identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Branch­ID Branch identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Transaction­Year Transaction year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Transaction­No Transaction number | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Transaction­Type­ID Transaction type identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Cheque­No Cheque number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Drawer­ID Drawer identifier | int | 4 | NULL allowed |
|  | Due­Date Due date | smalldatetime | 4 | NULL allowed |
|  | Amount Amount | float | 8 | NULL allowed |
|  | Foreign­Amount Foreign amount | float | 8 | NULL allowed |
| ![](data:image/png;base64...) | Currency­ID Currency identifier | smallint | 2 | NULL allowed |
|  | Exchange­Rate Exchange rate | float | 8 | NULL allowed |
|  | Check­Status Check status | smallint | 2 | NULL allowed |
|  | Change­Status­Date Change status date | smalldatetime | 4 | NULL allowed |
|  | Is­Gero Flag indicating gero | bit | 1 | NULL allowed |
|  | Cust­Bank­Acc­No Cust bank acc number | varchar(200) | 200 | NULL allowed |
|  | AC\_­Payee Ac payee | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Checks\_­Banks | Company­ID->[[dbo].[Banks].[Company­ID]](#PYH+j4Qz5uStxKmaxbJgMvXBdEw=), Bank­ID->[[dbo].[Banks].[ID]](#PYH+j4Qz5uStxKmaxbJgMvXBdEw=) |
| FK\_­Checks\_­Branches | Company­ID->[[dbo].[Branches].[Company­ID]](#BMb4NUvwYVL/5aaAQB++QZZcgeI=), Bank­ID->[[dbo].[Branches].[Bank­ID]](#BMb4NUvwYVL/5aaAQB++QZZcgeI=), Branch­ID->[[dbo].[Branches].[ID]](#BMb4NUvwYVL/5aaAQB++QZZcgeI=) |
| FK\_­Checks\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Checks\_­Currencies | Currency­ID->[[dbo].[Currencies].[ID]](#k0NURIzYF8aeO/uxKYIEdxSccAg=) |
| FK\_­Checks\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |
| FK\_­Checks\_­Drawers | Company­ID->[[dbo].[Drawers].[Company­ID]](#wNA1/7+fkspPVPr8ZtNm55GqVVs=), Customer­ID->[[dbo].[Drawers].[Customer­ID]](#wNA1/7+fkspPVPr8ZtNm55GqVVs=), Drawer­ID->[[dbo].[Drawers].[ID]](#wNA1/7+fkspPVPr8ZtNm55GqVVs=) |
| FK\_­Checks\_­Receipts | Company­ID->[[dbo].[Receipts].[Company­ID]](#HG1TRL9sPjSgLFh35//BPsYmHtk=), Transaction­Type­ID->[[dbo].[Receipts].[Transaction­Type­ID]](#HG1TRL9sPjSgLFh35//BPsYmHtk=), Transaction­Year->[[dbo].[Receipts].[Transaction­Year]](#HG1TRL9sPjSgLFh35//BPsYmHtk=), Transaction­No->[[dbo].[Receipts].[Transaction­No]](#HG1TRL9sPjSgLFh35//BPsYmHtk=) |
| FK\_­Checks\_­Transactions­Types | Transaction­Type­ID->[[dbo].[Transactions­Types].[ID]](#5KHGGmOv19tzIe7dNJ3JOc6tR1w=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Class­Target­Rate] |

MS\_­Description

This table stores target rates or performance ratios related to specific classes, supporting KPI measurement and target evaluation.

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| Companyid Company identifier | int | 4 | NULL allowed |
| Class­ID Class identifier | int | 4 | NULL allowed |
| Class­Name Class name | nvarchar(100) | 200 | NULL allowed |
| rate Rate | int | 4 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Clients] |

MS\_­Description

Stores the main information of clients registered in the system. Each record represents a client entity and contains the necessary data used for identification, configuration, and system access management. The table is mainly used to manage client records and support system operations related to client-based settings.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | ID ID identifier | smallint | 2 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Clients­Active] |

MS\_­Description

Stores the activation status of clients within the system. Each record indicates whether a specific client is currently active and allowed to use the system. The table is mainly used to manage client access, control system availability, and support licensing or subscription validation.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Client­ID Client identifier | smallint | 2 | NOT NULL |
|  | WF\_­Client­ID Wf client identifier | smallint | 2 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Clients­Active\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Clients­WFID] |

MS\_­Description

This table stores workflow-related identifiers linked to clients, supporting workflow setup or client-specific approval processes.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | ID ID identifier | smallint | 2 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Companies] |

MS\_­Description

This table stores the master list of companies defined in the system and acts as a core reference for company-based data segregation

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | ID ID identifier | smallint | 2 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Short­Name Short name | nvarchar(50) | 100 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |
|  | Address Address | nvarchar(200) | 400 | NULL allowed |
|  | Telephone­No Telephone number | nvarchar(50) | 100 | NULL allowed |
|  | Fax­No Fax number | nvarchar(50) | 100 | NULL allowed |
|  | POBox Po box | nvarchar(50) | 100 | NULL allowed |
|  | Web­Site Web site | nvarchar(100) | 200 | NULL allowed |
|  | Email Email | nvarchar(100) | 200 | NULL allowed |
|  | Logo Logo | image | max | NULL allowed |
|  | Notes Notes | nvarchar(300) | 600 | NULL allowed |
|  | Sales­Tax­Num Sales tax number | nvarchar(100) | 200 | NULL allowed |
| ![](data:image/png;base64...) | Currency­ID Currency identifier | smallint | 2 | NULL allowed |
|  | Server­Date Server date | smalldatetime | 4 | NULL allowed |
|  | Data­Size Data size | int | 4 | NULL allowed |
|  | Log­Size Log size | int | 4 | NULL allowed |
|  | Null­Data Null data | int | 4 | NULL allowed |
|  | Logo2 Logo 2 | image | max | NULL allowed |
|  | Water­Mark­Image Water mark image | image | max | NULL allowed |
|  | CID Cid | int | 4 | NULL allowed |
|  | Company­UID Company unique identifier | varchar(50) | 50 | NULL allowed |
|  | Sales­Tax­Serial Sales tax serial | nvarchar(100) | 200 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Companies\_­Currencies | Currency­ID->[[dbo].[Currencies].[ID]](#k0NURIzYF8aeO/uxKYIEdxSccAg=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Company­Branches] |

MS\_­Description

This table stores the branches that belong to each company and supports organizational and operational branch-level structure.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Short­Name Short name | nvarchar(100) | 200 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |
|  | Address Address | nvarchar(300) | 600 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Company­Branches\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Company­Parameters] |

MS\_­Description

Stores configuration parameters that control how the system behaves for each company. The table contains various settings such as operational flags, default values, integration options, financial rules, and system behavior controls. These parameters allow administrators to customize system functionality (for example pricing rules, posting behavior, workflow options, or integration settings) without modifying the application code. Each record represents a specific parameter linked to a company and is used by different modules of the system during sales, inventory, financial, and integration processes.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
|  | Auto­Send­Invoice­To­ERP Flag indicating auto send invoice to erp | bit | 1 | NULL allowed |
|  | Auto­Send­Return­Invoice­To­ERP Flag indicating auto send return invoice to erp | bit | 1 | NULL allowed |
|  | Auto­Send­Receipts­To­ERP Flag indicating auto send receipts to erp | bit | 1 | NULL allowed |
|  | Auto­Send­Order­To­ERP Flag indicating auto send order to erp | bit | 1 | NULL allowed |
|  | Auto­Send­Return­Order­To­ERP Flag indicating auto send return order to erp | bit | 1 | NULL allowed |
|  | Calc­Item­Balance Calc item balance | bit | 1 | NULL allowed |
|  | Serial­Type Serial type | int | 4 | NULL allowed |
|  | Use­Range­Price Flag indicating use range price | bit | 1 | NULL allowed |
|  | Lock­On­Send­Data Lock on send data | bit | 1 | NULL allowed |
|  | Number­Saved­Fraction Number saved fraction | int | 4 | NULL allowed |
|  | Trunc­Round­Value Trunc round value | int | 4 | NULL allowed |
|  | Lock­Edit­Approved­Trans Lock edit approved trans | bit | 1 | NULL allowed |
|  | Max­Record­In­Search Max record in search | int | 4 | NULL allowed |
|  | Enable­Pass­Policy Flag indicating enable pass policy | bit | 1 | NULL allowed |
|  | Pass­Length Pass length | int | 4 | NULL allowed |
|  | Max­Login Max login | int | 4 | NULL allowed |
|  | Time­Out­Login­On­Tab Time out login on tab | int | 4 | NULL allowed |
|  | Enable­Verification­Code Flag indicating enable verification code | bit | 1 | NULL allowed |
|  | Enable­Mac­Address­On­Tab Flag indicating enable mac address on tab | bit | 1 | NULL allowed |
|  | Pass­Expiry­Days Pass expiry days | int | 4 | NULL allowed |
|  | Activation­Code­Days Activation code days | int | 4 | NULL allowed |
|  | SMSLink Sms link | nvarchar(250) | 500 | NULL allowed |
|  | Use­Recaptcha­In­Login Flag indicating use recaptcha in login | bit | 1 | NULL allowed |
|  | Send­Cust­Visit­Exit­Note­By­Email Send cust visit exit note by email | bit | 1 | NULL allowed |
|  | Auto­Approve­Load­Order Flag indicating auto approve load order | bit | 1 | NULL allowed |
|  | Dash­Board­Step­Size Dash board step size | float | 8 | NULL allowed |
|  | Url­Sama­Service Url sama service | nvarchar(1000) | 2000 | NULL allowed |
|  | Url­Sama­Service­Json Url sama service json | nvarchar(1000) | 2000 | NULL allowed |
|  | Auto­Approve­Customer­GPS Flag indicating auto approve customer gps | bit | 1 | NULL allowed |
|  | Auto­Approve­WF Flag indicating auto approve wf | bit | 1 | NULL allowed |
|  | Use­Bonus­Target­By­Promotion Flag indicating use bonus target by promotion | bit | 1 | NULL allowed |
|  | Send­Cust­Reciepts­By­Email Send cust reciepts by email | bit | 1 | NULL allowed |
|  | Enable­WFSales­Order Flag indicating enable wf sales order | bit | 1 | NULL allowed |
|  | Enable­WFLoad­Order Flag indicating enable wf load order | bit | 1 | NULL allowed |
|  | Enable­WFUn­Load­Order Flag indicating enable wf un load order | bit | 1 | NULL allowed |
|  | Enable­WFReturn­Order Flag indicating enable wf return order | bit | 1 | NULL allowed |
|  | Use­Invoice­Settlement Flag indicating use invoice settlement | bit | 1 | NULL allowed |
|  | Invoice­Settlement­Date Invoice settlement date | smalldatetime | 4 | NULL allowed |
|  | Max­Load­Order­Confirm Max load order confirm | tinyint | 1 | NULL allowed |
|  | Allow­Water­Mark­Image Flag indicating allow water mark image | bit | 1 | NULL allowed |
|  | Allow­Bonus­With­Price Flag indicating allow bonus with price | bit | 1 | NULL allowed |
|  | Allow­Apply­All­Next­Promotion Flag indicating allow apply all next promotion | bit | 1 | NULL allowed |
|  | Allow­Zero­Amount­In­Recipt­Request Flag indicating allow zero amount in recipt request | bit | 1 | NULL allowed |
|  | Send­Void­Reciepts­By­Email Send void reciepts by email | bit | 1 | NULL allowed |
|  | Use­Promotions­Approve Flag indicating use promotions approve | bit | 1 | NULL allowed |
|  | Allow­Early­Repayment­Discount Flag indicating allow early repayment discount | bit | 1 | NULL allowed |
|  | Use­Item­Bonus­Target­Group Flag indicating use item bonus target group | bit | 1 | NULL allowed |
|  | Not­Allow­Duplicate­Item­In­Promotions Not allow duplicate item in promotions | bit | 1 | NULL allowed |
|  | Use­Date­In­Output­Group Flag indicating use date in output group | bit | 1 | NULL allowed |
|  | Manual­Insert­Salesman­ID Manual insert salesman identifier | bit | 1 | NULL allowed |
|  | Enable­WFSales­Quotation Flag indicating enable wf sales quotation | bit | 1 | NULL allowed |
|  | Use­Pass­Key­With­Time Flag indicating use pass key with time | bit | 1 | NULL allowed |
|  | Cust­Stock­Items­Target­By­Ref Cust stock items target by reference | bit | 1 | NULL allowed |
|  | Use­Basket­Items Flag indicating use basket items | bit | 1 | NULL allowed |
|  | Use­Promotion­WF Flag indicating use promotion wf | bit | 1 | NULL allowed |
|  | Use­New­Trans­Serials Flag indicating use new trans serials | bit | 1 | NULL allowed |
|  | Use­Max­Load­Order­Amount Flag indicating use max load order amount | bit | 1 | NULL allowed |
|  | Use­Bonus­Limit­In­WF Flag indicating use bonus limit in wf | bit | 1 | NULL allowed |
|  | Auto­Reject­Bonus­Limit­WF Flag indicating auto reject bonus limit wf | bit | 1 | NULL allowed |
|  | Passkey­By­Generated­Key Passkey by generated key | bit | 1 | NULL allowed |
|  | Phinix­Last­Session­ID Phinix last session identifier | varchar(50) | 50 | NULL allowed |
|  | Last­Master­Data­Job­Run­Time Last master data job run time | datetime | 8 | NULL allowed |
|  | Use­Increase­Credit­Limit­WFRequest Flag indicating use increase credit limit wf request | bit | 1 | NULL allowed |
|  | Use­Olives­Images­For­Customer­Gallery Flag indicating use olives images for customer gallery | bit | 1 | NULL allowed |
|  | Tow­Factor­Auth­Tablet­Admin­Login Tow factor auth tablet admin login | bit | 1 | NULL allowed |
|  | Use­Must­Update­Data­In­Send­Data Flag indicating use must update data in send data | bit | 1 | NULL allowed |
|  | Custom­Galary­Image­URL Custom galary image url | nvarchar(500) | 1000 | NULL allowed |
|  | Use­One­Login­At­Same­Time Flag indicating use one login at same time | bit | 1 | NULL allowed |
|  | Dont­Update­Layout­Settings Dont update layout settings | bit | 1 | NULL allowed |
|  | WF\_­Group­By­Requests Wf group by requests | bit | 1 | NULL allowed |
|  | Latitude Geographic latitude | varchar(50) | 50 | NULL allowed |
|  | Longitude Geographic longitude | varchar(50) | 50 | NULL allowed |
|  | Enable­Verification­Code­In­WF Flag indicating enable verification code in wf | bit | 1 | NULL allowed |
|  | Price­With­Tax Price with tax | bit | 1 | NULL allowed |
|  | Use­Sales­Order­Limit Flag indicating use sales order limit | bit | 1 | NULL allowed |
|  | Use­Accumulated­Amount Flag indicating use accumulated amount | bit | 1 | NULL allowed |
|  | Use­Payment­Type­In­Item Flag indicating use payment type in item | bit | 1 | NULL allowed |
|  | Open­Unload­Order­Date Open unload order date | bit | 1 | NULL allowed |
|  | Mobile­App­Version Mobile app version | varchar(50) | 50 | NULL allowed |
|  | Tax­Price­List Tax price list | int | 4 | NULL allowed |
|  | Use­WFRe­Assign Flag indicating use wf re assign | bit | 1 | NULL allowed |
|  | Show­Exceptions­Issues­Dash­Board Show exceptions issues dash board | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Company­Parameters\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Competitive­Items] |

MS\_­Description

Stores information about competitor products available in the market. The table is used to record and analyze competitive items, allowing the system to compare them with the company’s products for market analysis, pricing strategy, and sales reporting.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Competitive­Item­Code Competitive item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NULL allowed |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
| ![](data:image/png;base64...) | Categ­Code Categ code | nvarchar(20) | 40 | NULL allowed |
|  | Competitive­Company Competitive company | nvarchar(100) | 200 | NULL allowed |
|  | Item­Image Item image | image | max | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Competitive­Items\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Competitive­Items\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Competitive­Items\_­Items­Categories | Company­ID->[[dbo].[Items­Categories].[Company­ID]](#VLpTtrh4X181/GF+u73WO6VXNcU=), Categ­Code->[[dbo].[Items­Categories].[Categ­Code]](#VLpTtrh4X181/GF+u73WO6VXNcU=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Competitve­Items­Data­DF] |

MS\_­Description

Stores the detailed records of competitive items data collected during field visits. Each record contains information about competitor products such as item details, price, availability, or promotional status. The table is mainly used to support market analysis and help the company monitor competitor activity through data captured by sales representatives.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Tr­Year Tr year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Tr­No Tr number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Competitive­Item Competitive item | nvarchar(100) | 200 | NOT NULL |
|  | Qty Quantity | money | 8 | NULL allowed |
|  | Price Price | float | 8 | NULL allowed |
|  | Notes Notes | nvarchar(300) | 600 | NULL allowed |
|  | Item­Image Item image | image | max | NULL allowed |
|  | Shelf­Price Shelf price | float | 8 | NULL allowed |
|  | Retail­Price Retail price | float | 8 | NULL allowed |
|  | Whole­Sale­Price Whole sale price | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Competitve­Items­Data­DF\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Competitve­Items­Data­DF\_­Competitve­Items­Data­HF | Company­ID->[[dbo].[Competitve­Items­Data­HF].[Company­ID]](#xwPjLYIo+jJaGV7rij2frhvGio4=), Tr­Year->[[dbo].[Competitve­Items­Data­HF].[Tr­Year]](#xwPjLYIo+jJaGV7rij2frhvGio4=), Tr­No->[[dbo].[Competitve­Items­Data­HF].[Tr­No]](#xwPjLYIo+jJaGV7rij2frhvGio4=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Competitve­Items­Data­HF] |

MS\_­Description

Stores the header records of competitive items data collected during field visits. Each record represents a competitive data collection transaction performed by a salesperson at a specific customer or location, while the related detail records store the competitor item information. The table is mainly used to organize competitor data entries and link them with the salesperson, customer, and visit information for market analysis.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Tr­Year Tr year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Tr­No Tr number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Sales­Persons Sales persons | int | 4 | NULL allowed |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NULL allowed |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |
|  | Notes Notes | nvarchar(300) | 600 | NULL allowed |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |
|  | Tr­Date­Time Tr date time | smalldatetime | 4 | NULL allowed |
|  | Server­Date Server date | smalldatetime | 4 | NULL allowed |
|  | Is­Prospective­Customer Flag indicating prospective customer | bit | 1 | NULL allowed |
| ![](data:image/png;base64...) | Prospective­Customer­ID Prospective customer identifier | bigint | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Competitve­Items­Data­HF\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Competitve­Items­Data­HF\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |
| FK\_­Competitve­Items­Data­HF\_­Prospective­Customers | Company­ID->[[dbo].[Prospective­Customers].[Company­ID]](#QwqkjSfpb3x+znCX5SBEksY/jeE=), Prospective­Customer­ID->[[dbo].[Prospective­Customers].[ID]](#QwqkjSfpb3x+znCX5SBEksY/jeE=) |
| FK\_­Competitve­Items­Data­HF\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Persons->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Contract­Items] |

MS\_­Description

Stores the items associated with specific contracts in the system. Each record links a contract with the items included in the agreement, allowing the system to manage contract-based pricing, quantities, or conditions for those items during sales and operational processes.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Contract­ID Contract identifier | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |
|  | Max­Qty Max quantity | money | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Contract­Items\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Contract­Items\_­Contracts | Company­ID->[[dbo].[Contracts].[Company­ID]](#zSXpPHadqD7+V+akfh1GN7CwldI=), Contract­ID->[[dbo].[Contracts].[Contract­ID]](#zSXpPHadqD7+V+akfh1GN7CwldI=) |
| FK\_­Contract­Items\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Contract­Items\_­Items­Units | Company­ID->[[dbo].[Items­Units].[Company­ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=), Unit­ID->[[dbo].[Items­Units].[ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Contracts] |

MS\_­Description

Stores the main records of contracts created in the system. Each record represents a contract agreement between the company and a customer, defining terms such as contract period, conditions, and related details. The table is used to manage and track contractual agreements and link them with the corresponding items and transactions.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Contract­ID Contract identifier | nvarchar(100) | 200 | NOT NULL |
|  | Contract­Name Contract name | nvarchar(200) | 400 | NULL allowed |
|  | Start­Date Start date | smalldatetime | 4 | NULL allowed |
|  | End­Date End date | smalldatetime | 4 | NULL allowed |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Contracts\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Contracts\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Coupons­Books­Details] |

MS\_­Description

Stores the detailed records of coupon books issued in the system. Each record represents an individual coupon within a coupon book, including coupon number, status, and related information. The table is mainly used to track the usage, redemption, and management of coupons distributed to customers.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Book­ID Book identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Cuopon­Number Cuopon number | nvarchar(100) | 200 | NOT NULL |
|  | Cuopon­Barcode Cuopon barcode | nvarchar(100) | 200 | NULL allowed |
| ![](data:image/png;base64...) | Promotion­ID Promotion identifier | int | 4 | NULL allowed |
|  | Is­Used Flag indicating used | bit | 1 | NULL allowed |
|  | Used­In­Tr­Type Used in tr type | smallint | 2 | NULL allowed |
|  | Used­In­Tr­Year Used in tr year | smallint | 2 | NULL allowed |
|  | Used­In­Tr­No Used in tr number | int | 4 | NULL allowed |
|  | Exp­Date Exp date | smalldatetime | 4 | NULL allowed |
|  | Is­Posted Flag indicating posted | bit | 1 | NULL allowed |
|  | Customer­ID Customer identifier | bigint | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Coupons­Books­Details\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Coupons­Books­Details\_­Coupons­Books­Headers | Company­ID->[[dbo].[Coupons­Books­Headers].[Company­ID]](#0ON2VfRM0v9FQb1E8yKRDkUcwjA=), Book­ID->[[dbo].[Coupons­Books­Headers].[ID]](#0ON2VfRM0v9FQb1E8yKRDkUcwjA=) |
| FK\_­Coupons­Books­Details\_­Promotions­Headers | Company­ID->[[dbo].[Promotions­Headers].[Company­ID]](#ahTdfFcl5CBnl0mrOXzm3bmregU=), Promotion­ID->[[dbo].[Promotions­Headers].[ID]](#ahTdfFcl5CBnl0mrOXzm3bmregU=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Coupons­Books­Headers] |

MS\_­Description

Stores the main (header) records of coupon books created in the system. Each record represents a coupon book issued to a customer or sales entity and groups multiple coupon details under one book. The table is used to manage coupon book distribution, track issuance information, and link the book with its related coupon detail records.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Book­No Book number | nvarchar(100) | 200 | NULL allowed |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Coupons­Books­Headers\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Coupons­Books­Headers\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Currencies] |

MS\_­Description

Stores the master list of currencies used in the system for financial and sales transactions. Each record represents a currency with its related information, allowing the system to manage transactions in multiple currencies and support currency conversion and financial reporting.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | ID ID identifier | smallint | 2 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Short­Name Short name | nvarchar(10) | 20 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |
|  | Fraction Fraction | smallint | 2 | NULL allowed |
|  | Cash­Box Cash box | varchar(50) | 50 | NULL allowed |
|  | Chq­Box Chq box | varchar(50) | 50 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Currencies\_­Currencies | ID->[[dbo].[Currencies].[ID]](#k0NURIzYF8aeO/uxKYIEdxSccAg=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Currencies­Denominations] |

MS\_­Description

Stores the denominations of each currency used in the system. Each record represents a specific currency unit such as coins or banknotes and defines its conversion rate relative to the main currency unit. The table is mainly used to support cash handling, payment processing, and accurate financial calculations when dealing with different currency denominations.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Currency­ID Currency identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Deno­ID Deno identifier | smallint | 2 | NOT NULL |
|  | Deno­Name Deno name | varchar(500) | 500 | NULL allowed |
|  | Convert­Rate Convert rate | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Currencies­Rate] |

MS\_­Description

Stores the exchange rates of currencies used in the system by date. Each record represents the exchange rate of a specific currency on a certain date, allowing the system to apply the correct conversion rate during financial and sales transactions. The table is mainly used to support multi-currency operations, currency conversion, and accurate financial reporting.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Default |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |  |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Currency­ID Currency identifier | smallint | 2 | NOT NULL |  |
| ![](data:image/png;base64...) | Ex­Date Ex date | smalldatetime | 4 | NOT NULL |  |
|  | Ex­Rate Ex rate | float | 8 | NULL allowed |  |
|  | Entry­Date Entry date | smalldatetime | 4 | NULL allowed | (getdate()) |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Currencies­Rate\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Currencies­Rate\_­Currencies | Currency­ID->[[dbo].[Currencies].[ID]](#k0NURIzYF8aeO/uxKYIEdxSccAg=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customer­Chq­List] |

MS\_­Description

This table stores the checks issued by customers as part of payment transactions. It helps the system track check numbers, related customers, and payment details used in collections and financial reconciliation.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Comp­No Comp number | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | nvarchar(50) | 100 | NOT NULL |
| ![](data:image/png;base64...) | Chq­No Chq number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Bank­No Bank number | int | 4 | NOT NULL |
|  | Bank­Desc Bank description | varchar(100) | 100 | NULL allowed |
|  | Dept­No Dept number | int | 4 | NULL allowed |
|  | Dept­Name Dept name | varchar(100) | 100 | NULL allowed |
|  | Due­Date Due date | smalldatetime | 4 | NULL allowed |
|  | Vou­No Vou number | int | 4 | NULL allowed |
|  | Vou­Date Vou date | smalldatetime | 4 | NULL allowed |
|  | Chq­Status Chq status | varchar(100) | 100 | NULL allowed |
|  | Amount Amount | float | 8 | NULL allowed |
|  | Paid­Amount Paid amount | float | 8 | NULL allowed |
|  | Rem­Amount Rem amount | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customer­Class­Targets] |

MS\_­Description

This table defines target values assigned to different customer classes. It helps the system evaluate sales or collection performance based on customer classification.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Customer­Class­ID Customer class identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Target­Year Target year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Target­Month Target month | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Target­Type­ID Target type identifier | int | 4 | NULL allowed |
|  | Amount Amount | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Customer­Class­Targets\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Customer­Class­Targets\_­Customers­Classes | Company­ID->[[dbo].[Customers­Classes].[Company­ID]](#KrR7yySr/q1jKoCUyhbUJhKzp6M=), Customer­Class­ID->[[dbo].[Customers­Classes].[ID]](#KrR7yySr/q1jKoCUyhbUJhKzp6M=) |
| FK\_­Customer­Class­Targets\_­Targets­Types | Target­Type­ID->[[dbo].[Targets­Types].[ID]](#0/4snZsACLzbPDsnGKCgpJuaMnM=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customer­Class­Targets­Details] |

MS\_­Description

This table stores the detailed records of customer class targets, such as the breakdown of target values by item, period, or business dimension.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Customer­Class­ID Customer class identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Target­Year Target year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Target­Month Target month | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Target­Reference­ID Target reference identifier | int | 4 | NOT NULL |
|  | Quantity Quantity | float | 8 | NULL allowed |
|  | Amount Amount | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Customer­Class­Targets­Details\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Customer­Class­Targets­Details\_­Customer­Class­Targets | Company­ID->[[dbo].[Customer­Class­Targets].[Company­ID]](#IT4JhR/yxVJEqAmwFRM4MjjAGnw=), Customer­Class­ID->[[dbo].[Customer­Class­Targets].[Customer­Class­ID]](#IT4JhR/yxVJEqAmwFRM4MjjAGnw=), Target­Year->[[dbo].[Customer­Class­Targets].[Target­Year]](#IT4JhR/yxVJEqAmwFRM4MjjAGnw=), Target­Month->[[dbo].[Customer­Class­Targets].[Target­Month]](#IT4JhR/yxVJEqAmwFRM4MjjAGnw=) |
| FK\_­Customer­Class­Targets­Details\_­Customers­Classes | Company­ID->[[dbo].[Customers­Classes].[Company­ID]](#KrR7yySr/q1jKoCUyhbUJhKzp6M=), Customer­Class­ID->[[dbo].[Customers­Classes].[ID]](#KrR7yySr/q1jKoCUyhbUJhKzp6M=) |
| FK\_­Customer­Class­Targets­Details\_­Targets­References | Company­ID->[[dbo].[Targets­References].[Company­ID]](#pTJEdyfW1its0oUM5wpR5Npe6Js=), Target­Reference­ID->[[dbo].[Targets­References].[ID]](#pTJEdyfW1its0oUM5wpR5Npe6Js=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customer­Data\_­Sample] |

MS\_­Description

This table stores sample or temporary customer data used for testing, training, or demonstration purposes. It helps simulate real customer records without affecting the main customer master data.

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| Comp­No Comp number | int | 4 | NULL allowed |
| Cust­ID Cust identifier | bigint | 8 | NULL allowed |
| postion Postion | bigint | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customer­Login­Actions] |

MS\_­Description

This table stores customer login-related actions, helping the system track customer access, login events, or activities performed during login sessions.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | ID ID identifier | nvarchar(50) | 100 | NOT NULL |
|  | Description Description | nvarchar(50) | 100 | NULL allowed |
|  | Is­Standard Flag indicating standard | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customer­Paid­Trans\_­Form­ERP] |

MS\_­Description

This table stores customer payment transactions received from the ERP system. It is used to synchronize financial data between the ERP and the mobile sales system.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ERPInv­No Erp inv number | varchar(500) | 500 | NOT NULL |
| ![](data:image/png;base64...) | ERPYear Erp year | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | New­Inv­ID New inv identifier | bigint | 8 | NOT NULL |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customer­Phone] |

MS\_­Description

This table stores customer phone numbers and contact phone details used for communication and customer record management.

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| Card­Name Card name | nvarchar(300) | 600 | NULL allowed |
| Phone1 Phone 1 | nvarchar(20) | 40 | NULL allowed |
| Phone2 Phone 2 | nvarchar(20) | 40 | NULL allowed |
| Cellular Cellular | nvarchar(20) | 40 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customer­Receivables­Info] |

MS\_­Description

This table stores receivable-related information for customers, helping the system track outstanding balances, due amounts, and financial status.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Comp­No Comp number | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |
|  | Exclude­Cash­Payments Exclude cash payments | float | 8 | NULL allowed |
|  | Exclude­Returns Exclude returns | float | 8 | NULL allowed |
|  | Exclude­Pending­Orders Exclude pending orders | float | 8 | NULL allowed |
|  | Exception­Collection­Manager Exception collection manager | float | 8 | NULL allowed |
|  | Receivables­Month Receivables month | smallint | 2 | NULL allowed |
|  | Receivables­Year Receivables year | smallint | 2 | NULL allowed |
|  | Receivables Receivables | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers] |

MS\_­Description

This table stores the main customer master data used across the system, including customer identity, classification, location, and operational details.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Default |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |  |
| ![](data:image/png;base64...)![](data:image/png;base64...) | ID ID identifier | bigint | 8 | NOT NULL |  |
|  | Name Name | nvarchar(200) | 400 | NULL allowed |  |
|  | Foreign­Name Foreign name | nvarchar(200) | 400 | NULL allowed |  |
|  | Short­Name Short name | nvarchar(50) | 100 | NULL allowed |  |
| ![](data:image/png;base64...) | Type­ID Type identifier | int | 4 | NULL allowed |  |
| ![](data:image/png;base64...) | Location­ID Location identifier | int | 4 | NULL allowed |  |
|  | Reference1 Reference 1 | nvarchar(50) | 100 | NULL allowed |  |
|  | Reference2 Reference 2 | nvarchar(50) | 100 | NULL allowed |  |
|  | Account Account | nvarchar(50) | 100 | NULL allowed |  |
|  | Barcode Barcode | nvarchar(20) | 40 | NULL allowed |  |
|  | Contact Contact | nvarchar(100) | 200 | NULL allowed |  |
|  | Telephone­No Telephone number | nvarchar(50) | 100 | NULL allowed |  |
|  | Mobile­No Mobile number | nvarchar(50) | 100 | NULL allowed |  |
|  | Fax­No Fax number | nvarchar(50) | 100 | NULL allowed |  |
|  | POBox Po box | nvarchar(50) | 100 | NULL allowed |  |
|  | Address Address | nvarchar(200) | 400 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Web­Site Web site | nvarchar(100) | 200 | NULL allowed |  |
|  | Email Email | nvarchar(100) | 200 | NULL allowed |  |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |  |
|  | User­ID User identifier | nvarchar(20) | 40 | NULL allowed |  |
|  | Password Password | nvarchar(20) | 40 | NULL allowed |  |
|  | Customer­Balance Customer balance | float | 8 | NULL allowed |  |
|  | Chq­Balance Chq balance | float | 8 | NULL allowed |  |
|  | Customer­Image Customer image | image | max | NULL allowed |  |
|  | Balance Balance | float | 8 | NULL allowed |  |
|  | Send­Inv­By­Email Send inv by email | bit | 1 | NULL allowed |  |
|  | Commercial­Registration­No Commercial registration number | nvarchar(100) | 200 | NULL allowed |  |
|  | Professionlicence­No Professionlicence number | nvarchar(100) | 200 | NULL allowed |  |
|  | New­Cust­Ref­No New cust ref number | nvarchar(100) | 200 | NULL allowed |  |
|  | Notes Notes | nvarchar(max) | max | NULL allowed |  |
| ![](data:image/png;base64...) | Group\_­ID Group identifier | int | 4 | NULL allowed |  |
| ![](data:image/png;base64...) | Class­ID Class identifier | int | 4 | NULL allowed |  |
|  | Tab­Sys­ID Tab sys identifier | nvarchar(50) | 100 | NULL allowed |  |
|  | Tax­Number Tax number | nvarchar(100) | 200 | NULL allowed |  |
|  | Company­National­ID Company national identifier | varchar(1000) | 1000 | NULL allowed |  |
|  | Is­Collected­GPS Flag indicating collected gps | bit | 1 | NULL allowed |  |
|  | Erp\_­Reference Erp reference | varchar(50) | 50 | NULL allowed |  |
|  | Assets­Ref1 Assets ref 1 | nvarchar(50) | 100 | NULL allowed |  |
|  | Assets­Ref2 Assets ref 2 | nvarchar(50) | 100 | NULL allowed |  |
|  | Status Status | nvarchar(100) | 200 | NULL allowed |  |
|  | Delivery­Car­Type Delivery car type | int | 4 | NULL allowed |  |
|  | Is­Closed Flag indicating closed | bit | 1 | NULL allowed |  |
|  | Day­Off Day off | nvarchar(100) | 200 | NULL allowed |  |
|  | Working­Days Working days | nvarchar(100) | 200 | NULL allowed |  |
|  | Suspended­Reason Suspended reason | nvarchar(200) | 400 | NULL allowed |  |
|  | Price­List­ID\_­Tmp Price list id tmp | int | 4 | NULL allowed |  |
|  | PType\_­Tmp P type tmp | int | 4 | NULL allowed |  |
|  | Is­WFSuspended Flag indicating wf suspended | bit | 1 | NULL allowed |  |
|  | Create­Date Create date | smalldatetime | 4 | NULL allowed | (getdate()) |
|  | Reference3 Reference 3 | float | 8 | NULL allowed |  |
|  | Exemted­Date Exemted date | smalldatetime | 4 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Customers\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Customers\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |
| FK\_­Customers\_­Customers­Classes | Company­ID->[[dbo].[Customers­Classes].[Company­ID]](#KrR7yySr/q1jKoCUyhbUJhKzp6M=), Class­ID->[[dbo].[Customers­Classes].[ID]](#KrR7yySr/q1jKoCUyhbUJhKzp6M=) |
| FK\_­Customers\_­Customers­Groups | Company­ID->[[dbo].[Customers­Groups].[Company­ID]](#okyn1+fvA5B2jRl9YiDWFhbVXIg=), Group\_­ID->[[dbo].[Customers­Groups].[Group­ID]](#okyn1+fvA5B2jRl9YiDWFhbVXIg=) |
| FK\_­Customers\_­Customers­Types | Company­ID->[[dbo].[Customers­Types].[Company­ID]](#mUOPMl0ZzNBySPnrrjXsxaUEKvo=), Type­ID->[[dbo].[Customers­Types].[ID]](#mUOPMl0ZzNBySPnrrjXsxaUEKvo=) |
| FK\_­Customers\_­Locations | Company­ID->[[dbo].[Locations].[Company­ID]](#eNuBnAAgcTN3Hu1UlDB+jaS/yKQ=), Location­ID->[[dbo].[Locations].[ID]](#eNuBnAAgcTN3Hu1UlDB+jaS/yKQ=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers2] |

MS\_­Description

This table stores an additional or alternative set of customer records, typically used for extended customer data, legacy records, or integration purposes.

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| Company­ID Company identifier | smallint | 2 | NOT NULL |
| Name Name | nvarchar(200) | 400 | NULL allowed |
| Type­ID Type identifier | int | 4 | NULL allowed |
| Location­ID Location identifier | int | 4 | NULL allowed |
| Salesmanno Salesmanno | int | 4 | NULL allowed |
| Payment­Type Payment type | int | 4 | NULL allowed |
| Pricelist Pricelist | int | 4 | NULL allowed |
| Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |
| Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |
| ISAdded111 Flag indicating added 111 | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customer­Sales­By­Category] |

MS\_­Description

This table stores customer sales summarized or classified by item category, helping analyze customer buying behavior across product groups.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Comp­No Comp number | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Customer­No Customer number | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Categ Categ | varchar(50) | 50 | NOT NULL |
|  | Net­Sales Net sales | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­Balance­Aging] |

MS\_­Description

This table stores aging information for customer balances, showing how long outstanding amounts have remained unpaid across aging periods.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |
|  | Balance­Age1 Balance age 1 | float | 8 | NULL allowed |
|  | Balance­Age2 Balance age 2 | float | 8 | NULL allowed |
|  | Balance­Age3 Balance age 3 | float | 8 | NULL allowed |
|  | Balance­Age4 Balance age 4 | float | 8 | NULL allowed |
|  | Balance­Age5 Balance age 5 | float | 8 | NULL allowed |
|  | Balance­Age6 Balance age 6 | float | 8 | NULL allowed |
|  | Balance­Age7 Balance age 7 | float | 8 | NULL allowed |
|  | Balance­Age8 Balance age 8 | float | 8 | NULL allowed |
|  | Balance­Age9 Balance age 9 | float | 8 | NULL allowed |
|  | Balance­Age10 Balance age 10 | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­Balance­Aging\_­Inmaa] |

MS\_­Description

This table stores customer balance aging information related to the Inmaa integration or reporting structure. It supports financial analysis for that specific business process.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |
|  | Balance­Age1 Balance age 1 | float | 8 | NULL allowed |
|  | Balance­Age2 Balance age 2 | float | 8 | NULL allowed |
|  | Balance­Age3 Balance age 3 | float | 8 | NULL allowed |
|  | Balance­Age4 Balance age 4 | float | 8 | NULL allowed |
|  | Balance­Age5 Balance age 5 | float | 8 | NULL allowed |
|  | Balance­Age6 Balance age 6 | float | 8 | NULL allowed |
|  | Balance­Age7 Balance age 7 | float | 8 | NULL allowed |
|  | Balance­Age8 Balance age 8 | float | 8 | NULL allowed |
|  | Balance­Age9 Balance age 9 | float | 8 | NULL allowed |
|  | Balance­Age10 Balance age 10 | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­Bonus­Types­Link] |

MS\_­Description

This table links customers with applicable bonus or incentive types. It allows the system to determine which bonus rules apply to each customer.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Bonus­Type Bonus type | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­Classes] |

MS\_­Description

This table stores customer classification categories such as retail, wholesale, or key accounts. It helps organize customers for reporting, pricing, and marketing strategies.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Short­Name Short name | nvarchar(50) | 100 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Customers­Classes\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­Contact­Persons] |

MS\_­Description

This table stores contact person information related to customers. It keeps details of individuals responsible for communication with the customer.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Short­Name Short name | nvarchar(100) | 200 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­Contact­Persons­Link] |

MS\_­Description

This table links customers with their contact persons. It ensures each contact record is associated with the correct customer.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |  |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |  |
| ![](data:image/png;base64...) | Contact­Person­ID Contact person identifier | int | 4 | NOT NULL |  |
| ![](data:image/png;base64...) | ID ID identifier | bigint | 8 | NOT NULL | 1 - 1 |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­Financial­Details] |

MS\_­Description

This table stores financial settings related to customers. It includes credit limits, payment terms, and financial rules used in sales transactions.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Default |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |  |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |  |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Positions­ID Positions identifier | int | 4 | NOT NULL |  |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Business­Unit­ID Business unit identifier | int | 4 | NOT NULL |  |
| ![](data:image/png;base64...) | Payment­Type­ID Payment type identifier | int | 4 | NULL allowed |  |
| ![](data:image/png;base64...) | Price­List­ID Price list identifier | int | 4 | NULL allowed |  |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Route­ID Route identifier | int | 4 | NULL allowed |  |
| ![](data:image/png;base64...) | Customers­Promotions­Groups­ID Customers promotions groups identifier | int | 4 | NULL allowed |  |
|  | Credit­Limit Credit limit | float | 8 | NULL allowed |  |
|  | Due­Days Due days | smallint | 2 | NULL allowed |  |
|  | Chqs­Due­Days Chqs due days | smallint | 2 | NULL allowed |  |
|  | Allow­Chqs Flag indicating allow chqs | bit | 1 | NULL allowed |  |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |  |
|  | Favourite­Visit­Time Favourite visit time | smalldatetime | 4 | NULL allowed |  |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |  |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |  |
|  | Tax­Include Tax include | bit | 1 | NULL allowed | ((1)) |
|  | Discount­Perc Discount percentage | float | 8 | NULL allowed |  |
|  | Credit­Cash Credit cash | smallint | 2 | NULL allowed |  |
|  | Customer­Balance Customer balance | float | 8 | NULL allowed |  |
|  | Chq­Balance Chq balance | float | 8 | NULL allowed |  |
|  | Visit­Order Visit order | int | 4 | NULL allowed |  |
|  | Max­Invoice­Value Max invoice value | float | 8 | NULL allowed |  |
|  | Max­Invoice­Count Max invoice count | int | 4 | NULL allowed |  |
|  | Chq­Limit Chq limit | float | 8 | NULL allowed |  |
|  | Tax\_1\_­Include Tax 1 include | bit | 1 | NULL allowed | ((1)) |
|  | Tax\_2\_­Include Tax 2 include | bit | 1 | NULL allowed | ((1)) |
|  | Allow­Manual­Discount Flag indicating allow manual discount | bit | 1 | NULL allowed |  |
| ![](data:image/png;base64...) | Company­Branche­ID Company branche identifier | int | 4 | NULL allowed |  |
|  | Early­Repayment­Discount­Perc Early repayment discount percentage | float | 8 | NULL allowed |  |
| ![](data:image/png;base64...) | Class­ID Class identifier | int | 4 | NULL allowed |  |
|  | Discount­Early­Pay­Days Discount early pay days | int | 4 | NULL allowed |  |
|  | Location­Line­ID Location line identifier | int | 4 | NULL allowed |  |
|  | Delivery­Days Delivery days | int | 4 | NULL allowed |  |
|  | Order­Cash­Discount Order cash discount | float | 8 | NULL allowed |  |
|  | Currency­ID Currency identifier | int | 4 | NULL allowed |  |
|  | Return­Credit­Limit Return credit limit | float | 8 | NULL allowed |  |
|  | Return­Balance Return balance | float | 8 | NULL allowed |  |
|  | Location­ID Location identifier | int | 4 | NULL allowed |  |
|  | Sales­Order­Limit Sales order limit | float | 8 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Customers­Financial­Details\_­Business­Units | Company­ID->[[dbo].[Business­Units].[Company­ID]](#nfNLb+EhlWiX9kN6JEFSAV6syXI=), Business­Unit­ID->[[dbo].[Business­Units].[ID]](#nfNLb+EhlWiX9kN6JEFSAV6syXI=) |
| FK\_­Customers­Financial­Details\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Customers­Financial­Details\_­Company­Branches | Company­ID->[[dbo].[Company­Branches].[Company­ID]](#QtIx7cCe02/M8Iq2UstqD1tTYh4=), Company­Branche­ID->[[dbo].[Company­Branches].[ID]](#QtIx7cCe02/M8Iq2UstqD1tTYh4=) |
| FK\_­Customers­Financial­Details\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |
| FK\_­Customers­Financial­Details\_­Customers­Classes | Company­ID->[[dbo].[Customers­Classes].[Company­ID]](#KrR7yySr/q1jKoCUyhbUJhKzp6M=), Class­ID->[[dbo].[Customers­Classes].[ID]](#KrR7yySr/q1jKoCUyhbUJhKzp6M=) |
| FK\_­Customers­Financial­Details\_­Customers­Promotions­Groups | Company­ID->[[dbo].[Customers­Promotions­Groups].[Company­ID]](#CFvv0vB6qnd5JDiJpBfVpPfz9FY=), Customers­Promotions­Groups­ID->[[dbo].[Customers­Promotions­Groups].[ID]](#CFvv0vB6qnd5JDiJpBfVpPfz9FY=) |
| FK\_­Customers­Financial­Details\_­Payments­Types | Company­ID->[[dbo].[Payments­Types].[Company­ID]](#lO8zg+RAFUjBCTc7z+Mf67JVfuQ=), Payment­Type­ID->[[dbo].[Payments­Types].[ID]](#lO8zg+RAFUjBCTc7z+Mf67JVfuQ=) |
| FK\_­Customers­Financial­Details\_­Positions | Company­ID->[[dbo].[Positions].[Company­ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=), Positions­ID->[[dbo].[Positions].[ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=) |
| FK\_­Customers­Financial­Details\_­Price­Lists | Company­ID->[[dbo].[Price­Lists].[Company­ID]](#UTuGUXmxHIFiIaREw25LxgcqPnU=), Price­List­ID->[[dbo].[Price­Lists].[ID]](#UTuGUXmxHIFiIaREw25LxgcqPnU=) |
| FK\_­Customers­Financial­Details\_­Routes­Information | Company­ID->[[dbo].[Routes­Information].[Company­ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=), Route­ID->[[dbo].[Routes­Information].[ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­Financial­Details\_­Old] |

MS\_­Description

This table stores historical customer financial details. It is maintained for reference, auditing, or migration from previous system configurations.

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| Company­ID Company identifier | smallint | 2 | NOT NULL |
| Customer­ID Customer identifier | bigint | 8 | NOT NULL |
| Positions­ID Positions identifier | int | 4 | NOT NULL |
| Business­Unit­ID Business unit identifier | int | 4 | NOT NULL |
| Payment­Type­ID Payment type identifier | int | 4 | NULL allowed |
| Price­List­ID Price list identifier | int | 4 | NULL allowed |
| Route­ID Route identifier | int | 4 | NULL allowed |
| Customers­Promotions­Groups­ID Customers promotions groups identifier | int | 4 | NULL allowed |
| Credit­Limit Credit limit | float | 8 | NULL allowed |
| Due­Days Due days | smallint | 2 | NULL allowed |
| Chqs­Due­Days Chqs due days | smallint | 2 | NULL allowed |
| Allow­Chqs Flag indicating allow chqs | bit | 1 | NULL allowed |
| Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |
| Favourite­Visit­Time Favourite visit time | smalldatetime | 4 | NULL allowed |
| Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
| Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |
| Tax­Include Tax include | bit | 1 | NULL allowed |
| Discount­Perc Discount percentage | float | 8 | NULL allowed |
| Credit­Cash Credit cash | smallint | 2 | NULL allowed |
| Customer­Balance Customer balance | float | 8 | NULL allowed |
| Chq­Balance Chq balance | float | 8 | NULL allowed |
| Visit­Order Visit order | int | 4 | NULL allowed |
| Max­Invoice­Value Max invoice value | float | 8 | NULL allowed |
| Max­Invoice­Count Max invoice count | int | 4 | NULL allowed |
| Chq­Limit Chq limit | float | 8 | NULL allowed |
| Tax\_1\_­Include Tax 1 include | bit | 1 | NULL allowed |
| Tax\_2\_­Include Tax 2 include | bit | 1 | NULL allowed |
| Allow­Manual­Discount Flag indicating allow manual discount | bit | 1 | NULL allowed |
| Company­Branche­ID Company branche identifier | int | 4 | NULL allowed |
| Early­Repayment­Discount­Perc Early repayment discount percentage | float | 8 | NULL allowed |
| Class­ID Class identifier | int | 4 | NULL allowed |
| Discount­Early­Pay­Days Discount early pay days | int | 4 | NULL allowed |
| Location­Line­ID Location line identifier | int | 4 | NULL allowed |
| Delivery­Days Delivery days | int | 4 | NULL allowed |
| Order­Cash­Discount Order cash discount | float | 8 | NULL allowed |
| Currency­ID Currency identifier | int | 4 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­Financial­Details2] |

MS\_­Description

This table stores extended financial information for customers. It supports additional financial configurations required by business processes or integrations.

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| Company­ID Company identifier | smallint | 2 | NOT NULL |
| Customer­ID Customer identifier | bigint | 8 | NOT NULL |
| Positions­ID Positions identifier | int | 4 | NOT NULL |
| Business­Unit­ID Business unit identifier | int | 4 | NOT NULL |
| Payment­Type­ID Payment type identifier | int | 4 | NULL allowed |
| Price­List­ID Price list identifier | int | 4 | NULL allowed |
| Route­ID Route identifier | int | 4 | NULL allowed |
| Customers­Promotions­Groups­ID Customers promotions groups identifier | int | 4 | NULL allowed |
| Credit­Limit Credit limit | float | 8 | NULL allowed |
| Due­Days Due days | smallint | 2 | NULL allowed |
| Chqs­Due­Days Chqs due days | smallint | 2 | NULL allowed |
| Allow­Chqs Flag indicating allow chqs | bit | 1 | NULL allowed |
| Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |
| Favourite­Visit­Time Favourite visit time | smalldatetime | 4 | NULL allowed |
| Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
| Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |
| Tax­Include Tax include | bit | 1 | NULL allowed |
| Discount­Perc Discount percentage | float | 8 | NULL allowed |
| Credit­Cash Credit cash | smallint | 2 | NULL allowed |
| Customer­Balance Customer balance | float | 8 | NULL allowed |
| Chq­Balance Chq balance | float | 8 | NULL allowed |
| Visit­Order Visit order | int | 4 | NULL allowed |
| Max­Invoice­Value Max invoice value | float | 8 | NULL allowed |
| Max­Invoice­Count Max invoice count | int | 4 | NULL allowed |
| Chq­Limit Chq limit | float | 8 | NULL allowed |
| Tax\_1\_­Include Tax 1 include | bit | 1 | NULL allowed |
| Tax\_2\_­Include Tax 2 include | bit | 1 | NULL allowed |
| Allow­Manual­Discount Flag indicating allow manual discount | bit | 1 | NULL allowed |
| Company­Branche­ID Company branche identifier | int | 4 | NULL allowed |
| Early­Repayment­Discount­Perc Early repayment discount percentage | float | 8 | NULL allowed |
| Class­ID Class identifier | int | 4 | NULL allowed |
| Discount­Early­Pay­Days Discount early pay days | int | 4 | NULL allowed |
| Location­Line­ID Location line identifier | int | 4 | NULL allowed |
| Delivery­Days Delivery days | int | 4 | NULL allowed |
| Order­Cash­Discount Order cash discount | float | 8 | NULL allowed |
| Currency­ID Currency identifier | int | 4 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­GPSLocations] |

MS\_­Description

This table stores GPS coordinates for customer locations. It helps verify visit locations, support route planning, and improve field sales tracking.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Line­ID Line identifier | int | 4 | NOT NULL |
|  | GPSX Gpsx | nvarchar(100) | 200 | NULL allowed |
|  | GPSY Gpsy | nvarchar(100) | 200 | NULL allowed |
|  | Notes Notes | nvarchar(1000) | 2000 | NULL allowed |
|  | Loc\_­Address Loc address | nvarchar(1000) | 2000 | NULL allowed |
|  | Posted Posted | bit | 1 | NULL allowed |
|  | Location­ID Location identifier | int | 4 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Customers­GPSLocations\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Customers­GPSLocations\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­Groups] |

MS\_­Description

This table organizes customers into groups. These groups are used for pricing strategies, promotions, and reporting segmentation.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Group­ID Group identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Foreign­Name Foreign name | nvarchar(200) | 400 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Customers­Groups\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­Item­Qty­Limit] |

MS\_­Description

This table defines quantity limits for items sold to specific customers. It helps enforce sales restrictions and manage inventory allocation.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
|  | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |
|  | Sold­Qty­Limit Sold qty limit | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­Items­Assigment] |

MS\_­Description

Stores the items assigned to specific customers in the system. Each record links a customer with an item to define which items are available, allowed, or specifically relevant for that customer. The table is mainly used to control item availability by customer and support sales, distribution, and customer-specific product assignments.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Positions­ID Positions identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Customers­Items­Assigment\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Customers­Items­Assigment\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |
| FK\_­Customers­Items­Assigment\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Customers­Items­Assigment\_­Positions | Company­ID->[[dbo].[Positions].[Company­ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=), Positions­ID->[[dbo].[Positions].[ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­Items­Log] |

MS\_­Description

This table records changes related to customer item assignments. It provides a history of updates and modifications for tracking purposes.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | bigint | 8 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NULL allowed |  |
| ![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NULL allowed |  |
| ![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NULL allowed |  |
|  | Visit­Date Visit date | smalldatetime | 4 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Customers­Items­Log\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Customers­Items­Log\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |
| FK\_­Customers­Items­Log\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Customers­Items­Log\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Person­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­Log] |

MS\_­Description

This table stores historical logs of changes made to customer records. It supports auditing and tracking of customer data modifications.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | bigint | 8 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NULL allowed |  |
| ![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NULL allowed |  |
|  | Visit­Date Visit date | smalldatetime | 4 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Customers­Log\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Customers­Log\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |
| FK\_­Customers­Log\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Person­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­Monthly­Collection­Target] |

MS\_­Description

This table stores monthly collection targets assigned to customers. It helps monitor collection performance and financial targets.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Target­Month Target month | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Target­Year Target year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Salesman­ID Salesman identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Customer­Ref1 Customer ref 1 | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...) | Customer­Ref2 Customer ref 2 | nvarchar(100) | 200 | NOT NULL |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­Paid­Trans­List] |

MS\_­Description

Stores the list of payment transactions made by customers. Each record represents a payment received from a customer and is used to track amounts paid against outstanding invoices or balances. The table helps the system monitor customer collections, update financial balances, and support reporting on payment history.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Paid­Trans­Year Paid trans year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Paid­Trans­No Paid trans number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Paid­Trans­Type­ID Paid trans type identifier | smallint | 2 | NOT NULL |
|  | Paid­Trans­Amount Paid trans amount | float | 8 | NULL allowed |
|  | Paid­Trans­Remaining­Amount Paid trans remaining amount | float | 8 | NULL allowed |
|  | Paid­Trans­Due­Date Paid trans due date | smalldatetime | 4 | NULL allowed |
|  | Paid­Trans­Date Paid trans date | smalldatetime | 4 | NULL allowed |
|  | Ref1 Ref 1 | nvarchar(500) | 1000 | NULL allowed |
|  | Ref2 Ref 2 | nvarchar(500) | 1000 | NULL allowed |
|  | Ref3 Ref 3 | nvarchar(500) | 1000 | NULL allowed |
|  | Ref4 Ref 4 | nvarchar(500) | 1000 | NULL allowed |
|  | Ref5 Ref 5 | nvarchar(500) | 1000 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­Payment­Types­Link] |

MS\_­Description

Stores the relationship between customers and the payment types assigned to them. Each record links a customer to an allowed payment method such as cash, credit, or check. The table is mainly used to control and validate the payment methods that can be used during sales and collection transactions.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Payment­Type Payment type | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­Promotions­Exceptions] |

MS\_­Description

Stores exceptions related to promotion rules for specific customers. Each record defines cases where a promotion should not be applied to a particular customer, even if the customer normally qualifies for that promotion. The table is mainly used to control promotion eligibility and handle special business conditions.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Promotion­ID Promotion identifier | int | 4 | NOT NULL |
|  | Is­Include Flag indicating include | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Customers­Promotions­Exceptions\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Customers­Promotions­Exceptions\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |
| FK\_­Customers­Promotions­Exceptions\_­Promotions­Headers | Company­ID->[[dbo].[Promotions­Headers].[Company­ID]](#ahTdfFcl5CBnl0mrOXzm3bmregU=), Promotion­ID->[[dbo].[Promotions­Headers].[ID]](#ahTdfFcl5CBnl0mrOXzm3bmregU=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­Promotions­Groups] |

MS\_­Description

Stores the promotion groups defined for customers in the system. Each record represents a group used to organize customers for promotional campaigns and marketing offers. The table is mainly used to manage promotion eligibility and apply promotional rules to specific customer groups.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NULL allowed |
| ![](data:image/png;base64...) | Company­Branch­ID Company branch identifier | int | 4 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Customers­Promotions­Groups\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Customers­Promotions­Groups\_­Company­Branches | Company­ID->[[dbo].[Company­Branches].[Company­ID]](#QtIx7cCe02/M8Iq2UstqD1tTYh4=), Company­Branch­ID->[[dbo].[Company­Branches].[ID]](#QtIx7cCe02/M8Iq2UstqD1tTYh4=) |
| FK\_­Customers­Promotions­Groups\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­Promotions­Groups­Link] |

MS\_­Description

Stores the relationship between customers and promotion groups. Each record links a customer to a specific promotion group, allowing the system to determine which promotional campaigns or offers apply to that customer. The table is mainly used to manage promotion eligibility and apply group-based promotion rules during sales transactions.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Customers­Promotions­Groups­ID Customers promotions groups identifier | int | 4 | NOT NULL |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Customers­Promotions­Groups­Link\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Customers­Promotions­Groups­Link\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |
| FK\_­Customers­Promotions­Groups­Link\_­Customers­Promotions­Groups | Company­ID->[[dbo].[Customers­Promotions­Groups].[Company­ID]](#CFvv0vB6qnd5JDiJpBfVpPfz9FY=), Customers­Promotions­Groups­ID->[[dbo].[Customers­Promotions­Groups].[ID]](#CFvv0vB6qnd5JDiJpBfVpPfz9FY=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­Return­Item­Qty­Limit] |

MS\_­Description

Stores the maximum quantity of items that a customer is allowed to return. Each record defines a return limit for a specific item and customer, helping the system control return transactions and prevent excessive or unauthorized item returns during sales operations.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
|  | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |
|  | Return­Qty­Limit Return qty limit | float | 8 | NULL allowed |
|  | Returned­Qty Returned quantity | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­Sales­From0to­Max] |

MS\_­Description

Stores the sales range values defined for customers, from minimum to maximum sales amounts. Each record represents a sales range used to classify or evaluate customer sales performance. The table is mainly used for sales analysis, customer segmentation, and applying business rules based on sales levels.

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| Type­ID Type identifier | int | 4 | NULL allowed |
| Type­Name Type name | nvarchar(200) | 400 | NULL allowed |
| Customer­ID Customer identifier | bigint | 8 | NULL allowed |
| Customer­Name Customer name | nvarchar(200) | 400 | NULL allowed |
| Sales­Value Sales value | float | 8 | NULL allowed |
| Return­Value Return value | float | 8 | NULL allowed |
| Net­Sales­Value Net sales value | nvarchar(200) | 400 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customer­Statment­Of­Account] |

MS\_­Description

This table stores customer account statement data including debit, credit, and balance transactions. It provides a financial summary of customer activity.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Default |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |  |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |  |
| ![](data:image/png;base64...) | Tr­Type Tr type | varchar(50) | 50 | NOT NULL |  |
| ![](data:image/png;base64...) | Tr­No Tr number | varchar(50) | 50 | NOT NULL |  |
| ![](data:image/png;base64...) | Tr­Ser Tr ser | smallint | 2 | NOT NULL |  |
| ![](data:image/png;base64...) | Dept­No Dept number | int | 4 | NOT NULL | ((0)) |
| ![](data:image/png;base64...) | Tr­Date Tr date | smalldatetime | 4 | NOT NULL |  |
|  | Tr­Name Tr name | varchar(50) | 50 | NULL allowed |  |
|  | Debit Debit | money | 8 | NULL allowed |  |
|  | Credit Credit | money | 8 | NULL allowed |  |
|  | Notes Notes | varchar(300) | 300 | NULL allowed |  |
|  | Balance Balance | money | 8 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customer­Stock­Tacking] |

MS\_­Description

This table stores stock counting records for items at customer locations. It helps verify inventory levels and manage stock visibility.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­Year Order year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
|  | Order­Date Order date | smalldatetime | 4 | NULL allowed |
| ![](data:image/png;base64...) | Customers­ID Customers identifier | bigint | 8 | NULL allowed |
| ![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NULL allowed |
|  | Notes Notes | nvarchar(500) | 1000 | NULL allowed |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |
| ![](data:image/png;base64...) | Route­ID Route identifier | int | 4 | NULL allowed |
|  | Document­Type­ID Document type identifier | int | 4 | NULL allowed |
|  | Tr­Date­Time Tr date time | smalldatetime | 4 | NULL allowed |
|  | Print­Original­Count Print original count | int | 4 | NULL allowed |
|  | Print­Copy­Count Print copy count | int | 4 | NULL allowed |
|  | Server­Date Server date | smalldatetime | 4 | NULL allowed |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |
|  | Location­Line­ID Location line identifier | int | 4 | NULL allowed |
|  | Is­Linked­To­Sales­Order Flag indicating linked to sales order | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Customer­Stock­Tacking\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Customer­Stock­Tacking\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customers­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |
| FK\_­Customer­Stock­Tacking\_­Routes­Information | Company­ID->[[dbo].[Routes­Information].[Company­ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=), Route­ID->[[dbo].[Routes­Information].[ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=) |
| FK\_­Customer­Stock­Tacking\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Person­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customer­Stock­Tacking­Details] |

MS\_­Description

This table stores detailed item lines for customer stock-taking transactions. It includes item quantities counted during stock verification.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Order­Year Order year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |
|  | Quantity Quantity | float | 8 | NULL allowed |
|  | Item­Image Item image | image | max | NULL allowed |
|  | Exp­Date Exp date | smalldatetime | 4 | NULL allowed |
|  | Notes Notes | nvarchar(300) | 600 | NULL allowed |
|  | SP\_­Qty Sp quantity | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Customer­Stock­Tacking­Details\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Customer­Stock­Tacking­Details\_­Customer­Stock­Tacking | Company­ID->[[dbo].[Customer­Stock­Tacking].[Company­ID]](#UqtoPsN1f++adGXeDAi3Yi79T8I=), Order­Year->[[dbo].[Customer­Stock­Tacking].[Order­Year]](#UqtoPsN1f++adGXeDAi3Yi79T8I=), Order­No->[[dbo].[Customer­Stock­Tacking].[Order­No]](#UqtoPsN1f++adGXeDAi3Yi79T8I=) |
| FK\_­Customer­Stock­Tacking­Details\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Customer­Stock­Tacking­Details\_­Items­Units | Company­ID->[[dbo].[Items­Units].[Company­ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=), Unit­ID->[[dbo].[Items­Units].[ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­Types] |

MS\_­Description

This table defines different customer types used in the system. It helps categorize customers for operational and reporting purposes.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Short­Name Short name | nvarchar(50) | 100 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |
|  | Sales­Order­Limit Sales order limit | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Customers­Types\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­Visit­Activity] |

MS\_­Description

Stores the activities performed during customer visits by sales representatives or merchandisers. Each record represents an activity carried out at a customer location, such as product display, stock check, or promotional execution. The table is mainly used to track field operations, monitor visit performance, and support reporting on sales team activities.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Positions­ID Positions identifier | int | 4 | NOT NULL |
|  | Visit­Activity­In­Order Visit activity in order | varchar(4000) | 4000 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Customers­Visit­Activity\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Customers­Visit­Activity\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |
| FK\_­Customers­Visit­Activity\_­Positions | Company­ID->[[dbo].[Positions].[Company­ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=), Positions­ID->[[dbo].[Positions].[ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customers­WFFunctions­Auto­Approve] |

MS\_­Description

This table stores workflow functions that are automatically approved for certain customers. It helps streamline approval processes based on predefined rules.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Function­ID Function identifier | smallint | 2 | NOT NULL |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Customers­WFFunctions­Auto­Approve\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |
| FK\_­Customers­WFFunctions­Auto­Approve\_­Customers­WFFunctions­Auto­Approve | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Customers­WFFunctions­Auto­Approve\_­WF\_­Functions | Function­ID->[[dbo].[WF\_­Functions].[ID]](#R6akNrGibdwM/6sX4OhptH8w0Bc=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customer­Targets] |

MS\_­Description

This table stores sales or collection targets assigned to customers. It helps evaluate performance against predefined business objectives.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Target­Year Target year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Target­Month Target month | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Target­Type­ID Target type identifier | int | 4 | NULL allowed |
|  | Amount Amount | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Customer­Targets\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Customer­Targets\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |
| FK\_­Customer­Targets\_­Targets­Types | Target­Type­ID->[[dbo].[Targets­Types].[ID]](#0/4snZsACLzbPDsnGKCgpJuaMnM=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customer­Targets­Details] |

MS\_­Description

Stores the detailed records of targets assigned to customers. Each record contains the breakdown of target values such as sales or collection targets by item, category, or period. The table is mainly used to support target tracking, performance measurement, and reporting for customer-based objectives.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Target­Year Target year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Target­Month Target month | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Target­Reference­ID Target reference identifier | int | 4 | NOT NULL |
|  | Quantity Quantity | float | 8 | NULL allowed |
|  | Amount Amount | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Customer­Targets­Details\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Customer­Targets­Details\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |
| FK\_­Customer­Targets­Details\_­Customer­Targets | Company­ID->[[dbo].[Customer­Targets].[Company­ID]](#xFtDW8F50DUM+y3PCtJ+lSb9kJ0=), Customer­ID->[[dbo].[Customer­Targets].[Customer­ID]](#xFtDW8F50DUM+y3PCtJ+lSb9kJ0=), Target­Year->[[dbo].[Customer­Targets].[Target­Year]](#xFtDW8F50DUM+y3PCtJ+lSb9kJ0=), Target­Month->[[dbo].[Customer­Targets].[Target­Month]](#xFtDW8F50DUM+y3PCtJ+lSb9kJ0=) |
| FK\_­Customer­Targets­Details\_­Targets­References | Company­ID->[[dbo].[Targets­References].[Company­ID]](#pTJEdyfW1its0oUM5wpR5Npe6Js=), Target­Reference­ID->[[dbo].[Targets­References].[ID]](#pTJEdyfW1its0oUM5wpR5Npe6Js=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customer­Type­Early­Pay­Days] |

MS\_­Description

Stores the number of early payment days defined for each customer type. The table is used to determine the allowed period for early payment discounts and supports financial rules related to payment incentives by customer classification.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Customer­Type­ID Customer type identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Discount­Early­Pay­Days Discount early pay days | int | 4 | NOT NULL |
|  | Early­Repayment­Discount­Perc Early repayment discount percentage | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customer­Type­Targets] |

MS\_­Description

Stores target values assigned to each customer type for sales, collections, or other performance measurements. The table is mainly used to define business targets by customer category and support performance evaluation across different customer segments.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Customer­Type­ID Customer type identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Target­Year Target year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Target­Month Target month | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Target­Type­ID Target type identifier | int | 4 | NULL allowed |
|  | Amount Amount | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Customertype­Targets\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Customertype­Targets\_­Customerstypes | Company­ID->[[dbo].[Customers­Types].[Company­ID]](#mUOPMl0ZzNBySPnrrjXsxaUEKvo=), Customer­Type­ID->[[dbo].[Customers­Types].[ID]](#mUOPMl0ZzNBySPnrrjXsxaUEKvo=) |
| FK\_­Customertype­Targets\_­Targets­Types | Target­Type­ID->[[dbo].[Targets­Types].[ID]](#0/4snZsACLzbPDsnGKCgpJuaMnM=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Customer­Type­Targets­Details] |

MS\_­Description

Stores the detailed breakdown of target values linked to customer type targets. The table is used to define target details by item, category, or other business dimensions and supports more accurate target measurement and reporting.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Customertype­ID Customertype identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Target­Year Target year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Target­Month Target month | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Target­Reference­ID Target reference identifier | int | 4 | NOT NULL |
|  | Quantity Quantity | float | 8 | NULL allowed |
|  | Amount Amount | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Customer­Type­Targets­Details\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Customer­Type­Targets­Details\_­Customerstypes | Company­ID->[[dbo].[Customers­Types].[Company­ID]](#mUOPMl0ZzNBySPnrrjXsxaUEKvo=), Customertype­ID->[[dbo].[Customers­Types].[ID]](#mUOPMl0ZzNBySPnrrjXsxaUEKvo=) |
| FK\_­Customer­Type­Targets­Details\_­Customertype­Targets | Company­ID->[[dbo].[Customer­Type­Targets].[Company­ID]](#bBVLP3r/2IH82Om8eX+mV9+gJ3E=), Customertype­ID->[[dbo].[Customer­Type­Targets].[Customer­Type­ID]](#bBVLP3r/2IH82Om8eX+mV9+gJ3E=), Target­Year->[[dbo].[Customer­Type­Targets].[Target­Year]](#bBVLP3r/2IH82Om8eX+mV9+gJ3E=), Target­Month->[[dbo].[Customer­Type­Targets].[Target­Month]](#bBVLP3r/2IH82Om8eX+mV9+gJ3E=) |
| FK\_­Customer­Type­Targets­Details\_­Targets­References | Company­ID->[[dbo].[Targets­References].[Company­ID]](#pTJEdyfW1its0oUM5wpR5Npe6Js=), Target­Reference­ID->[[dbo].[Targets­References].[ID]](#pTJEdyfW1its0oUM5wpR5Npe6Js=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Daily­Procedures] |

MS\_­Description

Stores records of daily operational procedures executed within the system. The table is used to track routine daily processes, system activities, and operational actions required to support normal business operations.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Short­Name Short name | nvarchar(10) | 20 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Daily­Procedures\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Debit­Credit­Note­Trans] |

MS\_­Description

Stores debit and credit note transactions issued for customers during financial and sales operations. The table is used to record balance adjustments resulting from returns, corrections, pricing differences, or other accounting-related changes.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Comp­No Comp number | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Vou­Year Vou year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Vou­No Vou number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Vou­Type Vou type | smallint | 2 | NOT NULL |
|  | Vou­Date Vou date | smalldatetime | 4 | NULL allowed |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |
|  | Salesman­No Salesman number | int | 4 | NULL allowed |
|  | Inv­No Inv number | varchar(500) | 500 | NULL allowed |
|  | Inv­Amount Inv amount | float | 8 | NULL allowed |
|  | Tot­Disccount Tot disccount | float | 8 | NULL allowed |
|  | Tax Tax | float | 8 | NULL allowed |
|  | Net­Disccount Net disccount | float | 8 | NULL allowed |
|  | Server­Date Server date | smalldatetime | 4 | NULL allowed |
|  | Tr­Date­Time Tr date time | smalldatetime | 4 | NULL allowed |
|  | Notes Notes | varchar(200) | 200 | NULL allowed |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Delivery­Cars] |

MS\_­Description

Stores information about vehicles used in delivery and distribution operations ,This table stores information about delivery vehicles used in distribution operations. It helps track vehicles assigned to delivery routes and sales teams.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Load­Wieght Load wieght | float | 8 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |
|  | Car­Type Car type | int | 4 | NULL allowed |
|  | Barcode Barcode | nvarchar(100) | 200 | NULL allowed |
| ![](data:image/png;base64...) | Branch­ID Branch identifier | int | 4 | NULL allowed |
|  | GPSX Gpsx | float | 8 | NULL allowed |
|  | GPSY Gpsy | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Delivery­Cars\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Delivery­Cars\_­Company­Branches | Company­ID->[[dbo].[Company­Branches].[Company­ID]](#QtIx7cCe02/M8Iq2UstqD1tTYh4=), Branch­ID->[[dbo].[Company­Branches].[ID]](#QtIx7cCe02/M8Iq2UstqD1tTYh4=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Delivery­Manifest] |

MS\_­Description

Stores delivery manifest records that summarize deliveries prepared for dispatch. ,This table stores delivery manifest information, which represents the list of deliveries prepared for shipment. It helps organize items and invoices assigned to each delivery trip.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Serial Serial | int | 4 | NOT NULL |
|  | Delivery­Salesman­No Delivery salesman number | int | 4 | NULL allowed |
|  | Assistant­Salesman­No Assistant salesman number | int | 4 | NULL allowed |
|  | Delivery­Car­ID Delivery car identifier | int | 4 | NULL allowed |
|  | Is­Posted Flag indicating posted | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Delivery­Prova­D] |

MS\_­Description

Stores the detail lines of delivery proof transactions. The table is used to record item-level or document-level details that confirm delivery execution and support proof of delivery processes.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Delivery­Prova­No Delivery prova number | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Order­Year Order year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Item­Code Item code | varchar(50) | 50 | NOT NULL |
| ![](data:image/png;base64...) | Unit­ID Unit identifier | varchar(50) | 50 | NOT NULL |
|  | Loaded­Qty Loaded quantity | float | 8 | NULL allowed |
|  | Picked­Qty Picked quantity | float | 8 | NULL allowed |
|  | Tot­Weight Tot weight | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Delivery­Prova­H] |

MS\_­Description

This table stores the header records of delivery proof transactions. It groups delivery proof details under a single delivery confirmation record.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Delivery­Prova­No Delivery prova number | bigint | 8 | NOT NULL |
|  | Delivery­Salesman­No Delivery salesman number | int | 4 | NULL allowed |
|  | Delivery­Car­ID Delivery car identifier | int | 4 | NULL allowed |
|  | Delivery­Date Delivery date | smalldatetime | 4 | NULL allowed |
|  | Reference1 Reference 1 | varchar(50) | 50 | NULL allowed |
|  | Reference2 Reference 2 | varchar(50) | 50 | NULL allowed |
|  | Posted­To­ERP Posted to erp | bit | 1 | NULL allowed |
|  | Approved Flag indicating approved | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Delivery­Route] |

MS\_­Description

Stores delivery route definitions used in distribution operations. The table is mainly used to organize customer delivery sequences, assign routes to vehicles or drivers, and improve route planning and execution.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Comp­No Comp number | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Salesman­No Salesman number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Route­Date Route date | smalldatetime | 4 | NOT NULL |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Device­Reports­List] |

MS\_­Description

Stores the list of reports available for devices used in field operations. The table is used to control which reports can be accessed, generated, or displayed on mobile devices or tablets.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name­AR Name ar | nvarchar(1000) | 2000 | NULL allowed |
|  | Name­EN Name en | nvarchar(1000) | 2000 | NULL allowed |
|  | Reference1 Reference 1 | varchar(50) | 50 | NULL allowed |
|  | Reference2 Reference 2 | varchar(50) | 50 | NULL allowed |
|  | Sp\_­Name Sp name | varchar(500) | 500 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Devices­Info] |

MS\_­Description

Stores information about devices used by the system, such as tablets or handheld units assigned to field users. The table is mainly used to identify devices, manage configurations, and support device-level tracking.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Device­Name Device name | nvarchar(100) | 200 | NULL allowed |  |
|  | Mac­Address Mac address | nvarchar(200) | 400 | NULL allowed |  |
|  | Create­Date Create date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |  |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |  |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Devices­Info\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Discount­Early­Pay­By­Invoice­Ref] |

MS\_­Description

Stores early payment discount records linked to specific invoices. The table is used to track discounts granted when invoices are paid before their due dates and supports financial calculations for payment incentives.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Invoice­Ref Invoice reference | varchar(500) | 500 | NOT NULL |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |
|  | Salesperson­ID Salesperson identifier | int | 4 | NULL allowed |
|  | Discount­Perc Discount percentage | float | 8 | NULL allowed |
|  | Ref1 Ref 1 | varchar(50) | 50 | NULL allowed |
|  | Ref2 Ref 2 | varchar(50) | 50 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Documents­Types] |

MS\_­Description

Stores the master list of document types used in the system, such as invoices, receipts, returns, and orders. The table is mainly used to standardize document classification and support transaction processing across modules.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Transaction­Type­ID Transaction type identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Short­Name Short name | nvarchar(10) | 20 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |
|  | Notes Notes | nvarchar(max) | max | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Documents­Types\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Documents­Types\_­Transactions­Types | Transaction­Type­ID->[[dbo].[Transactions­Types].[ID]](#5KHGGmOv19tzIe7dNJ3JOc6tR1w=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[DR\_­Dynamic­Reports] |

MS\_­Description

Stores definitions of dynamic reports created within the system. The table is used to manage customizable reporting structures and allow users to generate reports based on selected business data and reporting requirements.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Report­ID Report identifier | bigint | 8 | NOT NULL |
|  | Report­Name­AR Report name ar | varchar(500) | 500 | NULL allowed |
|  | Report­Name­EN Report name en | varchar(500) | 500 | NULL allowed |
|  | Report­File­Name Report file name | varchar(500) | 500 | NULL allowed |
|  | Sp­Name Sp name | varchar(500) | 500 | NULL allowed |
|  | Allow­Translate Flag indicating allow translate | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[DR\_­Dynamic­Reports­Dictionary] |

MS\_­Description

Stores the dictionary and metadata of fields used in dynamic reports. The table is used to map report fields to database objects and support flexible report design and generation.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Report­ID Report identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Dictionary­ID Dictionary identifier | varchar(500) | 500 | NOT NULL |
|  | Dictionary­Text Dictionary text | varchar(max) | max | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[DR\_­Dynamic­Reports­Parameters] |

MS\_­Description

Stores the parameters used for dynamic reports. The table is mainly used to define report filters, user inputs, and selection criteria required for generating customized report outputs.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Report­ID Report identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Param­ID Param identifier | int | 4 | NOT NULL |
|  | Param­Caption Param caption | varchar(500) | 500 | NULL allowed |
|  | Param­SQLName Param sql name | varchar(500) | 500 | NULL allowed |
|  | Param­Type Param type | smallint | 2 | NULL allowed |
|  | Drop­Down­Source Drop down source | varchar(max) | max | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Drawers] |

MS\_­Description

Stores drawer or cash box records used in financial operations. The table is used to identify where cash collections, payments, or settlement amounts are stored and supports cash handling control.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Short­Name Short name | nvarchar(10) | 20 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |
|  | Drawers Drawers | nchar(10) | 20 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Drawers\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Drawers\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Efawateercom­Payment] |

MS\_­Description

Stores payment transactions processed through the Efawateercom integration. The table is used to record electronic payment details and support integration between the system and the Efawateercom payment platform.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | GUID Guid | uniqueidentifier | 16 | NOT NULL |
| ![](data:image/png;base64...) | Type­ID Type identifier | int | 4 | NOT NULL |
|  | Cust­ID Cust identifier | bigint | 8 | NOT NULL |
|  | Time­Stp Time stp | datetime | 8 | NOT NULL |
|  | Due­Amount Due amount | float | 8 | NOT NULL |
|  | Json­Req Json req | nvarchar(max) | max | NOT NULL |
|  | Json­Res Json res | nvarchar(max) | max | NOT NULL |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Emp­Details] |

MS\_­Description

Stores employee-related details used in the system. The table is mainly used to keep employee information required for operational, administrative, or reporting purposes.

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| Company­ID Company identifier | int | 4 | NULL allowed |
| Date­T Date t | datetime | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[ERPStores] |

MS\_­Description

Stores the list of stores or warehouses imported from the ERP system. Each record represents a warehouse used for inventory management and distribution operations. The table is mainly used to synchronize store data with the ERP system and support stock movements, loading operations, and item availability by store.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |  |
| ![](data:image/png;base64...) | Store­No Store number | int | 4 | NOT NULL | 1 - 1 |
|  | Ar­Desc Ar description | varchar(100) | 100 | NULL allowed |  |
|  | Eng­Desc Eng description | varchar(100) | 100 | NULL allowed |  |
|  | Reference1 Reference 1 | varchar(100) | 100 | NULL allowed |  |
|  | Reference2 Reference 2 | varchar(100) | 100 | NULL allowed |  |
|  | OID Oid | nvarchar(100) | 200 | NULL allowed |  |
|  | Car­No Car number | nvarchar(100) | 200 | NULL allowed |  |
|  | Remark Remark | nvarchar(100) | 200 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[ERPStores­Items­Link] |

MS\_­Description

This table stores the stores or warehouses imported from the ERP system. It is used to identify available warehouses in the system and link them with operational processes such as stock movement, loading, and item assignment.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Store­No Store number | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­ERPStores­Items­Link\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­ERPStores­Items­Link\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Error­Log] |

MS\_­Description

Stores system error records generated during application execution or database operations. The table records details about errors such as error messages, the process where the error occurred, and the date and time of the event. It is mainly used for troubleshooting, monitoring system issues, and supporting technical maintenance.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | ID ID identifier | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Mac­Address Mac address | nvarchar(100) | 200 | NULL allowed |  |
|  | IPAddress Ip address | nvarchar(100) | 200 | NULL allowed |  |
|  | PCName Pc name | nvarchar(100) | 200 | NULL allowed |  |
|  | User­ID User identifier | nvarchar(100) | 200 | NULL allowed |  |
|  | Tr­Date­Time Tr date time | datetime | 8 | NULL allowed |  |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Uri Uri | nvarchar(500) | 1000 | NULL allowed |  |
|  | Error­Description Error description | nvarchar(max) | max | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Excel] |

MS\_­Description

Stores temporary data imported from Excel files for processing within the system. The table is mainly used during data upload, migration, or bulk update operations where Excel files are used as a source of data before it is transferred to the main system tables.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ID ID identifier | int | 4 | NOT NULL | 1 - 1 |
| Cust­ID1 Cust id 1 | nvarchar(100) | 200 | NULL allowed |  |
| Salesman Salesman | nvarchar(100) | 200 | NULL allowed |  |
| Day Day | nvarchar(100) | 200 | NULL allowed |  |
| Week Week | nvarchar(100) | 200 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Excel2] |

MS\_­Description

Stores additional temporary data imported from Excel files. The table is typically used during data migration, bulk uploads, or testing processes where Excel is used as a staging source before the data is processed or moved to the main system tables.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ID ID identifier | int | 4 | NOT NULL | 1 - 1 |
| Cust­ID1 Cust id 1 | nvarchar(100) | 200 | NULL allowed |  |
| Salesman Salesman | nvarchar(100) | 200 | NULL allowed |  |
| Day Day | nvarchar(100) | 200 | NULL allowed |  |
| Week Week | nvarchar(100) | 200 | NULL allowed |  |
| Routename Routename | nvarchar(500) | 1000 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Excel­Reports] |

MS\_­Description

Stores information related to reports generated or exported in Excel format. The table is used to manage Excel report templates, configurations, or generated outputs, allowing users to produce and download business reports in Excel for analysis and reporting purposes.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Report­Sp Report sp | nvarchar(100) | 200 | NOT NULL |
|  | Report­Name Report name | nvarchar(500) | 1000 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[forupdateonly] |

MS\_­Description

Stores temporary records used during data updates or system maintenance processes. The table is mainly used as a staging or helper table to hold data that will be modified, synchronized, or transferred to other tables during update operations.

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| Compno Compno | int | 4 | NULL allowed |
| Customer­ID Customer identifier | bigint | 8 | NULL allowed |
| Positions­ID Positions identifier | int | 4 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Gap­Tags] |

MS\_­Description

Stores the tags used to classify GAP transactions in the system. These tags help categorize GAP-related activities and link them to specific processes or records, making it easier to track and analyze GAP operations.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Gap­Tag­ID Gap tag identifier | int | 4 | NOT NULL |
|  | Gap­Tag­Name Gap tag name | varchar(500) | 500 | NULL allowed |
|  | Data­Entry­Type Data entry type | tinyint | 1 | NULL allowed |
|  | Tag­Type­ID Tag type identifier | varchar(50) | 50 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Gap­Trans­Headers] |

MS\_­Description

Stores the main (header) records of GAP transactions. Each record represents a GAP operation and groups the related transaction details together, allowing the system to track and manage GAP activities as a single transaction.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Gap­Trans­Year Gap trans year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Gap­Trans­No Gap trans number | bigint | 8 | NOT NULL |
|  | Salesman­No Salesman number | int | 4 | NULL allowed |
|  | Notes Notes | varchar(max) | max | NULL allowed |
|  | Action­Date Action date | smalldatetime | 4 | NULL allowed |
|  | Assgined­Salesman­No Assgined salesman number | int | 4 | NULL allowed |
|  | Is­Done Flag indicating done | bit | 1 | NULL allowed |
|  | Device­Sys­ID Device sys identifier | varchar(50) | 50 | NULL allowed |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Gap­Trans­Tags] |

MS\_­Description

Stores the relationship between GAP transactions and their assigned tags. The table is used to link each GAP transaction with one or more tags, helping categorize and organize GAP activities for easier tracking and reporting.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Gap­Trans­Year Gap trans year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Gap­Trans­No Gap trans number | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Gap­Tag­ID Gap tag identifier | int | 4 | NOT NULL |
|  | Gap­Tag­Value Gap tag value | varchar(max) | max | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Gap­Trans­Time­Line] |

MS\_­Description

Stores the timeline records of GAP transactions. The table tracks the sequence of events and time-related activities associated with each GAP transaction, helping monitor progress, status changes, and operational history.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Gap­Trans­Year Gap trans year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Gap­Trans­No Gap trans number | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Time­Line­ID Time line identifier | int | 4 | NOT NULL |
|  | Salesman­No Salesman number | int | 4 | NULL allowed |
|  | Time­Line­Date­Time Time line date time | smalldatetime | 4 | NULL allowed |
|  | Notes Notes | varchar(max) | max | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Groups­Menu] |

MS\_­Description

Stores the relationship between user groups and system menu items. The table defines which menus or system functions are accessible for each user group, helping control user permissions and access rights within the application.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Group­ID Group identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Menu­ID Menu identifier | bigint | 8 | NOT NULL |
|  | Can­Read Can read | bit | 1 | NOT NULL |
|  | Can­Add Can add | bit | 1 | NOT NULL |
|  | Can­Edit Can edit | bit | 1 | NOT NULL |
|  | Can­Delete Can delete | bit | 1 | NOT NULL |

Foreign Keys

|  |  |  |
| --- | --- | --- |
| Name | Delete | Columns |
| FK\_dbo.Groups­Menu\_dbo.Menu\_­Menu­ID | Cascade | Menu­ID->[[dbo].[Menu].[ID]](#FnUAPCqnhxlqyV+PeKDOeSNn8tM=) |
| FK\_­Groups­Menu\_­Companies |  | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Image­Types] |

MS\_­Description

Stores the types of images used in the system. The table is used to classify images based on their purpose, such as customer images, item images, documents, or other attachments, helping organize and manage images within the application.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Short­Name Short name | nvarchar(50) | 100 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |
|  | Use­For Flag indicating use for | int | 4 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Image­Types\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Integration­Error­Log] |

MS\_­Description

Stores error records that occur during integration processes between the system and external systems such as ERP or third-party services. The table records details about failed transactions, error messages, and processing information to help monitor integration issues and support troubleshooting.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Company­Code Company code | nvarchar(50) | 100 | NULL allowed |  |
|  | Tr­Date­Time Tr date time | datetime | 8 | NULL allowed |  |
|  | Table­Name Table name | nvarchar(100) | 200 | NULL allowed |  |
|  | Error­Msg Error msg | nvarchar(max) | max | NULL allowed |  |
|  | Ref1 Ref 1 | nvarchar(100) | 200 | NULL allowed |  |
|  | Ref2 Ref 2 | nvarchar(100) | 200 | NULL allowed |  |
|  | Ref3 Ref 3 | nvarchar(100) | 200 | NULL allowed |  |
|  | Json­Data Json data | nvarchar(max) | max | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Integration­Posted­Transactions] |

MS\_­Description

Stores records of transactions that have been successfully posted to external systems through integration processes. The table helps track which transactions were sent to systems such as ERP, ensuring synchronization and preventing duplicate posting.

Columns

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity | Default |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |  |
|  | Comp­No Comp number | smallint | 2 | NULL allowed |  |  |
|  | Table­Name Table name | nvarchar(100) | 200 | NULL allowed |  |  |
|  | JSONData Json data | nvarchar(max) | max | NULL allowed |  |  |
|  | Result Result | nvarchar(max) | max | NULL allowed |  |  |
|  | Posted­Date­Time Posted date time | datetime | 8 | NULL allowed |  | (getdate()) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Intenal­Memo­Approve] |

MS\_­Description

Stores approval records related to internal memo transactions. The table is used to track the approval process of internal memos, including the approving user, approval status, and related workflow information.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |  |
|  | Intenal­Memo­ID Intenal memo identifier | numeric(30,0) | 17 | NULL allowed |  |
|  | User­ID User identifier | nvarchar(50) | 100 | NULL allowed |  |
|  | Assign­Date Assign date | smalldatetime | 4 | NULL allowed |  |
|  | Approve Flag indicating approve | bit | 1 | NULL allowed |  |
|  | Approve­Date Flag indicating approve date | smalldatetime | 4 | NULL allowed |  |
|  | Note Note | nvarchar(max) | max | NULL allowed |  |
|  | Is­Posted Flag indicating posted | bit | 1 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Intenal­Memo­Approve\_­Intenal­Memo­Approve | Auto­ID->[[dbo].[Intenal­Memo­Approve].[Auto­ID]](#Tjh2RLcpyf6GU0YgMoQxYIZQrVE=), Company­ID->[[dbo].[Intenal­Memo­Approve].[Company­ID]](#Tjh2RLcpyf6GU0YgMoQxYIZQrVE=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Internal­Memo] |

MS\_­Description

Stores internal memo records created within the system. The table is used to document internal notes, requests, or operational messages between users and may be linked to approval workflows or related business transactions.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Tr­Date­Time Tr date time | datetime | 8 | NULL allowed |  |
|  | Salesman­No Salesman number | int | 4 | NULL allowed |  |
|  | Memo­Subject Memo subject | nvarchar(500) | 1000 | NULL allowed |  |
|  | Memo­Department Memo department | nvarchar(500) | 1000 | NULL allowed |  |
|  | Memo­Description Memo description | nvarchar(max) | max | NULL allowed |  |
|  | First­Approval First approval | bit | 1 | NULL allowed |  |
|  | First­Approval­Description First approval description | nvarchar(max) | max | NULL allowed |  |
|  | First­Approval­User­ID First approval user identifier | varchar(50) | 50 | NULL allowed |  |
|  | Second­Approval Second approval | bit | 1 | NULL allowed |  |
|  | Second­Approval­Description Second approval description | nvarchar(max) | max | NULL allowed |  |
|  | Second­Approval­User­ID Second approval user identifier | varchar(50) | 50 | NULL allowed |  |
|  | Device­Sys­ID Device sys identifier | varchar(50) | 50 | NULL allowed |  |
|  | Send­To­User­ID Send to user identifier | varchar(50) | 50 | NULL allowed |  |
|  | Cust­ID Cust identifier | varchar(50) | 50 | NULL allowed |  |
|  | Merch­Auto­ID Merch auto identifier | numeric(30,0) | 17 | NULL allowed |  |
|  | User­ID User identifier | varchar(50) | 50 | NULL allowed |  |
|  | Created­By Created by | varchar(50) | 50 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Invoice­Delivery­DF] |

MS\_­Description

Stores the detailed records of invoices included in delivery transactions. Each record represents an invoice or item related to a specific delivery, helping track what was delivered and link delivery operations with the corresponding sales invoices.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Comp­No Comp number | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Vou­Year Vou year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Vou­No Vou number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Vou­Type Vou type | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Item­No Item number | varchar(20) | 20 | NOT NULL |
| ![](data:image/png;base64...) | Batch­No Batch number | varchar(16) | 16 | NOT NULL |
| ![](data:image/png;base64...) | Unit­Code Unit code | varchar(5) | 5 | NOT NULL |
|  | Qty Quantity | money | 8 | NULL allowed |
|  | Bonus Bonus | money | 8 | NULL allowed |
|  | Sell­Value Sell value | float | 8 | NULL allowed |
|  | Disc­Perc Disc percentage | money | 8 | NULL allowed |
|  | Disc­Value Disc value | float | 8 | NULL allowed |
|  | Tax­Perc Tax percentage | money | 8 | NULL allowed |
|  | Tax­Value Tax value | float | 8 | NULL allowed |
|  | Item­Desc Item description | varchar(100) | 100 | NULL allowed |
|  | Unit­Price Unit price | float | 8 | NULL allowed |
|  | Tot­Weight Tot weight | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Invoice­Delivery­HF] |

MS\_­Description

Stores the header information for invoice delivery transactions. Each record represents a delivery operation that groups multiple invoice delivery details, helping track delivery activities, assigned routes, vehicles, and related operational information.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Comp­No Comp number | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Vou­Year Vou year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Vou­No Vou number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Vou­Type Vou type | smallint | 2 | NOT NULL |
|  | Vou­Date Vou date | smalldatetime | 4 | NULL allowed |
|  | Salesman­No Salesman number | smallint | 2 | NULL allowed |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |
|  | Ref1 Ref 1 | varchar(50) | 50 | NULL allowed |
|  | Ref2 Ref 2 | varchar(50) | 50 | NULL allowed |
|  | Notes Notes | varchar(4000) | 4000 | NULL allowed |
|  | Is­Delivered Flag indicating delivered | bit | 1 | NULL allowed |
|  | Delivered­Date­Time Delivered date time | smalldatetime | 4 | NULL allowed |
|  | Delivered­Salesman­No Delivered salesman number | int | 4 | NULL allowed |
|  | Posted­To­ERP Posted to erp | bit | 1 | NULL allowed |
|  | Vou­Disc­Perc Vou disc percentage | float | 8 | NULL allowed |
|  | Customer­Disc­Perc Customer disc percentage | float | 8 | NULL allowed |
|  | Assign­Date­Time Assign date time | smalldatetime | 4 | NULL allowed |
|  | Cancel­Reason­ID Cancel reason identifier | int | 4 | NULL allowed |
|  | Delivered­Store­No Delivered store number | nvarchar(50) | 100 | NULL allowed |
|  | Route­Name Route name | nvarchar(50) | 100 | NULL allowed |
|  | Number­Of­Packages Number of packages | int | 4 | NULL allowed |
|  | Credit­Cash Credit cash | smallint | 2 | NULL allowed |
|  | Assistant­Salesman­No Assistant salesman number | int | 4 | NULL allowed |
|  | Shipping­Date Shipping date | smalldatetime | 4 | NULL allowed |
|  | Delivery­Car­ID Delivery car identifier | int | 4 | NULL allowed |
|  | Manifest­ID Manifest identifier | int | 4 | NULL allowed |
|  | ERPVou­No Erp vou number | nvarchar(50) | 100 | NULL allowed |
|  | Prova­No Prova number | bigint | 8 | NULL allowed |
|  | Amount Amount | float | 8 | NULL allowed |
|  | Payment­Type­ID Payment type identifier | int | 4 | NULL allowed |
|  | Route­ID Route identifier | int | 4 | NULL allowed |
|  | Delivery­Batch­ID Delivery batch identifier | int | 4 | NULL allowed |
|  | Ref­Order­Year Ref order year | smallint | 2 | NULL allowed |
|  | Ref­Order­No Ref order number | int | 4 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Invoice­History­DF] |

MS\_­Description

Stores the detailed history records of invoice transactions. The table keeps historical information about invoice items, quantities, prices, and related details, allowing the system to track past invoice activities for reporting, auditing, and analysis purposes.

sColumns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Comp­No Comp number | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Vou­Year Vou year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Vou­No Vou number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Vou­Type Vou type | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Item­No Item number | varchar(20) | 20 | NOT NULL |
| ![](data:image/png;base64...) | Batch­No Batch number | varchar(16) | 16 | NOT NULL |
| ![](data:image/png;base64...) | Unit­Code Unit code | varchar(5) | 5 | NOT NULL |
|  | Qty Quantity | money | 8 | NULL allowed |
|  | Bonus Bonus | money | 8 | NULL allowed |
|  | Sell­Value Sell value | float | 8 | NULL allowed |
|  | Disc­Perc Disc percentage | money | 8 | NULL allowed |
|  | Disc­Value Disc value | float | 8 | NULL allowed |
|  | Tax­Perc Tax percentage | money | 8 | NULL allowed |
|  | Tax­Value Tax value | float | 8 | NULL allowed |
|  | Item­Desc Item description | varchar(100) | 100 | NULL allowed |
|  | Unit­Price Unit price | float | 8 | NULL allowed |
|  | Vou­Disc­Value Vou disc value | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Invoice­History­HF] |

MS\_­Description

Stores the header records of historical invoice transactions. Each record represents a past invoice document and groups the related invoice detail lines, allowing the system to keep a historical archive of invoices for reporting, auditing, and analysis purposes.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Comp­No Comp number | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Vou­Year Vou year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Vou­No Vou number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Vou­Type Vou type | smallint | 2 | NOT NULL |
|  | Vou­Date Vou date | smalldatetime | 4 | NULL allowed |
|  | Store­No Store number | int | 4 | NULL allowed |
|  | Salesman­No Salesman number | smallint | 2 | NULL allowed |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |
|  | Inv­Status Inv status | varchar(50) | 50 | NULL allowed |
|  | Ref1 Ref 1 | varchar(50) | 50 | NULL allowed |
|  | Ref2 Ref 2 | varchar(50) | 50 | NULL allowed |
|  | Notes Notes | varchar(4000) | 4000 | NULL allowed |
|  | Vou­Disc­Perc Vou disc percentage | float | 8 | NULL allowed |
|  | Customer­Disc­Perc Customer disc percentage | float | 8 | NULL allowed |
|  | ERPVou­No Erp vou number | nvarchar(50) | 100 | NULL allowed |
|  | Payment­Disc­Perc Payment disc percentage | float | 8 | NULL allowed |
|  | Payment­Disc­Amt Payment disc amount | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Invoice­Return­Link] |

MS\_­Description

Stores the relationship between sales invoices and their corresponding return transactions. The table is used to link returned items to the original invoice, helping the system track return history and ensure accurate financial and inventory adjustments.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Ret­Vou­Type Ret vou type | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Ret­Vou­Year Ret vou year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Ret­Vou­No Ret vou number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Inv­Vou­Type Inv vou type | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Inv­Vou­Year Inv vou year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Inv­Vou­No Inv vou number | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |
|  | Qty Quantity | money | 8 | NULL allowed |
|  | Bonus Bonus | money | 8 | NULL allowed |
|  | Unit­Price Unit price | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Invoice­Return­Link\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Invoice­Return­Link\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Invoice­Return­Link\_­Items­Units | Company­ID->[[dbo].[Items­Units].[Company­ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=), Unit­ID->[[dbo].[Items­Units].[ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Issue­Items­Details] |

MS\_­Description

Stores the detailed item lines for item issue transactions. Each record represents an item issued from inventory, including quantities and related information, allowing the system to track which items were issued and support accurate inventory movement and control.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Order­Year Order year | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |
|  | Quantity Quantity | float | 8 | NULL allowed |
|  | Bonus Bonus | float | 8 | NULL allowed |
|  | Promises­Date Promises date | smalldatetime | 4 | NULL allowed |
|  | Price Price | float | 8 | NULL allowed |
|  | Discount­Amount Discount amount | float | 8 | NULL allowed |
|  | Discount­Percent Discount percent | float | 8 | NULL allowed |
|  | Voucher­Discount Voucher discount | float | 8 | NULL allowed |
|  | Tax­Type Tax type | smallint | 2 | NULL allowed |
|  | Tax­Percent Tax percent | float | 8 | NULL allowed |
|  | Tax­Amount Tax amount | float | 8 | NULL allowed |
|  | Foreign­Price Foreign price | float | 8 | NULL allowed |
|  | Foreign­Discount­Amount Foreign discount amount | float | 8 | NULL allowed |
|  | Foreign­Discount­Percent Foreign discount percent | float | 8 | NULL allowed |
|  | Foreign­Vou­Discount Foreign vou discount | float | 8 | NULL allowed |
|  | Foreign­Tax­Percent Foreign tax percent | float | 8 | NULL allowed |
|  | Foreign­Tax­Amount Foreign tax amount | float | 8 | NULL allowed |
|  | Customer­Discount­Amount Customer discount amount | float | 8 | NULL allowed |
|  | Foreign­Customer­Discount­Amount Foreign customer discount amount | float | 8 | NULL allowed |
|  | Orginal­Qty Orginal quantity | float | 8 | NULL allowed |
|  | Orginal­Bonus Orginal bonus | float | 8 | NULL allowed |
|  | UPrice U price | float | 8 | NULL allowed |
|  | Tax­Type1 Tax type 1 | smallint | 2 | NULL allowed |
|  | Tax­Percent1 Tax percent 1 | float | 8 | NULL allowed |
|  | Tax­Amount1 Tax amount 1 | float | 8 | NULL allowed |
|  | Tax­Type2 Tax type 2 | smallint | 2 | NULL allowed |
|  | Tax­Percent2 Tax percent 2 | float | 8 | NULL allowed |
|  | Tax­Amount2 Tax amount 2 | float | 8 | NULL allowed |
|  | Manual\_­Bonus Manual bonus | float | 8 | NULL allowed |
|  | Exchange­Rate Exchange rate | float | 8 | NULL allowed |
|  | Manual\_­Disc Manual disc | float | 8 | NULL allowed |
|  | Qty­As­Bonus Qty as bonus | float | 8 | NULL allowed |
|  | Notes Notes | nvarchar(300) | 600 | NULL allowed |
|  | Bonus­Tax Bonus tax | float | 8 | NULL allowed |
|  | Bonus­Amount Bonus amount | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Issue­Items­Details\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Issue­Items­Details\_­Issue­Items­Headers | Company­ID->[[dbo].[Issue­Items­Headers].[Company­ID]](#n0zsYIhgt3HFGDQDkIZ/hWP6jnM=), Order­Year->[[dbo].[Issue­Items­Headers].[Order­Year]](#n0zsYIhgt3HFGDQDkIZ/hWP6jnM=), Order­No->[[dbo].[Issue­Items­Headers].[Order­No]](#n0zsYIhgt3HFGDQDkIZ/hWP6jnM=) |
| FK\_­Issue­Items­Details\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Issue­Items­Details\_­Items­Units | Company­ID->[[dbo].[Items­Units].[Company­ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=), Unit­ID->[[dbo].[Items­Units].[ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Issue­Items­Headers] |

MS\_­Description

Stores the header records of item issue transactions. Each record represents an item issuance operation from inventory and groups the related item details, helping track when and why items were issued and supporting inventory management and control.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­Year Order year | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
|  | Order­Date Order date | smalldatetime | 4 | NULL allowed |
|  | Promises­Date Promises date | smalldatetime | 4 | NULL allowed |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NULL allowed |
| ![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NULL allowed |
|  | Price­List­ID Price list identifier | int | 4 | NULL allowed |
|  | Discount­Amount Discount amount | float | 8 | NULL allowed |
|  | Discount­Percent Discount percent | float | 8 | NULL allowed |
|  | Foreign­Discount­Amount Foreign discount amount | float | 8 | NULL allowed |
|  | Foreign­Discount­Percent Foreign discount percent | float | 8 | NULL allowed |
| ![](data:image/png;base64...) | Currency­ID Currency identifier | smallint | 2 | NULL allowed |
|  | Exchange­Rate Exchange rate | float | 8 | NULL allowed |
|  | Notes Notes | nvarchar(500) | 1000 | NULL allowed |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |
|  | Posted­To­ERP Posted to erp | bit | 1 | NULL allowed |
|  | Route­ID Route identifier | int | 4 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(50) | 100 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(50) | 100 | NULL allowed |
|  | Payment­Type Payment type | int | 4 | NULL allowed |
|  | Server­Date Server date | smalldatetime | 4 | NULL allowed |
|  | WFApproved Wf approved | bit | 1 | NULL allowed |
|  | Approved Flag indicating approved | bit | 1 | NULL allowed |
|  | Documents­Types­ID Documents types identifier | int | 4 | NULL allowed |
|  | Tr­Date­Time Tr date time | smalldatetime | 4 | NULL allowed |
|  | Business­Unit­ID Business unit identifier | int | 4 | NULL allowed |
|  | Customer­Discount­Perc Customer discount percentage | float | 8 | NULL allowed |
|  | Customer­Discount­Amount Customer discount amount | float | 8 | NULL allowed |
|  | Is­Void Flag indicating void | bit | 1 | NULL allowed |
|  | Print­Original­Count Print original count | int | 4 | NULL allowed |
|  | Print­Copy­Count Print copy count | int | 4 | NULL allowed |
|  | Contract­ID Contract identifier | nvarchar(100) | 200 | NULL allowed |
|  | Foreign­Customer­Discount­Perc Foreign customer discount percentage | float | 8 | NULL allowed |
|  | Foreign­Customer­Discount­Amount Foreign customer discount amount | float | 8 | NULL allowed |
|  | Is­Post­Back­Order Flag indicating post back order | bit | 1 | NULL allowed |
|  | Is­Post­Back­Order­To­ERP Flag indicating post back order to erp | bit | 1 | NULL allowed |
|  | Credit­Cash Credit cash | int | 4 | NULL allowed |
|  | Posted­By­Email Posted by email | bit | 1 | NULL allowed |
|  | Accept­Date Accept date | smalldatetime | 4 | NULL allowed |
|  | Detail­Count Detail count | int | 4 | NULL allowed |
|  | Delivery­Batch­ID Delivery batch identifier | int | 4 | NULL allowed |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |
|  | Extra­Note Extra note | nvarchar(max) | max | NULL allowed |
|  | Is­Delivered Flag indicating delivered | bit | 1 | NULL allowed |
|  | Manual\_­Disc Manual disc | float | 8 | NULL allowed |
|  | Back­Order­Year Back order year | smallint | 2 | NULL allowed |
|  | Back­Order­No Back order number | bigint | 8 | NULL allowed |
|  | Final­Approval Final approval | bit | 1 | NULL allowed |
|  | Posted­To­ERPDate­Time Posted to erp date time | smalldatetime | 4 | NULL allowed |
|  | Used­In­Auto­Upload­Order Used in auto upload order | bit | 1 | NULL allowed |
|  | Location­Line­ID Location line identifier | int | 4 | NULL allowed |
|  | Make­Cash­Discount Make cash discount | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Issue­Items­Headers\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Issue­Items­Headers\_­Currencies | Currency­ID->[[dbo].[Currencies].[ID]](#k0NURIzYF8aeO/uxKYIEdxSccAg=) |
| FK\_­Issue­Items­Headers\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |
| FK\_­Issue­Items­Headers\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Person­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Items] |

MS\_­Description

Stores the master data of items used in the system. The table includes basic item information such as item code, description, category, units, and other properties required for sales, inventory management, and reporting. It is mainly used as the primary reference for all item-related transactions across the system.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Foreign­Name Foreign name | nvarchar(100) | 200 | NULL allowed |
|  | Short­Name Short name | nvarchar(50) | 100 | NULL allowed |
|  | Barcode Barcode | nvarchar(20) | 40 | NULL allowed |
| ![](data:image/png;base64...) | Categ­Code Categ code | nvarchar(20) | 40 | NULL allowed |
| ![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |
|  | Fill­Size Fill size | nvarchar(50) | 100 | NULL allowed |
|  | Minimum­Stock Minimum stock | float | 8 | NULL allowed |
|  | Is­Expiry Flag indicating expiry | bit | 1 | NULL allowed |
|  | Validity­Days Validity days | int | 4 | NULL allowed |
|  | Volume Volume | float | 8 | NULL allowed |
|  | Weight Weight | float | 8 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |
|  | Item­Image Item image | image | max | NULL allowed |
| ![](data:image/png;base64...) | Target­Reference­ID Target reference identifier | int | 4 | NULL allowed |
|  | Qty­In­All­Stores Qty in all stores | money | 8 | NULL allowed |
|  | Default­Unit Default unit | smallint | 2 | NULL allowed |
|  | Reference3 Reference 3 | nvarchar(100) | 200 | NULL allowed |
|  | Reference4 Reference 4 | nvarchar(100) | 200 | NULL allowed |
|  | Reference5 Reference 5 | nvarchar(100) | 200 | NULL allowed |
|  | Is­Tax­Exempt Flag indicating tax exempt | bit | 1 | NULL allowed |
|  | Item­Replacement­Group Item replacement group | int | 4 | NULL allowed |
|  | Is\_weighted Flag indicating weighted | bit | 1 | NULL allowed |
|  | PDFFile­ID Pdf file identifier | numeric(30,0) | 17 | NULL allowed |
|  | Video­File­ID Video file identifier | numeric(30,0) | 17 | NULL allowed |
|  | Used­In­Upload­Order Used in upload order | bit | 1 | NULL allowed |
| ![](data:image/png;base64...) | Sub­Target­Reference­ID Sub target reference identifier | int | 4 | NULL allowed |
|  | Tax­Type Tax type | int | 4 | NULL allowed |
|  | Tax Tax | float | 8 | NULL allowed |
|  | Erp\_­Reference Erp reference | varchar(50) | 50 | NULL allowed |
|  | Item­Bonus­Target­Group­ID Item bonus target group identifier | int | 4 | NULL allowed |
|  | Item­Order­In­List Item order in list | int | 4 | NULL allowed |
| ![](data:image/png;base64...) | Suggest­Group­ID Suggest group identifier | int | 4 | NULL allowed |
| ![](data:image/png;base64...) | Class­ID Class identifier | int | 4 | NULL allowed |
|  | Basket­Item­No Basket item number | nvarchar(100) | 200 | NULL allowed |
|  | Basket­Volume Basket volume | float | 8 | NULL allowed |
|  | Is­Basket­Item Flag indicating basket item | bit | 1 | NULL allowed |
|  | Is­Cust­Stock­Item Flag indicating cust stock item | bit | 1 | NULL allowed |
|  | Van­Custody­Unit­Serial Van custody unit serial | smallint | 2 | NULL allowed |
|  | Promotion­Item­Group­ID Promotion item group identifier | int | 4 | NULL allowed |
|  | Is­Batch­Item Flag indicating batch item | bit | 1 | NULL allowed |
|  | Item­Qty­Status Item qty status | nvarchar(50) | 100 | NULL allowed |
|  | Is­Cash­Only Flag indicating cash only | smallint | 2 | NULL allowed |
|  | Is­Most­Sales Flag indicating most sales | bit | 1 | NULL allowed |
|  | Ref6 Ref 6 | nvarchar(100) | 200 | NULL allowed |
|  | Ref7 Ref 7 | nvarchar(100) | 200 | NULL allowed |
|  | Is­For­Sales Flag indicating for sales | bit | 1 | NULL allowed |
| ![](data:image/png;base64...) | Item­Group­ID Item group identifier | int | 4 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Items\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Items\_­Items­Categories | Company­ID->[[dbo].[Items­Categories].[Company­ID]](#VLpTtrh4X181/GF+u73WO6VXNcU=), Categ­Code->[[dbo].[Items­Categories].[Categ­Code]](#VLpTtrh4X181/GF+u73WO6VXNcU=) |
| FK\_­Items\_­Items­Classes | Company­ID->[[dbo].[Items­Classes].[Company­ID]](#tMGSpWb23eyxaVb5HBx7c2TARBU=), Class­ID->[[dbo].[Items­Classes].[ID]](#tMGSpWb23eyxaVb5HBx7c2TARBU=) |
| FK\_­Items\_­Items­Groups | Company­ID->[[dbo].[Items­Groups].[Company­ID]](#MZfHge8v9E75q53qtli4sSu4w7Y=), Item­Group­ID->[[dbo].[Items­Groups].[ID]](#MZfHge8v9E75q53qtli4sSu4w7Y=) |
| FK\_­Items\_­Items­Suggest­Group | Company­ID->[[dbo].[Items­Suggest­Group].[Company­ID]](#eFOPzB4o/FP/xq7NcBASDPwgaEw=), Suggest­Group­ID->[[dbo].[Items­Suggest­Group].[ID]](#eFOPzB4o/FP/xq7NcBASDPwgaEw=) |
| FK\_­Items\_­Items­Units | Company­ID->[[dbo].[Items­Units].[Company­ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=), Unit­ID->[[dbo].[Items­Units].[ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=) |
| FK\_­Items\_­Targets­References | Company­ID->[[dbo].[Targets­References].[Company­ID]](#pTJEdyfW1its0oUM5wpR5Npe6Js=), Target­Reference­ID->[[dbo].[Targets­References].[ID]](#pTJEdyfW1its0oUM5wpR5Npe6Js=) |
| FK\_­Items\_­Targets­References1 | Company­ID->[[dbo].[Targets­References].[Company­ID]](#pTJEdyfW1its0oUM5wpR5Npe6Js=), Sub­Target­Reference­ID->[[dbo].[Targets­References].[ID]](#pTJEdyfW1its0oUM5wpR5Npe6Js=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Items­Barcodes] |

MS\_­Description

Stores barcode information associated with items in the system. Each record links a barcode to a specific item and unit, allowing the system to identify items quickly during sales, inventory, and scanning operations.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |
| ![](data:image/png;base64...) | Barcode Barcode | nvarchar(100) | 200 | NOT NULL |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Items­Categories] |

MS\_­Description

Stores the categories used to classify items in the system. The table helps organize items into groups based on business needs, making it easier to manage pricing, reporting, promotions, and inventory analysis.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Categ­Code Categ code | nvarchar(20) | 40 | NOT NULL |
|  | Parent Parent | nvarchar(20) | 40 | NULL allowed |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Foreign­Name Foreign name | nvarchar(200) | 400 | NULL allowed |
|  | Short­Name Short name | nvarchar(50) | 100 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |
|  | Level Level | int | 4 | NULL allowed |
|  | Categ­Sort Categ sort | int | 4 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Items­Categories\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Items­Categ­Stock­Details] |

MS\_­Description

Stores stock-related details for items based on their categories. The table is used to manage inventory information for each item category, helping the system track stock quantities, control inventory levels, and support reporting and analysis by item category.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­Type­ID Transaction type identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­Year Transaction year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­No Transaction number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Categ­Code Categ code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |
|  | Quantity Quantity | float | 8 | NULL allowed |
|  | Notes Notes | nvarchar(300) | 600 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Items­Categ­Stock­Header] |

MS\_­Description

Stores the header records of stock transactions related to item categories. Each record represents a main stock operation grouped by category, while the related detail records contain the specific item quantities and stock information.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­Type­ID Transaction type identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­Year Transaction year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­No Transaction number | int | 4 | NOT NULL |
|  | Transaction­Date Transaction date | smalldatetime | 4 | NULL allowed |
|  | Sales­Person­ID Sales identifier | int | 4 | NULL allowed |
|  | Customer­ID Customer identifier | bigint | 8 | NULL allowed |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |
|  | Notes Notes | nvarchar(500) | 1000 | NULL allowed |
|  | Posted­To­ERP Posted to erp | bit | 1 | NULL allowed |
|  | Route­ID Route identifier | int | 4 | NULL allowed |
|  | Tr­Date­Time Tr date time | smalldatetime | 4 | NULL allowed |
|  | Server­Date Server date | smalldatetime | 4 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Items­Classes] |

MS\_­Description

Stores the classification of items used in the system. The table is used to group items into different classes based on business rules such as product type, brand, or marketing category, helping improve reporting, pricing strategies, and sales analysis.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NOT NULL |
|  | Short­Name Short name | nvarchar(10) | 20 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Items­Classes\_­Items­Classes | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Items­Group­Bonus­Target] |

MS\_­Description

Stores items group bonus target data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Short­Name Short name | nvarchar(10) | 20 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Items­Group­Bonus­Target\_­Items­Group­Bonus­Target | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Items­Groups] |

MS\_­Description

This Table defines item groups so that items would be linked to it later to be used in salesman transactions monitoring/qty limiting

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NOT NULL |
|  | Short­Name Short name | nvarchar(10) | 20 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Items­Groups\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Items­Inventory] |

MS\_­Description

Stores items inventory data ??

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(18,0) | 9 | NOT NULL |
|  | Company­ID Company identifier | smallint | 2 | NOT NULL |
|  | Item­Code Item code | varchar(50) | 50 | NULL allowed |
|  | Inv­Date Inv date | smalldatetime | 4 | NULL allowed |
|  | Cost Cost | float | 8 | NULL allowed |
|  | Qty Quantity | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Items­Minimum­Sales] |

MS\_­Description

This table contains predefined minimum sales amounts based on customer group and/or category. Salesmen will not be permitted to sell below these amounts for customers belonging to that group

Notes:

Requires system option /Options activation

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Item­Categ Item categ | varchar(50) | 50 | NOT NULL |
| ![](data:image/png;base64...) | Customer­Group Customer group | int | 4 | NOT NULL |
|  | Minimum­Sales Minimum sales | float | 8 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Items­Price­Exceptions] |

MS\_­Description

This table stores special item prices defined for specific customers and item codes. When such prices are defined, the salesperson must sell the item using the predefined special price, overriding the original price list linked to the customer

Note: needs system option activation

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |  |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |  |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |  |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |  |
|  | Start­Date Start date | smalldatetime | 4 | NULL allowed |  |
|  | End­Date End date | smalldatetime | 4 | NULL allowed |  |
|  | Price Price | float | 8 | NULL allowed |  |
|  | Tax­Type Tax type | int | 4 | NULL allowed |  |
|  | Tax Tax | float | 8 | NULL allowed |  |
|  | Discount­Percent Discount percent | float | 8 | NULL allowed |  |
|  | Use­In­Return Flag indicating use in return | bit | 1 | NULL allowed |  |
|  | Use­In­Sales Flag indicating use in sales | bit | 1 | NULL allowed |  |
|  | Sell­Price2 Sell price 2 | float | 8 | NULL allowed |  |
|  | Sell­Price3 Sell price 3 | float | 8 | NULL allowed |  |
|  | Qty Quantity | money | 8 | NULL allowed |  |
|  | Tax­Type1 Tax type 1 | int | 4 | NULL allowed |  |
|  | Tax1 Tax 1 | float | 8 | NULL allowed |  |
|  | Tax­Type2 Tax type 2 | int | 4 | NULL allowed |  |
|  | Tax2 Tax 2 | float | 8 | NULL allowed |  |
|  | Create­Date Create date | datetime | 8 | NULL allowed |  |
|  | Reference1 Reference 1 | varchar(50) | 50 | NULL allowed |  |
|  | Reference2 Reference 2 | varchar(50) | 50 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Items­Price­Exceptions\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Items­Price­Exceptions\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |
| FK\_­Items­Price­Exceptions\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Items­Price­Exceptions\_­Items­Units | Company­ID->[[dbo].[Items­Units].[Company­ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=), Unit­ID->[[dbo].[Items­Units].[ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Items­Priority] |

MS\_­Description

This table holds items that are given display priority in the salesman tablet. These items will appear at the top of the item list or in a dedicated section and can also be used in the suggested order list.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | bigint | 8 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
| ![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NULL allowed |  |
|  | Use­In­Suggested­Order Flag indicating use in suggested order | bit | 1 | NULL allowed |  |
| ![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NULL allowed |  |
|  | Qty Quantity | float | 8 | NULL allowed |  |
| ![](data:image/png;base64...) | Cust­Type­ID Cust type identifier | int | 4 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Items­Priority\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Items­Priority\_­Customers­Types | Company­ID->[[dbo].[Customers­Types].[Company­ID]](#mUOPMl0ZzNBySPnrrjXsxaUEKvo=), Cust­Type­ID->[[dbo].[Customers­Types].[ID]](#mUOPMl0ZzNBySPnrrjXsxaUEKvo=) |
| FK\_­Items­Priority\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Items­Priority\_­Items­Units | Company­ID->[[dbo].[Items­Units].[Company­ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=), Unit­ID->[[dbo].[Items­Units].[ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Items­Related­To­Items] |

MS\_­Description

Stores items related to items data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...) | Related­Item­Code Related item code | nvarchar(100) | 200 | NOT NULL |
|  | Unit­ID Unit identifier | nvarchar(50) | 100 | NULL allowed |
|  | Qty Quantity | float | 8 | NULL allowed |
|  | Master­Qty­U4 Master qty u 4 | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Items­Related­To­Items\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Items­Related­To­Items\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Items­Replacement­Details] |

MS\_­Description

This table contains items replacement transaction details that were performed from salesperson on a certain customer

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Default |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |  |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Transaction­Type­ID Transaction type identifier | smallint | 2 | NOT NULL |  |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Transaction­Year Transaction year | smallint | 2 | NOT NULL |  |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Transaction­No Transaction number | int | 4 | NOT NULL |  |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |  |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |  |
| ![](data:image/png;base64...) | Item­Serial Item serial | int | 4 | NOT NULL | ((0)) |
| ![](data:image/png;base64...) | In­Out­Type In out type | int | 4 | NOT NULL |  |
|  | Quantity Quantity | float | 8 | NULL allowed |  |
|  | Notes Notes | nvarchar(300) | 600 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Items­Replacement­Details\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Items­Replacement­Details\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Items­Replacement­Details\_­Items­Replacement­Headers | Company­ID->[[dbo].[Items­Replacement­Headers].[Company­ID]](#y11F0kJ6sM3TTvveJX8WrHifX1U=), Transaction­Type­ID->[[dbo].[Items­Replacement­Headers].[Transaction­Type­ID]](#y11F0kJ6sM3TTvveJX8WrHifX1U=), Transaction­Year->[[dbo].[Items­Replacement­Headers].[Transaction­Year]](#y11F0kJ6sM3TTvveJX8WrHifX1U=), Transaction­No->[[dbo].[Items­Replacement­Headers].[Transaction­No]](#y11F0kJ6sM3TTvveJX8WrHifX1U=) |
| FK\_­Items­Replacement­Details\_­Items­Units | Company­ID->[[dbo].[Items­Units].[Company­ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=), Unit­ID->[[dbo].[Items­Units].[ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Items­Replacement­Groups] |

MS\_­Description

This table stores item replacement group data for items with similar prices, allowing salesmen to perform item replacement transactions

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Short­Name Short name | nvarchar(50) | 100 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Items­Replacement­Groups\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Items­Replacement­Headers] |

MS\_­Description

Stores Items Replacement header records

This will hold main information about items replacement transaction done by the salesman such as year and no of transaction an customerid

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­Type­ID Transaction type identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­Year Transaction year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­No Transaction number | int | 4 | NOT NULL |
|  | Transaction­Date Transaction date | smalldatetime | 4 | NULL allowed |
| ![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NULL allowed |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NULL allowed |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |
|  | Notes Notes | nvarchar(500) | 1000 | NULL allowed |
|  | Posted­To­ERP Posted to erp | bit | 1 | NULL allowed |
| ![](data:image/png;base64...) | Route­ID Route identifier | int | 4 | NULL allowed |
|  | Tr­Date­Time Tr date time | smalldatetime | 4 | NULL allowed |
|  | Server­Date Server date | smalldatetime | 4 | NULL allowed |
|  | Posted­To­ERP\_­IN Posted to erp in | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Items­Replacement­Headers\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Items­Replacement­Headers\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |
| FK\_­Items­Replacement­Headers\_­Routes­Information | Company­ID->[[dbo].[Routes­Information].[Company­ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=), Route­ID->[[dbo].[Routes­Information].[ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=) |
| FK\_­Items­Replacement­Headers\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Person­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Items­Suggest­Group] |

MS\_­Description

Stores items suggest group data

This will hold suggested items groups that can be used by salesman based on a special criteria so that it will be focused on by salesman ??

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Short­Name Short name | nvarchar(10) | 20 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |
|  | Unit­Code Unit code | nvarchar(50) | 100 | NULL allowed |
|  | Qty Quantity | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Items­Suggest­Group­Link] |

MS\_­Description

Stores items suggest group link data

This table stores the linkage between items group IDs and there target amount per year and per month salesperson acting in field would have those groups linkage on his tablet for target achievement minimum quantities measurement of that group

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Suggest­Group­ID Suggest group identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Target­Month Target month | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Target­Year Target year | smallint | 2 | NOT NULL |
|  | Target­Count Target count | float | 8 | NULL allowed |
|  | Invoice­Min­Qty­Unit Invoice min qty unit | nvarchar(50) | 100 | NULL allowed |
|  | Invoice­Min­Qty Invoice min quantity | float | 8 | NULL allowed |
|  | Invoice­Min­Qty\_­Main Invoice min qty main | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Items­Suggest­Group­Link­With­Items] |

MS\_­Description

Stores items suggest group link with items data

This table stores the linkage between items and predefined suggested item group IDs so that each linked item appears within its corresponding group on the salesperson’s tablet

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Suggest­Group­ID Suggest group identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Item­Code Item code | nvarchar(50) | 100 | NOT NULL |
|  | Qty Quantity | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Items­Units] |

MS\_­Description

Stores items units data

This table contains general unit details that are linked to all items in the system. These units will be displayed on the salesperson’s tablet according to the units defined for each item individually

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | nvarchar(50) | 100 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Short­Name Short name | nvarchar(10) | 20 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |
|  | Is­Integer­Qty Flag indicating integer qty | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Items­Units\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Items­Units­Details] |

MS\_­Description

Stores Items Units detail line records

This will have the linkage of items to general units in the system, these linked units for each item will be the units shown on salesperson tablet per each item individually

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |
|  | Convert­Rate Convert rate | float | 8 | NULL allowed |
|  | Unit­Serial Unit serial | int | 4 | NULL allowed |
|  | Barcode Barcode | nvarchar(20) | 40 | NULL allowed |
|  | Volume Volume | float | 8 | NULL allowed |
|  | Weight Weight | float | 8 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |
|  | Used­In­Upload­Order Used in upload order | bit | 1 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Items­Units­Details\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Items­Units­Details\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Items­Units­Details\_­Items­Units | Company­ID->[[dbo].[Items­Units].[Company­ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=), Unit­ID->[[dbo].[Items­Units].[ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Items­Units­Details\_1] |

MS\_­Description

Stores items units details 1 data

Dummy data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |
|  | Convert­Rate Convert rate | float | 8 | NULL allowed |
|  | Unit­Serial Unit serial | int | 4 | NULL allowed |
|  | Barcode Barcode | nvarchar(20) | 40 | NULL allowed |
|  | Volume Volume | float | 8 | NULL allowed |
|  | Weight Weight | float | 8 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |
|  | Used­In­Upload­Order Used in upload order | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Items­Units­Details\_1\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Items­Units­Details\_1\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Items­Units­Details\_1\_­Items­Units | Company­ID->[[dbo].[Items­Units].[Company­ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=), Unit­ID->[[dbo].[Items­Units].[ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Jo­Tax­Result] |

MS\_­Description

Stores jo tax result data

This table is used to store QR Code and UUID unique numbers for invoices / return invoices that were deported to income department and a QR Code which are assigned by tax department

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­No Transaction number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­Type­ID Transaction type identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­Year Transaction year | int | 4 | NOT NULL |
|  | EINV\_­QR Einv qr | nvarchar(max) | max | NULL allowed |
|  | EINV\_­INV\_­UUID Einv inv uuid | nvarchar(max) | max | NULL allowed |
|  | status Status | nvarchar(max) | max | NULL allowed |
|  | Error­Message Error message | nvarchar(max) | max | NULL allowed |
|  | UUID Uuid | nvarchar(max) | max | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[JOTax­Settings] |

MS\_­Description

Stores jo tax settings data

This Table will hold all necessary settings including IPs and passkeys through which salesperson would have the ability to deport invoices / return invoices to income department to be registered and assigned a unique QR code

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Setting­Key Setting key | varchar(500) | 500 | NOT NULL |
|  | Setting­Value Setting value | nvarchar(max) | max | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[JSONData­Log] |

MS\_­Description

Stores json data log data

This Table will hold all Json log of each transaction that salesperson performed in market as reference to be used by technical support later if necessary

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Tab­Sys­ID Tab sys identifier | nvarchar(100) | 200 | NOT NULL |
|  | Salesperson­ID Salesperson identifier | int | 4 | NULL allowed |
|  | JSONData Json data | nvarchar(max) | max | NULL allowed |
|  | Tr­Date­Time Tr date time | smalldatetime | 4 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Kasih­Survey] |

MS\_­Description

Stores kasih survey data

This is a customized Survey data table for a certain customer (kasih)

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Customer­Name Customer name | nvarchar(500) | 1000 | NULL allowed |  |
|  | Customer­Image Customer image | image | max | NULL allowed |  |
|  | Customer­Image1 Customer image 1 | image | max | NULL allowed |  |
|  | Customer­Image2 Customer image 2 | image | max | NULL allowed |  |
|  | Customer­Image3 Customer image 3 | image | max | NULL allowed |  |
|  | Customer­Image4 Customer image 4 | image | max | NULL allowed |  |
|  | Shelf­Image­Before Shelf image before | image | max | NULL allowed |  |
|  | Shelf­Image­Before1 Shelf image before 1 | image | max | NULL allowed |  |
|  | Shelf­Image­Before2 Shelf image before 2 | image | max | NULL allowed |  |
|  | Shelf­Image­Before3 Shelf image before 3 | image | max | NULL allowed |  |
|  | Shelf­Image­Before4 Shelf image before 4 | image | max | NULL allowed |  |
|  | Shelf­Image­After Shelf image after | image | max | NULL allowed |  |
|  | Shelf­Image­After1 Shelf image after 1 | image | max | NULL allowed |  |
|  | Shelf­Image­After2 Shelf image after 2 | image | max | NULL allowed |  |
|  | Shelf­Image­After3 Shelf image after 3 | image | max | NULL allowed |  |
|  | Shelf­Image­After4 Shelf image after 4 | image | max | NULL allowed |  |
|  | Existing­Place Existing place | nvarchar(500) | 1000 | NULL allowed |  |
|  | Notes Notes | nvarchar(max) | max | NULL allowed |  |
|  | Item­Availability Item availability | nvarchar(500) | 1000 | NULL allowed |  |
|  | Item­Movement Item movement | nvarchar(500) | 1000 | NULL allowed |  |
|  | Need­Order Need order | nvarchar(500) | 1000 | NULL allowed |  |
|  | Item­Shown­By­Transmed Item shown by transmed | nvarchar(500) | 1000 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Language] |

MS\_­Description

Stores language data

Holds languages used in system (not used currently)

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | ID ID identifier | smallint | 2 | NOT NULL | 1 - 1 |
|  | Desc1 Desc 1 | nvarchar(50) | 100 | NULL allowed |  |
|  | Short­ID Short identifier | nvarchar(10) | 20 | NULL allowed |  |
|  | Lang­Image Lang image | image | max | NULL allowed |  |
|  | Is­Default Flag indicating default | bit | 1 | NULL allowed |  |
|  | Lang­Path Lang path | nvarchar(300) | 600 | NULL allowed |  |
|  | Is­Rtl Flag indicating rtl | bit | 1 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Language­Dictionary] |

MS\_­Description

Stores language dictionary data

Holds languages dictionary which is contains back office objects names in that language (not used currently)

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | ID ID identifier | nvarchar(200) | 400 | NOT NULL |
|  | Desc1 Desc 1 | nvarchar(max) | max | NULL allowed |
|  | Desc2 Desc 2 | nvarchar(max) | max | NULL allowed |
|  | Desc3 Desc 3 | nvarchar(max) | max | NULL allowed |
|  | Desc4 Desc 4 | nvarchar(max) | max | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Locations] |

MS\_­Description

Stores locations data

This Table would hold Geographical locations IDs and names , with possible parent relation between main location and sub location , these location are linked to customers through customers table by their IDs

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Parent Parent | int | 4 | NULL allowed |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Short­Name Short name | nvarchar(50) | 100 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |
|  | Loc\_­Level Loc level | int | 4 | NULL allowed |
|  | Population­No Population number | bigint | 8 | NULL allowed |
|  | Foreign­Name Foreign name | nvarchar(100) | 200 | NULL allowed |
|  | Posted­To­ERP Posted to erp | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Locations\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Locations\_­Locations | Company­ID->[[dbo].[Locations].[Company­ID]](#eNuBnAAgcTN3Hu1UlDB+jaS/yKQ=), Parent->[[dbo].[Locations].[ID]](#eNuBnAAgcTN3Hu1UlDB+jaS/yKQ=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Location­Targets] |

MS\_­Description

Stores location targets data.

This table would hold main data related to setting a certain achievement target for salesman per location of customers that ere sold items, based on year, month, and Qty/amount

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Location­ID Location identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Target­Year Target year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Target­Month Target month | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Target­Type­ID Target type identifier | int | 4 | NULL allowed |
|  | Amount Amount | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Location­Targets\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Location­Targets\_­Locations | Company­ID->[[dbo].[Locations].[Company­ID]](#eNuBnAAgcTN3Hu1UlDB+jaS/yKQ=), Location­ID->[[dbo].[Locations].[ID]](#eNuBnAAgcTN3Hu1UlDB+jaS/yKQ=) |
| FK\_­Location­Targets\_­Targets­Types | Target­Type­ID->[[dbo].[Targets­Types].[ID]](#0/4snZsACLzbPDsnGKCgpJuaMnM=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Location­Targets­Details] |

MS\_­Description

Stores Location Targets detail line records

This table would hold details data related to setting a certain achievement target for salesman per location of customers that were sold items, based on year, month, and Qty/amount and target reference attached to each item / or a number of items

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Location­ID Location identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Target­Year Target year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Target­Month Target month | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Target­Reference­ID Target reference identifier | int | 4 | NOT NULL |
|  | Quantity Quantity | float | 8 | NULL allowed |
|  | Amount Amount | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Location­Targets­Details\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Location­Targets­Details\_­Locations | Company­ID->[[dbo].[Locations].[Company­ID]](#eNuBnAAgcTN3Hu1UlDB+jaS/yKQ=), Location­ID->[[dbo].[Locations].[ID]](#eNuBnAAgcTN3Hu1UlDB+jaS/yKQ=) |
| FK\_­Location­Targets­Details\_­Location­Targets | Company­ID->[[dbo].[Location­Targets].[Company­ID]](#xv9Dx8qyzuMEHBOqJJxT0nswzg0=), Location­ID->[[dbo].[Location­Targets].[Location­ID]](#xv9Dx8qyzuMEHBOqJJxT0nswzg0=), Target­Year->[[dbo].[Location­Targets].[Target­Year]](#xv9Dx8qyzuMEHBOqJJxT0nswzg0=), Target­Month->[[dbo].[Location­Targets].[Target­Month]](#xv9Dx8qyzuMEHBOqJJxT0nswzg0=) |
| FK\_­Location­Targets­Details\_­Targets­References | Company­ID->[[dbo].[Targets­References].[Company­ID]](#pTJEdyfW1its0oUM5wpR5Npe6Js=), Target­Reference­ID->[[dbo].[Targets­References].[ID]](#pTJEdyfW1its0oUM5wpR5Npe6Js=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Log­Actions] |

MS\_­Description

Stores Log­Actions log records

This would hold general types of actions names and IDs that are done by salesman in field such as CustEntry,CustLeave, OrderIssue ..etc

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Action­Id Action id | nvarchar(20) | 40 | NOT NULL |
|  | Action­Desc Action description | varchar(50) | 50 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Log­Action­Transaction] |

MS\_­Description

Stores Log­Action­Transaction log records

This would hold all transactions actions IDs that were actually Done by Salesman on field , these actions are mandatory Data for report issuing on visits and transactions done by salesman

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Comp­No Comp number | smallint | 2 | NOT NULL |  |
|  | Action­ID Action identifier | nvarchar(20) | 40 | NOT NULL |  |
|  | Time­Stamp Time stamp | datetime | 8 | NOT NULL |  |
|  | Salesman­ID Salesman identifier | nvarchar(20) | 40 | NOT NULL |  |
|  | Data1 Data 1 | nvarchar(max) | max | NULL allowed |  |
|  | Data2 Data 2 | nvarchar(max) | max | NULL allowed |  |
|  | Data3 Data 3 | nvarchar(max) | max | NULL allowed |  |
|  | Data4 Data 4 | nvarchar(50) | 100 | NULL allowed |  |
|  | Data5 Data 5 | nvarchar(50) | 100 | NULL allowed |  |
|  | Gps­X Gps x | nchar(50) | 100 | NULL allowed |  |
|  | Gps­Y Gps y | nchar(50) | 100 | NULL allowed |  |
|  | Route­ID Route identifier | int | 4 | NULL allowed |  |
|  | OSFA\_­Auto­ID Osfa auto identifier | numeric(30,0) | 17 | NULL allowed |  |
|  | Posted­By­Email Posted by email | bit | 1 | NULL allowed |  |
|  | Vehicle­Id Vehicle id | varchar(50) | 50 | NULL allowed |  |
|  | Car­Counter Car counter | bigint | 8 | NULL allowed |  |
|  | Is­SMSSend Flag indicating sms send | bit | 1 | NULL allowed |  |
|  | GPSOn Gps on | bit | 1 | NULL allowed |  |
|  | Network­On Network on | bit | 1 | NULL allowed |  |
|  | Internet­On Internet on | bit | 1 | NULL allowed |  |
|  | App­Version App version | varchar(50) | 50 | NULL allowed |  |
|  | Is­Procced Flag indicating procced | bit | 1 | NULL allowed |  |
|  | Cust­Loc­Line­ID Cust loc line identifier | varchar(50) | 50 | NULL allowed |  |
|  | Assistants­IDs Assistants i ds | varchar(50) | 50 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Log­Action­Transaction\_] |

MS\_­Description

Stores Log­Action­Transaction\_ log records

Dummy Data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
| Comp­No Comp number | smallint | 2 | NOT NULL |  |
| Action­ID Action identifier | nvarchar(20) | 40 | NOT NULL |  |
| Time­Stamp Time stamp | datetime | 8 | NOT NULL |  |
| Salesman­ID Salesman identifier | nvarchar(20) | 40 | NOT NULL |  |
| Data1 Data 1 | nvarchar(max) | max | NULL allowed |  |
| Data2 Data 2 | nvarchar(max) | max | NULL allowed |  |
| Data3 Data 3 | nvarchar(max) | max | NULL allowed |  |
| Data4 Data 4 | nvarchar(50) | 100 | NULL allowed |  |
| Data5 Data 5 | nvarchar(50) | 100 | NULL allowed |  |
| Gps­X Gps x | nchar(50) | 100 | NULL allowed |  |
| Gps­Y Gps y | nchar(50) | 100 | NULL allowed |  |
| Route­ID Route identifier | int | 4 | NULL allowed |  |
| OSFA\_­Auto­ID Osfa auto identifier | numeric(30,0) | 17 | NULL allowed |  |
| Posted­By­Email Posted by email | bit | 1 | NULL allowed |  |
| Vehicle­Id Vehicle id | varchar(50) | 50 | NULL allowed |  |
| Car­Counter Car counter | bigint | 8 | NULL allowed |  |
| Is­SMSSend Flag indicating sms send | bit | 1 | NULL allowed |  |
| GPSOn Gps on | bit | 1 | NULL allowed |  |
| Network­On Network on | bit | 1 | NULL allowed |  |
| Internet­On Internet on | bit | 1 | NULL allowed |  |
| App­Version App version | varchar(50) | 50 | NULL allowed |  |
| Is­Procced Flag indicating procced | bit | 1 | NULL allowed |  |
| Cust­Loc­Line­ID Cust loc line identifier | varchar(50) | 50 | NULL allowed |  |
| Assistants­IDs Assistants i ds | varchar(50) | 50 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Maintinance­Orders] |

MS\_­Description

Stores maintinance orders data

This would hold Maintenance order basic data that is gathered by a maintenance representative

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Salesman­No Salesman number | int | 4 | NULL allowed |  |
|  | Customer­ID Customer identifier | bigint | 8 | NULL allowed |  |
|  | Cust­Tel Cust tel | varchar(500) | 500 | NULL allowed |  |
|  | Contact­Person Contact person | varchar(500) | 500 | NULL allowed |  |
|  | Licence­Person­Name Licence person name | varchar(500) | 500 | NULL allowed |  |
|  | Commercial­Cust­Name Commercial cust name | varchar(500) | 500 | NULL allowed |  |
|  | Maintenance­Order­Type Maintenance order type | int | 4 | NULL allowed |  |
|  | Favourite­Visit­Time Favourite visit time | varchar(500) | 500 | NULL allowed |  |
|  | Cust­Refrigerator Cust refrigerator | varchar(4000) | 4000 | NULL allowed |  |
|  | New­Cust­Name New cust name | varchar(500) | 500 | NULL allowed |  |
|  | New­Licence­Cust­Name New licence cust name | varchar(500) | 500 | NULL allowed |  |
|  | New­Contact­Person New contact person | varchar(500) | 500 | NULL allowed |  |
|  | New­Commercial­Cust­Name New commercial cust name | varchar(500) | 500 | NULL allowed |  |
|  | New­Cust­Tel New cust tel | varchar(500) | 500 | NULL allowed |  |
|  | Cust­Refrigerator­No Cust refrigerator number | varchar(500) | 500 | NULL allowed |  |
|  | Contract­No Contract number | varchar(500) | 500 | NULL allowed |  |
|  | Diagnostic Diagnostic | varchar(4000) | 4000 | NULL allowed |  |
|  | Maintenance­Notes Maintenance notes | varchar(max) | max | NULL allowed |  |
|  | Refrigerator­Serial­No Refrigerator serial number | varchar(500) | 500 | NULL allowed |  |
|  | Refrigerator­Model Refrigerator model | varchar(500) | 500 | NULL allowed |  |
|  | Refrigerator­Draw­Reason­ID Refrigerator draw reason identifier | int | 4 | NULL allowed |  |
|  | Refrigerator­Draw­Reason­Notes Refrigerator draw reason notes | varchar(max) | max | NULL allowed |  |
|  | Device­Sys­ID Device sys identifier | varchar(50) | 50 | NULL allowed |  |
|  | Customer­Has­Been­Visited Customer has been visited | bit | 1 | NULL allowed |  |
|  | Supervisor­Notes Supervisor notes | nvarchar(max) | max | NULL allowed |  |
|  | Evaluating­Customer­Site Evaluating customer site | nvarchar(max) | max | NULL allowed |  |
|  | Evaluating­Customer­Withdrawals Evaluating customer withdrawals | nvarchar(max) | max | NULL allowed |  |
|  | Evaluating­Customer­Financial­Position Evaluating customer financial position | nvarchar(max) | max | NULL allowed |  |
|  | Customer­Agreement Customer agreement | nvarchar(max) | max | NULL allowed |  |
|  | First­Approval First approval | bit | 1 | NULL allowed |  |
|  | First­Approval­Description First approval description | nvarchar(max) | max | NULL allowed |  |
|  | First­Approval­User­ID First approval user identifier | varchar(50) | 50 | NULL allowed |  |
|  | Second­Approval Second approval | bit | 1 | NULL allowed |  |
|  | Second­Approval­Description Second approval description | nvarchar(max) | max | NULL allowed |  |
|  | Second­Approval­User­ID Second approval user identifier | varchar(50) | 50 | NULL allowed |  |
|  | Send­To­User­ID Send to user identifier | nvarchar(50) | 100 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Maintinance­Orders­Approve] |

MS\_­Description

Stores maintinance orders approve data

This will hold information on approved / non approved maintenance orders list shown and managed by a back office user

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
|  | User­ID User identifier | nvarchar(50) | 100 | NULL allowed |
|  | Assign­Date Assign date | smalldatetime | 4 | NULL allowed |
|  | Approve Flag indicating approve | bit | 1 | NULL allowed |
|  | Approve­Date Flag indicating approve date | smalldatetime | 4 | NULL allowed |
|  | Note Note | nvarchar(max) | max | NULL allowed |
|  | Is­Posted Flag indicating posted | bit | 1 | NULL allowed |
| ![](data:image/png;base64...) | Lineserial Lineserial | int | 4 | NOT NULL |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MAZ\_­Route\_­EMAIL\_­Final] |

MS\_­Description

Stores maz route email final data

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| Salesman­Name Salesman name | nvarchar(200) | 400 | NULL allowed |
| Route­Date Route date | smalldatetime | 4 | NULL allowed |
| Route­Count Route count | int | 4 | NULL allowed |
| Positive­Call Positive call | int | 4 | NULL allowed |
| Negative­Call Negative call | int | 4 | NULL allowed |
| Out­Of­Route Out of route | int | 4 | NULL allowed |
| Not­VIsited Not v isited | int | 4 | NULL allowed |
| NOInvoices No invoices | int | 4 | NULL allowed |
| Total­Collection Total collection | float | 8 | NULL allowed |
| Total­Amount Total amount | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Menu] |

MS\_­Description

Stores menu data

This will hold all menu screens names shown to back office users

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | ID ID identifier | bigint | 8 | NOT NULL |
|  | Desc1 Desc 1 | nvarchar(200) | 400 | NULL allowed |
|  | Desc2 Desc 2 | nvarchar(200) | 400 | NULL allowed |
|  | Page­Url Page url | nvarchar(500) | 1000 | NULL allowed |
|  | Width Width | float | 8 | NULL allowed |
|  | Height Height | float | 8 | NULL allowed |
|  | Show­Actions Show actions | bit | 1 | NULL allowed |
|  | Parent­ID Parent identifier | bigint | 8 | NULL allowed |
|  | Menu­Icon Menu icon | nvarchar(100) | 200 | NULL allowed |
|  | Is­Active Flag indicating active | bit | 1 | NULL allowed |
|  | Search­Behavior Search behavior | nvarchar(50) | 100 | NULL allowed |
|  | Sort­No Sort number | bigint | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MIMETypes] |

MS\_­Description

Stores mime types data

This will hold information about all mime types used in system

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | App­Type App type | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...) | App­Ext App ext | nvarchar(100) | 200 | NOT NULL |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Assistants] |

MS\_­Description

Stores mms assistants data

This will hold information about assistance in an MMS system

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Assistants­ID Assistants identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Foreign­Name Foreign name | nvarchar(100) | 200 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |
|  | Day­Off Day off | nvarchar(100) | 200 | NULL allowed |
|  | Time­Work­From Time work from | smalldatetime | 4 | NULL allowed |
|  | Time­Work­To Time work to | smalldatetime | 4 | NULL allowed |
|  | Mobile­No Mobile number | nvarchar(500) | 1000 | NULL allowed |
|  | Email Email | nvarchar(500) | 1000 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Close­Order­Reasons] |

MS\_­Description

Stores mms close order reasons data

This wil hold basic information about MMS system Closed (fulfilled) orders

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Reason­ID Reason identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Foreign­Name Foreign name | nvarchar(100) | 200 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Devices­Info] |

MS\_­Description

Stores mms devices info data

This will hold information about the device that is Being offered Service by MMS system such as serial no , color size ..etc.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Device­ID Device identifier | int | 4 | NOT NULL |
|  | Parent Parent | int | 4 | NULL allowed |
|  | Name Name | nvarchar(500) | 1000 | NULL allowed |
|  | Foreign­Name Foreign name | nvarchar(500) | 1000 | NULL allowed |
|  | Device­Level Device level | int | 4 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |
|  | Size Size | nvarchar(100) | 200 | NULL allowed |
|  | Color Color | nvarchar(100) | 200 | NULL allowed |
|  | Use­Serial­No Flag indicating use serial no | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Diagnostic] |

MS\_­Description

Stores mms diagnostic data

This will hold diagnostic information on issues that appeared on the serviced device using MMS System

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Diagnostic­ID Diagnostic identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(200) | 400 | NULL allowed |
|  | Foreign­Name Foreign name | nvarchar(200) | 400 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |
|  | Is­Under­Warranty Flag indicating under warranty | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­DV\_­Error­Log] |

MS\_­Description

Stores mms dv error log data

This will hold Error log and description that showed on the serviced Device by MMS System

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | ID ID identifier | bigint | 8 | NOT NULL | 1 - 1 |
|  | Comp­No Comp number | smallint | 2 | NULL allowed |  |
|  | Salesman­No Salesman number | int | 4 | NULL allowed |  |
|  | Err­Desc Err description | ntext | max | NULL allowed |  |
|  | Sys­Date Sys date | smalldatetime | 4 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Invoice­Details] |

MS\_­Description

Stores MMS Invoice detail line records

This will hold invoice details in terms of attended items after offering service to a maintained device by MMS system

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Invoice­Year Invoice year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Invoice­No Invoice number | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Line­ID Line identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Item­No Item number | nvarchar(100) | 200 | NOT NULL |
|  | Qty Quantity | money | 8 | NULL allowed |
|  | Unit­Price Unit price | float | 8 | NULL allowed |
|  | Price Price | float | 8 | NULL allowed |
|  | Tax­Percent Tax percent | float | 8 | NULL allowed |
|  | Tax­Value Tax value | float | 8 | NULL allowed |
|  | Item­Discount­Percent Item discount percent | float | 8 | NULL allowed |
|  | Item­Discount­Value Item discount value | float | 8 | NULL allowed |
|  | Invoice­Discount­Value Invoice discount value | float | 8 | NULL allowed |
|  | Is­In­Warranty Flag indicating in warranty | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Invoices­Headers] |

MS\_­Description

Stores MMS Invoices header records

This will hold invoice basic information after offering service to a maintained device by MMS system

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Invoice­Year Invoice year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Invoice­No Invoice number | bigint | 8 | NOT NULL |
|  | Invoice­Date Invoice date | smalldatetime | 4 | NULL allowed |
|  | Invoice­Discount­Percent Invoice discount percent | float | 8 | NULL allowed |
|  | Total­Invoice­Discount­Value Total invoice discount value | float | 8 | NULL allowed |
|  | Total­Item­Discount­Value Total item discount value | float | 8 | NULL allowed |
|  | Total­Tax­Value Total tax value | float | 8 | NULL allowed |
|  | Total­Price Total price | float | 8 | NULL allowed |
|  | Notes Notes | nvarchar(500) | 1000 | NULL allowed |
|  | Order­Auto­ID Order auto identifier | numeric(30,0) | 17 | NULL allowed |
|  | Order­Sub­ID Order sub identifier | int | 4 | NULL allowed |
|  | Schedule­ID Schedule identifier | int | 4 | NULL allowed |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |
|  | Inv­Type Inv type | int | 4 | NULL allowed |
|  | Detail­Count Detail count | int | 4 | NULL allowed |
|  | Is­New­Serial Flag indicating new serial | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Items] |

MS\_­Description

Stores mms items data

This will contain a list of MMS system items available in store related to MMS system

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Item­No Item number | nvarchar(100) | 200 | NOT NULL |
|  | Name Name | nvarchar(500) | 1000 | NULL allowed |
|  | Foreign­Name Foreign name | nvarchar(500) | 1000 | NULL allowed |
|  | Item­Type Item type | int | 4 | NULL allowed |
|  | Category­ID Category identifier | int | 4 | NULL allowed |
|  | Unit­Price Unit price | float | 8 | NULL allowed |
|  | Barcode Barcode | nvarchar(200) | 400 | NULL allowed |
|  | Is­Required­Barcode Flag indicating required barcode | bit | 1 | NULL allowed |
|  | Is­Required­Serial­No Flag indicating required serial no | bit | 1 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |
|  | Is­In­Warranty Flag indicating in warranty | bit | 1 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Items­Categories] |

MS\_­Description

Stores mms items categories data

This will contain a list of category classification for items located on MMS system

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Category­ID Category identifier | int | 4 | NOT NULL |
|  | Parent Parent | int | 4 | NULL allowed |
|  | Name Name | nvarchar(500) | 1000 | NULL allowed |
|  | Foreign­Name Foreign name | nvarchar(500) | 1000 | NULL allowed |
|  | Category­Level Category level | int | 4 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Link\_­Device\_­Diagnostic] |

MS\_­Description

Stores mms link device diagnostic data

This will hold a relation between serviced device and diagnostic ID identifier for offered service for that device

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Device­ID Device identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Diagnostic­ID Diagnostic identifier | int | 4 | NOT NULL |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Link\_­Device\_­Items] |

MS\_­Description

Stores mms link device items data

This will hold a relation between serviced device and item no addressed for offered service for that device

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Device­ID Device identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Item­No Item number | nvarchar(100) | 200 | NOT NULL |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Link\_­Supervisor\_­Maintenance­Unit] |

MS\_­Description

Stores mms link supervisor maintenance unit data

???

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Supervisor­ID Supervisor identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Maintenance­Unit­ID Maintenance unit identifier | int | 4 | NOT NULL |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Link\_­Supervisor\_­Technician] |

MS\_­Description

Stores mms link supervisor technician data

???

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Supervisor­ID Supervisor identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Technician­ID Technician identifier | int | 4 | NOT NULL |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Link\_­Technician\_­Assistant] |

MS\_­Description

Stores mms link technician assistant data

???

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Technician­ID Technician identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Assistant­ID Assistant identifier | int | 4 | NOT NULL |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Maintenance­Technician] |

MS\_­Description

Stores mms maintenance technician data

This will hold information about the maintenance Technician offering service using MMS system

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Technician­ID Technician identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Foreign­Name Foreign name | nvarchar(100) | 200 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |
|  | Day­Off Day off | nvarchar(100) | 200 | NULL allowed |
|  | Time­Work­From Time work from | smalldatetime | 4 | NULL allowed |
|  | Time­Work­To Time work to | smalldatetime | 4 | NULL allowed |
|  | Mobile­No Mobile number | nvarchar(500) | 1000 | NULL allowed |
|  | Email Email | nvarchar(500) | 1000 | NULL allowed |
|  | Device­Password Device password | nvarchar(50) | 100 | NULL allowed |
|  | Is­Update­Stock Flag indicating update stock | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Maintenance­Technician\_­Items­Balance] |

MS\_­Description

Stores mms maintenance technician items balance data

This will hold information about items stock available in ­Maintenance Technician custody

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Technician­ID Technician identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Item­No Item number | nvarchar(100) | 200 | NOT NULL |
|  | Qty Quantity | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Maintenance­Technician­Permissions] |

MS\_­Description

Stores mms maintenance technician permissions data

This wil hodl information about permissions granted to a technician in MMS System

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Technician­ID Technician identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Permission­ID Permission identifier | int | 4 | NOT NULL |
|  | Permission­Access Permission access | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Maintenance­Technician­Permissions\_­Def] |

MS\_­Description

Stores mms maintenance technician permissions def data

???

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Permission­ID Permission identifier | int | 4 | NOT NULL |
|  | Ar­Name Ar name | nvarchar(200) | 400 | NULL allowed |
|  | Eng­Name Eng name | nvarchar(200) | 400 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Maintenance­Technician­Trans­Serials] |

MS\_­Description

Stores mms maintenance technician trans serials data

This will hold next transaction serials to be issued by technician tablet in terms of invoice and receipts

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Technician­ID Technician identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Ser­Year Ser year | smallint | 2 | NOT NULL |
|  | Invoice­Next­Serial Invoice next serial | bigint | 8 | NULL allowed |
|  | Receipt­Next­Serial Receipt next serial | bigint | 8 | NULL allowed |
|  | Invoice­Next­Serial\_2 Invoice next serial 2 | bigint | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Maintenance­Unit] |

MS\_­Description

Stores mms maintenance unit data

???

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Maintenance­Unit­ID Maintenance unit identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Foreign­Name Foreign name | nvarchar(100) | 200 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Order­Details] |

MS\_­Description

Stores MMS Order detail line records

This will have list of order items submitted by technician in MMS system

???

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­Auto­ID Order auto identifier | numeric(30,0) | 17 | NOT NULL |
| ![](data:image/png;base64...) | Order­Sub­ID Order sub identifier | int | 4 | NOT NULL |
|  | Device­ID Device identifier | int | 4 | NOT NULL |
|  | Diagnostic­ID Diagnostic identifier | int | 4 | NOT NULL |
|  | Serial­No Serial number | nvarchar(200) | 400 | NULL allowed |
|  | Is­In­Warranty Flag indicating in warranty | bit | 1 | NULL allowed |
|  | Warranty­No Warranty number | nvarchar(100) | 200 | NULL allowed |
|  | Warranty­Expire­Date Warranty expire date | smalldatetime | 4 | NULL allowed |
|  | Purchase­Date Purchase date | smalldatetime | 4 | NULL allowed |
|  | Purchase­Location Purchase location | nvarchar(200) | 400 | NULL allowed |
|  | Notes Notes | nvarchar(500) | 1000 | NULL allowed |
|  | Sub­Order­Status Sub order status | int | 4 | NULL allowed |
|  | Assigment­Date­Time Assigment date time | smalldatetime | 4 | NULL allowed |
|  | Diagnostic­Desc Diagnostic description | nvarchar(1000) | 2000 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Orders­Header] |

MS\_­Description

Stores MMS Orders header records

This will have list of order main information submitted by technician in MMS system

???

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
|  | Company­ID Company identifier | smallint | 2 | NOT NULL |  |
| ![](data:image/png;base64...) | Order­Auto­ID Order auto identifier | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Order­Year Order year | smallint | 2 | NULL allowed |  |
|  | Order­No Order number | bigint | 8 | NULL allowed |  |
|  | Order­Date Order date | smalldatetime | 4 | NULL allowed |  |
|  | Customer­ID Customer identifier | numeric(20,0) | 13 | NULL allowed |  |
|  | Order­Type­ID Order type identifier | int | 4 | NOT NULL |  |
|  | Tax­Type­ID Tax type identifier | int | 4 | NULL allowed |  |
|  | Reporter­ID Reporter identifier | int | 4 | NULL allowed |  |
|  | Show­Room Show room | nvarchar(200) | 400 | NULL allowed |  |
|  | Notes Notes | nvarchar(500) | 1000 | NULL allowed |  |
|  | User­ID User identifier | nvarchar(50) | 100 | NULL allowed |  |
|  | Order­Status Order status | int | 4 | NULL allowed |  |
|  | Call­Center­ID Call center identifier | int | 4 | NULL allowed |  |
|  | Entery­Date­Time Entery date time | smalldatetime | 4 | NULL allowed |  |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |  |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Order­Status] |

MS\_­Description

Stores mms order status data

This will have order Status Description of submitted by technician in MMS system

???

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Order­Status­ID Order status identifier | int | 4 | NOT NULL |
|  | Order­Status­Desc Order status description | varchar(150) | 150 | NULL allowed |
|  | Order­Status­Foreign­Desc Order status foreign description | varchar(150) | 150 | NULL allowed |
|  | Use­In­Device Flag indicating use in device | bit | 1 | NULL allowed |
|  | Need­Reason Need reason | int | 4 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Order­Types] |

MS\_­Description

Stores mms order types data

This will have list of order types that can be submitted by technician

???

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­Type­ID Order type identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Foreign­Name Foreign name | nvarchar(100) | 200 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Order­Visit­Details] |

MS\_­Description

Stores MMS Order Visit detail line records

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­Auto­ID Order auto identifier | numeric(30,0) | 17 | NOT NULL |
| ![](data:image/png;base64...) | Order­Sub­ID Order sub identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Schedule­ID Schedule identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Visit­ID Visit identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Line­ID Line identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Item­No Item number | nvarchar(100) | 200 | NOT NULL |
|  | Is­In­Warranty Flag indicating in warranty | bit | 1 | NULL allowed |
|  | Qty Quantity | money | 8 | NULL allowed |
|  | Item­Serial­No Item serial number | nvarchar(200) | 400 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Order­Visit­Images] |

MS\_­Description

Stores mms order visit images data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­Auto­ID Order auto identifier | numeric(30,0) | 17 | NOT NULL |
| ![](data:image/png;base64...) | Order­Sub­ID Order sub identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Schedule­ID Schedule identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Visit­ID Visit identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Line­ID Line identifier | int | 4 | NOT NULL |
|  | Image­Data Image data | image | max | NULL allowed |
|  | Is­Cust­Signs Flag indicating cust signs | bit | 1 | NULL allowed |
|  | Is­Replace Flag indicating replace | bit | 1 | NULL allowed |
|  | Image­Data­Base64 Image data base 64 | nvarchar(max) | max | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Order­Visits] |

MS\_­Description

Stores mms order visits data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­Auto­ID Order auto identifier | numeric(30,0) | 17 | NOT NULL |
| ![](data:image/png;base64...) | Order­Sub­ID Order sub identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Schedule­ID Schedule identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Visit­ID Visit identifier | int | 4 | NOT NULL |
|  | Start­Date­Time Start date time | smalldatetime | 4 | NULL allowed |
|  | End­Date­Time End date time | smalldatetime | 4 | NULL allowed |
|  | Start­Date­Time\_­Sys Start date time sys | smalldatetime | 4 | NULL allowed |
|  | End­Date­Time\_­Sys End date time sys | smalldatetime | 4 | NULL allowed |
|  | Procedure­Description Procedure description | nvarchar(max) | max | NULL allowed |
|  | Is­Device­Bring Flag indicating device bring | bit | 1 | NULL allowed |
|  | Bring­Date Bring date | smalldatetime | 4 | NULL allowed |
|  | Device­Attachment Device attachment | nvarchar(500) | 1000 | NULL allowed |
|  | Device­Status Device status | nvarchar(500) | 1000 | NULL allowed |
|  | Notes Notes | nvarchar(500) | 1000 | NULL allowed |
|  | Visit­Result Visit result | int | 4 | NULL allowed |
|  | Device­Serial­No Device serial number | nvarchar(200) | 400 | NULL allowed |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |
|  | Device­ID Device identifier | int | 4 | NULL allowed |
|  | Warranty­No Warranty number | nvarchar(100) | 200 | NULL allowed |
|  | Warranty­Expire­Date Warranty expire date | smalldatetime | 4 | NULL allowed |
|  | Purchase­Date Purchase date | smalldatetime | 4 | NULL allowed |
|  | Purchase­Location Purchase location | nvarchar(200) | 400 | NULL allowed |
|  | Cust\_­Full­Address Cust full address | nvarchar(500) | 1000 | NULL allowed |
|  | Cust\_­Telephone­No Cust telephone number | nvarchar(500) | 1000 | NULL allowed |
|  | Cust\_­Tax­Type­ID Cust tax type identifier | int | 4 | NULL allowed |
|  | Cust\_­Mobile­No Cust mobile number | nvarchar(500) | 1000 | NULL allowed |
|  | Expected­Amount Expected amount | float | 8 | NULL allowed |
|  | Diagnostic­Desc Diagnostic description | nvarchar(1000) | 2000 | NULL allowed |
|  | Close­Reason­ID Close reason identifier | int | 4 | NULL allowed |
|  | Diagnostic­ID Diagnostic identifier | int | 4 | NULL allowed |
|  | Service­Resolution­ID Service resolution identifier | int | 4 | NULL allowed |
|  | Service­Condition­ID Service condition identifier | int | 4 | NULL allowed |
|  | Posted­To­ERP Posted to erp | bit | 1 | NULL allowed |
|  | Is­In­Warranty Flag indicating in warranty | bit | 1 | NULL allowed |
|  | Cust­Name Cust name | nvarchar(500) | 1000 | NULL allowed |
|  | Show­Room­ID Show room identifier | int | 4 | NULL allowed |
|  | Other­Show­Room Other show room | nvarchar(500) | 1000 | NULL allowed |
|  | Inv­Ref Inv reference | nvarchar(500) | 1000 | NULL allowed |
|  | Is­Black­List Flag indicating black list | bit | 1 | NULL allowed |
|  | Is­Valid­Serial­No Flag indicating valid serial no | bit | 1 | NULL allowed |
|  | POInv­No Po inv number | nvarchar(500) | 1000 | NULL allowed |
|  | Cust\_­City­ID Cust city identifier | int | 4 | NULL allowed |
|  | Cust\_­Area­ID Cust area identifier | int | 4 | NULL allowed |
|  | Order­Status­Reason­ID Order status reason identifier | int | 4 | NULL allowed |
|  | Is­Replace Flag indicating replace | bit | 1 | NULL allowed |
|  | Replace­Note Replace note | nvarchar(max) | max | NULL allowed |
|  | Reading­Voltage Reading voltage | nvarchar(500) | 1000 | NULL allowed |
|  | Reading­Amber Reading amber | nvarchar(500) | 1000 | NULL allowed |
|  | Reading­Hertz Reading hertz | nvarchar(500) | 1000 | NULL allowed |
|  | Reading­Temp Reading temp | nvarchar(500) | 1000 | NULL allowed |
|  | Images­Count Images count | varchar(50) | 50 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Payments­Checks­Details] |

MS\_­Description

Stores MMS Payments Checks detail line records

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Payment­Year Payment year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Payment­No Payment number | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Line­ID Line identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Check­No Check number | int | 4 | NOT NULL |
|  | Due­Date Due date | smalldatetime | 4 | NULL allowed |
|  | Amount Amount | float | 8 | NULL allowed |
|  | Bank­ID Bank identifier | int | 4 | NULL allowed |
|  | Branch­ID Branch identifier | int | 4 | NULL allowed |
|  | Drawer­Name Drawer name | nvarchar(500) | 1000 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Payments­Header] |

MS\_­Description

Stores MMS Payments header records

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Payment­Year Payment year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Payment­No Payment number | bigint | 8 | NOT NULL |
|  | Payment­Date Payment date | smalldatetime | 4 | NULL allowed |
|  | Invoice­Year Invoice year | smallint | 2 | NOT NULL |
|  | Invoice­No Invoice number | bigint | 8 | NULL allowed |
|  | Cash­Amount Cash amount | float | 8 | NULL allowed |
|  | Check­Amount Check amount | float | 8 | NULL allowed |
|  | Notes Notes | nvarchar(500) | 1000 | NULL allowed |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |
|  | Order­Auto­ID Order auto identifier | numeric(30,0) | 17 | NULL allowed |
|  | Order­Sub­ID Order sub identifier | int | 4 | NULL allowed |
|  | Schedule­ID Schedule identifier | int | 4 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Reporters] |

MS\_­Description

Stores mms reporters data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Reporters­ID Reporters identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Foreign­Name Foreign name | nvarchar(100) | 200 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Schedule­Support­Visits] |

MS\_­Description

Stores mms schedule support visits data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­Auto­ID Order auto identifier | numeric(30,0) | 17 | NOT NULL |
| ![](data:image/png;base64...) | Order­Sub­ID Order sub identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Schedule­ID Schedule identifier | int | 4 | NOT NULL |
|  | Supervisor­ID Supervisor identifier | int | 4 | NULL allowed |
|  | Technician­ID Technician identifier | int | 4 | NULL allowed |
|  | Schedule­Date­Time Schedule date time | smalldatetime | 4 | NULL allowed |
|  | Assigment­Date­Time Assigment date time | smalldatetime | 4 | NULL allowed |
|  | Status Status | int | 4 | NULL allowed |
|  | Visit­Type Visit type | int | 4 | NULL allowed |
|  | Assistants­ID Assistants identifier | int | 4 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Schedule­Support­Visits\_­Log] |

MS\_­Description

Stores mms schedule support visits log data

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Log­ID Log identifier | numeric(18,0) | 9 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Order­Auto­ID Order auto identifier | numeric(30,0) | 17 | NULL allowed |  |
|  | Order­Sub­ID Order sub identifier | int | 4 | NULL allowed |  |
|  | Schedule­ID Schedule identifier | int | 4 | NULL allowed |  |
|  | Tr­Type Tr type | nvarchar(50) | 100 | NULL allowed |  |
|  | Tr­Date­Time Tr date time | smalldatetime | 4 | NULL allowed |  |
|  | User­ID User identifier | nvarchar(50) | 100 | NULL allowed |  |
|  | Technician­ID Technician identifier | int | 4 | NULL allowed |  |
|  | Assistants­ID Assistants identifier | int | 4 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Show­Rooms] |

MS\_­Description

Stores mms show rooms data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Show­Room­ID Show room identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Foreign­Name Foreign name | nvarchar(100) | 200 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Supervisors] |

MS\_­Description

Stores mms supervisors data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Supervisor­ID Supervisor identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Foreign­Name Foreign name | nvarchar(100) | 200 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |
|  | Mobile­No Mobile number | nvarchar(500) | 1000 | NULL allowed |
|  | Email Email | nvarchar(500) | 1000 | NULL allowed |
|  | Day­Off Day off | nvarchar(100) | 200 | NULL allowed |
|  | Time­Work­From Time work from | smalldatetime | 4 | NULL allowed |
|  | Time­Work­To Time work to | smalldatetime | 4 | NULL allowed |
|  | User­ID User identifier | nvarchar(50) | 100 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­System­Codes] |

MS\_­Description

Stores mms system codes data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Main­ID Main identifier | nvarchar(50) | 100 | NOT NULL |
| ![](data:image/png;base64...) | Sub­ID Sub identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(200) | 400 | NULL allowed |
|  | Foreign­Name Foreign name | nvarchar(200) | 400 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­System­Settings] |

MS\_­Description

Stores mms system settings data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Technician­ID Technician identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Option­ID Option identifier | int | 4 | NOT NULL |
|  | Option­Description Option description | varchar(500) | 500 | NULL allowed |
|  | Option­Value Option value | varchar(50) | 50 | NULL allowed |
|  | Notes Notes | varchar(500) | 500 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[MMS\_­Tax­Type] |

MS\_­Description

Stores mms tax type data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Tax­Type­ID Tax type identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Foreign­Name Foreign name | nvarchar(100) | 200 | NULL allowed |
|  | Tax­Percent Tax percent | float | 8 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Mobile­Version­Salesmen] |

MS\_­Description

Stores mobile version salesmen data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Compno Compno | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Multi­Targets] |

MS\_­Description

Stores multi targets data

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| Targe\_­Type\_­ID Targe type identifier | int | 4 | NULL allowed |
| Targe\_­Type\_name Targe type name | nvarchar(100) | 200 | NULL allowed |
| Target\_­Amount Target amount | float | 8 | NULL allowed |
| Achieved\_­Sales Achieved sales | float | 8 | NULL allowed |
| Achieved\_­Rate Achieved rate | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Nairoukh\_­Awtar\_­Salespersons­Exemptions] |

MS\_­Description

Stores nairoukh awtar salespersons exemptions data

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| Company­ID Company identifier | smallint | 2 | NULL allowed |
| Salesperson­ID Salesperson identifier | int | 4 | NULL allowed |
| Position­ID Position identifier | int | 4 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Nairoukh­Route­Customers­Position­Change] |

MS\_­Description

Stores nairoukh route customers position change data

Dummy data

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| Company­ID Company identifier | int | 4 | NULL allowed |
| Positions­ID Positions identifier | int | 4 | NULL allowed |
| Route­ID Route identifier | int | 4 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[New­Competitive­Items] |

MS\_­Description

Stores new competitive items data

This will Hold information about competitive items gathered by salesman using his tablet or added by back-office user about competitive items from other companies ,all available data would reflect on tablet after update

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | New­Competitive­Item­Code New competitive item code | nvarchar(100) | 200 | NOT NULL |
|  | Sales­Person Sales person | int | 4 | NULL allowed |
| ![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NULL allowed |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
| ![](data:image/png;base64...) | Categ­Code Categ code | nvarchar(20) | 40 | NULL allowed |
|  | Competitive­Company Competitive company | nvarchar(100) | 200 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­New­Competitive­Items\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­New­Competitive­Items\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­New­Competitive­Items\_­Items­Categories | Company­ID->[[dbo].[Items­Categories].[Company­ID]](#VLpTtrh4X181/GF+u73WO6VXNcU=), Categ­Code->[[dbo].[Items­Categories].[Categ­Code]](#VLpTtrh4X181/GF+u73WO6VXNcU=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[New­Customer­Default­Value] |

MS\_­Description

This Table is used to determine default inserted values in back office for added new customer by salesman such as pricelist , or due days , in case of any are being applicable upon adding a customer by salesman, this is used in procedure ot\_importNewcustomers as default values

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
|  | Business­Unit­ID Business unit identifier | int | 4 | NULL allowed |
| ![](data:image/png;base64...) | Payment­Type­ID Payment type identifier | int | 4 | NULL allowed |
| ![](data:image/png;base64...) | Price­List­ID Price list identifier | int | 4 | NULL allowed |
|  | Credit­Limit Credit limit | float | 8 | NULL allowed |
|  | Due­Days Due days | smallint | 2 | NULL allowed |
|  | Chqs­Due­Days Chqs due days | smallint | 2 | NULL allowed |
|  | Allow­Chqs Flag indicating allow chqs | bit | 1 | NULL allowed |
|  | Tax­Include Tax include | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­New­Customer­Default­Value\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­New­Customer­Default­Value\_­Payments­Types | Company­ID->[[dbo].[Payments­Types].[Company­ID]](#lO8zg+RAFUjBCTc7z+Mf67JVfuQ=), Payment­Type­ID->[[dbo].[Payments­Types].[ID]](#lO8zg+RAFUjBCTc7z+Mf67JVfuQ=) |
| FK\_­New­Customer­Default­Value\_­Price­Lists | Company­ID->[[dbo].[Price­Lists].[Company­ID]](#UTuGUXmxHIFiIaREw25LxgcqPnU=), Price­List­ID->[[dbo].[Price­Lists].[ID]](#UTuGUXmxHIFiIaREw25LxgcqPnU=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[New­Customer­Special­Fields\_­Def] |

MS\_­Description

This is a new added table to add new fields for new customers to be filled later by salesman in recent versions of OSFA application used by salesman in add customer function

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Field­ID Field identifier | int | 4 | NOT NULL |
|  | Field­Caption Field caption | varchar(500) | 500 | NULL allowed |
|  | Field­Foreign­Caption Field foreign caption | varchar(500) | 500 | NULL allowed |
|  | Is­Required Flag indicating required | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Notifications] |

MS\_­Description

This is a table to enter scheduled notifications by Special terms to send them to salesman through his tablet at certain events

Defined by client

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Tr­Date­Time Tr date time | datetime | 8 | NULL allowed |  |
|  | Salesman­No Salesman number | int | 4 | NULL allowed |  |
|  | Noti\_­Subject Noti subject | nvarchar(500) | 1000 | NULL allowed |  |
|  | Noti\_­Description Noti description | nvarchar(max) | max | NULL allowed |  |
|  | Ref1 Ref 1 | varchar(50) | 50 | NULL allowed |  |
|  | Ref2 Ref 2 | varchar(50) | 50 | NULL allowed |  |
|  | Is­Posted Flag indicating posted | bit | 1 | NULL allowed |  |
|  | Stop­OSFA Stop osfa | bit | 1 | NULL allowed |  |
|  | Must­Update­Data Must update data | bit | 1 | NULL allowed |  |
|  | Release­Trans­Lock Release trans lock | bit | 1 | NULL allowed |  |
|  | Special­Operation Special operation | nvarchar(50) | 100 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[No­Transactions­Log] |

MS\_­Description

This is a table listing log of reasons added by salesmen for not being able to perform a transaction in field by salesmen such as invoice

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | bigint | 8 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
| ![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NULL allowed |  |
| ![](data:image/png;base64...) | Route­ID Route identifier | int | 4 | NULL allowed |  |
|  | Reason­ID Reason identifier | int | 4 | NULL allowed |  |
|  | Visit­Date Visit date | smalldatetime | 4 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Notes Notes | nvarchar(500) | 1000 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­No­Transactions­Log\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­No­Transactions­Log\_­Routes­Information | Company­ID->[[dbo].[Routes­Information].[Company­ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=), Route­ID->[[dbo].[Routes­Information].[ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=) |
| FK\_­No­Transactions­Log\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Person­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[No­Transactions­Reasons] |

MS\_­Description

This is a table listing of reasons added by salesmen for not being able to perform a transaction in field by salesmen such as invoice

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Reason­Type Reason type | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |
|  | Is­Need­Note Flag indicating need note | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­No­Transactions­Reasons\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Olives­Menu] |

MS\_­Description

This Table will hold Olives back-office Menu sections and sub sections names, this section will contain pages names shown to end user

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Parent Parent | int | 4 | NULL allowed |
|  | Ar­Name Ar name | varchar(200) | 200 | NULL allowed |
|  | Eng­Name Eng name | varchar(200) | 200 | NULL allowed |
|  | Page­Name Page name | varchar(100) | 100 | NULL allowed |
|  | Pr­ID Pr identifier | int | 4 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Olives­Pages] |

MS\_­Description

This Will contain all pages named and ID located on the back-office web application for end user

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Ar­Name Ar name | nvarchar(200) | 400 | NULL allowed |
|  | Eng­Name Eng name | nvarchar(200) | 400 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Olives­User­Permissions] |

MS\_­Description

Every back office web application user has certain permission to access / change information on back office web application and this table contains these pages and every user permissions to use them

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | User­ID User identifier | nvarchar(50) | 100 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Pr­ID Pr identifier | int | 4 | NOT NULL |
|  | Can­Access Can access | bit | 1 | NULL allowed |
|  | Can­Add Can add | bit | 1 | NULL allowed |
|  | Can­Edit Can edit | bit | 1 | NULL allowed |
|  | Can­Delete Can delete | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Olives­User­Permissions\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Olives­User­Permissions\_­Olives­Pages | Pr­ID->[[dbo].[Olives­Pages].[ID]](#umDYyQd/6G5m1+B9mm2585SO9Co=) |
| FK\_­Olives­User­Permissions\_­Users | User­ID->[[dbo].[Users].[User­ID]](#xK94j3lvTOeFWmPRc97loDl7d/s=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[OLV\_­PDC] |

MS\_­Description

Stores olv pdc data ??

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| Check­Num Check number | int | 4 | NULL allowed |
| Check­Sum Check sum | float | 8 | NULL allowed |
| Rcpt­Date Rcpt date | smalldatetime | 4 | NULL allowed |
| Card­Code Card code | nvarchar(50) | 100 | NULL allowed |
| Card­Name Card name | nvarchar(200) | 400 | NULL allowed |
| Check­Date Check date | smalldatetime | 4 | NULL allowed |
| Bank­Name Bank name | nvarchar(200) | 400 | NULL allowed |
| Salesperson­ID Salesperson identifier | int | 4 | NULL allowed |
| Salesman­Name Salesman name | nvarchar(200) | 400 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Orders­Delivery­Details] |

MS\_­Description

This Table contain items details about every delivery order that need to be delivered by a delivery salesman to designated customers

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Delivery­Year Delivery year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Delivery­No Delivery number | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Order­Year Order year | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Unit­Code Unit code | nvarchar(50) | 100 | NOT NULL |
|  | Qty Quantity | float | 8 | NULL allowed |
|  | Bonus Bonus | float | 8 | NULL allowed |
|  | UPrice U price | float | 8 | NULL allowed |
|  | Item­Disc­Perc Item disc percentage | float | 8 | NULL allowed |
|  | Tax­Perc Tax percentage | float | 8 | NULL allowed |
|  | Tax­Type Tax type | smallint | 2 | NULL allowed |
|  | Transfer­Order­Year Transfer order year | smallint | 2 | NULL allowed |
|  | Transfer­Order­No Transfer order number | int | 4 | NULL allowed |
|  | Delivery­Date Delivery date | smalldatetime | 4 | NULL allowed |
|  | User­ID User identifier | nvarchar(50) | 100 | NULL allowed |
|  | Is­Delivered Flag indicating delivered | bit | 1 | NULL allowed |
|  | Delivered­Date­Time Delivered date time | smalldatetime | 4 | NULL allowed |
| ![](data:image/png;base64...) | Car­ID Car identifier | int | 4 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Orders­Delivery­Details\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Orders­Delivery­Details\_­Delivery­Cars | Company­ID->[[dbo].[Delivery­Cars].[Company­ID]](#TNGzSieGVszmfgt8DhcppCKtHI8=), Car­ID->[[dbo].[Delivery­Cars].[ID]](#TNGzSieGVszmfgt8DhcppCKtHI8=) |
| FK\_­Orders­Delivery­Details\_­Orders­Delivery­Details | Company­ID->[[dbo].[Orders­Details].[Company­ID]](#ac0JxNTydSTnAtNRvzK3jD4cJoI=), Order­Year->[[dbo].[Orders­Details].[Order­Year]](#ac0JxNTydSTnAtNRvzK3jD4cJoI=), Order­No->[[dbo].[Orders­Details].[Order­No]](#ac0JxNTydSTnAtNRvzK3jD4cJoI=), Item­Code->[[dbo].[Orders­Details].[Item­Code]](#ac0JxNTydSTnAtNRvzK3jD4cJoI=), Unit­Code->[[dbo].[Orders­Details].[Unit­ID]](#ac0JxNTydSTnAtNRvzK3jD4cJoI=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Orders­Delivery­Info] |

MS\_­Description

This table contains information regarding customers having delivery orders such as Customer name , customer address …etc.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Order­Year Order year | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
|  | Po­No Po number | nvarchar(50) | 100 | NULL allowed |
|  | Cust­Name Cust name | nvarchar(100) | 200 | NULL allowed |
|  | Cust­Address Cust address | nvarchar(200) | 400 | NULL allowed |
|  | Mob­No Mob number | nvarchar(50) | 100 | NULL allowed |
|  | Tel­No Tel number | nvarchar(50) | 100 | NULL allowed |
|  | Notes Notes | nvarchar(max) | max | NULL allowed |
|  | Ref1 Ref 1 | nvarchar(50) | 100 | NULL allowed |
|  | Ref2 Ref 2 | nvarchar(50) | 100 | NULL allowed |
|  | Attachment­Path Attachment path | nvarchar(50) | 100 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Orders­Delivery­Info\_­Orders­Headers | Company­ID->[[dbo].[Orders­Headers].[Company­ID]](#DayzTm2CXWhInZ/pRQJ0Z15TOuE=), Order­Year->[[dbo].[Orders­Headers].[Order­Year]](#DayzTm2CXWhInZ/pRQJ0Z15TOuE=), Order­No->[[dbo].[Orders­Headers].[Order­No]](#DayzTm2CXWhInZ/pRQJ0Z15TOuE=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Orders­Details] |

MS\_­Description

This tables contains items details information for order transaction type performed by salesman in field such as qty and price

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Order­Year Order year | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |
|  | Quantity Quantity | float | 8 | NULL allowed |
|  | Bonus Bonus | float | 8 | NULL allowed |
|  | Promises­Date Promises date | smalldatetime | 4 | NULL allowed |
|  | Price Price | float | 8 | NULL allowed |
|  | Discount­Amount Discount amount | float | 8 | NULL allowed |
|  | Discount­Percent Discount percent | float | 8 | NULL allowed |
|  | Voucher­Discount Voucher discount | float | 8 | NULL allowed |
|  | Tax­Type Tax type | smallint | 2 | NULL allowed |
|  | Tax­Percent Tax percent | float | 8 | NULL allowed |
|  | Tax­Amount Tax amount | float | 8 | NULL allowed |
|  | Foreign­Price Foreign price | float | 8 | NULL allowed |
|  | Foreign­Discount­Amount Foreign discount amount | float | 8 | NULL allowed |
|  | Foreign­Discount­Percent Foreign discount percent | float | 8 | NULL allowed |
|  | Foreign­Vou­Discount Foreign vou discount | float | 8 | NULL allowed |
|  | Foreign­Tax­Percent Foreign tax percent | float | 8 | NULL allowed |
|  | Foreign­Tax­Amount Foreign tax amount | float | 8 | NULL allowed |
|  | Customer­Discount­Amount Customer discount amount | float | 8 | NULL allowed |
|  | Foreign­Customer­Discount­Amount Foreign customer discount amount | float | 8 | NULL allowed |
|  | Orginal­Qty Orginal quantity | float | 8 | NULL allowed |
|  | Orginal­Bonus Orginal bonus | float | 8 | NULL allowed |
|  | UPrice U price | float | 8 | NULL allowed |
|  | Tax­Type1 Tax type 1 | smallint | 2 | NULL allowed |
|  | Tax­Percent1 Tax percent 1 | float | 8 | NULL allowed |
|  | Tax­Amount1 Tax amount 1 | float | 8 | NULL allowed |
|  | Tax­Type2 Tax type 2 | smallint | 2 | NULL allowed |
|  | Tax­Percent2 Tax percent 2 | float | 8 | NULL allowed |
|  | Tax­Amount2 Tax amount 2 | float | 8 | NULL allowed |
|  | Manual\_­Bonus Manual bonus | float | 8 | NULL allowed |
|  | Exchange­Rate Exchange rate | float | 8 | NULL allowed |
|  | Manual\_­Disc Manual disc | float | 8 | NULL allowed |
|  | Qty­As­Bonus Qty as bonus | float | 8 | NULL allowed |
|  | Notes Notes | nvarchar(300) | 600 | NULL allowed |
|  | Bonus­Tax Bonus tax | float | 8 | NULL allowed |
|  | Bonus­Amount Bonus amount | float | 8 | NULL allowed |
|  | Line­Sort Line sort | smallint | 2 | NULL allowed |
|  | Ref1 Ref 1 | varchar(500) | 500 | NULL allowed |
|  | Ref2 Ref 2 | varchar(500) | 500 | NULL allowed |
|  | Ref3 Ref 3 | varchar(500) | 500 | NULL allowed |
|  | Total­Price Total price | float | 8 | NULL allowed |
|  | Sys­Code­Type­ID Sys code type identifier | nvarchar(100) | 200 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Orders­Details\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Orders­Details\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Orders­Details\_­Items­Units | Company­ID->[[dbo].[Items­Units].[Company­ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=), Unit­ID->[[dbo].[Items­Units].[ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=) |
| FK\_­Orders­Details\_­Orders­Headers | Company­ID->[[dbo].[Orders­Headers].[Company­ID]](#DayzTm2CXWhInZ/pRQJ0Z15TOuE=), Order­Year->[[dbo].[Orders­Headers].[Order­Year]](#DayzTm2CXWhInZ/pRQJ0Z15TOuE=), Order­No->[[dbo].[Orders­Headers].[Order­No]](#DayzTm2CXWhInZ/pRQJ0Z15TOuE=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Orders­Details\_­Log] |

MS\_­Description

Stores orders details log data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Order­Year Order year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | User­Id User identifier | nvarchar(100) | 200 | NOT NULL |
|  | Quantity Quantity | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Orders­Headers] |

MS\_­Description

This tables contains general information for order transaction type performed by salesman in field such as customer and year and order no ..etc.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­Year Order year | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
|  | Order­Date Order date | smalldatetime | 4 | NULL allowed |
|  | Promises­Date Promises date | smalldatetime | 4 | NULL allowed |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NULL allowed |
| ![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NULL allowed |
| ![](data:image/png;base64...) | Price­List­ID Price list identifier | int | 4 | NULL allowed |
|  | Discount­Amount Discount amount | float | 8 | NULL allowed |
|  | Discount­Percent Discount percent | float | 8 | NULL allowed |
|  | Foreign­Discount­Amount Foreign discount amount | float | 8 | NULL allowed |
|  | Foreign­Discount­Percent Foreign discount percent | float | 8 | NULL allowed |
| ![](data:image/png;base64...) | Currency­ID Currency identifier | smallint | 2 | NULL allowed |
|  | Exchange­Rate Exchange rate | float | 8 | NULL allowed |
|  | Notes Notes | nvarchar(500) | 1000 | NULL allowed |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |
|  | Posted­To­ERP Posted to erp | bit | 1 | NULL allowed |
| ![](data:image/png;base64...) | Route­ID Route identifier | int | 4 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(50) | 100 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(50) | 100 | NULL allowed |
|  | Payment­Type Payment type | int | 4 | NULL allowed |
|  | Server­Date Server date | smalldatetime | 4 | NULL allowed |
|  | WFApproved Wf approved | bit | 1 | NULL allowed |
|  | Approved Flag indicating approved | bit | 1 | NULL allowed |
|  | Documents­Types­ID Documents types identifier | int | 4 | NULL allowed |
|  | Tr­Date­Time Tr date time | smalldatetime | 4 | NULL allowed |
| ![](data:image/png;base64...) | Business­Unit­ID Business unit identifier | int | 4 | NULL allowed |
|  | Customer­Discount­Perc Customer discount percentage | float | 8 | NULL allowed |
|  | Customer­Discount­Amount Customer discount amount | float | 8 | NULL allowed |
|  | Is­Void Flag indicating void | bit | 1 | NULL allowed |
|  | Print­Original­Count Print original count | int | 4 | NULL allowed |
|  | Print­Copy­Count Print copy count | int | 4 | NULL allowed |
| ![](data:image/png;base64...) | Contract­ID Contract identifier | nvarchar(100) | 200 | NULL allowed |
|  | Foreign­Customer­Discount­Perc Foreign customer discount percentage | float | 8 | NULL allowed |
|  | Foreign­Customer­Discount­Amount Foreign customer discount amount | float | 8 | NULL allowed |
|  | Is­Post­Back­Order Flag indicating post back order | bit | 1 | NULL allowed |
|  | Is­Post­Back­Order­To­ERP Flag indicating post back order to erp | bit | 1 | NULL allowed |
|  | Credit­Cash Credit cash | int | 4 | NULL allowed |
|  | Posted­By­Email Posted by email | bit | 1 | NULL allowed |
|  | Accept­Date Accept date | smalldatetime | 4 | NULL allowed |
|  | Detail­Count Detail count | int | 4 | NULL allowed |
|  | Delivery­Batch­ID Delivery batch identifier | int | 4 | NULL allowed |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |
|  | Extra­Note Extra note | nvarchar(max) | max | NULL allowed |
|  | Is­Delivered Flag indicating delivered | bit | 1 | NULL allowed |
|  | Manual\_­Disc Manual disc | float | 8 | NULL allowed |
|  | Back­Order­Year Back order year | smallint | 2 | NULL allowed |
|  | Back­Order­No Back order number | bigint | 8 | NULL allowed |
|  | Final­Approval Final approval | bit | 1 | NULL allowed |
|  | Posted­To­ERPDate­Time Posted to erp date time | smalldatetime | 4 | NULL allowed |
|  | Used­In­Auto­Upload­Order Used in auto upload order | bit | 1 | NULL allowed |
|  | Location­Line­ID Location line identifier | int | 4 | NULL allowed |
|  | Make­Cash­Discount Make cash discount | bit | 1 | NULL allowed |
|  | Quotation­Year Quotation year | smallint | 2 | NULL allowed |
|  | Quotation­No Quotation number | int | 4 | NULL allowed |
|  | Need­Approval Need approval | bit | 1 | NULL allowed |
|  | Driver­No Driver number | int | 4 | NULL allowed |
|  | No­Need­Credit­Check No need credit check | bit | 1 | NULL allowed |
|  | Trans­Fees Trans fees | float | 8 | NULL allowed |
|  | Foreign­Trans­Fees Foreign trans fees | float | 8 | NULL allowed |
|  | Check­In­Time Check in time | smalldatetime | 4 | NULL allowed |
|  | Customer­Name Customer name | nvarchar(200) | 400 | NULL allowed |
|  | Address Address | nvarchar(max) | max | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Orders­Headers\_­Business­Units | Company­ID->[[dbo].[Business­Units].[Company­ID]](#nfNLb+EhlWiX9kN6JEFSAV6syXI=), Business­Unit­ID->[[dbo].[Business­Units].[ID]](#nfNLb+EhlWiX9kN6JEFSAV6syXI=) |
| FK\_­Orders­Headers\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Orders­Headers\_­Contracts | Company­ID->[[dbo].[Contracts].[Company­ID]](#zSXpPHadqD7+V+akfh1GN7CwldI=), Contract­ID->[[dbo].[Contracts].[Contract­ID]](#zSXpPHadqD7+V+akfh1GN7CwldI=) |
| FK\_­Orders­Headers\_­Currencies | Currency­ID->[[dbo].[Currencies].[ID]](#k0NURIzYF8aeO/uxKYIEdxSccAg=) |
| FK\_­Orders­Headers\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |
| FK\_­Orders­Headers\_­Price­Lists | Company­ID->[[dbo].[Price­Lists].[Company­ID]](#UTuGUXmxHIFiIaREw25LxgcqPnU=), Price­List­ID->[[dbo].[Price­Lists].[ID]](#UTuGUXmxHIFiIaREw25LxgcqPnU=) |
| FK\_­Orders­Headers\_­Routes­Information | Company­ID->[[dbo].[Routes­Information].[Company­ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=), Route­ID->[[dbo].[Routes­Information].[ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=) |
| FK\_­Orders­Headers\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Person­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[OT\_­Send­Log] |

MS\_­Description

Upon send data to salesman tablet , this log will show all sending processes details and time of execution for debug purposes of technical support team

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Salesman­No Salesman number | int | 4 | NULL allowed |  |
|  | Sys­Date Sys date | datetime | 8 | NULL allowed |  |
|  | Log­Text Log text | nvarchar(max) | max | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[OWGM\_­Gates] |

MS\_­Description

Stores owgm gates data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Gate­ID Gate identifier | int | 4 | NOT NULL |
|  | Gate­Name Gate name | nvarchar(100) | 200 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |
|  | Is­Working Flag indicating working | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[OWGM\_­Gates­Users] |

MS\_­Description

Stores owgm gates users data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Gate­User­ID Gate user identifier | int | 4 | NOT NULL |
|  | Gate­User­Name Gate user name | nvarchar(100) | 200 | NULL allowed |
|  | Gate­ID Gate identifier | int | 4 | NOT NULL |
|  | Device­Password Device password | varchar(50) | 50 | NULL allowed |
|  | Mac­Address Mac address | nvarchar(500) | 1000 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |
|  | Is­Working Flag indicating working | bit | 1 | NULL allowed |
|  | Is­Break Flag indicating break | bit | 1 | NULL allowed |
|  | Allow­Prepare Flag indicating allow prepare | bit | 1 | NULL allowed |
|  | Allow­Delivery Flag indicating allow delivery | bit | 1 | NULL allowed |
|  | Is­Gate­Assigment Flag indicating gate assigment | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[OWGM\_­Lock­Log] |

MS\_­Description

Stores owgm lock log data

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(18,0) | 9 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Gate­User­ID Gate user identifier | int | 4 | NULL allowed |  |
|  | Log­Date­Time Log date time | datetime | 8 | NULL allowed |  |
|  | Barcode Barcode | nvarchar(500) | 1000 | NULL allowed |  |
|  | Device­Trans­Type Device trans type | int | 4 | NULL allowed |  |
|  | Current­Trans­Type Current trans type | int | 4 | NULL allowed |  |
|  | Lock­Reason Lock reason | varchar(50) | 50 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[OWGM\_­Transactions] |

MS\_­Description

Stores owgm transactions data

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Trans­ID Trans identifier | numeric(18,0) | 9 | NOT NULL | 1 - 1 |
|  | Trans­Type Trans type | int | 4 | NOT NULL |  |
|  | Company­ID Company identifier | smallint | 2 | NOT NULL |  |
|  | Tr­Date­Time Tr date time | datetime | 8 | NULL allowed |  |
|  | Barcode Barcode | nvarchar(500) | 1000 | NULL allowed |  |
|  | ERP\_­Trans­Year Erp trans year | int | 4 | NULL allowed |  |
|  | ERP\_­Trans­Type Erp trans type | int | 4 | NULL allowed |  |
|  | ERP\_­Trans­No Erp trans number | bigint | 8 | NULL allowed |  |
|  | Gate­User­ID Gate user identifier | int | 4 | NULL allowed |  |
|  | Salesman­No Salesman number | int | 4 | NULL allowed |  |
|  | Salesman­Name Salesman name | varchar(500) | 500 | NULL allowed |  |
|  | Trans­Gate­ID Trans gate identifier | int | 4 | NULL allowed |  |
|  | Gate­Date­Time­Assigment Gate date time assigment | datetime | 8 | NULL allowed |  |
|  | Delivery­User­ID Delivery user identifier | int | 4 | NULL allowed |  |
|  | Delivery­User­Date­Time­Assigment Delivery user date time assigment | datetime | 8 | NULL allowed |  |
|  | Is­Done Flag indicating done | bit | 1 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Payments­Orders] |

MS\_­Description

This table holds data for a specific transaction type done by salespersons whereby he issues a payment for a customer in return for received item/items

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­Year Order year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Salesperson­ID Salesperson identifier | int | 4 | NULL allowed |
|  | Order­Date Order date | smalldatetime | 4 | NULL allowed |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NULL allowed |
|  | Amount Amount | float | 8 | NULL allowed |
|  | Issued­Amount Issued amount | float | 8 | NULL allowed |
|  | Is­Issued Flag indicating issued | bit | 1 | NULL allowed |
|  | Issued­Date Issued date | smalldatetime | 4 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |
|  | Ref­No Ref number | nvarchar(50) | 100 | NULL allowed |
|  | Posted­To­ERP Posted to erp | bit | 1 | NULL allowed |
|  | Foreign­Issued­Amount Foreign issued amount | float | 8 | NULL allowed |
|  | Currency­ID Currency identifier | smallint | 2 | NULL allowed |
|  | Exchange­Rate Exchange rate | float | 8 | NULL allowed |
|  | Order­Type Order type | int | 4 | NULL allowed |
|  | Is­From­Cash Flag indicating from cash | bit | 1 | NULL allowed |
|  | Notes Notes | varchar(max) | max | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Payments­Orders\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Payments­Orders\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |
| FK\_­Payments­Orders\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Salesperson­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Payments­Types] |

MS\_­Description

This table contains payment types for customers serviced by salesmen and usually are taken by ERP system such as Cash, checks ...etc. or entered through a back office user should the system be used as a stand alone system.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Short­Name Short name | nvarchar(10) | 20 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |
|  | Due­Days Due days | int | 4 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Payments­Types\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Pending­Invoices] |

MS\_­Description

This table contains Invoices that have not yet been considered formal invoices ??

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Salesman­No Salesman number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Customer­No Customer number | nvarchar(20) | 40 | NOT NULL |
| ![](data:image/png;base64...) | Alias­Name Alias name | nvarchar(50) | 100 | NOT NULL |
| ![](data:image/png;base64...) | Item­No Item number | nvarchar(20) | 40 | NOT NULL |
|  | Qty Quantity | float | 8 | NULL allowed |
|  | Unit Unit | nvarchar(20) | 40 | NULL allowed |
|  | Bonus Bonus | float | 8 | NULL allowed |
|  | Sell­Price Sell price | float | 8 | NULL allowed |
|  | Ref1 Ref 1 | datetime | 8 | NULL allowed |
|  | Ref2 Ref 2 | nvarchar(20) | 40 | NULL allowed |
|  | Item­Discount­Perc Item discount percentage | float | 8 | NULL allowed |
|  | Vou­Discount­Perc Vou discount percentage | float | 8 | NULL allowed |
|  | Customer­Discount­Perc Customer discount percentage | float | 8 | NULL allowed |
|  | Tax­Perc Tax percentage | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Pending­Orders­Details] |

MS\_­Description

This table contains Orders Details such as item code, its quantity, total …etc. that have not yet been considered formal Orders ??

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Order­Date Order date | smalldatetime | 4 | NOT NULL |
| ![](data:image/png;base64...) | Itemcode Itemcode | nvarchar(100) | 200 | NOT NULL |
|  | Name Name | nvarchar(200) | 400 | NULL allowed |
|  | Total Total | float | 8 | NULL allowed |
|  | Qantity Qantity | float | 8 | NULL allowed |
|  | Bonus Bonus | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Pending­Orders­Headers] |

MS\_­Description

This table contains Orders main information such as Order no, Customer no, …etc. that have not yet been considered formal Orders??

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Salesperson­ID Salesperson identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Customer­No Customer number | bigint | 8 | NOT NULL |
|  | Customer­Name Customer name | nvarchar(300) | 600 | NOT NULL |
|  | Order­Date Order date | smalldatetime | 4 | NOT NULL |
|  | Total­Before­Tax Total before tax | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Planogram­Media] |

MS\_­Description

This Table Contains files attached to an image that is used as a template to attach to customers, these templates are linked in another table to customers that would reflect on salesperson tablet where a before and after image photos are taken by salesperson related to each template , example : Shelf image template , a before shelf content or order of items change image is taken , and also after that change.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NOT NULL |  |
|  | Name Name | nvarchar(max) | max | NULL allowed |  |
|  | File­Path File path | nvarchar(max) | max | NULL allowed |  |
|  | Ref1 Ref 1 | varchar(50) | 50 | NULL allowed |  |
|  | Ref2 Ref 2 | varchar(50) | 50 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Planogram­Media­Customers­Link] |

MS\_­Description

This Table contains the linkage between an image template file and a before and after planogram image transaction done by salespersons as a transaction by taken these photos through his tablet

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Planogram­File­Auto­ID Planogram file auto identifier | numeric(30,0) | 17 | NOT NULL |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[POADetails] |

MS\_­Description

Stores POA detail line records ??

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | POAID Poaid | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |
|  | Visit­Count Visit count | int | 4 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[POAHeader] |

MS\_­Description

Stores POA header records ??

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | POAID Poaid | bigint | 8 | NOT NULL |
|  | Sales­Person­ID Sales identifier | int | 4 | NULL allowed |
|  | POAYear Poa year | int | 4 | NULL allowed |
|  | POAMonth Poa month | int | 4 | NULL allowed |
|  | Approved Flag indicating approved | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Pos\_­Invoice­Order­HF] |

MS\_­Description

Stores Pos Invoice Order header records ??

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| Bus­Unit­ID Bus unit identifier | int | 4 | NULL allowed |
| Ca­Cr Ca cr | int | 4 | NULL allowed |
| Comp­No Comp number | int | 4 | NULL allowed |
| Customer­Discount­Amount Customer discount amount | float | 8 | NULL allowed |
| Customer­Discount­Perc Customer discount percentage | float | 8 | NULL allowed |
| Customer­Name Customer name | nchar(10) | 20 | NULL allowed |
| Customer­No Customer number | int | 4 | NULL allowed |
| Delivery­Location Delivery location | nchar(10) | 20 | NULL allowed |
| Doc­Type Doc type | int | 4 | NULL allowed |
| Ex­Rate Ex rate | float | 8 | NULL allowed |
| Foreign­Customer­Discount­Amount Foreign customer discount amount | float | 8 | NULL allowed |
| Foreign­Customer­Discount­Perc Foreign customer discount percentage | float | 8 | NULL allowed |
| Foreign­Discount­Amount Foreign discount amount | float | 8 | NULL allowed |
| Foreign­Discount­Percent Foreign discount percent | float | 8 | NULL allowed |
| GPSX Gpsx | nchar(10) | 20 | NULL allowed |
| GPSY Gpsy | nchar(10) | 20 | NULL allowed |
| Is­Prospective­Customer Flag indicating prospective customer | bit | 1 | NULL allowed |
| Is­Void Flag indicating void | int | 4 | NULL allowed |
| Notes Notes | nchar(50) | 100 | NULL allowed |
| Order­Date Order date | nchar(50) | 100 | NULL allowed |
| Order­No Order number | int | 4 | NULL allowed |
| Order­Year Order year | int | 4 | NULL allowed |
| Payment­Type Payment type | int | 4 | NULL allowed |
| Print­Copy­Count Print copy count | int | 4 | NULL allowed |
| Print­Original­Count Print original count | int | 4 | NULL allowed |
| Pr­No Pr number | nchar(20) | 40 | NULL allowed |
| Promises­Date Promises date | nchar(20) | 40 | NULL allowed |
| Salesman­No Salesman number | int | 4 | NULL allowed |
| Tr­Date­Time Tr date time | nvarchar(50) | 100 | NULL allowed |
| Vou­Disc Vou disc | float | 8 | NULL allowed |
| Vou­Disc­Per Vou disc per | float | 8 | NULL allowed |
| Gross­Total Gross total | float | 8 | NULL allowed |
| Discount Discount | float | 8 | NULL allowed |
| Tax Tax | float | 8 | NULL allowed |
| Grand­Total Grand total | float | 8 | NULL allowed |
| Discount­Type Discount type | int | 4 | NULL allowed |
| Discount­Value Discount value | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Positions] |

MS\_­Description

This Table contain an ID and other information , this ID is considered as unique identifier that attached to a salespersons id where certain linkage and permissions are linked to Salespersons through this ID , such as Salesperson Device permission as in Order taking, Invoice issuing ..etc. , additionally Customers assignment for a salesperson , Item assignment for a salespersons , all of these would Reflect on salesperson Tablet / mobile application to conduct Transactions in field

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(500) | 1000 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |
|  | Erp\_­Reference Erp reference | varchar(50) | 50 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Positions\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Price­List­Details] |

MS\_­Description

This table contains Details about Price , tax, other info for each code for each item code based on a unique Price list ID identifier , these details are then transferred to Salesperson tablet so that he can sell an item in a certain price and other criteria as unit and tax and discount based on the unique price list id attached to his customer

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Price­List­ID Price list identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |
|  | Price Price | float | 8 | NULL allowed |
|  | Tax­Type Tax type | int | 4 | NULL allowed |
|  | Tax Tax | float | 8 | NULL allowed |
|  | Discount­Percent Discount percent | float | 8 | NULL allowed |
|  | Use­In­Return Flag indicating use in return | bit | 1 | NULL allowed |
|  | Use­In­Sales Flag indicating use in sales | bit | 1 | NULL allowed |
|  | Sell­Price2 Sell price 2 | float | 8 | NULL allowed |
|  | Sell­Price3 Sell price 3 | float | 8 | NULL allowed |
|  | Qty Quantity | money | 8 | NULL allowed |
|  | Tax­Type1 Tax type 1 | int | 4 | NULL allowed |
|  | Tax1 Tax 1 | float | 8 | NULL allowed |
|  | Tax­Type2 Tax type 2 | int | 4 | NULL allowed |
|  | Tax2 Tax 2 | float | 8 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |
|  | Max­Disc­Perc Max disc percentage | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Price­List­Details\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Price­List­Details\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Price­List­Details\_­Items­Units | Company­ID->[[dbo].[Items­Units].[Company­ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=), Unit­ID->[[dbo].[Items­Units].[ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=) |
| FK\_­Price­List­Details\_­Price­Lists | Company­ID->[[dbo].[Price­Lists].[Company­ID]](#UTuGUXmxHIFiIaREw25LxgcqPnU=), Price­List­ID->[[dbo].[Price­Lists].[ID]](#UTuGUXmxHIFiIaREw25LxgcqPnU=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Price­List­Details­From­GCI] |

MS\_­Description

Stores price list details from gci data

Custom used table for a special clients containing prices details

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| Company­ID Company identifier | smallint | 2 | NOT NULL |
| Price­List­ID Price list identifier | int | 4 | NOT NULL |
| Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |
| Price Price | float | 8 | NULL allowed |
| Tax­Type Tax type | int | 4 | NULL allowed |
| Tax Tax | float | 8 | NULL allowed |
| Discount­Percent Discount percent | float | 8 | NULL allowed |
| Use­In­Return Flag indicating use in return | bit | 1 | NULL allowed |
| Use­In­Sales Flag indicating use in sales | bit | 1 | NULL allowed |
| Sell­Price2 Sell price 2 | float | 8 | NULL allowed |
| Sell­Price3 Sell price 3 | float | 8 | NULL allowed |
| Qty Quantity | money | 8 | NULL allowed |
| Tax­Type1 Tax type 1 | int | 4 | NULL allowed |
| Tax1 Tax 1 | float | 8 | NULL allowed |
| Tax­Type2 Tax type 2 | int | 4 | NULL allowed |
| Tax2 Tax 2 | float | 8 | NULL allowed |
| Reference1 Reference 1 | nvarchar(100) | 200 | NULL allowed |
| Reference2 Reference 2 | nvarchar(100) | 200 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Price­List­Qty­Ranges] |

MS\_­Description

Stores price list qty ranges data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Price­List­ID Price list identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |
| ![](data:image/png;base64...) | From­Qty From quantity | float | 8 | NOT NULL |
| ![](data:image/png;base64...) | To­Qty To quantity | float | 8 | NOT NULL |
|  | Price Price | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Price­Lists] |

MS\_­Description

This Table contains main information about pricelists linked between customers and salespersons through salesperson position and reflected on salesperson mobile device or tablet to perform transactions such as orders and invoices through the assigned price list details for each time , the table contains information such as a unique id identifier for each pricelist and start time and end time …etc.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Start­Date Start date | smalldatetime | 4 | NULL allowed |
|  | End­Date End date | smalldatetime | 4 | NULL allowed |
|  | Notes Notes | nvarchar(200) | 400 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |
|  | Currency­ID Currency identifier | smallint | 2 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Procedure­Change­Log] |

MS\_­Description

This Table contains information about PC name, SQL Procedure and Date and time at which last adjustments were done to adjust an SQL Procedure it is considered as back history change log

Columns

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity | Default |
| ![](data:image/png;base64...) | Id Id identifier | int | 4 | NOT NULL | 1 - 1 |  |
|  | Object­Name Object name | nvarchar(128) | 256 | NULL allowed |  |  |
|  | Object­Schema Object schema | nvarchar(128) | 256 | NULL allowed |  |  |
|  | Event­Type Event type | nvarchar(50) | 100 | NULL allowed |  |  |
|  | Old­Definition Old definition | nvarchar(max) | max | NULL allowed |  |  |
|  | New­Definition New definition | nvarchar(max) | max | NULL allowed |  |  |
|  | Login­Name Login name | nvarchar(128) | 256 | NULL allowed |  |  |
|  | Host­Name Host name | nvarchar(128) | 256 | NULL allowed |  |  |
|  | IPAddress Ip address | nvarchar(50) | 100 | NULL allowed |  |  |
|  | Change­Time Change time | datetime | 8 | NULL allowed |  | (getdate()) |
|  | Proc­Definition Proc definition | nvarchar(max) | max | NULL allowed |  |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Promotion­Budget] |

MS\_­Description

This Table contains definitions of different promotion budget limit assigned to each promotion where Promotion could stop being valid after that limit on salesperson tablet in field

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | IONumber Io number | nvarchar(200) | 400 | NOT NULL |
|  | IODescription Io description | nvarchar(200) | 400 | NULL allowed |
|  | IODate Io date | datetime | 8 | NULL allowed |
|  | IOLimit­Value Io limit value | float | 8 | NULL allowed |
|  | IOValue Io value | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Promotion­Classes] |

MS\_­Description

This table is filled with unique IDs as classification id to be linked to each promotion individually as a classification mean to be used later in other purposes as a way of classification

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(50) | 100 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(50) | 100 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Promotion­Classes\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Promotion­Item­Groups] |

MS\_­Description

Stores promotion item groups data ??

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NOT NULL |
|  | Short­Name Short name | nvarchar(10) | 20 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Promotions­Approval­Log] |

MS\_­Description

This Table contains log of promotions that have been approved / not approved by users and there approval date and ID

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | decimal(18,0) | 9 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NOT NULL |  |
|  | User­ID User identifier | nvarchar(50) | 100 | NOT NULL |  |
|  | Promo­ID Promo identifier | int | 4 | NOT NULL |  |
|  | Approved­By Flag indicating approved by | nvarchar(50) | 100 | NULL allowed |  |
|  | Approve­Date Flag indicating approve date | smalldatetime | 4 | NULL allowed |  |
|  | Notes Notes | nvarchar(200) | 400 | NULL allowed |  |
|  | Approved Flag indicating approved | bit | 1 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Promotions­Approval­Setup] |

MS\_­Description

This table holds the promotion approving setup for users

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | User­ID User identifier | nvarchar(50) | 100 | NOT NULL |
|  | Level Level | smallint | 2 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Promotions­Cond­Un­Cod­Input] |

MS\_­Description

This table contains criteria based on which promotion inputs are built such as input qty input type (qty/amount) promotion ID,etc., it is part of a number of tables which promotion setup rely on for their definition to be complete and to be used in field by salespersons

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Promotion­ID Promotion identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...) | Item­Serial Item serial | smallint | 2 | NOT NULL |
|  | Item­Unit­ID Item unit identifier | nvarchar(50) | 100 | NULL allowed |
|  | Quantity Quantity | float | 8 | NULL allowed |
|  | Input­Type Input type | smallint | 2 | NULL allowed |
|  | To­Quantity To quantity | float | 8 | NULL allowed |
|  | Not­Double Not double | bit | 1 | NULL allowed |
|  | Start­Date Start date | smalldatetime | 4 | NULL allowed |
|  | End­Date End date | smalldatetime | 4 | NULL allowed |
|  | Promotion­Item­Group­ID Promotion item group identifier | int | 4 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Promotions­Cond­Un­Cod­Output] |

MS\_­Description

This table contains criteria based on which promotion inputs are built such as promotion ID, item code, output type qty... etc., it is part of a number of tables upon which promotion setup rely on for their definition to be complete and to be used in field by salespersons

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Promotion­ID Promotion identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...) | Item­Serial Item serial | smallint | 2 | NOT NULL |
|  | Item­Unit­ID Item unit identifier | nvarchar(50) | 100 | NULL allowed |
|  | Quantity Quantity | float | 8 | NULL allowed |
|  | Out­Put­Type Out put type | int | 4 | NULL allowed |
|  | Discount­Type Discount type | smallint | 2 | NULL allowed |
|  | Is­Conditional Flag indicating conditional | bit | 1 | NULL allowed |
|  | Discount­Value Discount value | float | 8 | NULL allowed |
|  | Start­Date Start date | smalldatetime | 4 | NULL allowed |
|  | End­Date End date | smalldatetime | 4 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Promotions­Cond­Un­Cod­Output\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Promotions­Cond­Un­Cod­Output\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Promotions­Cond­Un­Cod­Output\_­Promotions­Headers | Company­ID->[[dbo].[Promotions­Headers].[Company­ID]](#ahTdfFcl5CBnl0mrOXzm3bmregU=), Promotion­ID->[[dbo].[Promotions­Headers].[ID]](#ahTdfFcl5CBnl0mrOXzm3bmregU=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Promotions­Customers­Groups­Link] |

MS\_­Description

This table contains Customer promotions groups IDs that are linked to promotions so that promotions are only applied on those customers , it is part of a number of tables which promotions rely on for their definition to be complete and to be used in field by salespersons

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Promotion­ID Promotion identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Customers­Promotions­Groups­ID Customers promotions groups identifier | int | 4 | NOT NULL |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Promotions­Customers­Groups­Link\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Promotions­Customers­Groups­Link\_­Customers­Promotions­Groups | Company­ID->[[dbo].[Customers­Promotions­Groups].[Company­ID]](#CFvv0vB6qnd5JDiJpBfVpPfz9FY=), Customers­Promotions­Groups­ID->[[dbo].[Customers­Promotions­Groups].[ID]](#CFvv0vB6qnd5JDiJpBfVpPfz9FY=) |
| FK\_­Promotions­Customers­Groups­Link\_­Promotions­Headers | Company­ID->[[dbo].[Promotions­Headers].[Company­ID]](#ahTdfFcl5CBnl0mrOXzm3bmregU=), Promotion­ID->[[dbo].[Promotions­Headers].[ID]](#ahTdfFcl5CBnl0mrOXzm3bmregU=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Promotions­Dont­Apply] |

MS\_­Description

This table contains promotions that are excluded from being applied in field based on special criteria

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Promotion­ID Promotion identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Dont­Apply­Promotion­ID Dont apply promotion identifier | int | 4 | NOT NULL |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Promotion­Selection­Groups] |

MS\_­Description

This table contains a kind of classification for promotions to be selected and linked later

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(50) | 100 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(50) | 100 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Promotion­Selection­Groups\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Promotion­Selection­Groups­Link] |

MS\_­Description

This table holds linked of promotions selection groups to promotions

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Selection­Group­ID Selection group identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Promotion­ID Promotion identifier | int | 4 | NOT NULL |
|  | Is­Master Flag indicating master | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Promotions­Headers] |

MS\_­Description

This table holds main identification of promotion such as ID, promotion type, Promotion name, start date, end date …etc it is part of a number of tables which promotions rely on for their definition to be complete and to be used in field by salespersons

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Promotion­Type Promotion type | int | 4 | NULL allowed |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |
|  | Start­Date Start date | smalldatetime | 4 | NULL allowed |
|  | End­Date End date | smalldatetime | 4 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |
|  | Input­Qty­Amount Input qty amount | float | 8 | NULL allowed |
|  | Out­Put­Type Out put type | int | 4 | NULL allowed |
|  | Out­Qty­Amount Out qty amount | float | 8 | NULL allowed |
|  | Out­Qty­Amount\_2 Out qty amount 2 | float | 8 | NULL allowed |
|  | Use­In­Return Flag indicating use in return | bit | 1 | NULL allowed |
|  | Use­In­Sales Flag indicating use in sales | bit | 1 | NULL allowed |
| ![](data:image/png;base64...) | Input­Item­Unit­ID Input item unit identifier | nvarchar(50) | 100 | NULL allowed |
|  | Out­Item­Unit­ID Out item unit identifier | nvarchar(50) | 100 | NULL allowed |
|  | Promotion­Details Promotion details | nvarchar(200) | 400 | NULL allowed |
|  | Use­Rate­To­Calc­Bonus Flag indicating use rate to calc bonus | bit | 1 | NULL allowed |
|  | Not­Double Not double | bit | 1 | NULL allowed |
|  | Apply­For­All­Unit Apply for all unit | bit | 1 | NULL allowed |
|  | Discount­Type Discount type | smallint | 2 | NULL allowed |
|  | Include­In­Target­Bonus Include in target bonus | bit | 1 | NULL allowed |
|  | Round­Type Round type | smallint | 2 | NULL allowed |
|  | Is­Need­Coupon Flag indicating need coupon | bit | 1 | NULL allowed |
|  | Invoice­Type Invoice type | smallint | 2 | NULL allowed |
|  | Run­After­All­Promos Run after all promos | bit | 1 | NULL allowed |
|  | Notes Notes | nvarchar(max) | max | NULL allowed |
|  | Out­Put­Same­Input Out put same input | bit | 1 | NULL allowed |
|  | Salesman­Can­Change­Out­Put­Qty Salesman can change out put quantity | bit | 1 | NULL allowed |
|  | Is­Amount­Without­Tax Flag indicating amount without tax | bit | 1 | NULL allowed |
|  | Need­Work­Flow­Approval Need work flow approval | bit | 1 | NULL allowed |
|  | Max­Qty Max quantity | float | 8 | NULL allowed |
|  | Approved­By Flag indicating approved by | int | 4 | NULL allowed |
|  | Bonus­With­Price Bonus with price | bit | 1 | NULL allowed |
|  | Is­Required­In­Trans Flag indicating required in trans | bit | 1 | NULL allowed |
|  | Is­Approved Flag indicating approved | bit | 1 | NULL allowed |
| ![](data:image/png;base64...) | Promotion­Class Promotion class | int | 4 | NULL allowed |
|  | Accumulated­Amount Accumulated amount | float | 8 | NULL allowed |
|  | IONumber Io number | nvarchar(200) | 400 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Promotions­Headers\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Promotions­Headers\_­Items­Units | Company­ID->[[dbo].[Items­Units].[Company­ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=), Input­Item­Unit­ID->[[dbo].[Items­Units].[ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=) |
| FK\_­Promotions­Headers\_­Promotion­Classes | Company­ID->[[dbo].[Promotion­Classes].[Company­ID]](#2hsG62388LC8A5b97+xZe9r4UMo=), Promotion­Class->[[dbo].[Promotion­Classes].[ID]](#2hsG62388LC8A5b97+xZe9r4UMo=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Promotions­Priorities] |

MS\_­Description

This Table contains names and IDs of piretites that are set for promotion used so that promotions ID can be linked to these priorities later

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |
|  | Apply­All­Next­Promotion Apply all next promotion | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Promotions­Priorities\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Promotions­Priorities­Link] |

MS\_­Description

This table have links between promotions id to priorities , once they are linked to this table , salespersons in field applying these promotions will be forced to apply the first applicable promotion in order , so once applied all other following promotions on those priority would not.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Priority­ID Priority identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Promotion­ID Promotion identifier | int | 4 | NOT NULL |
|  | Priority­Serial Priority serial | int | 4 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Promotions­Priorities­Link\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Promotions­Priorities­Link\_­Promotions­Headers | Company­ID->[[dbo].[Promotions­Headers].[Company­ID]](#ahTdfFcl5CBnl0mrOXzm3bmregU=), Promotion­ID->[[dbo].[Promotions­Headers].[ID]](#ahTdfFcl5CBnl0mrOXzm3bmregU=) |
| FK\_­Promotions­Priorities­Link\_­Promotions­Priorities | Company­ID->[[dbo].[Promotions­Priorities].[Company­ID]](#vW9ydMaj0P2bPNmRT1PpK/4eQLU=), Priority­ID->[[dbo].[Promotions­Priorities].[ID]](#vW9ydMaj0P2bPNmRT1PpK/4eQLU=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Promotions­Range­Input] |

MS\_­Description

This Table contains definition of a special type of promotions called promotion 14 , this promotion holds special criteria that enables back office user to choose a range of qty inputs to apply special discount or amount in output of promotion

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Promotion­ID Promotion identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Unit­ID Item unit identifier | nvarchar(50) | 100 | NOT NULL |
| ![](data:image/png;base64...) | From­Quantity From quantity | float | 8 | NOT NULL |
|  | To­Quantity To quantity | float | 8 | NULL allowed |
|  | Output­Quantity Output quantity | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Promotions­Range­Input\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Promotions­Range­Input\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Promotions­Range­Input\_­Items­Units | Company­ID->[[dbo].[Items­Units].[Company­ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=), Item­Unit­ID->[[dbo].[Items­Units].[ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=) |
| FK\_­Promotions­Range­Input\_­Promotions­Headers | Company­ID->[[dbo].[Promotions­Headers].[Company­ID]](#ahTdfFcl5CBnl0mrOXzm3bmregU=), Promotion­ID->[[dbo].[Promotions­Headers].[ID]](#ahTdfFcl5CBnl0mrOXzm3bmregU=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Promotions­Salesman­Groups­Link] |

MS\_­Description

In this table Linkage of salespersons groups would be linked to Promotions IDs so that promotion would only applied to that certain groups salesmen in field it is a table from a list of other tables that promotions rely on for their definition to be complete and to be used in field by salespersons

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Promotion­ID Promotion identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Sales­Persons­Group­ID Sales persons group identifier | int | 4 | NOT NULL |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Promotions­Salesman­Groups­Link\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Promotions­Salesman­Groups­Link\_­Promotions­Headers | Company­ID->[[dbo].[Promotions­Headers].[Company­ID]](#ahTdfFcl5CBnl0mrOXzm3bmregU=), Promotion­ID->[[dbo].[Promotions­Headers].[ID]](#ahTdfFcl5CBnl0mrOXzm3bmregU=) |
| FK\_­Promotions­Salesman­Groups­Link\_­Sales­Persons­Groups | Company­ID->[[dbo].[Sales­Persons­Groups].[Company­ID]](#IJwFVeRoDj2cXKxVh0vr44Q0tYU=), Sales­Persons­Group­ID->[[dbo].[Sales­Persons­Groups].[ID]](#IJwFVeRoDj2cXKxVh0vr44Q0tYU=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Promotion­Types] |

MS\_­Description

This table is defined ID types of promotions based on which promotion applied through special terms and criteria which promotions rely on for their definition to be complete and to be used in field by salespersons

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(50) | 100 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Prompt­Embeddings] |

MS\_­Description

Stores prompt embeddings data ??

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Id Id identifier | int | 4 | NOT NULL | 1 - 1 |
|  | Prompt­Text Prompt text | nvarchar(max) | max | NULL allowed |  |
|  | Response Response | nvarchar(max) | max | NULL allowed |  |
|  | Embedding Embedding | nvarchar(max) | max | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Prospective­Customers] |

MS\_­Description

This Table contains Prospective customers that were added by salespersons in field by a special type of transaction called prospective customers through which salesperson would enter data for a prospective customer.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | bigint | 8 | NOT NULL |
|  | Name Name | nvarchar(200) | 400 | NULL allowed |
|  | Foreign­Name Foreign name | nvarchar(200) | 400 | NULL allowed |
|  | Short­Name Short name | nvarchar(50) | 100 | NULL allowed |
|  | Type­ID Type identifier | int | 4 | NULL allowed |
|  | Location­ID Location identifier | int | 4 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(50) | 100 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(200) | 400 | NULL allowed |
|  | Account Account | nvarchar(50) | 100 | NULL allowed |
|  | Barcode Barcode | nvarchar(20) | 40 | NULL allowed |
|  | Contact Contact | nvarchar(100) | 200 | NULL allowed |
|  | Telephone­No Telephone number | nvarchar(50) | 100 | NULL allowed |
|  | Mobile­No Mobile number | nvarchar(50) | 100 | NULL allowed |
|  | Fax­No Fax number | nvarchar(50) | 100 | NULL allowed |
|  | POBox Po box | nvarchar(50) | 100 | NULL allowed |
|  | Address Address | nvarchar(200) | 400 | NULL allowed |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |
|  | Web­Site Web site | nvarchar(100) | 200 | NULL allowed |
|  | Email Email | nvarchar(100) | 200 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |
|  | User­ID User identifier | nvarchar(20) | 40 | NULL allowed |
|  | Password Password | nvarchar(20) | 40 | NULL allowed |
|  | Customer­Image Customer image | image | max | NULL allowed |
|  | Price­List­ID Price list identifier | int | 4 | NULL allowed |
|  | Positions­ID Positions identifier | int | 4 | NULL allowed |
|  | Tax­Include Tax include | bit | 1 | NULL allowed |
|  | Credit­Cash Credit cash | smallint | 2 | NULL allowed |
|  | Commercial­Registration­No Commercial registration number | nvarchar(100) | 200 | NULL allowed |
|  | Professionlicence­No Professionlicence number | nvarchar(100) | 200 | NULL allowed |
|  | New­Cust­Ref­No New cust ref number | nvarchar(100) | 200 | NULL allowed |
|  | Tab­Sys­ID Tab sys identifier | varchar(500) | 500 | NULL allowed |
|  | Class\_­ID Class identifier | int | 4 | NULL allowed |
|  | Posted­To­ERP Posted to erp | bit | 1 | NULL allowed |
|  | Company­National­ID Company national identifier | varchar(1000) | 1000 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Prosto­Soft­Accounts] |

MS\_­Description

Stores prosto soft accounts data ??

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
|  | S\_­M S m | bigint | 8 | NULL allowed |
|  | S\_­M\_­M S m m | bigint | 8 | NULL allowed |
|  | S\_­D S d | bigint | 8 | NULL allowed |
|  | S\_­D\_­M S d m | bigint | 8 | NULL allowed |
|  | S\_­T S t | bigint | 8 | NULL allowed |
|  | S\_­V S v | bigint | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Receipt­Requests] |

MS\_­Description

Stores receipt requests data ??

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­Year Order year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
|  | Order­Date Order date | smalldatetime | 4 | NULL allowed |
|  | Customer­ID Customer identifier | bigint | 8 | NULL allowed |
|  | Amount Amount | float | 8 | NULL allowed |
|  | Notes Notes | nvarchar(500) | 1000 | NULL allowed |
|  | Order­Status Order status | int | 4 | NULL allowed |
|  | Payment­Type Payment type | int | 4 | NULL allowed |
|  | Is­Settlement Flag indicating settlement | bit | 1 | NULL allowed |
|  | Priority Priority | bit | 1 | NULL allowed |
|  | Created­By Created by | nvarchar(50) | 100 | NULL allowed |
|  | Created­Date Created date | smalldatetime | 4 | NULL allowed |
|  | Document­Type­ID Document type identifier | int | 4 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Receipt­Requests­Invoices­Link] |

MS\_­Description

Stores receipt requests invoices link data ??

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­Year Order year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Paid­Trans­Year Paid trans year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Paid­Trans­No Paid trans number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Paid­Trans­Type­ID Paid trans type identifier | smallint | 2 | NOT NULL |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Receipt­Requests­Schedule] |

MS\_­Description

Stores receipt requests schedule data ??

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­Year Order year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Schedule­ID Schedule identifier | int | 4 | NOT NULL |
|  | Sales­Person­ID Sales identifier | int | 4 | NULL allowed |
|  | Is­Void Flag indicating void | bit | 1 | NULL allowed |
|  | Schedule­Date­Time Schedule date time | smalldatetime | 4 | NULL allowed |
|  | Assigment­Date­Time Assigment date time | smalldatetime | 4 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Receipts] |

MS\_­Description

This Table contains information on receipts issuance transaction performed by salesman in fields it holds information such as Serial no of receipt, Customerid, Amount , ..etc

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Transaction­Type­ID Transaction type identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­Year Transaction year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­No Transaction number | int | 4 | NOT NULL |
|  | Transaction­Date Transaction date | smalldatetime | 4 | NULL allowed |
|  | Document­Type­ID Document type identifier | int | 4 | NULL allowed |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NULL allowed |
| ![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NULL allowed |
|  | Amount Amount | float | 8 | NULL allowed |
|  | Foreign­Amount Foreign amount | float | 8 | NULL allowed |
| ![](data:image/png;base64...) | Currency­ID Currency identifier | smallint | 2 | NULL allowed |
|  | Exchange­Rate Exchange rate | float | 8 | NULL allowed |
|  | Is­Printed Flag indicating printed | bit | 1 | NULL allowed |
|  | Notes Notes | nvarchar(500) | 1000 | NULL allowed |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |
| ![](data:image/png;base64...) | Route­ID Route identifier | int | 4 | NULL allowed |
|  | Posted­To­ERP Posted to erp | bit | 1 | NULL allowed |
|  | Collected Collected | bit | 1 | NULL allowed |
|  | Discount Discount | float | 8 | NULL allowed |
|  | Ref­No Ref number | nvarchar(50) | 100 | NULL allowed |
|  | Tr­Date­Time Tr date time | smalldatetime | 4 | NULL allowed |
|  | Print­Original­Count Print original count | int | 4 | NULL allowed |
|  | Print­Copy­Count Print copy count | int | 4 | NULL allowed |
|  | Is­WFApproved Flag indicating wf approved | bit | 1 | NULL allowed |
|  | WFApprove­Desc Wf approve description | nvarchar(200) | 400 | NULL allowed |
|  | Is­Void Flag indicating void | bit | 1 | NULL allowed |
|  | Accept­Date Accept date | smalldatetime | 4 | NULL allowed |
|  | Server­Date Server date | smalldatetime | 4 | NULL allowed |
|  | Detail­Count Detail count | int | 4 | NULL allowed |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |
|  | Accepted­By Accepted by | nvarchar(50) | 100 | NULL allowed |
|  | Receipt­Request­Year Receipt request year | smallint | 2 | NULL allowed |
|  | Receipt­Request­No Receipt request number | int | 4 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(50) | 100 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(50) | 100 | NULL allowed |
|  | Posted­To­Email Posted to email | bit | 1 | NULL allowed |
|  | Bank\_­Transfer­No Bank transfer number | nvarchar(200) | 400 | NULL allowed |
|  | Bank\_­Transfer\_­Date Bank transfer date | smalldatetime | 4 | NULL allowed |
|  | Bank\_­Transfer\_­Amount Bank transfer amount | float | 8 | NULL allowed |
|  | Bank\_­Transfer\_­Bank­ID Bank transfer bank identifier | int | 4 | NULL allowed |
|  | Bank\_­Transfer\_­Bank­Account Bank transfer bank account | int | 4 | NULL allowed |
|  | First­Void First void | bit | 1 | NULL allowed |
|  | Void­Posted­To­ERP Void posted to erp | bit | 1 | NULL allowed |
|  | Void­Posted­To­Email Void posted to email | bit | 1 | NULL allowed |
|  | Voided­By­User Voided by user | nvarchar(50) | 100 | NULL allowed |
|  | Second­Collected Second collected | bit | 1 | NULL allowed |
|  | Posted­To­ERPDate­Time Posted to erp date time | smalldatetime | 4 | NULL allowed |
|  | Location­Line­ID Location line identifier | int | 4 | NULL allowed |
|  | Foreign­Discount Foreign discount | float | 8 | NULL allowed |
|  | Is­Deposit­In­Bank Flag indicating deposit in bank | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Receipts\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Receipts\_­Currencies | Currency­ID->[[dbo].[Currencies].[ID]](#k0NURIzYF8aeO/uxKYIEdxSccAg=) |
| FK\_­Receipts\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |
| FK\_­Receipts\_­Routes­Information | Company­ID->[[dbo].[Routes­Information].[Company­ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=), Route­ID->[[dbo].[Routes­Information].[ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=) |
| FK\_­Receipts\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Person­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |
| FK\_­Receipts\_­Transactions­Types | Transaction­Type­ID->[[dbo].[Transactions­Types].[ID]](#5KHGGmOv19tzIe7dNJ3JOc6tR1w=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Receipts\_­Branches] |

MS\_­Description

This table contains linked branches and other info for receipt issued transaction done salesperson in field

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­Type­ID Transaction type identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­Year Transaction year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­No Transaction number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Branch­ID Branch identifier | int | 4 | NOT NULL |
|  | Amount Amount | float | 8 | NULL allowed |
|  | Ref1 Ref 1 | varchar(500) | 500 | NULL allowed |
|  | Ref2 Ref 2 | varchar(500) | 500 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Receipts\_­Currency] |

MS\_­Description

This table contains currency and other info for receipt issued transaction done by salesperson in field

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Transaction­Type­ID Transaction type identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Transaction­Year Transaction year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Transaction­No Transaction number | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Currency­ID Currency identifier | smallint | 2 | NOT NULL |
|  | Amount Amount | float | 8 | NULL allowed |
|  | Exchange­Rate Exchange rate | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Receipts\_­Currency\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Receipts\_­Currency\_­Currencies | Currency­ID->[[dbo].[Currencies].[ID]](#k0NURIzYF8aeO/uxKYIEdxSccAg=) |
| FK\_­Receipts\_­Currency\_­Receipts | Company­ID->[[dbo].[Receipts].[Company­ID]](#HG1TRL9sPjSgLFh35//BPsYmHtk=), Transaction­Type­ID->[[dbo].[Receipts].[Transaction­Type­ID]](#HG1TRL9sPjSgLFh35//BPsYmHtk=), Transaction­Year->[[dbo].[Receipts].[Transaction­Year]](#HG1TRL9sPjSgLFh35//BPsYmHtk=), Transaction­No->[[dbo].[Receipts].[Transaction­No]](#HG1TRL9sPjSgLFh35//BPsYmHtk=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Receipts\_­Paid­Trans] |

MS\_­Description

This Table Contains information about for receipt issued transaction done by salesman when that receipt covers invoice/invoices in whole or partially, here we can find the paid transaction no (invoice /invoices numbers) that were covered by the receipt

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­Year Transaction year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­No Transaction number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­Type­ID Transaction type identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Paid­Trans­Year Paid trans year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Paid­Trans­No Paid trans number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Paid­Trans­Type­ID Paid trans type identifier | smallint | 2 | NOT NULL |
|  | Paid­Amount Paid amount | float | 8 | NULL allowed |
|  | Posted­To­ERP Posted to erp | bit | 1 | NULL allowed |
|  | Ref1 Ref 1 | nvarchar(500) | 1000 | NULL allowed |
|  | Ref2 Ref 2 | nvarchar(500) | 1000 | NULL allowed |
|  | Ref3 Ref 3 | nvarchar(500) | 1000 | NULL allowed |
|  | Ref4 Ref 4 | nvarchar(500) | 1000 | NULL allowed |
|  | Discount­Amount Discount amount | float | 8 | NULL allowed |
|  | Discount­Percent Discount percent | float | 8 | NULL allowed |
|  | Is­Manual­Reconciliation Flag indicating manual reconciliation | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Receipts\_­Paid­Trans\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Receipts\_­Paid­Trans­Checks] |

MS\_­Description

This Table Contains information about for checks related to receipts issued transaction done by salesman when that receipt covers invoice/invoices in whole or partially, here we can find the paid transaction no (invoice /invoices numbers) that were covered by the receipt

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­Year Transaction year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­No Transaction number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­Type­ID Transaction type identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Paid­Trans­Bank­ID Paid trans bank identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Paid­Trans­Branch­ID Paid trans branch identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Paid­Trans­Year Paid trans year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Paid­Trans­No Paid trans number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Paid­Trans­Type­ID Paid trans type identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Paid­Trans­Customer­ID Paid trans customer identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Paid­Trans­Cheque­No Paid trans cheque number | int | 4 | NOT NULL |
|  | Paid­Amount Paid amount | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Rec­Link­Inv] |

MS\_­Description

Stores rec link inv data ??

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| Father­Code Father code | nvarchar(20) | 40 | NULL allowed |
| Doc­Due­Date Doc due date | smalldatetime | 4 | NULL allowed |
| Doc­Date Doc date | smalldatetime | 4 | NULL allowed |
| SAPInvoice­ID Sap invoice identifier | int | 4 | NULL allowed |
| Invoice­Number Invoice number | int | 4 | NULL allowed |
| Invoice­Client­ID Invoice client identifier | int | 4 | NULL allowed |
| Invoice­Final­Amount Invoice final amount | float | 8 | NULL allowed |
| Invoice­Remaining­Amount Invoice remaining amount | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Report5Customers­Excemptions] |

MS\_­Description

This is a custom Table for a client that is used for excluding some customers so that they are not found in a special report out put

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| Company­ID Company identifier | smallint | 2 | NULL allowed |
| Customer­ID Customer identifier | nvarchar(50) | 100 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Reprinted­Transactions] |

MS\_­Description

This table contains information about reprinted transactions done by salesman in field , their count , their re print reason ..etc. this is used for reporting purposes

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Tr­Type­ID Tr type identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Tr­Year Tr year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Tr­No Tr number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Ser­ID Ser identifier | numeric(30,0) | 17 | NOT NULL |
|  | Tr­Date­Time Tr date time | smalldatetime | 4 | NULL allowed |
| ![](data:image/png;base64...) | Reprint­Reason­ID Reprint reason identifier | int | 4 | NULL allowed |
|  | Copy­Count Copy count | int | 4 | NULL allowed |
|  | Is­Re­Print Flag indicating re print | bit | 1 | NULL allowed |
|  | Tablet­Sys­ID Tablet sys identifier | nvarchar(50) | 100 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Reprinted­Transactions\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Reprinted­Transactions\_­Reprint­Reasons | Company­ID->[[dbo].[Reprint­Reasons].[Company­ID]](#BmIpENCX8UPPP42kgYWU2hnd3ns=), Reprint­Reason­ID->[[dbo].[Reprint­Reasons].[ID]](#BmIpENCX8UPPP42kgYWU2hnd3ns=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Reprint­Reasons] |

MS\_­Description

In this table are definitions of report reasons for transactions done by salesman in field , it is a select of multiple reasons that salesman would choose when he does reprint of a transaction it is used for report purpose

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Reprint­Reasons\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­Salesman­No­Transaction] |

MS\_­Description

Stores request salesman no transaction data

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Read­Notification Flag indicating read notification | bit | 1 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­Salesman­Will­Not­Visit] |

MS\_­Description

Stores request salesman will not visit data

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Reason­ID Reason identifier | int | 4 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | OSFA\_­Auto­ID Osfa auto identifier | numeric(30,0) | 17 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Add­Discount] |

MS\_­Description

Stores request to add discount data

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Invoice­Amount Invoice amount | float | 8 | NULL allowed |  |
|  | Discount­Amount Discount amount | float | 8 | NULL allowed |  |
|  | Discount­Percent Discount percent | float | 8 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Notes Notes | varchar(max) | max | NULL allowed |  |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Request­To­Add­Discount\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Add­Discount­In­Order] |

MS\_­Description

Stores request to add discount in order data

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Invoice­Amount Invoice amount | float | 8 | NULL allowed |  |
|  | Discount­Amount Discount amount | float | 8 | NULL allowed |  |
|  | Discount­Percent Discount percent | float | 8 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | OSFA\_­Auto­ID Osfa auto identifier | numeric(18,0) | 9 | NULL allowed |  |
|  | Notes Notes | nvarchar(max) | max | NULL allowed |  |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Request­To­Add­Discount­In­Order\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Add­Drawer] |

MS\_­Description

Stores request to add drawer data

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Receipt­Amount Receipt amount | float | 8 | NULL allowed |  |
|  | Checks­Info Checks info | nvarchar(max) | max | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |  |
|  | OSFA\_­Auto­ID Osfa auto identifier | numeric(30,0) | 17 | NOT NULL |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Add­Extra­Bonus] |

MS\_­Description

Stores request to add extra bonus data

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Tr­Type Tr type | int | 4 | NULL allowed |  |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Invoice­Amount Invoice amount | float | 8 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | OSFA\_­Auto­ID Osfa auto identifier | numeric(30,0) | 17 | NULL allowed |  |
|  | Notes Notes | nvarchar(max) | max | NULL allowed |  |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |  |
|  | Bonus­Amount Bonus amount | float | 8 | NULL allowed |  |
|  | Bonus­Type Bonus type | nvarchar(50) | 100 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Add­Extra­Bonus­And­Discount] |

MS\_­Description

Stores request to add extra bonus and discount data

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Tr­Type Tr type | int | 4 | NULL allowed |  |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Approve­Percent Flag indicating approve percent | float | 8 | NULL allowed |  |
|  | Invoice­Amount Invoice amount | float | 8 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | OSFA\_­Auto­ID Osfa auto identifier | numeric(30,0) | 17 | NULL allowed |  |
|  | Notes Notes | nvarchar(max) | max | NULL allowed |  |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |  |
|  | Invoice­Details­JSON Invoice details json | nvarchar(max) | max | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Add­New­Customer] |

MS\_­Description

Stores request to add new customer data

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Notes Notes | nvarchar(max) | max | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | OSFA\_­Auto­ID Osfa auto identifier | numeric(30,0) | 17 | NULL allowed |  |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Request­To­Add­New­Customer\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Allow­Take­Checks­From­Customer] |

MS\_­Description

Stores request to allow take checks from customer data

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Receipt­Amount Receipt amount | float | 8 | NULL allowed |  |
|  | Checks­Info Checks info | nvarchar(max) | max | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | OSFA\_­Auto­ID Osfa auto identifier | numeric(30,0) | 17 | NULL allowed |  |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Approve­Promotion] |

MS\_­Description

Stores request to approve promotion data

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Promotion­Info Promotion info | nvarchar(max) | max | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | OSFA\_­Auto­ID Osfa auto identifier | numeric(30,0) | 17 | NULL allowed |  |
|  | Promotion­ID Promotion identifier | int | 4 | NULL allowed |  |
|  | Is­Canceled Flag indicating canceled | bit | 1 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Approve­Promotion­Details] |

MS\_­Description

Stores Request To Approve Promotion detail line records

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Req­Auto­ID Req auto identifier | numeric(30,0) | 17 | NOT NULL |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Promotion­ID Promotion identifier | int | 4 | NOT NULL |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |
|  | Master­Req­ID Master req identifier | numeric(30,0) | 17 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Request­To­Approve­Promotion­Details\_­Request­To­Approve­Promotion | Req­Auto­ID->[[dbo].[Request­To­Approve­Promotion].[Auto­ID]](#pQ6HwEn2SmwM1uYR5CoBxuewGVk=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Cancel­Payment] |

MS\_­Description

Stores request to cancel payment data

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Tr­Year Tr year | smallint | 2 | NULL allowed |  |
|  | Tr­Type Tr type | smallint | 2 | NULL allowed |  |
|  | Tr­No Tr number | int | 4 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Receipt­Amount Receipt amount | float | 8 | NULL allowed |  |
|  | Checks­Info Checks info | nvarchar(max) | max | NULL allowed |  |
|  | Invoice­Info Invoice info | nvarchar(max) | max | NULL allowed |  |
|  | Notes Notes | nvarchar(max) | max | NULL allowed |  |
|  | Discount­Amount Discount amount | float | 8 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | OSFA\_­Auto­ID Osfa auto identifier | numeric(30,0) | 17 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Change­Delivery­Payment­Type] |

MS\_­Description

Stores request to change delivery payment type data

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Original­Salesperson­No Original salesperson number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Tr­Type­ID Tr type identifier | smallint | 2 | NULL allowed |  |
|  | Tr­Type­Year Tr type year | smallint | 2 | NULL allowed |  |
|  | Tr­Type­No Tr type number | int | 4 | NULL allowed |  |
|  | Invoice­Amount Invoice amount | float | 8 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Old­Payment­Type Old payment type | int | 4 | NULL allowed |  |
|  | New­Payment­Type New payment type | int | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | OSFA\_­Auto­ID Osfa auto identifier | numeric(30,0) | 17 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Request­To­Change­Delivery­Payment­Type\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Change­Invoice­Payment­Type] |

MS\_­Description

Stores request to change invoice payment type data

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Invoice­Amount Invoice amount | float | 8 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |  |
|  | Inv­Due­Days Inv due days | int | 4 | NULL allowed |  |
|  | Is­Canceled Flag indicating canceled | bit | 1 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Request­To­Change­Invoice­Payment­Type\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Change­Item­Sell­Price] |

MS\_­Description

Stores requests submitted by sales representatives to change the selling price of an item during sales operations. The table records request details including salesperson, customer, transaction type, invoice amount, request date, approval status, geographic location, and related notes. It is mainly used for tracking and approving price change requests coming from field sales devices or tablet systems

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Tr­Type Tr type | int | 4 | NULL allowed |  |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Invoice­Amount Invoice amount | float | 8 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | OSFA\_­Auto­ID Osfa auto identifier | numeric(18,0) | 9 | NULL allowed |  |
|  | Notes Notes | nvarchar(max) | max | NULL allowed |  |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Exceed­Check­Due­Date] |

MS\_­Description

Stores requests submitted by sales representatives to exceed the allowed check due date for a customer. The table records request details such as company, salesperson, customer, receipt amount, check information, request date, approval status, geographic location, and tablet system identifier. It is used to track and approve exceptions to the customer's standard payment due period.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Receipt­Amount Receipt amount | float | 8 | NULL allowed |  |
|  | Checks­Info Checks info | nvarchar(max) | max | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |  |
|  | Customer­Due­Days Customer due days | smallint | 2 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Request­To­Exceed­Check­Due­Date\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Exceed­Chq­Limit] |

MS\_­Description

Stores requests submitted by sales representatives to exceed the allowed check limit for a customer. The table records request details including company, salesperson, customer, receipt amount, check information, request date, approval status, geographic location, and device identifier. It also stores the customer’s current credit limit, outstanding balances, check balances, and the amount by which the limit is requested to be exceeded. The table is used for monitoring and approving exceptions to customer check limit policies.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Receipt­Amount Receipt amount | float | 8 | NULL allowed |  |
|  | Checks­Info Checks info | nvarchar(max) | max | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | OSFA\_­Auto­ID Osfa auto identifier | numeric(30,0) | 17 | NOT NULL |  |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |  |
|  | Customer­Credit­Limit Customer credit limit | float | 8 | NULL allowed |  |
|  | Customer­Banalce Customer banalce | float | 8 | NULL allowed |  |
|  | Customer­Chq­Banalce Customer chq banalce | float | 8 | NULL allowed |  |
|  | Exceed­Amount Exceed amount | float | 8 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Request­To­Exceed­Chq­Limit\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Exceed­Customer­Credit­Limit] |

MS\_­Description

Stores requests submitted by sales representatives to exceed the defined credit limit of a customer during sales transactions. The table records request details including company, salesperson, customer, invoice amount, request date, approval status, geographic location, notes, and tablet system identifier. It also captures the customer’s current credit limit, outstanding balances, check balances, and the amount requested to exceed the allowed limit. This table is used for tracking and approving credit limit exceptions.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Invoice­Amount Invoice amount | float | 8 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Notes Notes | nvarchar(4000) | 8000 | NULL allowed |  |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |  |
|  | Customer­Credit­Limit Customer credit limit | float | 8 | NULL allowed |  |
|  | Customer­Banalce Customer banalce | float | 8 | NULL allowed |  |
|  | Customer­Chq­Banalce Customer chq banalce | float | 8 | NULL allowed |  |
|  | Exceed­Amount Exceed amount | float | 8 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Request­To­Exceed­Customer­Credit­Limit\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Exceed­Customer­Credit­Limit­In­Order] |

MS\_­Description

Stores requests submitted by sales representatives to exceed the defined credit limit of a customer during sales transactions. The table records request details including company, salesperson, customer, invoice amount, request date, approval status, geographic location, notes, and tablet system identifier. It also captures the customer’s current credit limit, outstanding balances, check balances, and the amount requested to exceed the allowed limit. This table is used for tracking and approving credit limit exceptions.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Invoice­Amount Invoice amount | float | 8 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | OSFA\_­Auto­ID Osfa auto identifier | numeric(18,0) | 9 | NULL allowed |  |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |  |
|  | Customer­Credit­Limit Customer credit limit | float | 8 | NULL allowed |  |
|  | Customer­Banalce Customer banalce | float | 8 | NULL allowed |  |
|  | Customer­Chq­Banalce Customer chq banalce | float | 8 | NULL allowed |  |
|  | Exceed­Amount Exceed amount | float | 8 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Request­To­Exceed­Customer­Credit­Limit­In­Order\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Exceed­Customer­Invoice­Due­Days] |

MS\_­Description

Stores requests submitted by sales representatives to exceed the allowed invoice due days for a customer. The table records request details including company, salesperson, customer, invoice amount, request date, approval status, geographic location, and tablet system identifier. It is used to track and approve exceptions to the customer's standard invoice payment period.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Invoice­Amount Invoice amount | float | 8 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Request­To­Exceed­Customer­Invoice­Due­Days\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Exceed­Customer­Invoice­Due­Days­In­Order] |

MS\_­Description

Stores requests submitted by sales representatives to exceed the allowed invoice due days for a customer during the sales order process. The table records request details including company, salesperson, customer, order amount, request date, approval status, geographic location, device identifiers, and related notes. It is used to track and approve exceptions to the customer's standard invoice payment terms when creating sales orders.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Invoice­Amount Invoice amount | float | 8 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | OSFA\_­Auto­ID Osfa auto identifier | numeric(30,0) | 17 | NULL allowed |  |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |  |
|  | Notes Notes | varchar(max) | max | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Request­To­Exceed­Customer­Invoice­Due­Days­In­Order\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Exceed­Customer­Visit­Order] |

MS\_­Description

Stores requests submitted by sales representatives to exceed or override the predefined customer visit order in the sales route. The table records request details including company, salesperson, customer, transaction date, approval status, geographic location, related notes, and device identifiers. It is used to track and approve exceptions when a salesperson needs to visit a customer outside the planned visit sequence.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | OSFA\_­Auto­ID Osfa auto identifier | numeric(30,0) | 17 | NULL allowed |  |
|  | Notes Notes | nvarchar(4000) | 8000 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Exceed­Finish­All­Tasks] |

MS\_­Description

Stores requests submitted by sales representatives to override the requirement of completing all assigned tasks during a customer visit or sales activity. The table records request details including company, salesperson, customer, transaction date, approval status, geographic location, related notes, and device identifiers. It is used to track and approve exceptions when a salesperson needs to finish an activity without completing all required tasks. The table also records whether the request was canceled.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | OSFA\_­Auto­ID Osfa auto identifier | numeric(30,0) | 17 | NULL allowed |  |
|  | Notes Notes | varchar(4000) | 4000 | NULL allowed |  |
|  | Is­Canceled Flag indicating canceled | bit | 1 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Request­To­Exceed­Finish­All­Tasks\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Exceed­Invoice­Amount] |

MS\_­Description

Stores requests submitted by sales representatives to exceed the allowed invoice amount during sales transactions. The table records request details including company, salesperson, customer, invoice amount, request date, approval status, geographic location, related notes, and device identifiers. It is used to track and approve exceptions when issuing invoices that exceed the permitted invoice value.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Invoice­Amount Invoice amount | float | 8 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | OSFA\_­Auto­ID Osfa auto identifier | numeric(18,0) | 9 | NULL allowed |  |
|  | Notes Notes | nvarchar(max) | max | NULL allowed |  |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Exceed­Invoice­Count] |

MS\_­Description

Stores requests submitted by sales representatives to exceed the allowed invoice count for a customer during sales operations. The table records request details including company, salesperson, customer, invoice count, transaction date, approval status, geographic location, related notes, and tablet system identifiers. It is used to track and approve exceptions when issuing more invoices than the permitted number.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Invoice­Count Invoice count | int | 4 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | OSFA\_­Auto­ID Osfa auto identifier | numeric(18,0) | 9 | NULL allowed |  |
|  | Notes Notes | nvarchar(max) | max | NULL allowed |  |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Exceed­Pay­Invoice­Discount] |

MS\_­Description

Stores requests submitted by sales representatives to exceed the maximum allowed discount percentage on customer invoice payments. The table records request details including company, salesperson, customer, payment amount, transaction date, approval status, geographic location, notes, tablet system identifiers, and the maximum discount allowed. It is used to track and approve exceptions to standard payment discount policies.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |
|  | Payment­Amount Payment amount | float | 8 | NULL allowed |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |
|  | OSFA\_­Auto­ID Osfa auto identifier | numeric(18,0) | 9 | NULL allowed |
|  | Notes Notes | nvarchar(max) | max | NULL allowed |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |
|  | Max­Discount­Perc Max discount percentage | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Exceed­Pay­Over­Balance] |

MS\_­Description

Stores requests submitted by sales representatives to record a customer payment that exceeds the current outstanding balance. The table records request details including company, salesperson, customer, receipt amount, customer balance, transaction date, approval status, geographic location, and device identifiers. It is used to track and approve exceptions when receiving payments greater than the customer's outstanding balance.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Receipt­Amount Receipt amount | float | 8 | NULL allowed |  |
|  | Customer­Banalce Customer banalce | float | 8 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | OSFA\_­Auto­ID Osfa auto identifier | numeric(30,0) | 17 | NOT NULL |  |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Exceed­Salesman­Credit­Limit] |

MS\_­Description

Stores requests submitted by sales representatives to exceed the defined credit limit assigned to a salesperson during sales transactions. The table records request details including company, salesperson, customer, invoice amount, transaction date, approval status, geographic location, and device identifiers. It also stores the salesperson’s credit limit, current balance, and the amount requested to exceed the allowed limit. This table is used to track and approve exceptions to salesperson credit limit policies.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Invoice­Amount Invoice amount | float | 8 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |  |
|  | Salesman­Credit­Limit Salesman credit limit | float | 8 | NULL allowed |  |
|  | Salesman­Banalce Salesman banalce | float | 8 | NULL allowed |  |
|  | Exceed­Amount Exceed amount | float | 8 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Request­To­Exceed­Salesman­Credit­Limit\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Increase­Customer­Creditlimit] |

MS\_­Description

Stores requests to increase the credit limit assigned to a customer. The table records request details including company, order reference (year and number), approval status, current customer credit limit, outstanding balances, check balances, order amount, requested exceed amount, allowed due days, and related notes. It is used to track and approve changes to the customer's credit limit based on sales orders or business requirements.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Order­Year Order year | smallint | 2 | NULL allowed |  |
|  | Order­No Order number | int | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Customer­Credit­Limit Customer credit limit | float | 8 | NULL allowed |  |
|  | Customer­Banalce Customer banalce | float | 8 | NULL allowed |  |
|  | Customer­Chq­Banalce Customer chq banalce | float | 8 | NULL allowed |  |
|  | Order­Amount Order amount | float | 8 | NULL allowed |  |
|  | Exceed­Amount Exceed amount | float | 8 | NULL allowed |  |
|  | Due­Days Due days | int | 4 | NULL allowed |  |
|  | Notes Notes | nvarchar(4000) | 8000 | NULL allowed |  |
|  | SID Sid | numeric(30,0) | 17 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Link­Customer­To­Salesman] |

MS\_­Description

Stores requests submitted by sales representatives to link or assign a customer to a specific salesperson. The table records request details including company, salesperson, customer, visit time, transaction date, approval status, geographic location, device identifiers, and related notes. It is used to track and approve changes in customer–salesperson assignments within the sales routing or territory management process.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Visit­Time Visit time | smalldatetime | 4 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | OSFA\_­Auto­ID Osfa auto identifier | numeric(30,0) | 17 | NULL allowed |  |
|  | Notes Notes | nvarchar(4000) | 8000 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Login­To­Customer­Without­Verficiation] |

MS\_­Description

Stores requests submitted by sales representatives to log in to a customer account without completing the standard verification process. The table records request details including company, salesperson, customer, transaction date, approval status, geographic location, device identifiers, and user information. It also tracks whether the request was shown and whether the login was completed after approval. This table is used to monitor and approve exceptions to the customer verification requirement.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | OSFA\_­Auto­ID Osfa auto identifier | numeric(30,0) | 17 | NULL allowed |  |
|  | User­ID User identifier | nvarchar(50) | 100 | NULL allowed |  |
|  | Is­Shown Flag indicating shown | bit | 1 | NULL allowed |  |
|  | Logged­In Logged in | bit | 1 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Request­To­Login­To­Customer­Without­Verficiation\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Make­Transaction­To­Suspended­Customer] |

MS\_­Description

Stores requests submitted by sales representatives to perform transactions for customers whose accounts are currently suspended. The table records request details including company, transaction type, salesperson, customer, transaction date, approval status, geographic location, and device identifiers. It is used to track and approve exceptions that allow temporary transactions with suspended customers.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Tr­Type Tr type | int | 4 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | OSFA\_­Auto­ID Osfa auto identifier | numeric(18,0) | 9 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Make­Zero­Amount­Invoice] |

MS\_­Description

Stores requests submitted by sales representatives to create an invoice with a zero amount. The table records request details including company, salesperson, customer, transaction date, approval status, geographic location, notes, device identifiers, and invoice details in JSON format. It is used to track and approve exceptions when issuing invoices that do not contain a payable amount.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | OSFA\_­Auto­ID Osfa auto identifier | numeric(18,0) | 9 | NULL allowed |  |
|  | Notes Notes | nvarchar(max) | max | NULL allowed |  |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |  |
|  | Invoice­Destiails­JSON Invoice destiails json | nvarchar(max) | max | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Return­Invoice] |

MS\_­Description

Stores requests submitted by sales representatives to return or cancel a previously issued customer invoice. The table records request details including company, salesperson, customer, invoice amount, transaction date, approval status, geographic location, notes, and tablet system identifiers. It is used to track and approve invoice return requests before processing them in the system.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Invoice­Amount Invoice amount | float | 8 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |  |
|  | Notes Notes | varchar(4000) | 4000 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Request­To­Return­Invoice\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Visit­Customer­Not­In­Route] |

MS\_­Description

Stores requests submitted by sales representatives to visit a customer who is not included in their predefined sales route. The table records request details including company, salesperson, customer, transaction date, approval status, and geographic location. It is used to track and approve exceptions when a salesperson needs to visit customers outside their assigned route.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Request­To­Visit­Customer­Not­In­Route\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Request­To­Void­Transaction] |

MS\_­Description

Stores requests submitted by sales representatives to void or cancel an existing transaction in the system. The table records request details including company, salesperson, transaction type, transaction reference (year and number), transaction date, approval status, and geographic location. It is used to track and approve requests for canceling previously recorded transactions.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Sales­Person­No Sales person number | int | 4 | NULL allowed |  |
|  | Tr­Type­ID Tr type identifier | smallint | 2 | NULL allowed |  |
|  | Tr­Type­Year Tr type year | smallint | 2 | NULL allowed |  |
|  | Tr­Type­No Tr type number | int | 4 | NULL allowed |  |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |  |
|  | Is­Aproved Flag indicating aproved | bit | 1 | NULL allowed |  |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |  |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Return­Orders­Details] |

MS\_­Description

Stores detailed line items for customer return orders, including company, transaction reference (year and number), item code, unit, item serial, quantity, bonus, price, discounts, voucher discounts, customer-specific discounts, taxes, foreign currency amounts, manual bonuses, manual discounts, bonus taxes, return reason, item status, expiration date, exchange rates, and notes. It is used to track all financial, item-level, and operational details for returned orders, ensuring accurate calculation of amounts, taxes, and adjustments.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Transaction­Year Transaction year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Transaction­No Transaction number | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |
|  | Item­Serial Item serial | int | 4 | NULL allowed |
|  | Quantity Quantity | float | 8 | NULL allowed |
|  | Bonus Bonus | float | 8 | NULL allowed |
|  | Price Price | float | 8 | NULL allowed |
|  | Discount­Amount Discount amount | float | 8 | NULL allowed |
|  | Discount­Percent Discount percent | float | 8 | NULL allowed |
|  | Voucher­Discount Voucher discount | float | 8 | NULL allowed |
|  | Tax­Type Tax type | smallint | 2 | NULL allowed |
|  | Tax­Percent Tax percent | float | 8 | NULL allowed |
|  | Tax­Amount Tax amount | float | 8 | NULL allowed |
|  | Foreign­Price Foreign price | float | 8 | NULL allowed |
|  | Foreign­Discount­Amount Foreign discount amount | float | 8 | NULL allowed |
|  | Foreign­Discount­Percent Foreign discount percent | float | 8 | NULL allowed |
|  | Foreign­Vou­Discount Foreign vou discount | float | 8 | NULL allowed |
|  | Foreign­Tax­Percent Foreign tax percent | float | 8 | NULL allowed |
|  | Foreign­Tax­Amount Foreign tax amount | float | 8 | NULL allowed |
|  | Item­Status Item status | smallint | 2 | NULL allowed |
|  | Customer­Discount­Amount Customer discount amount | float | 8 | NULL allowed |
|  | Foreign­Customer­Discount­Amount Foreign customer discount amount | float | 8 | NULL allowed |
|  | UPrice U price | float | 8 | NULL allowed |
|  | Tax­Type1 Tax type 1 | smallint | 2 | NULL allowed |
|  | Tax­Percent1 Tax percent 1 | float | 8 | NULL allowed |
|  | Tax­Amount1 Tax amount 1 | float | 8 | NULL allowed |
|  | Tax­Type2 Tax type 2 | smallint | 2 | NULL allowed |
|  | Tax­Percent2 Tax percent 2 | float | 8 | NULL allowed |
|  | Tax­Amount2 Tax amount 2 | float | 8 | NULL allowed |
|  | Manual\_­Bonus Manual bonus | float | 8 | NULL allowed |
|  | Exchange­Rate Exchange rate | float | 8 | NULL allowed |
|  | Notes Notes | nvarchar(max) | max | NULL allowed |
|  | Manual\_­Disc Manual disc | float | 8 | NULL allowed |
|  | Return­Reason Return reason | int | 4 | NULL allowed |
|  | Bonus­Tax Bonus tax | float | 8 | NULL allowed |
|  | Bonus­Amount Bonus amount | float | 8 | NULL allowed |
|  | Exp­Date Exp date | smalldatetime | 4 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Return­Orders­Details\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Return­Orders­Details\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Return­Orders­Details\_­Items­Units | Company­ID->[[dbo].[Items­Units].[Company­ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=), Unit­ID->[[dbo].[Items­Units].[ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=) |
| FK\_­Return­Orders­Details\_­Return­Orders­Headers | Company­ID->[[dbo].[Return­Orders­Headers].[Company­ID]](#437+uqToRlwutPBVm9jW7LjF9Zw=), Transaction­Year->[[dbo].[Return­Orders­Headers].[Transaction­Year]](#437+uqToRlwutPBVm9jW7LjF9Zw=), Transaction­No->[[dbo].[Return­Orders­Headers].[Transaction­No]](#437+uqToRlwutPBVm9jW7LjF9Zw=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Return­Orders­Headers] |

MS\_­Description

Stores header information for customer return orders, including company, transaction reference (year and number), transaction date, salesperson, customer, price list, credit/cash indicator, discounts, currency, exchange rate, printing status, geographic location, route, ERP posting status, void flag, customer discounts, workflow approvals, final approval, document type, extra notes, reason, and timestamps. It is used to manage and track overall return order information before linking with detailed line items.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­Year Transaction year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­No Transaction number | int | 4 | NOT NULL |
|  | Transaction­Date Transaction date | smalldatetime | 4 | NULL allowed |
| ![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NULL allowed |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NULL allowed |
| ![](data:image/png;base64...) | Price­List­ID Price list identifier | int | 4 | NULL allowed |
|  | Credit­Cash Credit cash | int | 4 | NULL allowed |
|  | Discount­Amount Discount amount | float | 8 | NULL allowed |
|  | Discount­Percent Discount percent | float | 8 | NULL allowed |
|  | Foreign­Discount­Amount Foreign discount amount | float | 8 | NULL allowed |
|  | Foreign­Discount­Percent Foreign discount percent | float | 8 | NULL allowed |
|  | Notes Notes | nvarchar(500) | 1000 | NULL allowed |
| ![](data:image/png;base64...) | Currency­ID Currency identifier | smallint | 2 | NULL allowed |
|  | Exchange­Rate Exchange rate | float | 8 | NULL allowed |
|  | Is­Printed Flag indicating printed | bit | 1 | NULL allowed |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |
| ![](data:image/png;base64...) | Route­ID Route identifier | int | 4 | NULL allowed |
|  | Posted­To­ERP Posted to erp | bit | 1 | NULL allowed |
|  | Is­Void Flag indicating void | bit | 1 | NULL allowed |
|  | Customer­Name Customer name | varchar(200) | 200 | NULL allowed |
|  | WFApproved Wf approved | bit | 1 | NULL allowed |
|  | Approve Flag indicating approve | bit | 1 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(50) | 100 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(50) | 100 | NULL allowed |
|  | Tr­Date­Time Tr date time | smalldatetime | 4 | NULL allowed |
|  | Customer­Discount­Perc Customer discount percentage | float | 8 | NULL allowed |
|  | Customer­Discount­Amount Customer discount amount | float | 8 | NULL allowed |
|  | Print­Original­Count Print original count | int | 4 | NULL allowed |
|  | Print­Copy­Count Print copy count | int | 4 | NULL allowed |
|  | Is­WFApproved Flag indicating wf approved | bit | 1 | NULL allowed |
|  | WFApprove­Desc Wf approve description | nvarchar(200) | 400 | NULL allowed |
|  | Foreign­Customer­Discount­Perc Foreign customer discount percentage | float | 8 | NULL allowed |
|  | Foreign­Customer­Discount­Amount Foreign customer discount amount | float | 8 | NULL allowed |
|  | Server­Date Server date | smalldatetime | 4 | NULL allowed |
|  | Manual\_­Disc Manual disc | float | 8 | NULL allowed |
|  | Location­Line­ID Location line identifier | int | 4 | NULL allowed |
|  | Final­Approval Final approval | bit | 1 | NULL allowed |
|  | Document­Type­ID Document type identifier | int | 4 | NULL allowed |
|  | Extra­Notes Extra notes | varchar(max) | max | NULL allowed |
|  | Reason Reason | nvarchar(200) | 400 | NULL allowed |
|  | Posted­To­ERPDate­Time Posted to erp date time | smalldatetime | 4 | NULL allowed |
|  | Accept­Date Accept date | smalldatetime | 4 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Return­Orders­Headers\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Return­Orders­Headers\_­Currencies | Currency­ID->[[dbo].[Currencies].[ID]](#k0NURIzYF8aeO/uxKYIEdxSccAg=) |
| FK\_­Return­Orders­Headers\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |
| FK\_­Return­Orders­Headers\_­Price­Lists | Company­ID->[[dbo].[Price­Lists].[Company­ID]](#UTuGUXmxHIFiIaREw25LxgcqPnU=), Price­List­ID->[[dbo].[Price­Lists].[ID]](#UTuGUXmxHIFiIaREw25LxgcqPnU=) |
| FK\_­Return­Orders­Headers\_­Routes­Information | Company­ID->[[dbo].[Routes­Information].[Company­ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=), Route­ID->[[dbo].[Routes­Information].[ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=) |
| FK\_­Return­Orders­Headers\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Person­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Routes­Information] |

MS\_­Description

Stores information about sales routes within the company. The table includes route identifier, name, short name, and reference fields used for internal tracking. It is used to define and manage customer visit paths for sales representatives.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Short­Name Short name | nvarchar(10) | 20 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Routes­Information\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Acheivment­Grades] |

MS\_­Description

Stores sales achievement grades for company performance tracking. Each grade includes an identifier, name, minimum and maximum values, and a factor used to calculate salesperson performance, commissions, or other metrics. It is used to categorize and evaluate sales representatives based on their achieved results.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Min­Value Min value | float | 8 | NULL allowed |
|  | Max­Value Max value | float | 8 | NULL allowed |
|  | Factor Factor | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Sales­Acheivment­Grades\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Salesman­Cash­Settlement] |

MS\_­Description

Stores cash settlement records for salesmen within the company. Each record includes company, settlement ID, salesperson, currency, transaction date, total amount to be settled, and the amount actually paid. It is used to track and reconcile cash collections by sales representatives.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | decimal(18,0) | 9 | NOT NULL |
| ![](data:image/png;base64...) | Salesman­ID Salesman identifier | int | 4 | NOT NULL |
|  | Currency­ID Currency identifier | int | 4 | NULL allowed |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |
|  | Total­Amount Total amount | float | 8 | NULL allowed |
|  | Paid­Amount Paid amount | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Salesman­Cash­Settlement\_­Companies1 | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Salesman­Cash­Settlement\_­Salespersons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Salesman­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Order­Delivery­DF] |

MS\_­Description

Stores detailed line items for sales order deliveries, including company, order reference (year and number), item number, unit code, ordered quantity, bonus, delivered quantity, outstanding quantity, sell value, discount percentage and value, tax percentage and value, inventory quantities, voucher discounts, unit price, manual bonuses, total weight, and picked quantity. It is used to track and manage the fulfillment and delivery status of each item in a sales order.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Comp­No Comp number | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­Year Order year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Item­No Item number | varchar(20) | 20 | NOT NULL |
| ![](data:image/png;base64...) | Unit­Code Unit code | varchar(5) | 5 | NOT NULL |
|  | Orderd­Qty Orderd quantity | money | 8 | NULL allowed |
|  | Bonus Bonus | money | 8 | NULL allowed |
|  | Delivered­Qty Delivered quantity | money | 8 | NULL allowed |
|  | Outstanding­Qty Outstanding quantity | money | 8 | NULL allowed |
|  | Sell­Value Sell value | float | 8 | NULL allowed |
|  | Disc­Perc Disc percentage | money | 8 | NULL allowed |
|  | Disc­Value Disc value | float | 8 | NULL allowed |
|  | Tax­Perc Tax percentage | money | 8 | NULL allowed |
|  | Tax­Value Tax value | float | 8 | NULL allowed |
|  | Qty­OH Qty oh | money | 8 | NULL allowed |
|  | Item­Desc Item description | varchar(100) | 100 | NULL allowed |
|  | Inv­Qty Inv quantity | money | 8 | NULL allowed |
|  | Voucher­Discount Voucher discount | float | 8 | NULL allowed |
|  | Tax­Type Tax type | smallint | 2 | NULL allowed |
|  | UPrice U price | float | 8 | NULL allowed |
|  | Manual\_­Bonus Manual bonus | float | 8 | NULL allowed |
|  | Tot­Wieght Tot wieght | float | 8 | NULL allowed |
|  | Picked­Qty Picked quantity | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Order­Delivery­HF] |

MS\_­Description

Stores header information for sales order deliveries, including company, order reference (year and number), order date, salesperson, customer, order state and reason, purchase order number, discount amounts and percentages, customer discounts, planned delivery date, vehicle identifier, delivery status and timestamp, and ERP posting status. It is used to manage and track the overall delivery status of sales orders before linking to detailed line items.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Comp­No Comp number | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­Year Order year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
|  | Order­Date Order date | smalldatetime | 4 | NULL allowed |
|  | Salesman­No Salesman number | smallint | 2 | NULL allowed |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |
|  | Order­State Order state | smallint | 2 | NULL allowed |
|  | Reason Reason | smallint | 2 | NULL allowed |
|  | Order­State­Desc Order state description | varchar(50) | 50 | NULL allowed |
|  | Reason­Desc Reason description | varchar(50) | 50 | NULL allowed |
|  | PO\_­No Po number | varchar(50) | 50 | NULL allowed |
|  | Discount­Amount Discount amount | float | 8 | NULL allowed |
|  | Discount­Percent Discount percent | float | 8 | NULL allowed |
|  | Customer­Discount­Perc Customer discount percentage | float | 8 | NULL allowed |
|  | Customer­Discount­Amount Customer discount amount | float | 8 | NULL allowed |
|  | Order­Delivery­Date Order delivery date | smalldatetime | 4 | NULL allowed |
|  | Car­ID Car identifier | int | 4 | NULL allowed |
|  | Is­Delivered Flag indicating delivered | bit | 1 | NULL allowed |
|  | Delivered­Date­Time Delivered date time | smalldatetime | 4 | NULL allowed |
|  | Posted­To­ERP Posted to erp | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Order­History­DF] |

MS\_­Description

Stores detailed line items for historical sales orders, including company, order reference (year and number), item number, unit code, ordered quantity, bonus, delivered quantity, outstanding quantity, sell value, discount percentages and values, taxes, inventory quantities, voucher discounts, unit price, manual bonuses, total weight, and picked quantity. It is used to track and archive historical sales order fulfillment and financial details at the item level.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Comp­No Comp number | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­Year Order year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Item­No Item number | varchar(20) | 20 | NOT NULL |
| ![](data:image/png;base64...) | Unit­Code Unit code | varchar(5) | 5 | NOT NULL |
|  | Orderd­Qty Orderd quantity | money | 8 | NULL allowed |
|  | Bonus Bonus | money | 8 | NULL allowed |
|  | Delivered­Qty Delivered quantity | money | 8 | NULL allowed |
|  | Outstanding­Qty Outstanding quantity | money | 8 | NULL allowed |
|  | Sell­Value Sell value | float | 8 | NULL allowed |
|  | Disc­Perc Disc percentage | money | 8 | NULL allowed |
|  | Disc­Value Disc value | float | 8 | NULL allowed |
|  | Tax­Perc Tax percentage | money | 8 | NULL allowed |
|  | Tax­Value Tax value | float | 8 | NULL allowed |
|  | Qty­OH Qty oh | money | 8 | NULL allowed |
|  | Item­Desc Item description | varchar(100) | 100 | NULL allowed |
|  | Inv­Qty Inv quantity | money | 8 | NULL allowed |
|  | Voucher­Discount Voucher discount | float | 8 | NULL allowed |
|  | Tax­Type Tax type | smallint | 2 | NULL allowed |
|  | UPrice U price | float | 8 | NULL allowed |
|  | Manual\_­Bonus Manual bonus | float | 8 | NULL allowed |
|  | Tot­Wieght Tot wieght | float | 8 | NULL allowed |
|  | Picked­Qty Picked quantity | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Order­History­HF] |

MS\_­Description

Stores header information for historical sales orders, including company, order reference (year and number), order date, salesperson, customer, order state and reason, order state and reason descriptions, purchase order number, discount amounts and percentages, customer discounts, and planned delivery date. It is used to archive and review past sales orders and their overall status.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Comp­No Comp number | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­Year Order year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
|  | Order­Date Order date | smalldatetime | 4 | NULL allowed |
|  | Salesman­No Salesman number | smallint | 2 | NULL allowed |
|  | Customer­No Customer number | bigint | 8 | NULL allowed |
|  | Order­State Order state | smallint | 2 | NULL allowed |
|  | Reason Reason | smallint | 2 | NULL allowed |
|  | Order­State­Desc Order state description | varchar(50) | 50 | NULL allowed |
|  | Reason­Desc Reason description | varchar(50) | 50 | NULL allowed |
|  | PO\_­No Po number | varchar(50) | 50 | NULL allowed |
|  | Discount­Amount Discount amount | float | 8 | NULL allowed |
|  | Discount­Percent Discount percent | float | 8 | NULL allowed |
|  | Customer­Discount­Perc Customer discount percentage | float | 8 | NULL allowed |
|  | Customer­Discount­Amount Customer discount amount | float | 8 | NULL allowed |
|  | Order­Delivery­Date Order delivery date | smalldatetime | 4 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Person­Bonus­Limit] |

MS\_­Description

Stores bonus limits for salespersons within the company, including salesperson identifier, bonus year, bonus month, bonus type, and maximum bonus amount. It is used to control and manage the allowable bonuses for sales representatives each period.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Bonus­Year Bonus year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Bonus­Month Bonus month | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Bonus­Type Bonus type | int | 4 | NOT NULL |
|  | Bonus­Limit Bonus limit | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Sales­Person­Bonus­Limit\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Sales­Person­Bonus­Limit\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Person­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Salesperson­Class­Target] |

MS\_­Description

Stores salesperson targets by class, including class identifier and target frequency, to monitor and manage expected sales or visit performance.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Salesman­ID Salesman identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Class­ID Class identifier | int | 4 | NOT NULL |
|  | Target­Frequency Target frequency | int | 4 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Person­Collections­Targets] |

MS\_­Description

Stores collection targets for salespersons, including company, salesperson identifier, target year, target month, target amount, and number of days. It is used to monitor and manage expected cash collections by sales representatives over a specific period.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Target­Year Target year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Target­Month Target month | int | 4 | NOT NULL |
|  | Amount Amount | float | 8 | NULL allowed |
|  | Days­Number Days number | int | 4 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Sales­Person­Collections­Targets\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Sales­Person­Collections­Targets\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Person­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Person­Contracts­Assignment] |

MS\_­Description

Stores assignments of contracts to salespersons or positions within the company. Each record includes company, position identifier, and contract identifier, and is used to manage and track which contracts are assigned to which sales personnel or positions.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Positions­ID Positions identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Contract­ID Contract identifier | nvarchar(100) | 200 | NOT NULL |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Sales­Person­Contracts­Assignment\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Sales­Person­Contracts­Assignment\_­Contracts | Company­ID->[[dbo].[Contracts].[Company­ID]](#zSXpPHadqD7+V+akfh1GN7CwldI=), Contract­ID->[[dbo].[Contracts].[Contract­ID]](#zSXpPHadqD7+V+akfh1GN7CwldI=) |
| FK\_­Sales­Person­Contracts­Assignment\_­Positions | Company­ID->[[dbo].[Positions].[Company­ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=), Positions­ID->[[dbo].[Positions].[ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Person­Customer­Count­Targets­DF] |

MS\_­Description

Stores detailed customer count targets for salespersons within the company. Each record includes company, salesperson identifier, target year, target month, target reference identifier, and expected customer count. It is used to track and manage how many customers a salesperson is expected to visit or handle during a specific period.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Target­Year Target year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Target­Month Target month | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Target­Reference­ID Target reference identifier | int | 4 | NOT NULL |
|  | Customer­Count Customer count | nchar(10) | 20 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Person­Customer­Count­Targets­HF] |

MS\_­Description

Stores header information for salesperson customer count targets within the company. Each record includes company, salesperson identifier, target year, and target month. It is used as the summary for detailed customer count targets recorded in the corresponding detail table.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Target­Year Target year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Target­Month Target month | int | 4 | NOT NULL |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Salesperson­Customers­Visits­By­Date] |

MS\_­Description

Stores records of customer visits by salespersons on specific dates. Each record includes company, salesperson position, customer identifier, visit date, notes, and approval status. It is used to track and manage daily customer visit activities and ensure compliance with planned schedules.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Position­ID Position identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Date Date | date | 3 | NOT NULL |
|  | Notes Notes | nvarchar(max) | max | NULL allowed |
|  | Is­Approved Flag indicating approved | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Salesperson­Cust­Stock­Items­Assignment] |

MS\_­Description

Stores assignments of stock items to salespersons or positions within the company. Each record includes company, position identifier, and item code, and is used to manage which stock items are assigned to specific sales personnel for customer visits or sales responsibilities.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Positions­ID Positions identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Salesperson­Cust­Stock­Items­Assignment\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Salesperson­Cust­Stock­Items­Assignment\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Salesperson­Cust­Stock­Items­Assignment\_­Positions | Company­ID->[[dbo].[Positions].[Company­ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=), Positions­ID->[[dbo].[Positions].[ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Salesperson­Cust­Stock­Items­Target­Link] |

MS\_­Description

Stores links between stock item targets and salespersons or positions within the company. Each record includes company, position identifier, item code, target month, and target year. It is used to track and manage sales or visit targets for specific stock items per salesperson and period.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Positions­ID Positions identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...) | Target­Month Target month | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Target­Year Target year | int | 4 | NOT NULL |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Person­Group­Item­Bonus­Target] |

MS\_­Description

Stores bonus targets for items assigned to sales person groups within the company. Each record includes company, sales person group identifier, target year, item code, unit identifier, monthly targets (M1–M12), and source. It is used to manage and monitor achievement of item-specific bonus targets for sales groups throughout the year.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Sales­Person­Group­ID Sales person group identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Target­Year Target year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |
|  | M1 M 1 | float | 8 | NULL allowed |
|  | M2 M 2 | float | 8 | NULL allowed |
|  | M3 M 3 | float | 8 | NULL allowed |
|  | M4 M 4 | float | 8 | NULL allowed |
|  | M5 M 5 | float | 8 | NULL allowed |
|  | M6 M 6 | float | 8 | NULL allowed |
|  | M7 M 7 | float | 8 | NULL allowed |
|  | M8 M 8 | float | 8 | NULL allowed |
|  | M9 M 9 | float | 8 | NULL allowed |
|  | M10 M 10 | float | 8 | NULL allowed |
|  | M11 M 11 | float | 8 | NULL allowed |
|  | M12 M 12 | float | 8 | NULL allowed |
|  | Source Source | smallint | 2 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Sales­Person­Group­Item­Bonus­Target\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Sales­Person­Group­Item­Bonus­Target\_­Items­Units | Company­ID->[[dbo].[Items­Units].[Company­ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=), Unit­ID->[[dbo].[Items­Units].[ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=) |
| FK\_­Sales­Person­Group­Item­Bonus­Target\_­Sales­Persons­Groups | Company­ID->[[dbo].[Sales­Persons­Groups].[Company­ID]](#IJwFVeRoDj2cXKxVh0vr44Q0tYU=), Sales­Person­Group­ID->[[dbo].[Sales­Persons­Groups].[ID]](#IJwFVeRoDj2cXKxVh0vr44Q0tYU=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Person­Group­Item­Qty­Limit] |

MS\_­Description

Stores sales person group item qty limit data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Sales­Person­Group­ID Sales person group identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Items­Target­Group Items target group | nvarchar(100) | 200 | NOT NULL |
|  | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |
|  | Sold­Qty­Limit Sold qty limit | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Person­Item­Bonus­Target] |

MS\_­Description

Stores sales person item bonus target data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Target­Year Target year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |
|  | M1 M 1 | float | 8 | NULL allowed |
|  | M2 M 2 | float | 8 | NULL allowed |
|  | M3 M 3 | float | 8 | NULL allowed |
|  | M4 M 4 | float | 8 | NULL allowed |
|  | M5 M 5 | float | 8 | NULL allowed |
|  | M6 M 6 | float | 8 | NULL allowed |
|  | M7 M 7 | float | 8 | NULL allowed |
|  | M8 M 8 | float | 8 | NULL allowed |
|  | M9 M 9 | float | 8 | NULL allowed |
|  | M10 M 10 | float | 8 | NULL allowed |
|  | M11 M 11 | float | 8 | NULL allowed |
|  | M12 M 12 | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Sales­Person­Item­Bonus­Target\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Sales­Person­Item­Bonus­Target\_­Items­Units | Company­ID->[[dbo].[Items­Units].[Company­ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=), Unit­ID->[[dbo].[Items­Units].[ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=) |
| FK\_­Sales­Person­Item­Bonus­Target\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Person­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Person­Item­Bonus­Target­By­Customer] |

MS\_­Description

Stores monthly bonus targets for individual salespersons per item within the company. Each record includes company, salesperson identifier, target year, item code, unit identifier, and monthly targets (M1–M12). It is used to manage and monitor achievement of item-specific bonus targets for each salesperson throughout the year.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Target­Year Target year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |
|  | M1 M 1 | float | 8 | NULL allowed |
|  | M2 M 2 | float | 8 | NULL allowed |
|  | M3 M 3 | float | 8 | NULL allowed |
|  | M4 M 4 | float | 8 | NULL allowed |
|  | M5 M 5 | float | 8 | NULL allowed |
|  | M6 M 6 | float | 8 | NULL allowed |
|  | M7 M 7 | float | 8 | NULL allowed |
|  | M8 M 8 | float | 8 | NULL allowed |
|  | M9 M 9 | float | 8 | NULL allowed |
|  | M10 M 10 | float | 8 | NULL allowed |
|  | M11 M 11 | float | 8 | NULL allowed |
|  | M12 M 12 | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Person­Items­Assignment] |

MS\_­Description

Stores assignments of items to salespersons or positions within the company. Each record includes company, position identifier, item code, definition date, and suspension status. It is used to manage which items are assigned to each salesperson and track any temporary suspensions.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Positions­ID Positions identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
|  | Definition­Date Definition date | smalldatetime | 4 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Sales­Person­Items­Assignment\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Sales­Person­Items­Assignment\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Sales­Person­Items­Assignment\_­Positions | Company­ID->[[dbo].[Positions].[Company­ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=), Positions­ID->[[dbo].[Positions].[ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Person­Items­Balance] |

MS\_­Description

Stores item balances for salespersons within the company. Each record includes company, salesperson identifier, item code, unit code, and item quantity. It is used to track and manage the available stock of items assigned to each salesperson.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
|  | Unit­Code Unit code | varchar(10) | 10 | NOT NULL |
|  | Item­Quantity Item quantity | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Sales­Person­Items­Balance\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Sales­Person­Items­Balance\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Sales­Person­Items­Balance\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Person­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Person­Items­Balance­Batches] |

MS\_­Description

Stores item balances by batches for salespersons within the company. Each record includes company, salesperson identifier, item code, batch number, unit code, and item quantity. It is used to track and manage available stock per batch for each salesperson

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...) | Batch­No Batch number | nvarchar(100) | 200 | NOT NULL |
|  | Unit­Code Unit code | varchar(10) | 10 | NOT NULL |
|  | Item­Quantity Item quantity | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Person­Items­Sales­Units] |

MS\_­Description

Stores sales units for items assigned to salespersons or positions within the company. Each record includes company, position identifier, item code, unit code, and optional reference fields. It is used to manage which units of each item can be sold by each salesperson or position.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Positions­ID Positions identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Unit­Code Unit code | nvarchar(50) | 100 | NOT NULL |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Sales­Person­Items­Sales­Units\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Sales­Person­Items­Sales­Units\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Sales­Person­Items­Sales­Units\_­Positions | Company­ID->[[dbo].[Positions].[Company­ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=), Positions­ID->[[dbo].[Positions].[ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=) |
| FK\_­Sales­Person­Items­Sales­Units\_­Sales­Person­Items­Sales­Units | Company­ID->[[dbo].[Items­Units].[Company­ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=), Unit­Code->[[dbo].[Items­Units].[ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Person­Items­Use­In­Load­Order] |

MS\_­Description

Stores items and units assigned to salespersons or positions for use in load orders within the company. Each record includes company, position identifier, item code, and unit code. It is used to manage which items can be included when preparing load orders for each salesperson.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Positions­ID Positions identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...) | Unit­Code Unit code | nvarchar(50) | 100 | NOT NULL |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Sales­Person­Items­Use­In­Load­Order\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Sales­Person­Items­Use­In­Load­Order\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Sales­Person­Items­Use­In­Load­Order\_­Positions | Company­ID->[[dbo].[Positions].[Company­ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=), Positions­ID->[[dbo].[Positions].[ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Person­New­Customers­Targets] |

MS\_­Description

Stores targets for new customers assigned to salespersons within the company. Each record includes company, salesperson identifier, target year, target month, target value, and number of days. It is used to track and manage expected sales or visits for new customers per period.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Target­Year Target year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Target­Month Target month | int | 4 | NOT NULL |
|  | Value Value | int | 4 | NULL allowed |
|  | Days­Number Days number | int | 4 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Sales­Person­New­Customers­Targets\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Sales­Person­New­Customers­Targets\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Person­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Person­Notbook­Transactions­Serials] |

MS\_­Description

Stores notebook transaction serial ranges for salespersons within the company. Each record includes company, salesperson identifier, series year, series type, notebook number, customer identifier, from and to serial numbers, next available serial, and suspension status. It is used to track and manage sequential numbering of transactions in salesperson notebooks.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Default |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |  |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NOT NULL |  |
| ![](data:image/png;base64...) | Ser­Year Ser year | smallint | 2 | NOT NULL |  |
| ![](data:image/png;base64...) | Ser­Type Ser type | smallint | 2 | NOT NULL |  |
| ![](data:image/png;base64...) | Notbook­No Notbook number | nvarchar(50) | 100 | NOT NULL |  |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL | ((0)) |
|  | From­No From number | int | 4 | NULL allowed |  |
|  | To­No To number | int | 4 | NULL allowed |  |
|  | Next­Serial Next serial | int | 4 | NULL allowed |  |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Sales­Person­Notbook­Transactions­Serials\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Sales­Person­Notbook­Transactions­Serials\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Person­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Salesperson­Route­By­Date] |

MS\_­Description

Stores daily route assignments for salespersons or positions within the company. Each record includes company, position identifier, route identifier, date, and notes. It is used to manage and track which routes are assigned to each salesperson on specific dates.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Position­ID Position identifier | int | 4 | NOT NULL |
|  | Route­ID Route identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Date Date | date | 3 | NOT NULL |
|  | Notes Notes | nvarchar(max) | max | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Persons] |

MS\_­Description

Stores comprehensive details of salespersons within the company. Each record includes company, salesperson ID, parent, business unit, group, cash box and debit accounts, device ID, name and foreign name, reference fields, salesperson type, telephone, email, suspension status, position, stock update flag, day off, level, user ID, company branch ID, credit limit, data send flags, vehicle information, serial reference, maximum stock and load order values, car ID, coverage, productivity, and distribution targets, geographic coordinates, route check, asset store number, ERP posting status, barcode, item group, and monthly allowed discount value. It is used to manage, monitor, and coordinate all operational, financial, sales, and performance aspects of sales personnel.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Parent Parent | int | 4 | NULL allowed |
|  | Business­Unit­ID Business unit identifier | int | 4 | NULL allowed |
| ![](data:image/png;base64...) | Group­ID Group identifier | int | 4 | NULL allowed |
|  | Cash­Box­Account Cash box account | nvarchar(20) | 40 | NULL allowed |
|  | Debit­Account Debit account | nvarchar(20) | 40 | NULL allowed |
|  | Device­ID Device identifier | nvarchar(50) | 100 | NULL allowed |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Foreign­Name Foreign name | nvarchar(100) | 200 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |
|  | Sales­Person­Type Sales person type | int | 4 | NULL allowed |
|  | Telephone­No Telephone number | nvarchar(50) | 100 | NULL allowed |
|  | Email Email | nvarchar(100) | 200 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |
| ![](data:image/png;base64...) | Position­ID Position identifier | int | 4 | NULL allowed |
|  | Is­Updated­Stock Flag indicating updated stock | bit | 1 | NULL allowed |
|  | Day­Off Day off | nvarchar(100) | 200 | NULL allowed |
|  | Level Level | int | 4 | NULL allowed |
| ![](data:image/png;base64...) | User­ID User identifier | nvarchar(50) | 100 | NULL allowed |
| ![](data:image/png;base64...) | Company­Branche­ID Company branche identifier | int | 4 | NULL allowed |
|  | Credit­Limit Credit limit | float | 8 | NULL allowed |
|  | Is­Send­Data Flag indicating send data | bit | 1 | NULL allowed |
|  | Auto­Send­Data Flag indicating auto send data | bit | 1 | NULL allowed |
|  | Vehicle­Id Vehicle id | varchar(50) | 50 | NULL allowed |
|  | Serial­Ref Serial reference | varchar(50) | 50 | NULL allowed |
|  | Max­Stock­Value Max stock value | float | 8 | NULL allowed |
|  | Car­ID Car identifier | int | 4 | NULL allowed |
|  | Coverage­Target­Per Coverage target per | float | 8 | NULL allowed |
|  | Productivity­Target­Per Productivity target per | float | 8 | NULL allowed |
|  | Distribution­Target­Per Distribution target per | float | 8 | NULL allowed |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |
|  | Max­Load­Order­Amount Max load order amount | float | 8 | NULL allowed |
|  | Route­Check Route check | bit | 1 | NULL allowed |
|  | Asset­Store­No Asset store number | int | 4 | NULL allowed |
|  | Posted­To­ERP Posted to erp | bit | 1 | NULL allowed |
|  | Barcode Barcode | nvarchar(100) | 200 | NULL allowed |
|  | Traget­Percentage Traget percentage | float | 8 | NULL allowed |
|  | Item­Group Item group | int | 4 | NULL allowed |
|  | Monthly­Allowed­Discount­Value Monthly allowed discount value | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Sales­Persons\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Sales­Persons\_­Company­Branches | Company­ID->[[dbo].[Company­Branches].[Company­ID]](#QtIx7cCe02/M8Iq2UstqD1tTYh4=), Company­Branche­ID->[[dbo].[Company­Branches].[ID]](#QtIx7cCe02/M8Iq2UstqD1tTYh4=) |
| FK\_­Sales­Persons\_­Positions | Company­ID->[[dbo].[Positions].[Company­ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=), Position­ID->[[dbo].[Positions].[ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=) |
| FK\_­Sales­Persons\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Parent->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |
| FK\_­Sales­Persons\_­Sales­Persons­Groups | Company­ID->[[dbo].[Sales­Persons­Groups].[Company­ID]](#IJwFVeRoDj2cXKxVh0vr44Q0tYU=), Group­ID->[[dbo].[Sales­Persons­Groups].[ID]](#IJwFVeRoDj2cXKxVh0vr44Q0tYU=) |
| FK\_­Sales­Persons\_­Users | User­ID->[[dbo].[Users].[User­ID]](#xK94j3lvTOeFWmPRc97loDl7d/s=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Persons­Additional­Routes] |

MS\_­Description

Stores additional route assignments for salespersons or positions within the company. Each record includes company, position identifier, week number, day number, route identifier, and optional origin information (from position, from week, from day). It is used to manage extra or temporary routes assigned to salespersons beyond their regular schedule.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Position­ID Position identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Week­No Week number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Day­No Day number | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Route­ID Route identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | From­Position­ID From position identifier | int | 4 | NULL allowed |
|  | From­Week­No From week number | int | 4 | NULL allowed |
|  | From­Day­No From day number | int | 4 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Sales­Persons­Additional­Routes\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Sales­Persons­Additional­Routes\_­Positions | Company­ID->[[dbo].[Positions].[Company­ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=), Position­ID->[[dbo].[Positions].[ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=) |
| FK\_­Sales­Persons­Additional­Routes\_­Positions1 | Company­ID->[[dbo].[Positions].[Company­ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=), From­Position­ID->[[dbo].[Positions].[ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=) |
| FK\_­Sales­Persons­Additional­Routes\_­Routes­Information | Company­ID->[[dbo].[Routes­Information].[Company­ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=), Route­ID->[[dbo].[Routes­Information].[ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Salespersons­Assistants] |

MS\_­Description

Stores information about salespersons' assistants within the company. Each record includes company, assistant ID, name, telephone, reference fields, national ID, nationality, and suspension status. It is used to manage and track assistants supporting salespersons in their operations.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Tel Tel | nvarchar(50) | 100 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(50) | 100 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(50) | 100 | NULL allowed |
|  | National­ID National identifier | nvarchar(50) | 100 | NULL allowed |
|  | Nationality Nationality | nvarchar(50) | 100 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Salespersons­Assistants\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[ Salespersons¬Assistants¬Transactions] |

MS\_­Description

Stores transaction records linking salespersons with their assistants by date. Each record includes company, transaction date, salesperson identifier, and assistant identifier. It is used to track which assistant worked with which salesperson on specific dates.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Tr­Date Tr date | smalldatetime | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Salesperson­ID Salesperson identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Assistant­ID Assistant identifier | int | 4 | NOT NULL |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Salespersons­Assistants­Transactions\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Salespersons­Assistants­Transactions\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Salesperson­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |
| FK\_­Salespersons­Assistants­Transactions\_­Salespersons­Assistants | Company­ID->[[dbo].[Salespersons­Assistants].[Company­ID]](#0ccl2xEd8tya0kAz75PQRq0zNqs=), Assistant­ID->[[dbo].[Salespersons­Assistants].[ID]](#0ccl2xEd8tya0kAz75PQRq0zNqs=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Salespersons­Daily­Currency­Totals] |

MS\_­Description

Stores daily currency totals for salespersons within the company. Each record includes company, salesperson identifier, transaction date and time, currency identifier, actual amount, and system cash amount. It is used to compare actual cash held by the salesperson with the system-calculated amount for reconciliation purposes.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Tr­Date­Time Tr date time | date | 3 | NOT NULL |
| ![](data:image/png;base64...) | Currency­ID Currency identifier | int | 4 | NOT NULL |
|  | Actual­Amount Actual amount | float | 8 | NULL allowed |
|  | Sys­Cash­Amount Sys cash amount | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Persons­Device­Permissions] |

MS\_­Description

Stores device permissions for salespersons or positions within the company. Each record includes company, position identifier, user login credentials, and multiple permission flags controlling sales operations such as order taking, sales invoices, returns, receipts, transfers, discounts, customer management, pricing changes, stock operations, and other mobile sales activities.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Positions­ID Positions identifier | int | 4 | NOT NULL |
|  | User­Name User name | nvarchar(20) | 40 | NULL allowed |
|  | Password Password | nvarchar(20) | 40 | NULL allowed |
|  | Use­Default­Unit Flag indicating use default unit | bit | 1 | NULL allowed |
|  | Change­Price Change price | bit | 1 | NULL allowed |
|  | Make­Order­Taking Make order taking | bit | 1 | NULL allowed |
|  | Make­Transfer­Order Make transfer order | bit | 1 | NULL allowed |
|  | Make­Sales­Invoice Make sales invoice | bit | 1 | NULL allowed |
|  | Make­Return­Sales Make return sales | bit | 1 | NULL allowed |
|  | Make­Receipt Make receipt | bit | 1 | NULL allowed |
|  | Allow­Cons Flag indicating allow cons | bit | 1 | NULL allowed |
|  | Allow­Cust­Stock Flag indicating allow cust stock | bit | 1 | NULL allowed |
|  | Allow­Change­Order­Store Flag indicating allow change order store | bit | 1 | NULL allowed |
|  | Allow­Change­Order­Bus­Unit Flag indicating allow change order bus unit | bit | 1 | NULL allowed |
|  | Allow­Change­Order­Doc­Type Flag indicating allow change order doc type | bit | 1 | NULL allowed |
|  | Allow­Change­Order­Cust­Name Flag indicating allow change order cust name | bit | 1 | NULL allowed |
|  | Allow­Make­Bonus Flag indicating allow make bonus | bit | 1 | NULL allowed |
|  | Allow­Add­Cust Flag indicating allow add cust | bit | 1 | NULL allowed |
|  | Allow­Get­Cust­GPS Flag indicating allow get cust gps | bit | 1 | NULL allowed |
|  | Allow­Item­Disc Flag indicating allow item disc | bit | 1 | NULL allowed |
|  | Allow­Vou­Disc Flag indicating allow vou disc | bit | 1 | NULL allowed |
|  | Use­Multi­Store­In­Sales Flag indicating use multi store in sales | bit | 1 | NULL allowed |
|  | Canceled­Invoice­No Canceled invoice number | int | 4 | NULL allowed |
|  | Vou­Disc­Limit Vou disc limit | float | 8 | NULL allowed |
|  | Use­Barcode­For­Cust­Login Flag indicating use barcode for cust login | bit | 1 | NULL allowed |
|  | Min­Total­Of­Sales­Vou Min total of sales vou | float | 8 | NULL allowed |
|  | Check­Credit­Limit­In­Order Check credit limit in order | bit | 1 | NULL allowed |
|  | Amend­Change­Cash­Credit­In­Invoice Amend change cash credit in invoice | bit | 1 | NULL allowed |
|  | Amend­Change­Cash­Credit­In­Ret­Invoice Amend change cash credit in ret invoice | bit | 1 | NULL allowed |
|  | Cash­Only­Invoice Cash only invoice | bit | 1 | NULL allowed |
|  | Credit­Only­Return­Invoice Credit only return invoice | bit | 1 | NULL allowed |
|  | Allow­Competitive­Items Flag indicating allow competitive items | bit | 1 | NULL allowed |
|  | Allow­Add­Drawer Flag indicating allow add drawer | bit | 1 | NULL allowed |
|  | Max­Discount­Perc Max discount percentage | float | 8 | NULL allowed |
|  | Allow­Return­Order Flag indicating allow return order | bit | 1 | NULL allowed |
|  | Allow­Van­Transfer Flag indicating allow van transfer | bit | 1 | NULL allowed |
|  | Allow­Sales­Quotation Flag indicating allow sales quotation | bit | 1 | NULL allowed |
|  | Allow­Items­Replacement Flag indicating allow items replacement | bit | 1 | NULL allowed |
|  | Allow­Add­Prospective­Customer Flag indicating allow add prospective customer | bit | 1 | NULL allowed |
|  | Allow­Change­Price­In­Return Flag indicating allow change price in return | bit | 1 | NULL allowed |
|  | Allow­Item­Disc­In­Return Flag indicating allow item disc in return | bit | 1 | NULL allowed |
|  | Allow­Vou­Disc­In­Return Flag indicating allow vou disc in return | bit | 1 | NULL allowed |
|  | Allow­Unload­Order Flag indicating allow unload order | bit | 1 | NULL allowed |
|  | Allow­Make­Issue­Items Flag indicating allow make issue items | bit | 1 | NULL allowed |
|  | Allow­Debit­Credit­Note Flag indicating allow debit credit note | bit | 1 | NULL allowed |
|  | Allow­Items­Categ­Stock Flag indicating allow items categ stock | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Sales­Persons­Device­Permissions\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Sales­Persons­Device­Permissions\_­Positions | Company­ID->[[dbo].[Positions].[Company­ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=), Positions­ID->[[dbo].[Positions].[ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Persons­Device­Reports­Permissions] |

MS\_­Description

Stores report access permissions for salespersons or positions on mobile devices. Each record includes company, position identifier, and report identifier. It is used to control which reports are available for viewing by each salesperson on their device. Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Positions­ID Positions identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Report­ID Report identifier | int | 4 | NOT NULL |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Persons­Discount­Early­Pay­Discount] |

MS\_­Description

Stores early payment discount permissions for salespersons or positions within the company. Each record includes company, position identifier, effective date range, and discount percentage. It is used to allow salespersons to apply specific discounts when customers make early payments within the defined period.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Position­ID Position identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | From­Date From date | date | 3 | NOT NULL |
|  | To­Date To date | date | 3 | NOT NULL |
|  | Discount­Perc Discount percentage | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Salespersons­GPSTracking] |

MS\_­Description

Stores GPS tracking records for salespersons within the company. Each record includes company, salesperson identifier, transaction date and time, tablet system identifier, GPS coordinates (X and Y), and notes. It is used to track and monitor the geographic location and movement of salespersons during their field activities.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Tr­Date­Time Tr date time | datetime | 8 | NOT NULL |
| ![](data:image/png;base64...) | Tablet­Sys­ID Tablet sys identifier | varchar(100) | 100 | NOT NULL |
|  | Gps­X Gps x | varchar(50) | 50 | NULL allowed |
|  | Gps­Y Gps y | varchar(50) | 50 | NULL allowed |
|  | Notes Notes | varchar(1000) | 1000 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Persons­Groups] |

MS\_­Description

Stores salespersons groups within the company. Each record includes company, group identifier, group name, short name, reference fields, associated salesperson identifier, and company branch identifier. It is used to organize salespersons into groups for management, reporting, and operational purposes.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Short­Name Short name | nvarchar(50) | 100 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |
|  | Sales­Person­ID Sales identifier | int | 4 | NULL allowed |
|  | Company­Branch­ID Company branch identifier | int | 4 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Sales­Persons­Groups\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Persons­Items­Groups] |

MS\_­Description

Stores item groups used for salespersons within the company. Each record includes company, group identifier, name, short name, and reference fields. It is used to categorize items into groups for sales management, targeting, and operational control.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Short­Name Short name | nvarchar(50) | 100 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Salespersons­Messages] |

MS\_­Description

Stores internal messages sent to salespersons within the company. Each record includes company, salesperson identifier, message identifier, message date and time, message text, read status, read date and time, and user identifier. It is used to manage communication between the system or administrators and salespersons.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Salesperson­ID Salesperson identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Msg­ID Msg identifier | bigint | 8 | NOT NULL |
|  | Msg­Date­Time Msg date time | smalldatetime | 4 | NULL allowed |
|  | Message­Text Message text | nvarchar(max) | max | NULL allowed |
|  | Is­Read Flag indicating read | bit | 1 | NULL allowed |
|  | Read­Date­Time Read date time | smalldatetime | 4 | NULL allowed |
|  | User­ID User identifier | nvarchar(50) | 100 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Salespersons­Messages\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Salespersons­Messages\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Salesperson­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Salespersons­Messages­Definition] |

MS\_­Description

Stores predefined message templates for salespersons within the company. Each record includes company, message identifier, message title, and message text. It is used to define standard messages that can be sent to salespersons through the system.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Message­Title Message title | nvarchar(500) | 1000 | NULL allowed |
|  | Message­Text Message text | nvarchar(max) | max | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Person­Special­Targets] |

MS\_­Description

Stores special sales targets for individual salespersons within the company. Each record includes company, salesperson identifier, target year and month, target sales amount, average invoice count, and average item count. It is used to define specific sales objectives beyond general targets.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Target­Year Target year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Target­Month Target month | int | 4 | NOT NULL |
|  | Sales­Amount Sales amount | float | 8 | NULL allowed |
|  | Invoice­Avg­Count Invoice avg count | int | 4 | NULL allowed |
|  | Item­Avg­Count Item avg count | int | 4 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Salespersons­Procedures] |

MS\_­Description

Stores procedures performed by salespersons within the company. Each record includes company, procedure identifier, position identifier, customer identifier, procedure date, status, and transaction date and time. It is used to track and manage sales-related activities for each salesperson.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Procedure­ID Procedure identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Position­ID Position identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Procedure­Date Procedure date | smalldatetime | 4 | NOT NULL |
|  | Status Status | bit | 1 | NULL allowed |
|  | Tr­Date­Time Tr date time | datetime | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Salespersons­Procedures\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Salespersons­Procedures\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |
| FK\_­Salespersons­Procedures\_­Daily­Procedures | Company­ID->[[dbo].[Daily­Procedures].[Company­ID]](#poiMEFqRis/kSReUWjfL/6Ng9ck=), Procedure­ID->[[dbo].[Daily­Procedures].[ID]](#poiMEFqRis/kSReUWjfL/6Ng9ck=) |
| FK\_­Salespersons­Procedures\_­Positions | Company­ID->[[dbo].[Positions].[Company­ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=), Position­ID->[[dbo].[Positions].[ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Persons­Routes] |

MS\_­Description

Stores weekly route schedules for salespersons within the company. Each record includes company, position identifier, week day, weekly indicators (Week1 to Week4), and day. It is used to plan, assign, and monitor field routes for sales staff.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Positions­ID Positions identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Week­Day Week day | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Week1 Week 1 | int | 4 | NULL allowed |
| ![](data:image/png;base64...) | Week2 Week 2 | int | 4 | NULL allowed |
| ![](data:image/png;base64...) | Week3 Week 3 | int | 4 | NULL allowed |
| ![](data:image/png;base64...) | Week4 Week 4 | int | 4 | NULL allowed |
|  | Day Day | nvarchar(50) | 100 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Sales­Persons­Routes\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Sales­Persons­Routes\_­Positions | Company­ID->[[dbo].[Positions].[Company­ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=), Positions­ID->[[dbo].[Positions].[ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=) |
| FK\_­Sales­Persons­Routes\_­Routes­Information\_­Week1 | Company­ID->[[dbo].[Routes­Information].[Company­ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=), Week1->[[dbo].[Routes­Information].[ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=) |
| FK\_­Sales­Persons­Routes\_­Routes­Information\_­Week2 | Company­ID->[[dbo].[Routes­Information].[Company­ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=), Week2->[[dbo].[Routes­Information].[ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=) |
| FK\_­Sales­Persons­Routes\_­Routes­Information\_­Week3 | Company­ID->[[dbo].[Routes­Information].[Company­ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=), Week3->[[dbo].[Routes­Information].[ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=) |
| FK\_­Sales­Persons­Routes\_­Routes­Information\_­Week4 | Company­ID->[[dbo].[Routes­Information].[Company­ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=), Week4->[[dbo].[Routes­Information].[ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Salespersons­Security] |

MS\_­Description

Stores security and login information for salespersons within the company. Each record includes company, salesperson identifier, user identifier, password, suspension status, last password change date, and last activation code change date. It is used to manage system access and account security.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Salesperson­ID Salesperson identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | User­ID User identifier | nvarchar(50) | 100 | NULL allowed |
|  | Pass Pass | nvarchar(50) | 100 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |
|  | Last­Pass­Change­Date Last pass change date | smalldatetime | 4 | NULL allowed |
|  | Last­Activation­Code­Change­Date Last activation code change date | smalldatetime | 4 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Salespersons­Security\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Salespersons­Security\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Salesperson­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Salespersons­Send­Orders] |

MS\_­Description

Tracks orders sent by salespersons within the company. Each record includes send identifier, company, salesperson, request date and time, status, sent flag, result, start and finish date/time, and error count. It is used to monitor and manage order submission processes.

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Send­ID Send identifier | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Salesperson­ID Salesperson identifier | int | 4 | NULL allowed |  |
|  | Request­Date­Time Request date time | datetime | 8 | NULL allowed |  |
|  | Status Status | nvarchar(50) | 100 | NULL allowed |  |
|  | Is­Sent Flag indicating sent | bit | 1 | NULL allowed |  |
|  | Result Result | nvarchar(max) | max | NULL allowed |  |
|  | Start­Date­Time Start date time | datetime | 8 | NULL allowed |  |
|  | Finish­Date­Time Finish date time | datetime | 8 | NULL allowed |  |
|  | Error­Count Error count | int | 4 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Person­Stock­Tacking] |

MS\_­Description

Stores sales person stock tacking data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­Year Order year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
|  | Order­Date Order date | smalldatetime | 4 | NULL allowed |
| ![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NULL allowed |
|  | Notes Notes | nvarchar(500) | 1000 | NULL allowed |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |
|  | Route­ID Route identifier | int | 4 | NULL allowed |
|  | Tr­Date­Time Tr date time | smalldatetime | 4 | NULL allowed |
|  | Print­Original­Count Print original count | int | 4 | NULL allowed |
|  | Print­Copy­Count Print copy count | int | 4 | NULL allowed |
|  | Server­Date Server date | smalldatetime | 4 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(50) | 100 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(50) | 100 | NULL allowed |
|  | Posted­To­ERP Posted to erp | bit | 1 | NULL allowed |
|  | Is­Approved Flag indicating approved | bit | 1 | NULL allowed |
|  | Extra­Note Extra note | nvarchar(3000) | 6000 | NULL allowed |
|  | Unload­Order­No Unload order number | nvarchar(50) | 100 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Sales­Person­Stock­Tacking\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Sales­Person­Stock­Tacking\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Person­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Person­Stock­Tacking­Details] |

MS\_­Description

Records stock taking activities performed by salespersons. Each entry includes company, order year and number, order date, salesperson ID, notes, geographic coordinates, route ID, transaction datetime, print counts, server date, references, ERP posting status, approval flag, extra notes, and unload order number. It is used to track and manage field stock taking for accuracy and accountability.Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Order­Year Order year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |
|  | Begin­Quantity Begin quantity | float | 8 | NULL allowed |
|  | Curr­Quantity Curr quantity | float | 8 | NULL allowed |
|  | Quantity Quantity | float | 8 | NULL allowed |
|  | Notes Notes | nvarchar(300) | 600 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Sales­Person­Stock­Tacking­Details\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Sales­Person­Stock­Tacking­Details\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Sales­Person­Stock­Tacking­Details\_­Items­Units | Company­ID->[[dbo].[Items­Units].[Company­ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=), Unit­ID->[[dbo].[Items­Units].[ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=) |
| FK\_­Sales­Person­Stock­Tacking­Details\_­Sales­Person­Stock­Tacking | Company­ID->[[dbo].[Sales­Person­Stock­Tacking].[Company­ID]](#OHlpZ7FSFtTE/XSxq3pv60j7SGg=), Order­Year->[[dbo].[Sales­Person­Stock­Tacking].[Order­Year]](#OHlpZ7FSFtTE/XSxq3pv60j7SGg=), Order­No->[[dbo].[Sales­Person­Stock­Tacking].[Order­No]](#OHlpZ7FSFtTE/XSxq3pv60j7SGg=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Salesperson­Target­Reference­Focus­Item] |

MS\_­Description

Maps salespersons to focus items for specific sales targets. Each record includes company, salesperson ID, item code, and target reference ID. It is used to track which items each salesperson should prioritize to achieve assigned targets.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Salesperson­ID Salesperson identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Item­Code Item code | varchar(500) | 500 | NOT NULL |
|  | Target­Reference­ID Target reference identifier | int | 4 | NOT NULL |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Person­Targets] |

MS\_­Description

Stores sales targets and associated commissions for salespersons. Each record includes company, salesperson ID, target year and month, target type, target amount, days number, total commissions, and percentage allocations. It is used to track, evaluate, and manage salesperson performance against assigned targets.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Target­Year Target year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Target­Month Target month | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Target­Type­ID Target type identifier | int | 4 | NULL allowed |
|  | Amount Amount | float | 8 | NULL allowed |
|  | Days­Number Days number | int | 4 | NULL allowed |
|  | Total­Commissions\_1 Total commissions 1 | float | 8 | NULL allowed |
|  | Total­Commissions\_2 Total commissions 2 | float | 8 | NULL allowed |
|  | Total­Commissions\_3 Total commissions 3 | float | 8 | NULL allowed |
|  | Total­Commissions\_4 Total commissions 4 | float | 8 | NULL allowed |
|  | Perc\_­G1 Perc g 1 | float | 8 | NULL allowed |
|  | Perc\_­G2 Perc g 2 | float | 8 | NULL allowed |
|  | Perc\_­G3 Perc g 3 | float | 8 | NULL allowed |
|  | Perc\_­G4 Perc g 4 | float | 8 | NULL allowed |
|  | Perc\_­G3\_1234 Perc g 3 1234 | float | 8 | NULL allowed |
|  | Perc\_­G4\_1234 Perc g 4 1234 | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Sales­Person­Targets\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Sales­Person­Targets\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Person­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |
| FK\_­Sales­Person­Targets\_­Targets­Types | Target­Type­ID->[[dbo].[Targets­Types].[ID]](#0/4snZsACLzbPDsnGKCgpJuaMnM=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Person­Targets­Details] |

MS\_­Description

Stores detailed sales targets for each salesperson, including company, salesperson ID, target year and month, target reference ID, quantity, amount, days number, commission, and percentage allocations. Used to monitor and evaluate performance and commission distribution at a granular level.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Target­Year Target year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Target­Month Target month | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Target­Reference­ID Target reference identifier | int | 4 | NOT NULL |
|  | Quantity Quantity | float | 8 | NULL allowed |
|  | Amount Amount | float | 8 | NULL allowed |
|  | Days­Number Days number | int | 4 | NULL allowed |
|  | Commission Commission | float | 8 | NULL allowed |
|  | Perc\_­G1\_1 Perc g 1 1 | float | 8 | NULL allowed |
|  | Perc\_­G1\_2 Perc g 1 2 | float | 8 | NULL allowed |
|  | Perc\_­G1\_3 Perc g 1 3 | float | 8 | NULL allowed |
|  | Perc\_­G1\_4 Perc g 1 4 | float | 8 | NULL allowed |
|  | Perc\_­G2\_1 Perc g 2 1 | float | 8 | NULL allowed |
|  | Perc\_­G2\_2 Perc g 2 2 | float | 8 | NULL allowed |
|  | Perc\_­G2\_3 Perc g 2 3 | float | 8 | NULL allowed |
|  | Perc\_­G2\_4 Perc g 2 4 | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Sales­Person­Targets­Details\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Sales­Person­Targets­Details\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Person­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |
| FK\_­Sales­Person­Targets­Details\_­Sales­Person­Targets | Company­ID->[[dbo].[Sales­Person­Targets].[Company­ID]](#jtTF4ZU/xg5jXQSLOvkiNqRWA2g=), Sales­Person­ID->[[dbo].[Sales­Person­Targets].[Sales­Person­ID]](#jtTF4ZU/xg5jXQSLOvkiNqRWA2g=), Target­Year->[[dbo].[Sales­Person­Targets].[Target­Year]](#jtTF4ZU/xg5jXQSLOvkiNqRWA2g=), Target­Month->[[dbo].[Sales­Person­Targets].[Target­Month]](#jtTF4ZU/xg5jXQSLOvkiNqRWA2g=) |
| FK\_­Sales­Person­Targets­Details\_­Targets­References | Company­ID->[[dbo].[Targets­References].[Company­ID]](#pTJEdyfW1its0oUM5wpR5Npe6Js=), Target­Reference­ID->[[dbo].[Targets­References].[ID]](#pTJEdyfW1its0oUM5wpR5Npe6Js=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Person­Targets­Off­Days] |

MS\_­Description

Stores the off days for each salesperson’s sales targets, including company, salesperson ID, target year and month, and the specific off day. Used to account for non-working days when calculating monthly targets.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Target­Year Target year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Target­Month Target month | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Off­Day Off day | smalldatetime | 4 | NOT NULL |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Person­Transactions­Serials] |

MS\_­Description

Maintains the next serial numbers for various sales transactions for each salesperson, including order taking, transfer orders, sales invoices, returns, receipts, stock movements, van transfers, quotations, and other related transactions. Tracks company, salesperson ID, and year of serial to ensure unique sequencing of all transaction types.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Ser­Year Ser year | smallint | 2 | NOT NULL |
|  | Order­Taking­Next­Serial Order taking next serial | bigint | 8 | NULL allowed |
|  | Transfer­Order­Next­Serial Transfer order next serial | bigint | 8 | NULL allowed |
|  | Sales­Invoice­Next­Serial Sales invoice next serial | bigint | 8 | NULL allowed |
|  | Return­Sales­Next­Serial Return sales next serial | bigint | 8 | NULL allowed |
|  | Receipt­Next­Serial Receipt next serial | bigint | 8 | NULL allowed |
|  | Cons­Next­Serial Cons next serial | bigint | 8 | NULL allowed |
|  | Cust­Stock­Next­Serial Cust stock next serial | bigint | 8 | NULL allowed |
|  | Competitive­Items­Info­Next­Serial Competitive items info next serial | bigint | 8 | NULL allowed |
|  | Un­Load­Orders­Next­Serials Un load orders next serials | bigint | 8 | NULL allowed |
|  | Salesman­Stock­Next­Serial Salesman stock next serial | bigint | 8 | NULL allowed |
|  | Return­Order­Next­Serial Return order next serial | bigint | 8 | NULL allowed |
|  | Van­Transfer­Next­Serial Van transfer next serial | bigint | 8 | NULL allowed |
|  | Sales­Quotation­Next­Serial Sales quotation next serial | bigint | 8 | NULL allowed |
|  | Items­Replacement­Next­Serial Items replacement next serial | bigint | 8 | NULL allowed |
|  | Issue­Items­Next­Serial Issue items next serial | bigint | 8 | NULL allowed |
|  | Sales­Invoice­Next­Serial\_­Credit Sales invoice next serial credit | bigint | 8 | NULL allowed |
|  | Debit­Credit­Note­Next­Serial Debit credit note next serial | bigint | 8 | NULL allowed |
|  | Debit­Credit­Note­Next­Serial\_2 Debit credit note next serial 2 | bigint | 8 | NULL allowed |
|  | Receive­Items­Next­Serial Receive items next serial | bigint | 8 | NULL allowed |
|  | Payments­Orders­Next­Serial Payments orders next serial | bigint | 8 | NULL allowed |
|  | Items­Categ­Stock­Next­Serial Items categ stock next serial | bigint | 8 | NULL allowed |
|  | Bank­Deposit­Next­Serial Bank deposit next serial | bigint | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Sales­Person­Transactions­Serials\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Sales­Person­Transactions­Serials\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Person­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Person­Transactions­Serials­Multi] |

MS\_­Description

Tracks the next serial numbers for various sales transactions for each salesperson across multiple reference links. Includes order taking, transfer orders, sales invoices, returns, receipts, consignment, customer stock, competitive items info, unload orders, salesman stock, return orders, van transfers, and sales quotations. Ensures unique sequential numbers per salesperson, year, and reference link within the company.

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Ser­Year Ser year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Ref­Link Ref link | varchar(200) | 200 | NOT NULL |
|  | Order­Taking­Next­Serial Order taking next serial | bigint | 8 | NULL allowed |
|  | Transfer­Order­Next­Serial Transfer order next serial | bigint | 8 | NULL allowed |
|  | Sales­Invoice­Next­Serial Sales invoice next serial | bigint | 8 | NULL allowed |
|  | Return­Sales­Next­Serial Return sales next serial | bigint | 8 | NULL allowed |
|  | Receipt­Next­Serial Receipt next serial | bigint | 8 | NULL allowed |
|  | Cons­Next­Serial Cons next serial | bigint | 8 | NULL allowed |
|  | Cust­Stock­Next­Serial Cust stock next serial | bigint | 8 | NULL allowed |
|  | Competitive­Items­Info­Next­Serial Competitive items info next serial | bigint | 8 | NULL allowed |
|  | Un­Load­Orders­Next­Serials Un load orders next serials | bigint | 8 | NULL allowed |
|  | Salesman­Stock­Next­Serial Salesman stock next serial | bigint | 8 | NULL allowed |
|  | Return­Order­Next­Serial Return order next serial | bigint | 8 | NULL allowed |
|  | Van­Transfer­Next­Serial Van transfer next serial | bigint | 8 | NULL allowed |
|  | Sales­Quotation­Next­Serial Sales quotation next serial | bigint | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Sales­Person­Transactions­Serials­Multi\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Sales­Person­Transactions­Serials­Multi\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Person­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Quotation­Details] |

MS\_­Description

Stores Sales Quotation detail line records

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Order­Year Order year | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |
|  | Quantity Quantity | float | 8 | NULL allowed |
|  | Bonus Bonus | float | 8 | NULL allowed |
|  | Price Price | float | 8 | NULL allowed |
|  | Discount­Amount Discount amount | float | 8 | NULL allowed |
|  | Discount­Percent Discount percent | float | 8 | NULL allowed |
|  | Voucher­Discount Voucher discount | float | 8 | NULL allowed |
|  | Tax­Type Tax type | smallint | 2 | NULL allowed |
|  | Tax­Percent Tax percent | float | 8 | NULL allowed |
|  | Tax­Amount Tax amount | float | 8 | NULL allowed |
|  | Foreign­Price Foreign price | float | 8 | NULL allowed |
|  | Foreign­Discount­Amount Foreign discount amount | float | 8 | NULL allowed |
|  | Foreign­Discount­Percent Foreign discount percent | float | 8 | NULL allowed |
|  | Foreign­Vou­Discount Foreign vou discount | float | 8 | NULL allowed |
|  | Foreign­Tax­Percent Foreign tax percent | float | 8 | NULL allowed |
|  | Foreign­Tax­Amount Foreign tax amount | float | 8 | NULL allowed |
|  | Customer­Discount­Amount Customer discount amount | float | 8 | NULL allowed |
|  | Foreign­Customer­Discount­Amount Foreign customer discount amount | float | 8 | NULL allowed |
|  | UPrice U price | float | 8 | NULL allowed |
|  | Tax­Type1 Tax type 1 | smallint | 2 | NULL allowed |
|  | Tax­Percent1 Tax percent 1 | float | 8 | NULL allowed |
|  | Tax­Amount1 Tax amount 1 | float | 8 | NULL allowed |
|  | Tax­Type2 Tax type 2 | smallint | 2 | NULL allowed |
|  | Tax­Percent2 Tax percent 2 | float | 8 | NULL allowed |
|  | Tax­Amount2 Tax amount 2 | float | 8 | NULL allowed |
|  | Manual\_­Bonus Manual bonus | float | 8 | NULL allowed |
|  | Exchange­Rate Exchange rate | float | 8 | NULL allowed |
|  | Manual\_­Disc Manual disc | float | 8 | NULL allowed |
|  | Notes Notes | nvarchar(300) | 600 | NULL allowed |
|  | Bonus­Tax Bonus tax | float | 8 | NULL allowed |
|  | Bonus­Amount Bonus amount | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Sales­Quotation­Details\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Sales­Quotation­Details\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Sales­Quotation­Details\_­Items­Units | Company­ID->[[dbo].[Items­Units].[Company­ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=), Unit­ID->[[dbo].[Items­Units].[ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=) |
| FK\_­Sales­Quotation­Details\_­Sales­Quotation­Headers | Company­ID->[[dbo].[Sales­Quotation­Headers].[Company­ID]](#vsiuN2f/+QOPd7ByOOecNSo/qlU=), Order­Year->[[dbo].[Sales­Quotation­Headers].[Order­Year]](#vsiuN2f/+QOPd7ByOOecNSo/qlU=), Order­No->[[dbo].[Sales­Quotation­Headers].[Order­No]](#vsiuN2f/+QOPd7ByOOecNSo/qlU=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Quotation­Headers] |

MS\_­Description

Stores Sales Quotation header records

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­Year Order year | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
|  | Order­Date Order date | smalldatetime | 4 | NULL allowed |
|  | Customer­ID Customer identifier | bigint | 8 | NULL allowed |
|  | Sales­Person­ID Sales identifier | int | 4 | NULL allowed |
|  | Price­List­ID Price list identifier | int | 4 | NULL allowed |
|  | Discount­Amount Discount amount | float | 8 | NULL allowed |
|  | Discount­Percent Discount percent | float | 8 | NULL allowed |
|  | Foreign­Discount­Amount Foreign discount amount | float | 8 | NULL allowed |
|  | Foreign­Discount­Percent Foreign discount percent | float | 8 | NULL allowed |
|  | Currency­ID Currency identifier | smallint | 2 | NULL allowed |
|  | Exchange­Rate Exchange rate | float | 8 | NULL allowed |
|  | Notes Notes | nvarchar(500) | 1000 | NULL allowed |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |
|  | Posted­To­ERP Posted to erp | bit | 1 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(50) | 100 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(50) | 100 | NULL allowed |
|  | Payment­Type Payment type | int | 4 | NULL allowed |
|  | Server­Date Server date | smalldatetime | 4 | NULL allowed |
|  | WFApproved Wf approved | bit | 1 | NULL allowed |
|  | Approved Flag indicating approved | bit | 1 | NULL allowed |
|  | Documents­Types­ID Documents types identifier | int | 4 | NULL allowed |
|  | Tr­Date­Time Tr date time | smalldatetime | 4 | NULL allowed |
|  | Business­Unit­ID Business unit identifier | int | 4 | NULL allowed |
|  | Customer­Discount­Perc Customer discount percentage | float | 8 | NULL allowed |
|  | Customer­Discount­Amount Customer discount amount | float | 8 | NULL allowed |
|  | Is­Void Flag indicating void | bit | 1 | NULL allowed |
|  | Print­Original­Count Print original count | int | 4 | NULL allowed |
|  | Print­Copy­Count Print copy count | int | 4 | NULL allowed |
|  | Foreign­Customer­Discount­Perc Foreign customer discount percentage | float | 8 | NULL allowed |
|  | Foreign­Customer­Discount­Amount Foreign customer discount amount | float | 8 | NULL allowed |
|  | Credit­Cash Credit cash | int | 4 | NULL allowed |
|  | Customer­Name Customer name | nvarchar(100) | 200 | NULL allowed |
|  | Delivery­Location Delivery location | nvarchar(50) | 100 | NULL allowed |
|  | Promises­Date Promises date | smalldatetime | 4 | NULL allowed |
|  | Is­Prospective­Customer Flag indicating prospective customer | bit | 1 | NULL allowed |
|  | Normal­Customer­ID Normal customer identifier | bigint | 8 | NULL allowed |
|  | Manual\_­Disc Manual disc | float | 8 | NULL allowed |
|  | Location­Line­ID Location line identifier | int | 4 | NULL allowed |
|  | Delivery­Days Delivery days | int | 4 | NULL allowed |
|  | Posted­To­ERPDate­Time Posted to erp date time | smalldatetime | 4 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Trans­Details] |

MS\_­Description

Stores Sales Trans detail line records

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
|  | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Trans­Auto­ID Trans auto identifier | numeric(18,0) | 9 | NOT NULL |
|  | Tax­Perc Tax percentage | float | 8 | NULL allowed |
|  | Inv­Amount Inv amount | float | 8 | NULL allowed |
|  | Disc­Amount Disc amount | float | 8 | NULL allowed |
|  | Inv­Total Inv total | float | 8 | NULL allowed |
|  | Tax­Amount Tax amount | float | 8 | NULL allowed |
|  | Net­Amount Net amount | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Sales­Trans­Details\_­Sales­Trans­Header | Trans­Auto­ID->[[dbo].[Sales­Trans­Header].[Trans­Auto­ID]](#3p+bEPlkIn0MCQiOwvpTiOLoKFg=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Sales­Trans­Header] |

MS\_­Description

Stores Sales Trans header records

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
|  | Company­ID Company identifier | smallint | 2 | NOT NULL |  |
| ![](data:image/png;base64...) | Trans­Auto­ID Trans auto identifier | numeric(18,0) | 9 | NOT NULL | 1 - 1 |
|  | Invoice­Number Invoice number | nvarchar(200) | 400 | NULL allowed |  |
|  | Salesman­No Salesman number | int | 4 | NULL allowed |  |
|  | Trans­Date Trans date | datetime | 8 | NULL allowed |  |
|  | CACR Cacr | smallint | 2 | NULL allowed |  |
|  | Customer­Location­ID Customer location identifier | nvarchar(100) | 200 | NULL allowed |  |
|  | Customer­ID Customer identifier | bigint | 8 | NULL allowed |  |
|  | Asset­ID Asset identifier | bigint | 8 | NOT NULL |  |
|  | Address Address | nvarchar(500) | 1000 | NULL allowed |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Schedule­Delivery­Orders] |

MS\_­Description

Stores schedule delivery orders data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Order­Year Order year | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Schedule­ID Schedule identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NULL allowed |
| ![](data:image/png;base64...) | Car­ID Car identifier | int | 4 | NULL allowed |
|  | Schedule­Date­Time Schedule date time | smalldatetime | 4 | NULL allowed |
|  | Assigment­Date­Time Assigment date time | smalldatetime | 4 | NULL allowed |
|  | Status Status | int | 4 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Schedule­Delivery­Orders\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Schedule­Delivery­Orders\_­Delivery­Cars | Company­ID->[[dbo].[Delivery­Cars].[Company­ID]](#TNGzSieGVszmfgt8DhcppCKtHI8=), Car­ID->[[dbo].[Delivery­Cars].[ID]](#TNGzSieGVszmfgt8DhcppCKtHI8=) |
| FK\_­Schedule­Delivery­Orders\_­Orders­Headers | Company­ID->[[dbo].[Orders­Headers].[Company­ID]](#DayzTm2CXWhInZ/pRQJ0Z15TOuE=), Order­Year->[[dbo].[Orders­Headers].[Order­Year]](#DayzTm2CXWhInZ/pRQJ0Z15TOuE=), Order­No->[[dbo].[Orders­Headers].[Order­No]](#DayzTm2CXWhInZ/pRQJ0Z15TOuE=) |
| FK\_­Schedule­Delivery­Orders\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Person­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Seals­Transactions] |

MS\_­Description

Stores seals transactions data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Tr­Date­Time Tr date time | smalldatetime | 4 | NOT NULL |
|  | Seal­No1 Seal no 1 | varchar(100) | 100 | NULL allowed |
|  | Seal­No2 Seal no 2 | varchar(100) | 100 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Seals­Transactions\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Seals­Transactions\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Person­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[SMTPEmail­Settings] |

MS\_­Description

Stores smtp email settings data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
|  | From­Email From email | varchar(500) | 500 | NULL allowed |
|  | From­Email\_­PW From email pw | varchar(50) | 50 | NULL allowed |
|  | SMTP\_­HOST Smtp host | varchar(50) | 50 | NULL allowed |
|  | SMTP\_­Port Smtp port | int | 4 | NULL allowed |
|  | Service­TImer­Interval Service t imer interval | int | 4 | NULL allowed |
|  | Enable­Ssl Flag indicating enable ssl | smallint | 2 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Special­Customer­Target] |

MS\_­Description

Stores special customer target data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Cust1ID Cust 1 identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Cust2ID Cust 2 identifier | bigint | 8 | NOT NULL |
|  | All­Customers­Names All customers names | nvarchar(max) | max | NULL allowed |
|  | Location­Name Location name | nvarchar(max) | max | NULL allowed |
|  | Sales1Name Sales 1 name | nvarchar(max) | max | NULL allowed |
|  | Sales2Name Sales 2 name | nvarchar(max) | max | NULL allowed |
|  | Division Division | nvarchar(300) | 600 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Stock­Settelment­Collection] |

MS\_­Description

Stores stock settelment collection data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Settlment­Date Settlment date | smalldatetime | 4 | NOT NULL |
| ![](data:image/png;base64...) | Line­ID Line identifier | smallint | 2 | NOT NULL |
|  | Salesman­Collected­Amout Salesman collected amout | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Stores­Balances] |

MS\_­Description

Stores stores balances data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Store­No Store number | nvarchar(50) | 100 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
|  | Qty Quantity | money | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Stores­Balances\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Stores­Balances\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Survey­Customers] |

MS\_­Description

Stores survey customers data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Cust\_­Survey\_­No Cust survey number | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Survey\_­ID Survey identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Customer\_­No Customer number | bigint | 8 | NOT NULL |
|  | Survey\_­Date Survey date | datetime | 8 | NULL allowed |
|  | GPSX Gpsx | varchar(50) | 50 | NULL allowed |
|  | GPSY Gpsy | varchar(50) | 50 | NULL allowed |
|  | Salesman­No Salesman number | nvarchar(50) | 100 | NULL allowed |
|  | Posted­To­ERP Posted to erp | bit | 1 | NULL allowed |
|  | Item­Code Item code | nvarchar(100) | 200 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Survey­Customers\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Survey­Customers\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer\_­No->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Survey­Customers­Answers] |

MS\_­Description

Stores survey customers answers data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Cust\_­Survey\_­No Cust survey number | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Question\_­No Question number | int | 4 | NOT NULL |
|  | Answer Answer | varchar(1000) | 1000 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Survey­Customers­Answers\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Survey­Customers­Link] |

MS\_­Description

Stores survey customers link data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Survey\_­ID Survey identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Survey­Customers­Link\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Survey­Customers­Link\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |
| FK\_­Survey­Customers­Link\_­Surveys | Company­ID->[[dbo].[Surveys].[Company­ID]](#fNvXDUwEI42reNhV6GJ0DrgY+lY=), Survey\_­ID->[[dbo].[Surveys].[Survey\_­ID]](#fNvXDUwEI42reNhV6GJ0DrgY+lY=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Survey­Prospective­Customers] |

MS\_­Description

Stores survey prospective customers data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Cust\_­Survey\_­No Cust survey number | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Survey\_­ID Survey identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Customer\_­No Customer number | bigint | 8 | NOT NULL |
|  | Survey\_­Date Survey date | datetime | 8 | NULL allowed |
|  | GPSX Gpsx | varchar(50) | 50 | NULL allowed |
|  | GPSY Gpsy | varchar(50) | 50 | NULL allowed |
|  | Salesman­No Salesman number | nvarchar(50) | 100 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Survey­Prospective­Customers\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Survey­Prospective­Customers\_­Prospective­Customers | Company­ID->[[dbo].[Prospective­Customers].[Company­ID]](#QwqkjSfpb3x+znCX5SBEksY/jeE=), Customer\_­No->[[dbo].[Prospective­Customers].[ID]](#QwqkjSfpb3x+znCX5SBEksY/jeE=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Survey­Prospective­Customers­Answers] |

MS\_­Description

Stores survey prospective customers answers data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Cust\_­Survey\_­No Cust survey number | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Question\_­No Question number | int | 4 | NOT NULL |
|  | Answer Answer | varchar(1000) | 1000 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Survey­Prospective­Customers­Answers\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Surveys] |

MS\_­Description

Stores surveys data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Survey\_­ID Survey identifier | int | 4 | NOT NULL |
|  | Survey\_­Name Survey name | varchar(100) | 100 | NULL allowed |
|  | Active Active | bit | 1 | NULL allowed |
|  | Is­Required Flag indicating required | bit | 1 | NULL allowed |
|  | Is­Salesman­Survey Flag indicating salesman survey | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Surveys\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Surveys\_­Questions] |

MS\_­Description

Stores surveys questions data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Survey\_­ID Survey identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Question\_­No Question number | int | 4 | NOT NULL |
|  | Template\_­No Template number | int | 4 | NULL allowed |
|  | Question\_­String Question string | varchar(300) | 300 | NULL allowed |
|  | Sort­ID Sort identifier | int | 4 | NULL allowed |
|  | Is­Required Flag indicating required | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Surveys\_­Questions\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Surveys\_­Questions\_­Options] |

MS\_­Description

Stores surveys questions options data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Survey\_­ID Survey identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Question\_­No Question number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Option\_­No Option number | int | 4 | NOT NULL |
|  | Option\_­Desc Option description | varchar(50) | 50 | NULL allowed |
|  | Sort­ID Sort identifier | int | 4 | NULL allowed |
|  | Option­Image Option image | image | max | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Surveys\_­Questions\_­Options\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Survey­Salesmans] |

MS\_­Description

Stores survey salesmans data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Salesman\_­Survey\_­No Salesman survey number | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Survey\_­ID Survey identifier | int | 4 | NOT NULL |
|  | Survey\_­Date Survey date | datetime | 8 | NULL allowed |
|  | GPSX Gpsx | varchar(50) | 50 | NULL allowed |
|  | GPSY Gpsy | varchar(50) | 50 | NULL allowed |
|  | Salesman­No Salesman number | nvarchar(50) | 100 | NULL allowed |
|  | Posted­To­ERP Posted to erp | bit | 1 | NULL allowed |
|  | For­Salesman­No For salesman number | int | 4 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Survey­Salesmans\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Survey­Salesmans­Answers] |

MS\_­Description

Stores survey salesmans answers data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Salesman\_­Survey\_­No Salesman survey number | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Question\_­No Question number | int | 4 | NOT NULL |
|  | Answer Answer | varchar(1000) | 1000 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Survey­Salesmans­Answers\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Survey­Sales­Persons­Assignment] |

MS\_­Description

Stores survey sales persons assignment data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Survey\_­ID Survey identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Sales­Persons­ID Sales persons identifier | int | 4 | NOT NULL |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Survey­Position­Assignment\_­Salespersons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Persons­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |
| FK\_­Survey­Position­Assignment\_­Surveys | Company­ID->[[dbo].[Surveys].[Company­ID]](#fNvXDUwEI42reNhV6GJ0DrgY+lY=), Survey\_­ID->[[dbo].[Surveys].[Survey\_­ID]](#fNvXDUwEI42reNhV6GJ0DrgY+lY=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[System­Codes] |

MS\_­Description

Stores system codes data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Sys­Code­Type­ID Sys code type identifier | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...) | Sys­Code Sys code | nvarchar(100) | 200 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Can­Edit Can edit | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Table\_1] |

MS\_­Description

Stores table 1 data

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| id id identifier | bigint | 8 | NULL allowed |
| name Name | nchar(100) | 200 | NULL allowed |
| bal Bal | money | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Tag­Codes] |

MS\_­Description

Stores tag codes data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Tag­Type­ID Tag type identifier | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...) | Tag­ID Tag identifier | nvarchar(100) | 200 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Targets­References] |

MS\_­Description

Stores targets references data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(200) | 400 | NULL allowed |
|  | Short­Name Short name | nvarchar(10) | 20 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |
|  | Is­Focus­Items Flag indicating focus items | bit | 1 | NULL allowed |
|  | Ref­Wieght Ref wieght | float | 8 | NULL allowed |
|  | Ref­Paid­Target­Amt Ref paid target amount | float | 8 | NULL allowed |
|  | Unit­Code Unit code | nvarchar(50) | 100 | NULL allowed |
|  | Qty Quantity | float | 8 | NULL allowed |
|  | Is­Focus­Items­Productivity Flag indicating focus items productivity | bit | 1 | NULL allowed |
|  | Target­Percentage Target percentage | float | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Targets­References\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Targets­Types] |

MS\_­Description

Stores targets types data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Tax­Codes] |

MS\_­Description

Stores tax codes data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Tax­ID Tax identifier | int | 4 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |
|  | Percentage Percentage | float | 8 | NULL allowed |
|  | is­Exempt­Tax Flag indicating exempt tax | bit | 1 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(50) | 100 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(50) | 100 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Tech\_­Customization­Performed­Tasks] |

MS\_­Description

Stores tech customization performed tasks data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| Customization­Process­ID Customization process identifier | bigint | 8 | NOT NULL | 1 - 1 |
| Client­ID Client identifier | int | 4 | NULL allowed |  |
| Client­Name Client name | nvarchar(300) | 600 | NULL allowed |  |
| Technician­Name Technician name | nvarchar(300) | 600 | NULL allowed |  |
| Notes Notes | nvarchar(max) | max | NULL allowed |  |
| Reflected­On­Ststem Reflected on ststem | bit | 1 | NOT NULL |  |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Technical\_­CFD\_temp] |

MS\_­Description

Stores technical cfd temp data

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| Company­ID Company identifier | smallint | 2 | NOT NULL |
| Customer­ID Customer identifier | bigint | 8 | NOT NULL |
| Positions­ID Positions identifier | int | 4 | NOT NULL |
| Business­Unit­ID Business unit identifier | int | 4 | NOT NULL |
| Payment­Type­ID Payment type identifier | int | 4 | NULL allowed |
| Price­List­ID Price list identifier | int | 4 | NULL allowed |
| Route­ID Route identifier | int | 4 | NULL allowed |
| Customers­Promotions­Groups­ID Customers promotions groups identifier | int | 4 | NULL allowed |
| Credit­Limit Credit limit | float | 8 | NULL allowed |
| Due­Days Due days | smallint | 2 | NULL allowed |
| Chqs­Due­Days Chqs due days | smallint | 2 | NULL allowed |
| Allow­Chqs Flag indicating allow chqs | bit | 1 | NULL allowed |
| Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |
| Favourite­Visit­Time Favourite visit time | smalldatetime | 4 | NULL allowed |
| Reference1 Reference 1 | nvarchar(20) | 40 | NULL allowed |
| Reference2 Reference 2 | nvarchar(20) | 40 | NULL allowed |
| Tax­Include Tax include | bit | 1 | NULL allowed |
| Discount­Perc Discount percentage | float | 8 | NULL allowed |
| Credit­Cash Credit cash | smallint | 2 | NULL allowed |
| Customer­Balance Customer balance | float | 8 | NULL allowed |
| Chq­Balance Chq balance | float | 8 | NULL allowed |
| Visit­Order Visit order | int | 4 | NULL allowed |
| Max­Invoice­Value Max invoice value | float | 8 | NULL allowed |
| Max­Invoice­Count Max invoice count | int | 4 | NULL allowed |
| Chq­Limit Chq limit | float | 8 | NULL allowed |
| Tax\_1\_­Include Tax 1 include | bit | 1 | NULL allowed |
| Tax\_2\_­Include Tax 2 include | bit | 1 | NULL allowed |
| Allow­Manual­Discount Flag indicating allow manual discount | bit | 1 | NULL allowed |
| Company­Branche­ID Company branche identifier | int | 4 | NULL allowed |
| Early­Repayment­Discount­Perc Early repayment discount percentage | float | 8 | NULL allowed |
| Class­ID Class identifier | int | 4 | NULL allowed |
| Discount­Early­Pay­Days Discount early pay days | int | 4 | NULL allowed |
| Location­Line­ID Location line identifier | int | 4 | NULL allowed |
| Delivery­Days Delivery days | int | 4 | NULL allowed |
| Order­Cash­Discount Order cash discount | float | 8 | NULL allowed |
| Currency­ID Currency identifier | int | 4 | NULL allowed |
| Return­Credit­Limit Return credit limit | float | 8 | NULL allowed |
| Return­Balance Return balance | float | 8 | NULL allowed |
| Location­ID Location identifier | int | 4 | NULL allowed |
| Sales­Order­Limit Sales order limit | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Technical­Financial­Insert­Table\_­Temp] |

MS\_­Description

Stores technical financial insert table temp data

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| Compno Compno | int | 4 | NULL allowed |
| Cust­ID Cust identifier | bigint | 8 | NULL allowed |
| Pos Pos | int | 4 | NULL allowed |
| route­ID Route identifier | nchar(10) | 20 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Territories] |

MS\_­Description

Stores territories data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Territory­ID Territory identifier | bigint | 8 | NOT NULL |
|  | Sales­Person­ID Sales identifier | int | 4 | NULL allowed |
|  | Territory­Type Territory type | nvarchar(50) | 100 | NULL allowed |
|  | Tr­Date Tr date | smalldatetime | 4 | NULL allowed |
|  | Notes Notes | nvarchar(300) | 600 | NULL allowed |
|  | Tr­Date­Time Tr date time | smalldatetime | 4 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Territories\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Transactions­Batchs­Items­Info] |

MS\_­Description

Stores transactions batchs items info data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Vou­Type Vou type | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Vou­Year Vou year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Vou­No Vou number | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­No Item number | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Unit Unit | nvarchar(50) | 100 | NOT NULL |
| ![](data:image/png;base64...) | Batch­No Batch number | varchar(100) | 100 | NOT NULL |
| ![](data:image/png;base64...) | Qty Quantity | money | 8 | NOT NULL |
|  | Expire­Date Expire date | smalldatetime | 4 | NULL allowed |
|  | Bonus Bonus | money | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Transactions­Batchs­Items­Info\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Transactions­Batchs­Items­Info\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­No->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Transactions­Batchs­Items­Info\_­Items­Units | Company­ID->[[dbo].[Items­Units].[Company­ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=), Unit->[[dbo].[Items­Units].[ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Transactions­Batchs­Items­Invoice­Link] |

MS\_­Description

Stores transactions batchs items invoice link data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Vou­Type Vou type | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Vou­Year Vou year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Vou­No Vou number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Item­No Item number | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...) | Unit Unit | nvarchar(50) | 100 | NOT NULL |
| ![](data:image/png;base64...) | Batch­No Batch number | varchar(100) | 100 | NOT NULL |
| ![](data:image/png;base64...) | Inv­Year Inv year | nvarchar(50) | 100 | NOT NULL |
| ![](data:image/png;base64...) | Inv­No Inv number | nvarchar(50) | 100 | NOT NULL |
|  | Qty Quantity | money | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Transactions­Details] |

MS\_­Description

Stores Transactions detail line records

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Default |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |  |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Transaction­Type­ID Transaction type identifier | smallint | 2 | NOT NULL |  |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Transaction­Year Transaction year | smallint | 2 | NOT NULL |  |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Transaction­No Transaction number | int | 4 | NOT NULL |  |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |  |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |  |
| ![](data:image/png;base64...) | Item­Serial Item serial | int | 4 | NOT NULL | ((0)) |
|  | Quantity Quantity | float | 8 | NULL allowed |  |
|  | Bonus Bonus | float | 8 | NULL allowed |  |
|  | Price Price | float | 8 | NULL allowed |  |
|  | Discount­Amount Discount amount | float | 8 | NULL allowed |  |
|  | Discount­Percent Discount percent | float | 8 | NULL allowed |  |
|  | Voucher­Discount Voucher discount | float | 8 | NULL allowed |  |
|  | Tax­Type Tax type | smallint | 2 | NULL allowed |  |
|  | Tax­Percent Tax percent | float | 8 | NULL allowed |  |
|  | Tax­Amount Tax amount | float | 8 | NULL allowed |  |
|  | Foreign­Price Foreign price | float | 8 | NULL allowed |  |
|  | Foreign­Discount­Amount Foreign discount amount | float | 8 | NULL allowed |  |
|  | Foreign­Discount­Percent Foreign discount percent | float | 8 | NULL allowed |  |
|  | Foreign­Vou­Discount Foreign vou discount | float | 8 | NULL allowed |  |
|  | Foreign­Tax­Percent Foreign tax percent | float | 8 | NULL allowed |  |
|  | Foreign­Tax­Amount Foreign tax amount | float | 8 | NULL allowed |  |
|  | Item­Status Item status | smallint | 2 | NULL allowed |  |
|  | Customer­Discount­Amount Customer discount amount | float | 8 | NULL allowed |  |
|  | Foreign­Customer­Discount­Amount Foreign customer discount amount | float | 8 | NULL allowed |  |
|  | UPrice U price | float | 8 | NULL allowed |  |
|  | Tax­Type1 Tax type 1 | smallint | 2 | NULL allowed |  |
|  | Tax­Percent1 Tax percent 1 | float | 8 | NULL allowed |  |
|  | Tax­Amount1 Tax amount 1 | float | 8 | NULL allowed |  |
|  | Tax­Type2 Tax type 2 | smallint | 2 | NULL allowed |  |
|  | Tax­Percent2 Tax percent 2 | float | 8 | NULL allowed |  |
|  | Tax­Amount2 Tax amount 2 | float | 8 | NULL allowed |  |
|  | Approve Flag indicating approve | bit | 1 | NULL allowed |  |
|  | Manual\_­Bonus Manual bonus | float | 8 | NULL allowed |  |
|  | Exchange­Rate Exchange rate | float | 8 | NULL allowed |  |
|  | SP\_­Qty Sp quantity | float | 8 | NULL allowed |  |
|  | Item­Barcode Item barcode | varchar(500) | 500 | NULL allowed |  |
|  | Manual\_­Disc Manual disc | float | 8 | NULL allowed |  |
|  | Qty­As­Bonus Qty as bonus | float | 8 | NULL allowed |  |
|  | Notes Notes | nvarchar(300) | 600 | NULL allowed |  |
|  | Return­Reason Return reason | int | 4 | NULL allowed |  |
|  | Bonus­Tax Bonus tax | float | 8 | NULL allowed |  |
|  | Bonus­Amount Bonus amount | float | 8 | NULL allowed |  |
|  | Line­Sort Line sort | smallint | 2 | NULL allowed |  |
|  | Current­Qty Current quantity | float | 8 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Transactions­Details\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Transactions­Details\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Transactions­Details\_­Items­Units | Company­ID->[[dbo].[Items­Units].[Company­ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=), Unit­ID->[[dbo].[Items­Units].[ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=) |
| FK\_­Transactions­Details\_­Transactions­Headers | Company­ID->[[dbo].[Transactions­Headers].[Company­ID]](#GZhiGjtXLJ5ft4FPZAin/6qox5k=), Transaction­Type­ID->[[dbo].[Transactions­Headers].[Transaction­Type­ID]](#GZhiGjtXLJ5ft4FPZAin/6qox5k=), Transaction­Year->[[dbo].[Transactions­Headers].[Transaction­Year]](#GZhiGjtXLJ5ft4FPZAin/6qox5k=), Transaction­No->[[dbo].[Transactions­Headers].[Transaction­No]](#GZhiGjtXLJ5ft4FPZAin/6qox5k=) |
| FK\_­Transactions­Details\_­Transactions­Types | Transaction­Type­ID->[[dbo].[Transactions­Types].[ID]](#5KHGGmOv19tzIe7dNJ3JOc6tR1w=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Transactions­Headers] |

MS\_­Description

Stores Transactions header records

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Transaction­Type­ID Transaction type identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­Year Transaction year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­No Transaction number | int | 4 | NOT NULL |
|  | Transaction­Date Transaction date | smalldatetime | 4 | NULL allowed |
| ![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NULL allowed |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NULL allowed |
| ![](data:image/png;base64...) | Price­List­ID Price list identifier | int | 4 | NULL allowed |
| ![](data:image/png;base64...) | Document­Type­ID Document type identifier | int | 4 | NULL allowed |
|  | Credit­Cash Credit cash | int | 4 | NULL allowed |
|  | Discount­Amount Discount amount | float | 8 | NULL allowed |
|  | Discount­Percent Discount percent | float | 8 | NULL allowed |
|  | Foreign­Discount­Amount Foreign discount amount | float | 8 | NULL allowed |
|  | Foreign­Discount­Percent Foreign discount percent | float | 8 | NULL allowed |
|  | Notes Notes | nvarchar(500) | 1000 | NULL allowed |
| ![](data:image/png;base64...) | Currency­ID Currency identifier | smallint | 2 | NULL allowed |
|  | Exchange­Rate Exchange rate | float | 8 | NULL allowed |
|  | Is­Printed Flag indicating printed | bit | 1 | NULL allowed |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |
| ![](data:image/png;base64...) | Route­ID Route identifier | int | 4 | NULL allowed |
|  | Posted­To­ERP Posted to erp | bit | 1 | NULL allowed |
|  | Is­Void Flag indicating void | bit | 1 | NULL allowed |
|  | Customer­Name Customer name | varchar(200) | 200 | NULL allowed |
|  | Approve Flag indicating approve | bit | 1 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(50) | 100 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(50) | 100 | NULL allowed |
|  | Tr­Date­Time Tr date time | smalldatetime | 4 | NULL allowed |
| ![](data:image/png;base64...) | Business­Unit­ID Business unit identifier | int | 4 | NULL allowed |
|  | Posted­To­ERP\_­Rec Posted to erp rec | bit | 1 | NULL allowed |
| ![](data:image/png;base64...) | Payment­Type Payment type | int | 4 | NULL allowed |
|  | Customer­Discount­Perc Customer discount percentage | float | 8 | NULL allowed |
|  | Customer­Discount­Amount Customer discount amount | float | 8 | NULL allowed |
|  | Print­Original­Count Print original count | int | 4 | NULL allowed |
|  | Print­Copy­Count Print copy count | int | 4 | NULL allowed |
|  | Is­WFApproved Flag indicating wf approved | bit | 1 | NULL allowed |
|  | WFApprove­Desc Wf approve description | nvarchar(200) | 400 | NULL allowed |
|  | Is­Check­Invoice Flag indicating check invoice | bit | 1 | NULL allowed |
| ![](data:image/png;base64...) | Contract­ID Contract identifier | nvarchar(100) | 200 | NULL allowed |
|  | Foreign­Customer­Discount­Perc Foreign customer discount percentage | float | 8 | NULL allowed |
|  | Foreign­Customer­Discount­Amount Foreign customer discount amount | float | 8 | NULL allowed |
|  | Accept­Date Accept date | smalldatetime | 4 | NULL allowed |
|  | Server­Date Server date | smalldatetime | 4 | NULL allowed |
|  | Is­Linked­With­Inv Flag indicating linked with inv | bit | 1 | NULL allowed |
|  | Detail­Count Detail count | int | 4 | NULL allowed |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |
|  | Pay­Amount\_­Curr1 Pay amount curr 1 | float | 8 | NULL allowed |
|  | Pay­Amount\_­Curr2 Pay amount curr 2 | float | 8 | NULL allowed |
|  | Accepted­By Accepted by | nvarchar(50) | 100 | NULL allowed |
|  | Patient­Name Patient name | varchar(3000) | 3000 | NULL allowed |
|  | File­No File number | varchar(300) | 300 | NULL allowed |
|  | Location­Line­ID Location line identifier | int | 4 | NULL allowed |
|  | line­Manager­Approve Line manager approve | bit | 1 | NULL allowed |
|  | Delivery­Order­Year Delivery order year | smallint | 2 | NULL allowed |
|  | Delivery­Order­No Delivery order number | int | 4 | NULL allowed |
|  | Inv­Due­Days Inv due days | int | 4 | NULL allowed |
|  | Is­Direct­Online Flag indicating direct online | bit | 1 | NULL allowed |
|  | Manual\_­Disc Manual disc | float | 8 | NULL allowed |
|  | Is­Loan Flag indicating loan | bit | 1 | NULL allowed |
|  | Loan­Approve­By Loan approve by | nvarchar(100) | 200 | NULL allowed |
|  | Posted­To­ERPDate­Time Posted to erp date time | smalldatetime | 4 | NULL allowed |
|  | Salesman­Stock­Year Salesman stock year | int | 4 | NULL allowed |
|  | Salesman­Stock­No Salesman stock number | int | 4 | NULL allowed |
|  | EINV\_­QR Einv qr | nvarchar(max) | max | NULL allowed |
|  | EINV\_­INV\_­UUID Einv inv uuid | uniqueidentifier | 16 | NULL allowed |
|  | Is­From­Cash Flag indicating from cash | bit | 1 | NULL allowed |
|  | Is­Post­Void Flag indicating post void | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Transactions­Headers\_­Business­Units | Company­ID->[[dbo].[Business­Units].[Company­ID]](#nfNLb+EhlWiX9kN6JEFSAV6syXI=), Business­Unit­ID->[[dbo].[Business­Units].[ID]](#nfNLb+EhlWiX9kN6JEFSAV6syXI=) |
| FK\_­Transactions­Headers\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Transactions­Headers\_­Contracts | Company­ID->[[dbo].[Contracts].[Company­ID]](#zSXpPHadqD7+V+akfh1GN7CwldI=), Contract­ID->[[dbo].[Contracts].[Contract­ID]](#zSXpPHadqD7+V+akfh1GN7CwldI=) |
| FK\_­Transactions­Headers\_­Currencies | Currency­ID->[[dbo].[Currencies].[ID]](#k0NURIzYF8aeO/uxKYIEdxSccAg=) |
| FK\_­Transactions­Headers\_­Customers | Company­ID->[[dbo].[Customers].[Company­ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=), Customer­ID->[[dbo].[Customers].[ID]](#vx2ljPdzFSTVvX5bMeCbWd6Cv3k=) |
| FK\_­Transactions­Headers\_­Documents­Types | Company­ID->[[dbo].[Documents­Types].[Company­ID]](#gdlNDWGb4JDf/mDxiA3zOJvy/5o=), Transaction­Type­ID->[[dbo].[Documents­Types].[Transaction­Type­ID]](#gdlNDWGb4JDf/mDxiA3zOJvy/5o=), Document­Type­ID->[[dbo].[Documents­Types].[ID]](#gdlNDWGb4JDf/mDxiA3zOJvy/5o=) |
| FK\_­Transactions­Headers\_­Payments­Types | Company­ID->[[dbo].[Payments­Types].[Company­ID]](#lO8zg+RAFUjBCTc7z+Mf67JVfuQ=), Payment­Type->[[dbo].[Payments­Types].[ID]](#lO8zg+RAFUjBCTc7z+Mf67JVfuQ=) |
| FK\_­Transactions­Headers\_­Price­Lists | Company­ID->[[dbo].[Price­Lists].[Company­ID]](#UTuGUXmxHIFiIaREw25LxgcqPnU=), Price­List­ID->[[dbo].[Price­Lists].[ID]](#UTuGUXmxHIFiIaREw25LxgcqPnU=) |
| FK\_­Transactions­Headers\_­Routes­Information | Company­ID->[[dbo].[Routes­Information].[Company­ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=), Route­ID->[[dbo].[Routes­Information].[ID]](#/xmJfUelVYBo8GKROYRcdBbYMXI=) |
| FK\_­Transactions­Headers\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Person­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |
| FK\_­Transactions­Headers\_­Transactions­Types | Transaction­Type­ID->[[dbo].[Transactions­Types].[ID]](#5KHGGmOv19tzIe7dNJ3JOc6tR1w=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Transactions­Images] |

MS\_­Description

Stores transactions images data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­Type­ID Transaction type identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­Year Transaction year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­No Transaction number | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
|  | Item­Image Item image | image | max | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Transactions­Images\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Transactions­Images\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Transactions­Promotions] |

MS\_­Description

Stores transactions promotions data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Tr­Type­ID Tr type identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Tr­Year Tr year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Tr­No Tr number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Ser­ID Ser identifier | int | 4 | NOT NULL |
|  | Promotion­Code Promotion code | nvarchar(100) | 200 | NULL allowed |
|  | Promotion­Type Promotion type | int | 4 | NULL allowed |
|  | Promotion­Name Promotion name | nvarchar(200) | 400 | NULL allowed |
|  | Input­Item Input item | nvarchar(100) | 200 | NULL allowed |
|  | Input­Unit Input unit | nvarchar(100) | 200 | NULL allowed |
|  | Input­Qty Input quantity | money | 8 | NULL allowed |
|  | Input­Amount Input amount | float | 8 | NULL allowed |
|  | Item­No Item number | nvarchar(100) | 200 | NULL allowed |
|  | Unit­Code Unit code | nvarchar(100) | 200 | NULL allowed |
|  | Bonus Bonus | money | 8 | NULL allowed |
|  | Item­Discount­Amount Item discount amount | float | 8 | NULL allowed |
|  | Item­Discount­Percent Item discount percent | float | 8 | NULL allowed |
|  | Vou­Discount­Amount Vou discount amount | float | 8 | NULL allowed |
|  | Vou­Discount­Percent Vou discount percent | float | 8 | NULL allowed |
|  | Include­In­Target­Bonus Include in target bonus | bit | 1 | NULL allowed |
|  | Is­In­Input Flag indicating in input | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Transactions­Promotions\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Transactions­Serials] |

MS\_­Description

Stores transactions serials data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Ser­Year Ser year | smallint | 2 | NOT NULL |
|  | Order­Taking­Next­Serial Order taking next serial | bigint | 8 | NULL allowed |
|  | Transfer­Order­Next­Serial Transfer order next serial | bigint | 8 | NULL allowed |
|  | Sales­Invoice­Next­Serial Sales invoice next serial | bigint | 8 | NULL allowed |
|  | Return­Sales­Next­Serial Return sales next serial | bigint | 8 | NULL allowed |
|  | Receipt­Next­Serial Receipt next serial | bigint | 8 | NULL allowed |
|  | Cons­Next­Serial Cons next serial | bigint | 8 | NULL allowed |
|  | Cust­Stock­Next­Serial Cust stock next serial | bigint | 8 | NULL allowed |
|  | Competitive­Items­Info­Next­Serial Competitive items info next serial | bigint | 8 | NULL allowed |
|  | Un­Load­Orders­Next­Serials Un load orders next serials | bigint | 8 | NULL allowed |
|  | Salesman­Stock­Next­Serial Salesman stock next serial | bigint | 8 | NULL allowed |
|  | Return­Order­Next­Serial Return order next serial | bigint | 8 | NULL allowed |
|  | Van­Transfer­Next­Serial Van transfer next serial | bigint | 8 | NULL allowed |
|  | Sales­Quotation­Next­Serial Sales quotation next serial | bigint | 8 | NULL allowed |
|  | Items­Replacement­Next­Serial Items replacement next serial | bigint | 8 | NULL allowed |
|  | Issue­Items­Next­Serial Issue items next serial | bigint | 8 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Transactions­Serials\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Transactions­Suggested­Items] |

MS\_­Description

Stores transactions suggested items data

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| Comp­No Comp number | smallint | 2 | NULL allowed |
| Vou­Type Vou type | smallint | 2 | NULL allowed |
| Vou­Year Vou year | smallint | 2 | NULL allowed |
| Vou­No Vou number | int | 4 | NULL allowed |
| Item­No Item number | varchar(100) | 100 | NULL allowed |
| Unit Unit | varchar(100) | 100 | NULL allowed |
| Qty Quantity | float | 8 | NULL allowed |
| Unit­Price Unit price | float | 8 | NULL allowed |
| Ref1 Ref 1 | varchar(100) | 100 | NULL allowed |
| Ref2 Ref 2 | varchar(100) | 100 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Transactions­Types] |

MS\_­Description

Stores transactions types data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | ID ID identifier | smallint | 2 | NOT NULL |
|  | Name Name | nvarchar(100) | 200 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Transfers­Order\_­Auto] |

MS\_­Description

Stores transfers order auto data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | File­ID File identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |
|  | Quantity Quantity | float | 8 | NOT NULL |
|  | Tr­Date­Time Tr date time | smalldatetime | 4 | NOT NULL |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |
|  | File­Name File name | nvarchar(200) | 400 | NULL allowed |
|  | Last­Run­Date Last run date | smalldatetime | 4 | NULL allowed |
|  | Max­Qty Max quantity | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Transfers­Orders­Details] |

MS\_­Description

Stores Transfers Orders detail line records

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Order­Year Order year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Vou­Type Vou type | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |
|  | Quantity Quantity | float | 8 | NULL allowed |
|  | Qty­After­Approve Qty after approve | float | 8 | NULL allowed |
|  | Date­After­Approve Date after approve | smalldatetime | 4 | NULL allowed |
|  | Notes Notes | nvarchar(300) | 600 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Transfers­Orders­Details\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Transfers­Orders­Details\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Transfers­Orders­Details\_­Items­Units | Company­ID->[[dbo].[Items­Units].[Company­ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=), Unit­ID->[[dbo].[Items­Units].[ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=) |
| FK\_­Transfers­Orders­Details\_­Transfers­Orders­Headers | Company­ID->[[dbo].[Transfers­Orders­Headers].[Company­ID]](#HROFEZUB00Khi58CJy9R53BF/wI=), Order­Year->[[dbo].[Transfers­Orders­Headers].[Order­Year]](#HROFEZUB00Khi58CJy9R53BF/wI=), Order­No->[[dbo].[Transfers­Orders­Headers].[Order­No]](#HROFEZUB00Khi58CJy9R53BF/wI=), Vou­Type->[[dbo].[Transfers­Orders­Headers].[Vou­Type]](#HROFEZUB00Khi58CJy9R53BF/wI=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Transfers­Orders­Details\_­Error­Qty] |

MS\_­Description

Stores transfers orders details error qty data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­Year Order year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Vou­Type Vou type | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...) | Unit­ID Unit identifier | nvarchar(50) | 100 | NOT NULL |
|  | Quantity Quantity | float | 8 | NULL allowed |
|  | Date­Time Date time | smalldatetime | 4 | NULL allowed |
|  | Desc Description | nvarchar(max) | max | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Transfers­Orders­Headers] |

MS\_­Description

Stores Transfers Orders header records

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­Year Order year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Vou­Type Vou type | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NULL allowed |
|  | Order­Date Order date | smalldatetime | 4 | NULL allowed |
|  | Doc­Type Doc type | smallint | 2 | NULL allowed |
|  | Notes Notes | nvarchar(500) | 1000 | NULL allowed |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |
|  | Posted­To­ERP Posted to erp | bit | 1 | NULL allowed |
|  | Approve Flag indicating approve | bit | 1 | NULL allowed |
|  | WFApproved Wf approved | bit | 1 | NULL allowed |
|  | Store­No Store number | int | 4 | NULL allowed |
|  | Tr­Date­Time Tr date time | smalldatetime | 4 | NULL allowed |
|  | Print­Original­Count Print original count | int | 4 | NULL allowed |
|  | Print­Copy­Count Print copy count | int | 4 | NULL allowed |
|  | Server­Date Server date | smalldatetime | 4 | NULL allowed |
|  | Total­Stock Total stock | nvarchar(500) | 1000 | NULL allowed |
|  | Approve­Date Flag indicating approve date | smalldatetime | 4 | NULL allowed |
|  | Approved­By Flag indicating approved by | nvarchar(50) | 100 | NULL allowed |
|  | First­Approval First approval | bit | 1 | NULL allowed |
|  | Unload­Batch­No Unload batch number | bigint | 8 | NULL allowed |
|  | Reference1 Reference 1 | nvarchar(50) | 100 | NULL allowed |
|  | Reference2 Reference 2 | nvarchar(50) | 100 | NULL allowed |
|  | Post­To­Invoice Post to invoice | bit | 1 | NULL allowed |
|  | Approved­To­Sales­Order Flag indicating approved to sales order | bit | 1 | NULL allowed |
|  | Post­To­Sales­Order Post to sales order | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Transfers­Orders­Headers\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Transfers­Orders­Headers\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Sales­Person­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[User­Activity] |

MS\_­Description

Stores user-related data for User­Activity

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | User­ID User identifier | nvarchar(50) | 100 | NOT NULL |
|  | Amend­Credit­Limit Amend credit limit | bit | 1 | NULL allowed |
|  | Amend­Chqs­Due­Days Amend chqs due days | bit | 1 | NULL allowed |
|  | Amend­Allow­Chqs Amend allow chqs | bit | 1 | NULL allowed |
|  | Amend­Payment­Type Amend payment type | bit | 1 | NULL allowed |
|  | Amend­Due­Days Amend due days | bit | 1 | NULL allowed |
|  | Amend­Max­Invoice­Value Amend max invoice value | bit | 1 | NULL allowed |
|  | Amend­Invoice­Type Amend invoice type | bit | 1 | NULL allowed |
|  | Amend­Price­List Amend price list | bit | 1 | NULL allowed |
|  | Amend­Dicount Amend dicount | bit | 1 | NULL allowed |
|  | Amend­Max­Inoice­Count Amend max inoice count | bit | 1 | NULL allowed |
|  | Amend­Tax­Include Amend tax include | bit | 1 | NULL allowed |
|  | Hide­Bonus Hide bonus | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­User­Activity\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­User­Activity\_­Users | User­ID->[[dbo].[Users].[User­ID]](#xK94j3lvTOeFWmPRc97loDl7d/s=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[User­Company­Branches­Link] |

MS\_­Description

Stores user-related data for User­Company­Branches­Link

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | User­ID User identifier | nvarchar(50) | 100 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­Branche­ID Company branche identifier | int | 4 | NOT NULL |
|  | Have­Permission Have permission | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­User­Company­Branches­Link\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­User­Company­Branches­Link\_­Company­Branches | Company­ID->[[dbo].[Company­Branches].[Company­ID]](#QtIx7cCe02/M8Iq2UstqD1tTYh4=), Company­Branche­ID->[[dbo].[Company­Branches].[ID]](#QtIx7cCe02/M8Iq2UstqD1tTYh4=) |
| FK\_­User­Company­Branches­Link\_­Users | User­ID->[[dbo].[Users].[User­ID]](#xK94j3lvTOeFWmPRc97loDl7d/s=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[User­Customers­Promotions­Group­Link] |

MS\_­Description

Stores user-related data for User­Customers­Promotions­Group­Link

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | User­ID User identifier | nvarchar(50) | 100 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Customers­Promotions­Groups­ID Customers promotions groups identifier | int | 4 | NOT NULL |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­User­Customers­Promotions­Group­Link\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­User­Customers­Promotions­Group­Link\_­Customers­Promotions­Groups | Company­ID->[[dbo].[Customers­Promotions­Groups].[Company­ID]](#CFvv0vB6qnd5JDiJpBfVpPfz9FY=), Customers­Promotions­Groups­ID->[[dbo].[Customers­Promotions­Groups].[ID]](#CFvv0vB6qnd5JDiJpBfVpPfz9FY=) |
| FK\_­User­Customers­Promotions­Group­Link\_­Users | User­ID->[[dbo].[Users].[User­ID]](#xK94j3lvTOeFWmPRc97loDl7d/s=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[User­Promotions­Link] |

MS\_­Description

Stores user-related data for User­Promotions­Link

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | User­ID User identifier | nvarchar(50) | 100 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Promotion­Code Promotion code | int | 4 | NOT NULL |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­User­Promotions­Link\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­User­Promotions­Link\_­Promotions­Headers | Company­ID->[[dbo].[Promotions­Headers].[Company­ID]](#ahTdfFcl5CBnl0mrOXzm3bmregU=), Promotion­Code->[[dbo].[Promotions­Headers].[ID]](#ahTdfFcl5CBnl0mrOXzm3bmregU=) |
| FK\_­User­Promotions­Link\_­Users | User­ID->[[dbo].[Users].[User­ID]](#xK94j3lvTOeFWmPRc97loDl7d/s=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Users] |

MS\_­Description

Stores user-related data for Users

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | User­ID User identifier | nvarchar(50) | 100 | NOT NULL |
|  | User­PWD User pwd | nvarchar(50) | 100 | NULL allowed |
|  | User­Name User name | nvarchar(100) | 200 | NULL allowed |
|  | Phone­No Phone number | nvarchar(50) | 100 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |
|  | Last­Login­Date Last login date | smalldatetime | 4 | NULL allowed |
|  | Last­Pass­Change­Date Last pass change date | smalldatetime | 4 | NULL allowed |
|  | Trasn­Date­Close Trasn date close | smalldatetime | 4 | NULL allowed |
|  | All­Promotions All promotions | bit | 1 | NULL allowed |
|  | Email Email | nvarchar(500) | 1000 | NULL allowed |
|  | Is­Logged­In Flag indicating logged in | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Users­Close­Date] |

MS\_­Description

Stores user-related data for Users­Close­Date

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | User­ID User identifier | nvarchar(50) | 100 | NOT NULL |
|  | Trasn­Date­Close Trasn date close | smalldatetime | 4 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Users­Close­Date\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Users­Close­Date\_­Users­Close­Date | User­ID->[[dbo].[Users].[User­ID]](#xK94j3lvTOeFWmPRc97loDl7d/s=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Users­Favorite­Menu] |

MS\_­Description

Stores user-related data for Users­Favorite­Menu

Columns

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Data Type | Max Length (Bytes) | Nullability |
| Company­ID Company identifier | smallint | 2 | NOT NULL |
| User­ID User identifier | nvarchar(50) | 100 | NOT NULL |
| Page­ID Page identifier | int | 4 | NOT NULL |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Users­Groups] |

MS\_­Description

Stores user-related data for Users­Groups

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | bigint | 8 | NOT NULL |
|  | Name Name | nvarchar(50) | 100 | NULL allowed |
|  | Foreign­Name Foreign name | nvarchar(50) | 100 | NULL allowed |
|  | Notes Notes | nvarchar(500) | 1000 | NULL allowed |
|  | Is­Suspend Flag indicating suspend | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Users­Groups\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Users­Groups­Link] |

MS\_­Description

Stores user-related data for Users­Groups­Link

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Group­ID Group identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | User­ID User identifier | nvarchar(50) | 100 | NOT NULL |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Users­Groups­Link\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Users­Groups­Link\_­Users | User­ID->[[dbo].[Users].[User­ID]](#xK94j3lvTOeFWmPRc97loDl7d/s=) |
| FK\_­Users­Groups­Link\_­Users­Groups | Company­ID->[[dbo].[Users­Groups].[Company­ID]](#KDsSfvwpkrBNASfe9IQSaouPrJw=), Group­ID->[[dbo].[Users­Groups].[ID]](#KDsSfvwpkrBNASfe9IQSaouPrJw=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Vacations] |

MS\_­Description

Stores vacations data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Vac­ID Vac identifier | bigint | 8 | NOT NULL |
|  | Sales­Person­ID Sales identifier | int | 4 | NULL allowed |
|  | Vac­Type Vac type | nvarchar(50) | 100 | NULL allowed |
|  | From­Date From date | smalldatetime | 4 | NULL allowed |
|  | To­Date To date | smalldatetime | 4 | NULL allowed |
|  | Notes Notes | nvarchar(300) | 600 | NULL allowed |
|  | Tr­Date­Time Tr date time | smalldatetime | 4 | NULL allowed |
|  | Approved Flag indicating approved | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Vacations\_­Vacations | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Van­Transfer­Details] |

MS\_­Description

Stores Van Transfer detail line records

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Order­Year Order year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Salesperson­ID Salesperson identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Item­Code Item code | nvarchar(100) | 200 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Unit­Code Unit code | nvarchar(50) | 100 | NOT NULL |
|  | Quantity Quantity | float | 8 | NULL allowed |
|  | Notes Notes | nvarchar(300) | 600 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Van­Transfer­Details\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Van­Transfer­Details\_­Items | Company­ID->[[dbo].[Items].[Company­ID]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=), Item­Code->[[dbo].[Items].[Item­Code]](#zCBZEcIdQ+kga9iPqy7LOKrOa4s=) |
| FK\_­Van­Transfer­Details\_­Items­Units | Company­ID->[[dbo].[Items­Units].[Company­ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=), Unit­Code->[[dbo].[Items­Units].[ID]](#FMCFC97OKTqtLQAZvqd9162BcGI=) |
| FK\_­Van­Transfer­Details\_­Van­Transfer­Details | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Salesperson­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |
| FK\_­Van­Transfer­Details\_­Van­Transfer­Header | Company­ID->[[dbo].[Van­Transfer­Header].[Company­ID]](#p4970K6/GvlyIDOTHceKMW96gPw=), Order­Year->[[dbo].[Van­Transfer­Header].[Order­Year]](#p4970K6/GvlyIDOTHceKMW96gPw=), Order­No->[[dbo].[Van­Transfer­Header].[Order­No]](#p4970K6/GvlyIDOTHceKMW96gPw=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Van­Transfer­Header] |

MS\_­Description

Stores Van Transfer header records

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­Year Order year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Order­No Order number | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | From­Salesperson­ID From salesperson identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | To­Salesperson­ID To salesperson identifier | int | 4 | NOT NULL |
|  | Order­Date Order date | smalldatetime | 4 | NULL allowed |
|  | Notes Notes | nvarchar(500) | 1000 | NULL allowed |
|  | Latitude Geographic latitude | nvarchar(50) | 100 | NULL allowed |
|  | Longitude Geographic longitude | nvarchar(50) | 100 | NULL allowed |
|  | Tr­Date­Time Tr date time | smalldatetime | 4 | NULL allowed |
|  | Print­Original­Count Print original count | int | 4 | NULL allowed |
|  | Print­Copy­Count Print copy count | int | 4 | NULL allowed |
|  | Posted­To­ERP Posted to erp | bit | 1 | NULL allowed |
|  | Tablet­Sys­ID Tablet sys identifier | varchar(50) | 50 | NULL allowed |
|  | Server­Date Server date | smalldatetime | 4 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Van­Transfer­Header\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Van­Transfer­Header\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), To­Salesperson­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |
| FK\_­Van­Transfer­Header\_­Van­Transfer­Header | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), From­Salesperson­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Verification­Codes] |

MS\_­Description

Stores verification codes data

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Verification­Type Verification type | int | 4 | NULL allowed |  |
|  | User­ID User identifier | nvarchar(50) | 100 | NULL allowed |  |
| ![](data:image/png;base64...) | Salesperson­ID Salesperson identifier | int | 4 | NULL allowed |  |
|  | Verification­Code Verification code | int | 4 | NULL allowed |  |
|  | Is­Used Flag indicating used | bit | 1 | NULL allowed |  |
|  | Create­Date­Time Create date time | smalldatetime | 4 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Verification­Codes\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­Verification­Codes\_­Sales­Persons | Company­ID->[[dbo].[Sales­Persons].[Company­ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=), Salesperson­ID->[[dbo].[Sales­Persons].[ID]](#Z5/QhgfgWdjguIRuOMOrivMlDE8=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[WF\_­Functions] |

MS\_­Description

Stores wf functions data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | ID ID identifier | smallint | 2 | NOT NULL |
|  | Ar­Name Ar name | nvarchar(200) | 400 | NULL allowed |
|  | Eng­Name Eng name | nvarchar(200) | 400 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[WF\_­Master­Log] |

MS\_­Description

Stores wf master log data

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
| ![](data:image/png;base64...) | Req­ID Req identifier | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
|  | Function­ID Function identifier | smallint | 2 | NULL allowed |  |
|  | Position­ID Position identifier | int | 4 | NULL allowed |  |
|  | Req­Date Req date | smalldatetime | 4 | NULL allowed |  |
|  | GPSx Gp sx | nvarchar(50) | 100 | NULL allowed |  |
|  | GPSy Gp sy | nvarchar(50) | 100 | NULL allowed |  |
|  | Last­Status Last status | nvarchar(1) | 2 | NULL allowed |  |
|  | Notes Notes | nvarchar(200) | 400 | NULL allowed |  |
|  | Ref1 Ref 1 | nvarchar(100) | 200 | NULL allowed |  |
|  | Ref2 Ref 2 | nvarchar(100) | 200 | NULL allowed |  |
|  | Ref3 Ref 3 | nvarchar(100) | 200 | NULL allowed |  |
|  | Ref4 Ref 4 | nvarchar(100) | 200 | NULL allowed |  |
|  | Ref5 Ref 5 | nvarchar(100) | 200 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­WF\_­Master­Log\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[WF\_­Positions­Ver] |

MS\_­Description

Stores wf positions ver data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...)![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Position­ID Position identifier | int | 4 | NOT NULL |
|  | WFVer Wf ver | numeric(18,0) | 9 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­WF\_­Positions­Ver\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |
| FK\_­WF\_­Positions­Ver\_­Positions | Company­ID->[[dbo].[Positions].[Company­ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=), Position­ID->[[dbo].[Positions].[ID]](#0hezp3sBJ5vepFnPict7YRgZ7Gg=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[WF\_­Sales­Person­Items­Category­Values] |

MS\_­Description

Stores wf sales person items category values data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Item­Code Item code | nvarchar(20) | 40 | NOT NULL |
| ![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NOT NULL |
|  | Allow­Value Flag indicating allow value | float | 8 | NULL allowed |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[WF\_­Setup­Details] |

MS\_­Description

Stores WF Setup detail line records

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Auto­ID Flag indicating auto id | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Level­ID Level identifier | tinyint | 1 | NOT NULL |
| ![](data:image/png;base64...) | Sales­Person­Type Sales person type | int | 4 | NOT NULL |
|  | Setup­Value Setup value | float | 8 | NULL allowed |
|  | Is­Final­Approve Flag indicating final approve | bit | 1 | NULL allowed |
|  | See­All­Request See all request | bit | 1 | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­WF\_­Setup­Details\_­WF\_­Setup­Header | Auto­ID->[[dbo].[WF\_­Setup­Header].[Auto­ID]](#jTJzILI7QzyFMo/CaFcnOUl5LFo=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[WF\_­Setup­Header] |

MS\_­Description

Stores WF Setup header records

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | Auto­ID Flag indicating auto id | bigint | 8 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | From­Type From type | smallint | 2 | NULL allowed |  |
|  | From­ID From identifier | bigint | 8 | NULL allowed |  |
|  | Function­ID Function identifier | smallint | 2 | NULL allowed |  |
|  | Level­Count Level count | tinyint | 1 | NULL allowed |  |
|  | Is­Suspended Flag indicating suspended | bit | 1 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­WF\_­Setup­Header\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[WF\_­Sub­Log] |

MS\_­Description

Stores wf sub log data

Columns

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability | Identity |
| ![](data:image/png;base64...) | SID Sid | numeric(30,0) | 17 | NOT NULL | 1 - 1 |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NULL allowed |  |
|  | Req­ID Req identifier | numeric(30,0) | 17 | NULL allowed |  |
|  | Position­ID Position identifier | int | 4 | NULL allowed |  |
|  | Salesman­No Salesman number | int | 4 | NULL allowed |  |
|  | Req­Date Req date | smalldatetime | 4 | NULL allowed |  |
|  | Action­Need Action need | nvarchar(2) | 4 | NULL allowed |  |
|  | Action Action | nvarchar(1) | 2 | NULL allowed |  |
|  | Action­Date Action date | smalldatetime | 4 | NULL allowed |  |
|  | ARLevel Ar level | smallint | 2 | NULL allowed |  |
|  | Tr­Desc Tr description | nvarchar(200) | 400 | NULL allowed |  |
|  | Notes Notes | nvarchar(200) | 400 | NULL allowed |  |
|  | Ref1 Ref 1 | nvarchar(100) | 200 | NULL allowed |  |
|  | Ref2 Ref 2 | nvarchar(100) | 200 | NULL allowed |  |
|  | Ref3 Ref 3 | nvarchar(100) | 200 | NULL allowed |  |
|  | Ref4 Ref 4 | nvarchar(100) | 200 | NULL allowed |  |
|  | Ref5 Ref 5 | nvarchar(100) | 200 | NULL allowed |  |
|  | Is­Posted­Notification Flag indicating posted notification | bit | 1 | NULL allowed |  |
|  | Is­Canceled Flag indicating canceled | bit | 1 | NULL allowed |  |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­WF\_­Sub­Log\_­Companies | Company­ID->[[dbo].[Companies].[ID]](#xWl68O1P/ZZ1akX31muCMm2xzR0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[WFMobile­Permission­Definition] |

MS\_­Description

Stores wf mobile permission definition data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | Description Description | nvarchar(200) | 400 | NULL allowed |
|  | Is­Sys­Option Flag indicating sys option | bit | 1 | NULL allowed |
|  | Use­Multi­Select Flag indicating use multi select | bit | 1 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[WFMobile­Permission­Link] |

MS\_­Description

Stores wf mobile permission link data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Per­ID Per identifier | int | 4 | NOT NULL |
| ![](data:image/png;base64...) | Sales­Person­ID Sales identifier | int | 4 | NOT NULL |
|  | Per­Value Per value | nvarchar(200) | 400 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Widget\_­Functions] |

MS\_­Description

Stores widget functions data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Comp­No Comp number | int | 4 | NOT NULL |
|  | Company­Name Company name | nvarchar(300) | 600 | NULL allowed |
|  | Function­ID Function identifier | int | 4 | NULL allowed |
|  | Function­Name Function name | nvarchar(max) | max | NULL allowed |
|  | Called­Procedure­Name Called procedure name | nvarchar(max) | max | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Widget\_­User\_­Log­Action] |

MS\_­Description

Stores widget user log action data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...)![](data:image/png;base64...) | Comp­No Comp number | int | 4 | NOT NULL |
|  | Action­Date Action date | datetime | 8 | NULL allowed |
|  | User­ID User identifier | nvarchar(50) | 100 | NULL allowed |
|  | Function­ID Function identifier | int | 4 | NULL allowed |
|  | Called­Procedure Called procedure | nvarchar(max) | max | NULL allowed |

Foreign Keys

|  |  |
| --- | --- |
| Name | Columns |
| FK\_­Widget­Log­Action\_­Widget­Log­Action | Comp­No->[[dbo].[Widget\_­User\_­Log­Action].[Comp­No]](#OsIyNY2lcWgiY8r8Wg7R9sfJiN0=) |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Wieght­Targets] |

MS\_­Description

Stores wieght targets data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Salesperson­ID Salesperson identifier | int | 4 | NOT NULL |
|  | Coverage\_­Wieght Coverage wieght | float | 8 | NULL allowed |
|  | Coverage\_­Paid­Target­Amt Coverage paid target amount | float | 8 | NULL allowed |
|  | Distribution\_­Wieght Distribution wieght | float | 8 | NULL allowed |
|  | Distribution\_­Paid­Target­Amt Distribution paid target amount | float | 8 | NULL allowed |
|  | Productivity\_­Wieght Productivity wieght | float | 8 | NULL allowed |
|  | Productivity\_­Paid­Target­Amt Productivity paid target amount | float | 8 | NULL allowed |
|  | Sales­Target\_­Wieght Sales target wieght | float | 8 | NULL allowed |
|  | Sales­Target\_­Paid­Target­Amt Sales target paid target amount | float | 8 | NULL allowed |
|  | Target­Percentage Target percentage | float | 8 | NULL allowed |
|  | Target­Percentage\_­Coverage Target percentage coverage | float | 8 | NULL allowed |
|  | Target­Percentage\_­Productivity Target percentage productivity | float | 8 | NULL allowed |
|  | Target­Percentage\_­Distribution Target percentage distribution | float | 8 | NULL allowed |
|  | Target­Percentage\_­Sales Target percentage sales | float | 8 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Zatca­Company] |

MS\_­Description

Stores zatca company data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Identification­ID Identification identifier | nvarchar(10) | 20 | NOT NULL |
| ![](data:image/png;base64...) | Tax­Number Tax number | nvarchar(100) | 200 | NOT NULL |
|  | Identification­Scheme­ID Identification scheme identifier | nvarchar(10) | 20 | NULL allowed |
|  | Street­Name Street name | nvarchar(100) | 200 | NULL allowed |
|  | Building­Number Building number | nvarchar(10) | 20 | NULL allowed |
|  | City­Name City name | nvarchar(10) | 20 | NULL allowed |
|  | Postal­Zone Postal zone | nvarchar(10) | 20 | NULL allowed |
|  | City­Subdi­Vision­Name City subdi vision name | nvarchar(100) | 200 | NULL allowed |
|  | Registration­Name Registration name | nvarchar(100) | 200 | NULL allowed |
|  | Mode­ID Mode identifier | int | 4 | NULL allowed |
|  | Branch­ID Branch identifier | int | 4 | NULL allowed |
|  | Location Location | nvarchar(50) | 100 | NULL allowed |
|  | Business­Category Business category | nvarchar(50) | 100 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Zatca­Customer] |

MS\_­Description

Stores zatca customer data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Customer­ID Customer identifier | bigint | 8 | NOT NULL |
| ![](data:image/png;base64...) | Identification­ID Identification identifier | nvarchar(10) | 20 | NOT NULL |
| ![](data:image/png;base64...) | Tax­Number Tax number | nvarchar(100) | 200 | NOT NULL |
|  | Identification­Scheme­ID Identification scheme identifier | nvarchar(10) | 20 | NULL allowed |
|  | Street­Name Street name | nvarchar(100) | 200 | NULL allowed |
|  | Building­Number Building number | nvarchar(10) | 20 | NULL allowed |
|  | City­Name City name | nvarchar(10) | 20 | NULL allowed |
|  | Postal­Zone Postal zone | nvarchar(10) | 20 | NULL allowed |
|  | City­Subdi­Vision­Name City subdi vision name | nvarchar(100) | 200 | NULL allowed |
|  | Registration­Name Registration name | nvarchar(100) | 200 | NULL allowed |
|  | Customer­Type Customer type | int | 4 | NOT NULL |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Zatca­Mode] |

MS\_­Description

Stores zatca mode data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Mode­ID Mode identifier | int | 4 | NOT NULL |
|  | Mode­Desc Mode description | nvarchar(50) | 100 | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Zatca­Result­Generate­Xml] |

MS\_­Description

Stores zatca result generate xml data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­Type­ID Transaction type identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­Year Transaction year | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | Transaction­No Transaction number | int | 4 | NOT NULL |
|  | Encoded­Invoice Encoded invoice | nvarchar(max) | max | NULL allowed |
|  | Invoice­Hash Invoice hash | nvarchar(max) | max | NULL allowed |
|  | UUID Uuid | nvarchar(max) | max | NULL allowed |
|  | QRCode Qr code | nvarchar(max) | max | NULL allowed |
|  | Is­Valid Flag indicating valid | bit | 1 | NULL allowed |
|  | Error­Message Error message | nvarchar(max) | max | NULL allowed |
|  | Allowance­Total­Amount Allowance total amount | nvarchar(max) | max | NULL allowed |
|  | Charge­Total­Amount Charge total amount | nvarchar(max) | max | NULL allowed |
|  | Line­Extension­Amount Line extension amount | nvarchar(max) | max | NULL allowed |
|  | Payable­Amount Payable amount | nvarchar(max) | max | NULL allowed |
|  | Prepaid­Amount Prepaid amount | nvarchar(max) | max | NULL allowed |
|  | Tax­Exclusive­Amount Tax exclusive amount | nvarchar(max) | max | NULL allowed |
|  | Tax­Inclusive­Amount Tax inclusive amount | nvarchar(max) | max | NULL allowed |
|  | Tax­Amount Tax amount | nvarchar(max) | max | NULL allowed |
|  | Status­Code Status code | int | 4 | NULL allowed |
|  | Sending­Status Sending status | nvarchar(max) | max | NULL allowed |
|  | Is­Sent Flag indicating sent | bit | 1 | NULL allowed |
|  | Warning­Message Warning message | nvarchar(max) | max | NULL allowed |
|  | Zatca­Call­Error­Message Zatca call error message | nvarchar(max) | max | NULL allowed |
|  | Cleared­Invoice Cleared invoice | nvarchar(max) | max | NULL allowed |
|  | Zatca­QRCode Zatca qr code | nvarchar(max) | max | NULL allowed |

|  |
| --- |
| ![](data:image/png;base64...) [dbo].[Zatca­Sales­Persons] |

MS\_­Description

Stores zatca sales persons data

Columns

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Key | Name | Data Type | Max Length (Bytes) | Nullability |
| ![](data:image/png;base64...) | Company­ID Company identifier | smallint | 2 | NOT NULL |
| ![](data:image/png;base64...) | ID ID identifier | int | 4 | NOT NULL |
|  | CSID Csid | nvarchar(max) | max | NULL allowed |
|  | Private­Key Private key | nvarchar(max) | max | NULL allowed |
|  | Secretkey Secretkey | nvarchar(max) | max | NULL allowed |
|  | OTP Otp | nvarchar(max) | max | NULL allowed |
|  | Common­Name Common name | nvarchar(max) | max | NULL allowed |
|  | Serial­Number Serial number | nvarchar(max) | max | NULL allowed |
|  | CSR Csr | nvarchar(max) | max | NULL allowed |
