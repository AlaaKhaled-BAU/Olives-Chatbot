# 6.0 Promotions
There are 15 types of promotions in Olives system , when you set a promotions it will reflect on the front desk android
OSFA Application of a salesman, once a salesman logs into a customer and chooses items that are subject to promotion he
can proceed with the sales order and apply the assigned promotion, we will be discussing some available types of promo-
tions in the system as samples and the way they are defined by a back office user, since setting up a promotion is a delicate
and accurate procedure, we advice that you would fully test a promotion before going with it alive.
# 6.1 Promotions - Promotions Priorities-Priorities Definitions
Using the following Window will enable you to set up definitions for different priorities according to your desire ,
these priorities will be useful for salesman business in field which we will discuss in a later tab
Using the plus . X , or document icons you can cre-
ate delete or edit a priority definition, if you open a
priority or add one you will come across the above
window , you fill out the name, and if you desire you
can suspend the priority If is suspended is checked ,
if you check the apply for all next Promotion then all
promotions linked to this priority will be achieved (1)
Image 82 (Promotions Priorities)
# 6.1.1 Promotions - Promotions Priorities-Sort Priorities
Once you have set up the definitions from the previous tab “Priorities Definitions” you can sort the priority of
attached promotions see next image
When you select a specific priority all attached
promotions will appear with blue backgrounds , you
can drag any of them to change promotion priority
up and down, you can also delete any attached
promotion form the priority using the X icon beside
each, if you click the “Assign Promotions” Button a
new window will appear from which you can select
any promotion by right checking the box beside each
and then click Save at the bottom , if you change
order by drag you should press the “Update” Button
in Main window
(1) the promotion is linked to a priority through the promotion definition window which will be discussed later on in this guide under promotions defini-
tions
91

# 6.2.1 Promotions definition -Unconditional Promotion
Here you set input items sum quantity to yield output item quantity the word unconditional was used because it is not
significant which input item or items you use, only total sum quantity is essential to apply the term of the promotion.
let us demonstrate the sequence of this promotion windows as most of the system’s promotion types structure would be
similar :-
 Image 303 will include titles of a same promotions type as indicated inside that image’s rectangular red cut shape.
 when you open Edit window using a mouse left click of document icon (see red small arrow in image 303) for any pro-
motion title record, Image 304 will appear including header details window.
 Detailed header sub tabs will include promotion assigned salesmen, promotion assigned customers, input & output
Items as you see in image 304 .
 There are two ways to add items either one by one using the green plus sign, or a number of items using the “Add Batch
Button”.
 As you would notice in Image 304 (below ) the header contains sprites that you would need to fill with data , most sig-
nificant sprites to fill are Name , Promotion Details, start & end date which should be a valid date, Input quantity
amount, output type: discount or quantity, output quantity amount, discount Invoice type: (All, Credit, Cash or check),
round type: (down, up, or standard); this defines how you define fractions of out put quantities , standard: will add up
output if fraction is equal to or more than 0.5 it will be accumulated to one integer number if less than 0.5 it will be
neglected, if down is chosen any fraction will be neglected, & if up is selected any fraction would be accumulated to
reach 1 integer number, in addition you should at least click the check box use in sales to have the promotion active,
other features are also available such Use In Use In Return, Apply For All Units, Not Double: so that a promotion is not
doubled if double quantity is sold, Include In Target Bonus: promotion would not exceed target bonus set for the
salesman , Is Suspended: when box is right checked the promotion is considered suspended and will be inactive,
Need WF Approval : means that a salesperson is not allowed to apply the promotion unless he gets approval from his
supervisor/Supervisors through his tablet device front desk application through work flow activated feature .
 Referring to Image 304 below when you press edit of a promotion title header in image 303 you will see lower sub tabs
in image 304, using the first tab “Sales Person groups” , you assign the promotion for specific sales person groups, to
do this assignment , note that you would have to create a salesmen group first in order to use it here (see image 305
for the first sub tab of promotion) this creation is done from main system menu- salesperson-salesperson group sub
tab , once you have done that , assigned salesmen in that group will be able to apply the promotion for promotion
assigned customers.
 Promotion customers group are handled the same way in the second promotion sub tab referred to by image 306, but
with the exception is that customers groups for a promotion is created separately & not from regular customers
groups & they are created using the system menu tab (customers –customers promotion groups )
92

Image 303 (Main Unconditional Promotions window) Image 304 (Unconditional Promotions details header window)
Image 305 (Promotion Assigned Salesmen Groups) Image 306(Promotion Assigned Customers Groups) Image 307 (Promotion Input Items)
First Tab Second Tab Third Tab
Input Items are selected using the
third sub tab see Image 307
Output Items are selected using
the fourth sub tab see Image 308
Image 308 (Promotion output items window)
(Fourth Tab)
# 6.2.2 Promotions Definition-Conditional Promotion
Conditional Promotion is very similar to unconditional promotion but with some differences such as specific quantity
of each input item should be set to achieve the promotion terms for this reason you would notice that there is no
input quantity in header because it is already there in details of input items tab, another thing is that there is no
round feature please refer to image 309 & Image 310 below for differences.
Image309 (Conditional Promotion details Header window)
Image 310 (Unconditional Promotion details Header window)
93

# 6.2.3 Promotions Definition-Range Promotions
This Type of promotion cannot be applied unless input item is same as output item; you set up a range of quantity (from
to) when the quantity is within this range the promotion is applied.
For example if a customer buys 10-20 cartons of an input item X he will receive a bonus of 1 carton from same out put
item X note that same item should be chosen for this type of promotion, (see image 311 & Image 312).
* As always the case you would have to select a salesman group and a customer promotion group to assign the promo-
tion to (this is done from the first two sub tabs in details as mentioned in previous promotion types) and you will also
have to set the range details too, please refer to image 312.
Image 312 (Range Promotion details window)
Image 311 (Range Promotion headers window)
You can edit the details by clicking the document
icon
# 6.2.4 Promotions definition-Invoice Amount Promotions
Here you set your condition to be the total invoice money amount , so if a total value of invoice is reached then a Quantity
or a Discount is applicable for a certain customer, note that if you choose a “Discount” from out put type in details header
you would not have an out put item , but if you choose the out put type to be “Quantity” then you will add an out put
item details, please refer to image 313 & Image 314 and notice how changing output type would hide or reveal some
input sprites.
* As always the case you would have to select a salesman group and a customer promotion group to assign the promo-
tion to (this is done from the first two sub tabs in details as mentioned in previous promotion types)
Image 313 (Invoice Amount Details window) Image 314 (Invoice Amount Details window)
“Promotion output type selected as Discount” “Promotion output type selected as Quantity”
94

# 6.2.5 Promotions definition-Item Quantity Promotions
This type of promotions is similar to unconditional promotions but with irregular input and output quantities, you define the
items and their input and output quantities.
On the left you will see the win-
dow showing Item Quantity Pro-
motions main window, if you click
the edit or add icon you will go
the details windows below, click-
ing the magnifier icon -unlike the
edit icon- will only show you a
preview without enabling edit of
details
Item Quantity Promotions Header window
As always the case you will have
to choose salesperson group , and
customer promotion group to
assign to this promotion to, after
that you choose input and out put
items
Finally, you define the input and out put quan-
tities from Quantity (for input) , and output
quantity , it is imperative to note here that the
quantity entered on tablet will apply the out-
put according to the grater value, for example
as in the left window, if you choose 50 then
you will have the 30 bonus (9) + the 20 bonus
(4) which is a total of 13 bonus of the output
unit, if you right check the “Use Rate ToCalc
Bonus ” then bonus will be calculated relative
if you right check the “Is Required in Trans? ” then sales-
to the largest quantity.
man must apply this promotion in sales invoice for each
customer within the same customers promotion group.
95

# 6.2.6 Promotions definition-Package Promotion
Here you set input items as a quantity of each item , but input items & out put items are dealt with as a whole package so
the term out put items quantities term will not be accomplished unless all input items meet their input defined quantities,
you will not notice a lot of fields in header of the details window, because they are not needed here because quantities
are defined from down tabs.
* As always the case you would have to select a salesman group and a customer promotion group to assign the promo-
tion to (this is done from the first two sub tabs in details as mentioned in previous promotion types) please refer to image
315.
Through these regular tabs you select the tab and
edit it by selecting Salesperson Groups, Customers
Groups, Input Items & output Items
Image 315 (Package Promotion details window)
96

# 6.2.7 Promotions definition-Unconditional By Amount
After defining salesperson group and customer promotion group for this promotion , you enter the items you desire to
achieve the promotion term , this term is simply the total amount of purchased items regardless if the purchase was for all
listed items or some of them as long as the total amount value is achieved.
The header of this promotion is no different from
other promotions headers as you can see from the
left window, it will consist of ID , Name , Start Date,
End Date, Promotion class, and an Is suspended
field, pressing the edit icon will lead you to the
following details window.
Unconditional By Amount main window
If you select output discount then you would
have a discount percent or value is needed
to be set , but if you select quantity, the
discount field will disappear and an out put
items tab will appear in details to fill out ,
note that salesman can choose form the
output item if the items in output are more
than one item provided that he enters the
right output quantity.
Unconditional By Amount details window
97

# 6.2.8 Promotions definition-Items Amount Promotion
After defining salesperson group and customer promotion group for this promotion , you would notice that the details
window is different from other promotions, it does not have an amount or discount choice , and details tabs are also
different please refer to the details window.
The header of this promotion is no different from
other promotions headers, as you can see from the
left window, it will consist of ID , Name , Start Date,
End Date, Promotion class, and an Is suspended
field, pressing the edit icon will lead you to the
following details window.
Items Amount Promotion main window
Here you do not have to define input items as there
aren’t any , but you need to define Exception Items
that you would not want this promotion to include
in its estimation In “Exception Items” Tab , and you
need to define output items , and define output
quantity for each amount you desire from “Amount-
Quantity”, salesman can choose which output
items/items to choose from provided that he enters
the right output quantity as per promotion terms
and that “Output Item Same input item” check box
is not marked.
Items Amount Promotion Details window
98

# 6.2.9 Promotions definition-Open Bonus Promotion
In this Promotion you get to set specific Bonus max Quantity for Specific Item Units , salesman can select these items bonus-
es when sales invoice or return sales invoice is conducted but with max quantity that he couldn't exceed
The header of this promotion is no different from
other promotions headers, as you can see from the
left window, it will consist of ID , Name , Start Date,
End Date, Promotion class, and an Is suspended
field, pressing the edit icon will lead you to the
following details window.
Open Bonus Promotion main window
Having finished entering header of this details win-
dow and assigning the right salesperson group and
customers promotion group as in every promotion
you prepare you input items and their max quanti-
ties in the items tab, these items quantities are max
bonuses quantities that a salesman can dispense for
each listed item.
Open Bonus Promotion Details window
99

# 6.2.10 Promotions definition- Promotion 9
In this Promotion you get to set specific items in Input , salesman can select one out put items using his tablet , input quanti-
ty can be one or sum of all input quantities.
The header of this promotion is no different from
other promotions headers, as you can see from the
left window, it will consist of ID , Name , Start Date,
End Date, Promotion class, and an Is suspended
field, pressing the edit icon will lead you to the
following details window.
Promotion 9 main window
Having finished entering header of this details win-
dow and assigning the right salesperson group and
customers promotion group as in every promotion
you prepare, you enter input items and output
items , in this promotion the input quantity is set
from header , it can be the quantity of one or all
input items quantity sum , but salesman can only
have one output quantity applied in transaction , he
selects it by only making one click on the promotion
available quantities and then it will be shadowed
and then proceed for save.
Promotion 9 Details window
100

# 6.2.11 Promotion 10
In this Promotion you Specify an input quantity , Output quantity and discount amount from header , then you go down to
details and specify input and output items from details window.
The header of this promotion is no different from
other promotions headers, as you can see from the
left window, it will consist of ID , Name , Start Date,
End Date, Promotion class, and an Is suspended
field, pressing the edit icon will lead you to the
following details window.
Promotion 10 main window
Having finished entering header of this details win-
dow and assigning the right salesperson group and
customers promotion group as in every promotion
you prepare, you enter input items Quantity beside
“ Input Quantity Amount “ and output in “output
Quantity Amount” , in “Out Percent Amount” is a
fixed value that will always be the same even if you
exceeded the input quantity while the output items
quantity will be affected (doubled if input doubled
for instance), you select input items and output
items from “input items” and “output items” tabs
Promotion 10 Details window
101

# 6.2.12 Promotions definition-Promotion Input Output
The header of this promotion is no different from
other promotions headers, as you can see from the
left window, it will consist of ID , Name , Start Date,
End Date, Promotion class, and an Is suspended
field, pressing the edit icon will lead you to the
following details window.
Promotion Input Output main window
Once you select the Items Tab down the left details
window you will see all listed items , or you can click
the + icon to add a new item which will lead you to
the next image, go for next image for further illus-
tration
Through this left window you can click the edit in
items details or the add for were you can select both
input and output items and define their quantities.
Please note that each item input code should have
the same item output code so that this promotion
setup could be completed successfully.
102

# 6.2.13 Promotions-Promotion 12
This is a more complex promotion, the input is in the form of items while the output is in the form of groups , output
groups can be set as “by discount” or “by Amount”, as you look at the header of the promotion once you edit a record of a
promotion of this type, you will see it contains the usual main fields such as name, start date, end date, invoice type, In-
put type: Amount or quantity, WF Approval (needs approval by supervisor) ...etc. but you will notice and additional
“allow salesperson to choose Output (if checked) which means that a salesperson can choose which group to pick output
from, and “sales person can change output quantity” which (if checked) means a sales person can decide the out put
quantity of the output group see next images for illustration.
* As always the case you would have to select a salesman group and a customer promotion group to assign the promo-
tion to (this is done from the first two sub tabs in details as mentioned in previous promotion types) .
From the left image 316 you can see the header of
promotion 12, you set fundamental header details
such as: Name, Start and End date , invoice type:
credit or cash or all, input type : Amount or Quanti-
ty , if this promotion needs supervisor approval by
“Need WF approval” , use in sales , use in return, in
addition you have “Allow salesperson to choose
output” to enable salesman to choose which output
group to choose from in applying the promotion
and salesman can change output quantity which
means a sales man can decide the output quantity.
Image 316-A (Promotion 12 (showing Header only))
103

From the left image 316-B you can start to see the
details of Input Items, here you select the input
items , note that the input items are not conditional
so when either item term is met the promotion is
applicable, note that you set the input amount from
the output group details see Image 316-C.
Image 316-B (Promotion 12 (showing below details))
From the left image 316-C you set the output items
(groups) , you will find the discount rate beside each
group on the right hand of groups’ names, if you
edit one record you will go to image 316-D which
Image 316-C (Promotion 12 (Output headers)
will show you details of that selected group, if
output is set to “Quantity” you will find the quantity
which is the same for all items in that group (if “is
conditional” is checked), you should have at least
two groups in items output, if output is set to
“Amount” you won’t have items to put so the group
will only be a name indicating that a discount rate
is applicable.
Image 316-D (Promotion 12 (showing Output headers details
Of a selected group)
104

From the left image 316-E when you set the output
type to quantity you will notice that editing will
show you all items of the group , note that check
box is conditional is not checked this means that
output quantity is the same for all items of the
group, in case it is checked you can define each item
with different quantity see next (image 316F).
Image 316-E (Promotion 12 (Output Group details (Quantity selected))
From the left image 316-E as you see the “is condi-
tional” is checked so each item quantity will be set
individually for each item, you will notice that a
new column containing the quantity of each item
has appeared to the right of the unit.
Image 316-F (Promotion 12 (Output Group details (type selected as
Quantity and “is conditional” checked))
# 6.2.14 Promotions definition-Conditional Group Promotion
Here you set the input to be a number of items in at least one groups which will result in granting out put items , if you
set the promotion output to quantity you will have to define items in output , but if you set it to discount then you
wont have out put items to define because the out put would be a discount rate.
Looking at Image 317-A on the left which is the
window that you see when you add or edit a pro-
motion of this type, here you set the name and start
and end date and most importantly output type and
amount , you also have a Not Double check box if
you don’t want the promotion to reoccur if input is
doubled a customer will only have promotion out-
put one time (it will not double)1.
Image 317-A (Conditional Group Promotion header)
(1) It is fundamental to know that quantities are mandatory per input group not per input item so you can have different quantities of items within the
same group but what is crucial is the fact that one group quantity will meet its term for example: if quantity is set to 50 sum of item in group must be 50,
and the same if set as amount (total amount term of the input group must be met) no matter amount per each amount.
105

From the left image 317-B as you see, here we set the
output to discount which will hide output items col-
umn because output is an amount not items , you can
set the quantity or discount rate from the header too,
and you set the type of invoices to cash , credit , or all.
In addition you set discount type as percentage or
amount, but if you choose output type as quantity
this field will disappear.
Image 317-B (Conditional Group Promotion header)
See image 317-C , here is a mixed input types item
groups: two groups inputs are set by amount while
one is set by quantity, you can see the number of
amount or quantity in a column on the right side of
the group.
Image 317-C (Conditional Group Promotion Input Items window)
# 6.2.15 Promotions definition-Promotion 14
Here you set the input to be a number of items by amount or by quantity which will result in granting out put items or
a discount , the output is set as groups of items but they have a range in quantity from (quantity) to (quantity), the
output group and quantity is set according to input range.
From the image 318-A , once you edit or add a
record to this type of promotions you will see this
window view containing the header and below are
input and output, you fill in Name, and start and
end date, invoice type , and input type Amount or
quantity ..etc.
Image 318-A (Promotion 14 header window view)
106

From the image 318-A, once you edit or add a record
to this type of promotions you will see this window
view containing the header and below are input and
output, you fill in Name, and start and end date,
invoice type , and input type Amount or quanti-
ty ..etc.
Image 319-B (Promotion 14 Input window view)
From the image 319-C, you can see the output win-
dow view, the out put is set as groups of items & as
you see you can set the output to be as quantity or
as discount , once you edit one group you can see
what distinguishes this promotion is that input
groups set as quantities will contain ranges mini-
mum and maximum (from quantity/amount to
quantity/ amount) as you can see in image 319-D.
Image 319-C (Promotion 14 output window view)
Image 319-D(Promotion 14 output details window view)
107

# 6.3.1 Promotions Settings-Coupon Books
??????.
??????
Coupons Books Main window
??????
Coupons Books Details window
# 6.3.2 Promotions Settings-Copy Promotions
??????.
??????
Copy Promotions
108

# 6.3.3 Promotions Settings-Promotions Inquiry
As we have seen in Promotions Definitions main and sub tabs each type of promotions is existed in a separate win-
dow , this window is simply to show main information about all existed promotions in a singe page Such as ID , Type ,
Start Date , End Date ...etc.
Promotions Inquiry
# 6.3.4 Promotions Settings-Promotions WF Approve
As Suggests the name this is a window where you can assign promotions for approval request by Salesperson Supervi-
sor, Area Manager etc. Once promotion is assigned for approval it cannot take place for real unless a WF Approval is
granted by the intended employee, WFs are functions that will be illustrated in details in an upcoming topic in this
guide ???? Information and methodology Needs further verification
As we see from the left window you should
first the employee who is to grant the ap-
proval for the promotion and as in every
assigning process explained in previous top-
ics , unassigned promotions are under Unas-
signed section , while assigned promotion will
be right checked and located under the left
Assign Promotion section, right checking the
left promotions and pressing the orange
button will move them to the assigned sec-
tion, unchecking the left promotions and
pressing the orange icon will do the opposite.
Promotions WF Approve
109

# 6.3.5 Promotions Settings-Promotions Approval
?????
???????
Promotions Approval
# 6.3.6 Promotions Settings-Promotions Classes
This window Is to set a predefined class for the promotions , it basically a kind of a classification that describes the way
the promotion is used such as for what type of customers is this promotions is intended to be used for such as “Super
market Promotions”….etc.
Editing or adding a new record will
show the above window, showing
name , and two references fields which
can be of benefit for some usage but
are not mandatories, having finished
defining these classes they should be
linked to every promotion header in all
promotions types windows.
Promotions Classes
110

# 6.3.7 Promotions Settings-Coupons Barcode Generator
?????.
Through this left window you can gener-
ate a random Barcode for the coupon
that is to be delivered for the Customer,
You choose the customer , the promo-
tion ID , and set the expiry date and then
Press the Generate button to generate
the barcode code you should use . ????
Coupons Barcode Generator
# 6.3.8 Promotions Settings-Promotions Selection Groups
?????.
If you edit or add a new record
you will see the above window
in which you would find or add
the name of the promotion se-
lection group.?????
Promotions Selection Groups
111

# 6.3.9 Promotions Settings-Promotions Selection Groups Link
?????.
???
Promotions Selection Groups Link
112

