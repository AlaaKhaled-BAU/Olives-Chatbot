# 2.1 Items-Items
Items is one of the key elements of a sales business as it refers of to merchandize that a business owner
sells , and in order to have a smooth automated sales environment you need to define your sold items in a
logical customized way , things like item unique code , Item Category , Item Unit , Item Price are essential
pieces of information that you would have to define through the system , or have to be drawn from an inte-
grated ERP master Data base
Here are the basic Data records of
items, as you can see basic fields
names are: Item Code, Item Name,
Category Code, & foreign name
Image 29 (Items Window )
As you click the item main record in image 29 for
editing you will see this header table
(image30) ,inside this table they are a number of
data field to enter but most significant mandatories
are: Item Code, Name, Unit, category Code, without
these basic identifications you will fail to send data
to a salesman front office android application
Image 30 (Items Details header Window )
If you go down the page in image 30 you will
reach a header named “Item Units Details”, when
you click add in left bottom of image 30 you will
go to Items units details is if not existed which is
located in image 31, or click the edit if unit /units
are existed, Item Unit and Item Convert Rate are
mandatory Data, in our system we use the big-
gest unit to convert other units of an item to, if no
sub units are available then convert rate =1 for
Image 31 (Items Units Details Window ) the item, in addition there is barcode, weight,
...etc.
Example 1 unit conversion rate
If you set a cartoon of a certain item to be as the biggest unit you set smaller cartoons in this item as a second unit so if
the big cartoon contains 10 smaller cartoons then the convert rate for the smaller cartoon is 10 and so on.
33

# 2.2 Items-Measurement units
Through This window you can define Measurement Units (item units) in general for all items, this will only
consist of a unique ID and a name, when you define a unit in the items main window header you choose the
unit form these preset definitions
You can edit , add , or delete a record
through the conventional previously
mentioned tools at the beginning of
this guide
Once you edit a record this window
will appear containing ID, Name, &
Image 32 (Measurements Units Window ) short name of a measurement unit
# 2.3 Items-Categories
Through This window you can define Item Categories , this will consist of a unique category Code , a Name ,a
Foreign Name & a Short Name, when you define a unit in the items main window header in image 30 “ item
header” you choose the unit form these preset definitions
You can Search categories by name or category code
Once you edit a record this window will appear
containing Category Code, Name, Foreign
Name & short Name of a category, you may
Image 33 (Item Categories Window )
even add a sub category from the green plus
34

# 2.4 Items-Price lists
In order to make a transaction such as a sales invoice you need to have prices defined in your system data
base , but usually not all customers are sold with the same prices for all items, you might have a heavy con-
sumer customer or a whole sale and another retail customer , therefore, price lists window was created to
define different price lists for different customers for all items in your system as in the below image
Image 34 (Price list Window )
Image 35: Once you open a price list
from the document icon you will find a
list of all its’ items codes, names,
Units, Prices, Tax types, Taxes, Dis-
count percent & Shelf Prices, you can
navigate the pages by the page select
tools located at the bottom
Image 35 (Price list details Window )
35

# 2.5 Items-Target Reference
In this window you can define names of target references that you would like to set , these target will be
defined in details on the salesperson level and the items level it can be set later through those main tabs sub
tabs which are issues that we will discuss as we come across later on in this guide, you should note however
that there is a field to assign the item for a target reference that you find in Items details under Items tab .
Once you click edit from document icon
this window will show which contains
Name and Short Name of your Target
Reference
Image 36 (Target References Window )
36

# 2.6 Items-Item Priority
In some cases and for different reasons such as the desire to make a sale on an item to finish a quantity , you
can set a priority for some items so that a salesman tablet would show priority items at the top of all items
selling list
As you click edit from document icon this window will
show containing Item Name and a check box if you
would like this item to appear in suggested order1,
when an item record/ records is here items are shown
on top of the list in salesperson tablet application in the
same category in new order tab and they are shown in
green color.
If you right check the use in suggested Order you can
define customer type and quantity where these priori-
ty items would be automatically installed in suggested
order and suggested invoice.
(1) Suggested order is an auto generated OSFA (olives front office) feature that -if activated- will output suggested quantities of items based on a history
of items withdrawals & stock for a specific customer.
37

# 2.7 Items-Item Price Exceptions
In this window you can define Certain Item Price Exceptions from standard price lists that you have defined
before, these exceptions are done on certain customers basis
Opening a record of this window will show
you this window, you must enter a specific
customer name & other item data, this cus-
tomer will have a special price based on
Image 38 (Item Price Exceptions Window )
your entered parameters
# 2.7 Items-Item Replacement Groups
Sometimes a customer needs to replace certain items with other items from the same vendor , this option
enables you to set replacement groups provided that all items have the same prices .
Editing a record will show this window where
Name and Short name and other data for
you reference are entered and saved here
Image 39 (Item Replacement Groups Window )
38

# 2.8 Items-Upload Catalog Media

This following window means exactly what it implies which is a tool for uploading images catalogs of items ,
you have two options: a video and a pdf file formats using the button browse you select your desired file
from your local PC to the back office data base
| Using  the        | browse  button  | for  |
| ----------------- | --------------- | ---- |
| each  multimedia  | file  type      | you  |
can go to the destination where
| your  multimedia  | file  is  | located  |
| ----------------- | --------- | -------- |
and upload it to the system
Image 40 (Upload Catalog Media Window )
39

# 2.9 Items-Upload Catalog Multimedia with item link
This window is used to upload catalog multimedia for a specific item and link it to the multimedia file directly
without using the previous window “Upload Catalog Media” and then the “Link catalog media” win-
dow which will be explained later, but in this window you must name the uploaded file same as
item code that is desired to be linked
Using the browse button for
each multimedia file type you
can go to the destination where
your multimedia file is located
and upload it to the system but
make sure to name the file same
as desired item code in order to
establish the link between the
item to the catalog.
Image 41 (Upload Catalog Multimedia with item link)
# 2.10 Items-Link catalog Media
After uploading your catalog using tab 2.8 above you can link catalog Media to certain Items , this will reflect
on salesmen Tablets in a way that they can show a customer linked Catalogs for the items containing Images,
by selecting the pdf or video files through the drop down list and clicking the check box you can select the
items to assign a catalog media to, after having finished your selections you press update to save your selec-
tions choices, see red rectangular shapes on image 41
Image 41 (Link Catalog Media Window )
40

# 2.10 Items-Salespersons items Sales Units
Through This Window you can link Certain Items Units for a salesperson so that he can only perform transac-
tions using this unit of a specific item
When you open this window you select your
desired salesperson , your desired item code
form the header parameters , once you do,
the existed units of that item will appear
down the page then you can right check the
left box beside the desired unit and press
“Update” , now you have assigned that par-
ticular unit of item to that particular sales-
man , you can also copy that selection to
other salesmen using the ‘copy To” Button
Image 41 (Salespersons items Sales Units)
# 2.11 Items-Items Group Bonus Target
This window was added to the system so that you can arrange your items bonus targets in groups , here you
identify your bonus groups in parameter of your choice such as price criteria , VIP items, High Range
Items ...etc., note that you can link items to any group using a drop down list existed in items details win-
dow, please refer to the items window located in tab
Using the add delete , or edit icons , you can
either add, delete , or edit an item bonus
group,
Image 41 (Items Group Bonus Target )
41

# 2.12 Items-Copy Price List
To Facilitate price list generation, this tool was developed so that you can copy a price list from an already
existed price list, the source price list will be the upper beside from price list and the lower is the destination
price list is the lower beside to price list beside each phrase you will have a drop down list to select the price
list name and then press the copy to Price list button see the below image.
Image 42 (Copy Price List Window )
42

# 2.13 Items-Sort Items
Using this feature enables you to sort items appearance priority within a category of your choice manner so
you can advance certain items to appear at the top of the category item list
When you open this window you select your
desired Category , you should then press
Get Value button which will reveal all
items within that category in their current
order please refer to the next image
Items -Sort Items Step1
Having finished the previous step you will
see all items now you can drag any item
using your mouse left click up and down to
your order choice after you press the Up-
date Button to save your items order, you
should how ever send data to the involved
salesperson/salespersons to reflect this
change on their tablet.
Items -Sort Items Step2
43

# 2.14 Items-Items Suggested Group
Through This Window you get to set suggested group that will by default be entered in any suggested in-
voice or Order fro certain customers.
Items –items suggested group main window When you add /edit a record you set up
main information regarding the suggested
group , such as Name , item unit , and
Quantity (Qty), you can also add an image
indicating the group description
Items –items suggested group-details
44

By choosing the suggested group and their
target count using this left window , you
right check the box beside the customer /
customers you would like to assign the sug-
gested group to , then you press Update to
save your selection .
Items –Assign Item Suggested Group for customers
# 2.14 Items-Assign Items for Stores
Through This Window you can assign certain items for a specific store , usually these will be main stores that
are linked to salespersons.
By choosing the suggested group and their
target count using this left window , you
right check the box beside the customer /
customers you would like to assign the sug-
gested group to , then you press Update to
save your selection .
Items –Assign Items for stores
45

# 2.15 Items-Items Classes
This Window was created to assign a certain classification for each number of selected items so that these
items could be selected on this classification basis .
The left window is the main window for
setting up items classes , when you press
the Plus green sign you can enter the re-
quired data and then save please refer to
the next image for clarification.
Items –items classes main window
Items –items classes details window
# 2.16 Items-Assign Items for Return
This window will enable you to assign certain items to be used in return invoice , once you choose them and
send data to salespersons this will reflect on their tablet when they perform a return sales transaction.
The left window is for setting assigning
items to return invoice , you right check the
boxes beside the desired items and then
press the Assign Button to assign items to
return invoice transaction on salesperson’s
tablet, please remember that you always
need to send data to salesmen to reflect
back office changes.
Items –Assign Item for Return window
46

